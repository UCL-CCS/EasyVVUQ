"""
Dataset Import Utilities for EasyVVUQ

This module provides utilities for creating EasyVVUQ campaigns from existing datasets
that were not originally created with EasyVVUQ.
"""

import os
import json
import glob
import logging
import pandas as pd
import numpy as np
from pathlib import Path
from typing import List, Dict, Optional, Any
from collections import defaultdict

import easyvvuq as uq
from easyvvuq.constants import Status
from easyvvuq.actions import Actions, CreateRunDirectory, Encode, Decode, ExecuteLocal

__copyright__ = """

    Copyright 2018 Robin A. Richardson, David W. Wright

    This file is part of EasyVVUQ

    EasyVVUQ is free software: you can redistribute it and/or modify
    it under the terms of the Lesser GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    EasyVVUQ is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    Lesser GNU General Public License for more details.

    You should have received a copy of the Lesser GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
__license__ = "LGPL"

logger = logging.getLogger(__name__)


class DatasetImporter:
    """
    A utility class for importing existing datasets into EasyVVUQ campaigns.
    
    This class provides methods to discover, validate, and import simulation data
    from existing directory structures or file collections.
    """
    
    def __init__(self, root_dir: str, campaign_name: str = "imported_campaign"):
        """
        Initialize the DatasetImporter.
        
        Parameters
        ----------
        root_dir : str
            Root directory containing the existing dataset
        campaign_name : str, optional
            Name for the campaign to be created (default: "imported_campaign")
        """
        self.root_dir = Path(root_dir).resolve()
        self.campaign_name = campaign_name
        self.discovered_runs = []
        self.parameters = {}
        self.output_columns = []
        
        if not self.root_dir.exists():
            raise ValueError(f"Root directory does not exist: {self.root_dir}")
    
    def discover_directory_structure(self, 
                                   input_patterns: List[str] = None,
                                   output_patterns: List[str] = None,
                                   max_depth: int = 3) -> Dict[str, Any]:
        """
        Automatically discover the directory structure and identify runs.
        
        Parameters
        ----------
        input_patterns : List[str], optional
            List of glob patterns to match input files (default: common patterns)
        output_patterns : List[str], optional
            List of glob patterns to match output files (default: common patterns)
        max_depth : int, optional
            Maximum depth to search for files (default: 3)
        
        Returns
        -------
        Dict[str, Any]
            Dictionary containing discovered structure information
        """
        if input_patterns is None:
            input_patterns = [
                "*.json", "*.txt", "*.csv", "*.yaml", "*.yml", "*.xml",
                "input.*", "params.*", "config.*", "*input*", "*param*"
            ]
        
        if output_patterns is None:
            output_patterns = [
                "*.csv", "*.json", "*.txt", "*.out", "*.log", "*.dat",
                "output.*", "result.*", "*.results", "*output*", "*result*"
            ]
        
        discovered = {
            'runs': [],
            'structure_type': 'unknown',
            'input_files': [],
            'output_files': [],
            'common_structure': None
        }
        
        logger.info(f"Discovering directory structure in {self.root_dir}")
        
        # Search for potential run directories
        for root, dirs, files in os.walk(self.root_dir):
            current_depth = len(Path(root).relative_to(self.root_dir).parts)
            if current_depth > max_depth:
                continue
                
            # Look for input and output files in this directory
            input_files = []
            output_files = []
            
            for pattern in input_patterns:
                input_files.extend(glob.glob(os.path.join(root, pattern)))
            
            for pattern in output_patterns:
                output_files.extend(glob.glob(os.path.join(root, pattern)))
            
            # If we found both input and output files, this might be a run directory
            if input_files and output_files:
                run_info = {
                    'directory': root,
                    'input_files': input_files,
                    'output_files': output_files,
                    'relative_path': os.path.relpath(root, self.root_dir)
                }
                discovered['runs'].append(run_info)
                discovered['input_files'].extend(input_files)
                discovered['output_files'].extend(output_files)
        
        # Determine structure type
        if len(discovered['runs']) > 0:
            discovered['structure_type'] = 'run_directories'
        elif discovered['input_files'] or discovered['output_files']:
            discovered['structure_type'] = 'flat_files'
        
        logger.info(f"Discovered {len(discovered['runs'])} potential run directories")
        self.discovered_runs = discovered['runs']
        
        return discovered
    
    def infer_parameters(self, sample_files: List[str] = None, 
                        file_type: str = 'auto') -> Dict[str, Dict[str, Any]]:
        """
        Infer parameter definitions from sample input files.
        
        Parameters
        ----------
        sample_files : List[str], optional
            List of sample input files to analyze (default: use discovered files)
        file_type : str, optional
            Type of input files ('json', 'csv', 'yaml', 'auto') (default: 'auto')
        
        Returns
        -------
        Dict[str, Dict[str, Any]]
            Dictionary containing inferred parameter definitions
        """
        if sample_files is None:
            if not self.discovered_runs:
                raise ValueError("No runs discovered. Run discover_directory_structure first.")
            sample_files = [run['input_files'][0] for run in self.discovered_runs[:5]]
        
        parameters = {}
        all_params = defaultdict(list)
        
        for file_path in sample_files:
            try:
                params = self._parse_input_file(file_path, file_type)
                for key, value in params.items():
                    all_params[key].append(value)
            except Exception as e:
                logger.warning(f"Failed to parse {file_path}: {e}")
                continue
        
        # Infer parameter types and ranges
        for param_name, values in all_params.items():
            param_info = self._infer_parameter_info(param_name, values)
            parameters[param_name] = param_info
        
        self.parameters = parameters
        logger.info(f"Inferred {len(parameters)} parameters: {list(parameters.keys())}")
        
        return parameters
    
    def infer_output_columns(self, sample_files: List[str] = None,
                           file_type: str = 'auto') -> List[str]:
        """
        Infer output column names from sample output files.
        
        Parameters
        ----------
        sample_files : List[str], optional
            List of sample output files to analyze (default: use discovered files)
        file_type : str, optional
            Type of output files ('json', 'csv', 'yaml', 'auto') (default: 'auto')
        
        Returns
        -------
        List[str]
            List of output column names
        """
        if sample_files is None:
            if not self.discovered_runs:
                raise ValueError("No runs discovered. Run discover_directory_structure first.")
            sample_files = [run['output_files'][0] for run in self.discovered_runs[:5]]
        
        all_columns = set()
        
        for file_path in sample_files:
            try:
                columns = self._get_output_columns(file_path, file_type)
                all_columns.update(columns)
            except Exception as e:
                logger.warning(f"Failed to parse {file_path}: {e}")
                continue
        
        self.output_columns = list(all_columns)
        logger.info(f"Inferred {len(self.output_columns)} output columns: {self.output_columns}")
        
        return self.output_columns
    
    def create_campaign_from_dataset(self, 
                                   work_dir: str = "./",
                                   input_decoder: Optional[object] = None,
                                   output_decoder: Optional[object] = None,
                                   auto_infer: bool = True):
        """
        Create a new EasyVVUQ campaign from the discovered dataset.
        
        Parameters
        ----------
        work_dir : str, optional
            Working directory for the campaign (default: "./")
        input_decoder : object, optional
            Custom input decoder (default: auto-create based on file types)
        output_decoder : object, optional
            Custom output decoder (default: auto-create based on file types)
        auto_infer : bool, optional
            Whether to automatically infer parameters and outputs (default: True)
        
        Returns
        -------
        Campaign
            The created campaign with imported data
        """
        if not self.discovered_runs:
            raise ValueError("No runs discovered. Run discover_directory_structure first.")
        
        if auto_infer:
            if not self.parameters:
                self.infer_parameters()
            if not self.output_columns:
                self.infer_output_columns()
        
        # Create campaign
        campaign = uq.Campaign(name=self.campaign_name, work_dir=work_dir)
        
        # Create basic actions (since we're importing existing data, we don't need real execution)
        actions = Actions(
            CreateRunDirectory(work_dir),
            Encode(uq.encoders.GenericEncoder('', '', target_filename='dummy_input')),
            ExecuteLocal('echo "Imported data"'),
            Decode(uq.decoders.SimpleCSV('dummy_output', self.output_columns))
        )
        
        # Add app to campaign
        campaign.add_app(
            name=self.campaign_name,
            params=self.parameters,
            actions=actions
        )
        
        # Set up decoders
        if input_decoder is None:
            input_decoder = self._create_auto_decoder('input')
        if output_decoder is None:
            output_decoder = self._create_auto_decoder('output')
        
        # Import the runs
        self._import_runs_to_campaign(campaign, input_decoder, output_decoder)
        
        logger.info(f"Created campaign '{self.campaign_name}' with {len(self.discovered_runs)} runs")
        
        return campaign
    
    def _parse_input_file(self, file_path: str, file_type: str = 'auto') -> Dict[str, Any]:
        """Parse an input file and return parameters."""
        try:
            if file_type == 'auto':
                file_type = self._detect_file_type(file_path)
            
            if file_type == 'json':
                with open(file_path, 'r') as f:
                    return json.load(f)
            elif file_type == 'csv':
                df = pd.read_csv(file_path)
                return df.iloc[0].to_dict() if len(df) > 0 else {}
            elif file_type in ['yaml', 'yml']:
                try:
                    import yaml
                    with open(file_path, 'r') as f:
                        return yaml.safe_load(f)
                except ImportError:
                    logger.warning("PyYAML not installed, cannot parse YAML files")
                    return {}
            else:
                # Try to parse as key-value pairs
                params = {}
                with open(file_path, 'r') as f:
                    for line in f:
                        line = line.strip()
                        if '=' in line and not line.startswith('#'):
                            key, value = line.split('=', 1)
                            params[key.strip()] = self._convert_value(value.strip())
                return params
        except Exception as e:
            logger.warning(f"Failed to parse file {file_path}: {e}")
            return {}
    
    def _get_output_columns(self, file_path: str, file_type: str = 'auto') -> List[str]:
        """Get column names from an output file."""
        if file_type == 'auto':
            file_type = self._detect_file_type(file_path)
        
        if file_type == 'json':
            with open(file_path, 'r') as f:
                data = json.load(f)
                if isinstance(data, dict):
                    return list(data.keys())
                elif isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict):
                    return list(data[0].keys())
        elif file_type == 'csv':
            df = pd.read_csv(file_path, nrows=1)
            return list(df.columns)
        
        return []
    
    def _detect_file_type(self, file_path: str) -> str:
        """Detect file type based on extension."""
        ext = Path(file_path).suffix.lower()
        if ext == '.json':
            return 'json'
        elif ext == '.csv':
            return 'csv'
        elif ext in ['.yaml', '.yml']:
            return 'yaml'
        else:
            return 'text'
    
    def _convert_value(self, value_str: str) -> Any:
        """Convert string value to appropriate type."""
        value_str = value_str.strip()
        
        # Try boolean
        if value_str.lower() in ['true', 'false']:
            return value_str.lower() == 'true'
        
        # Try integer
        try:
            return int(value_str)
        except ValueError:
            pass
        
        # Try float
        try:
            return float(value_str)
        except ValueError:
            pass
        
        # Return as string
        return value_str
    
    def _infer_parameter_info(self, param_name: str, values: List[Any]) -> Dict[str, Any]:
        """Infer parameter information from a list of values."""
        if not values:
            return {"type": "string", "default": ""}
        
        # Remove None values
        values = [v for v in values if v is not None]
        
        if not values:
            return {"type": "string", "default": ""}
        
        # Determine type
        first_value = values[0]
        if isinstance(first_value, bool):
            param_type = "boolean"
            default = first_value
            param_info = {"type": param_type, "default": default}
        elif isinstance(first_value, int):
            param_type = "integer"
            min_val = min(values)
            max_val = max(values)
            default = values[0]
            param_info = {
                "type": param_type,
                "min": min_val,
                "max": max_val,
                "default": default
            }
        elif isinstance(first_value, float):
            param_type = "float"
            min_val = min(values)
            max_val = max(values)
            default = values[0]
            param_info = {
                "type": param_type,
                "min": min_val,
                "max": max_val,
                "default": default
            }
        else:
            param_type = "string"
            default = str(first_value)
            param_info = {"type": param_type, "default": default}
        
        return param_info
    
    def _create_auto_decoder(self, decoder_type: str) -> object:
        """Create an appropriate decoder based on discovered file types."""
        if decoder_type == 'input':
            # For input files, try to detect the most common format
            if self.discovered_runs:
                sample_file = self.discovered_runs[0]['input_files'][0]
                file_type = self._detect_file_type(sample_file)
                
                if file_type == 'json':
                    return uq.decoders.JSONDecoder('', list(self.parameters.keys()))
                elif file_type == 'csv':
                    return uq.decoders.SimpleCSV('', list(self.parameters.keys()))
        
        elif decoder_type == 'output':
            # For output files, try to detect the most common format
            if self.discovered_runs:
                sample_file = self.discovered_runs[0]['output_files'][0]
                file_type = self._detect_file_type(sample_file)
                
                if file_type == 'json':
                    return uq.decoders.JSONDecoder('', self.output_columns)
                elif file_type == 'csv':
                    return uq.decoders.SimpleCSV('', self.output_columns)
        
        # Default fallback
        return uq.decoders.SimpleCSV('', self.output_columns)
    
    def _import_runs_to_campaign(self, campaign: uq.Campaign, 
                               input_decoder: object, 
                               output_decoder: object):
        """Import discovered runs into the campaign."""
        input_files = []
        output_files = []
        
        for run in self.discovered_runs:
            # Use the first input and output file from each run
            if run['input_files']:
                input_files.append(run['input_files'][0])
            if run['output_files']:
                output_files.append(run['output_files'][0])
        
        # Use the existing add_external_runs method
        campaign.add_external_runs(input_files, output_files, input_decoder, output_decoder)


def create_campaign_from_directory(root_dir: str,
                                 campaign_name: str = "imported_campaign",
                                 work_dir: str = "./",
                                 input_patterns: List[str] = None,
                                 output_patterns: List[str] = None,
                                 auto_infer: bool = True):
    """
    Convenience function to create a campaign from an existing directory structure.
    
    Parameters
    ----------
    root_dir : str
        Root directory containing the existing dataset
    campaign_name : str, optional
        Name for the campaign to be created (default: "imported_campaign")
    work_dir : str, optional
        Working directory for the campaign (default: "./")
    input_patterns : List[str], optional
        List of glob patterns to match input files
    output_patterns : List[str], optional
        List of glob patterns to match output files
    auto_infer : bool, optional
        Whether to automatically infer parameters and outputs (default: True)
    
    Returns
    -------
    Campaign
        The created campaign with imported data
    
    Examples
    --------
    >>> campaign = create_campaign_from_directory(
    ...     root_dir="/path/to/simulation/runs",
    ...     campaign_name="my_imported_campaign"
    ... )
    """
    importer = DatasetImporter(root_dir, campaign_name)
    importer.discover_directory_structure(input_patterns, output_patterns)
    return importer.create_campaign_from_dataset(work_dir=work_dir, auto_infer=auto_infer)


def create_campaign_from_files(input_files: List[str],
                             output_files: List[str],
                             campaign_name: str = "imported_campaign",
                             work_dir: str = "./",
                             input_decoder: Optional[object] = None,
                             output_decoder: Optional[object] = None,
                             auto_infer: bool = True):
    """
    Create a campaign from explicit lists of input and output files.
    
    Parameters
    ----------
    input_files : List[str]
        List of input file paths
    output_files : List[str]
        List of output file paths
    campaign_name : str, optional
        Name for the campaign to be created (default: "imported_campaign")
    work_dir : str, optional
        Working directory for the campaign (default: "./")
    input_decoder : object, optional
        Custom input decoder (default: auto-create)
    output_decoder : object, optional
        Custom output decoder (default: auto-create)
    auto_infer : bool, optional
        Whether to automatically infer parameters and outputs (default: True)
    
    Returns
    -------
    Campaign
        The created campaign with imported data
    
    Examples
    --------
    >>> campaign = create_campaign_from_files(
    ...     input_files=["run1/input.json", "run2/input.json"],
    ...     output_files=["run1/output.csv", "run2/output.csv"],
    ...     campaign_name="my_campaign"
    ... )
    """
    if len(input_files) != len(output_files):
        raise ValueError("Number of input files must match number of output files")
    
    # Create a temporary directory structure for the importer
    temp_dir = Path(work_dir) / "temp_import"
    temp_dir.mkdir(exist_ok=True)
    
    # Create fake run directories
    discovered_runs = []
    for i, (input_file, output_file) in enumerate(zip(input_files, output_files)):
        run_dir = temp_dir / f"run_{i}"
        run_dir.mkdir(exist_ok=True)
        discovered_runs.append({
            'directory': str(run_dir),
            'input_files': [input_file],
            'output_files': [output_file],
            'relative_path': f"run_{i}"
        })
    
    # Create importer and set up discovered runs
    importer = DatasetImporter(str(temp_dir), campaign_name)
    importer.discovered_runs = discovered_runs
    
    if auto_infer:
        importer.infer_parameters(input_files)
        importer.infer_output_columns(output_files)
    
    return importer.create_campaign_from_dataset(
        work_dir=work_dir,
        input_decoder=input_decoder,
        output_decoder=output_decoder,
        auto_infer=False  # Already done above
    )
