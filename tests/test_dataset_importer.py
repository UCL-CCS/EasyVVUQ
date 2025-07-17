"""
Tests for the dataset importer functionality.
"""

import os
import json
import tempfile
import shutil
import pytest
from pathlib import Path
import pandas as pd

import easyvvuq as uq
from easyvvuq.utils.dataset_importer import DatasetImporter, create_campaign_from_directory, create_campaign_from_files


class TestDatasetImporter:
    """Test cases for the DatasetImporter class."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.temp_dir = tempfile.mkdtemp()
        self.test_data_dir = Path(self.temp_dir) / "test_data"
        self.test_data_dir.mkdir()
        
        # Create test data structure
        self.create_test_data()
    
    def teardown_method(self):
        """Clean up test fixtures."""
        shutil.rmtree(self.temp_dir)
    
    def create_test_data(self):
        """Create test data structure."""
        # Create run directories with input and output files
        for i in range(3):
            run_dir = self.test_data_dir / f"run_{i}"
            run_dir.mkdir()
            
            # Create input file (JSON)
            input_data = {
                "param1": 1.0 + i * 0.1,
                "param2": 10 + i,
                "param3": True if i % 2 == 0 else False,
                "output_file": "result.csv"
            }
            with open(run_dir / "input.json", "w") as f:
                json.dump(input_data, f)
            
            # Create output file (CSV)
            output_data = pd.DataFrame({
                "time": [0, 1, 2, 3, 4],
                "value": [1.0 + i, 1.1 + i, 1.2 + i, 1.3 + i, 1.4 + i],
                "error": [0.01, 0.02, 0.03, 0.04, 0.05]
            })
            output_data.to_csv(run_dir / "result.csv", index=False)
    
    def test_discover_directory_structure(self):
        """Test directory structure discovery."""
        importer = DatasetImporter(str(self.test_data_dir))
        discovered = importer.discover_directory_structure()
        
        assert discovered['structure_type'] == 'run_directories'
        assert len(discovered['runs']) == 3
        
        # Check that input and output files were found
        for run in discovered['runs']:
            assert len(run['input_files']) >= 1
            assert len(run['output_files']) >= 1
            assert any('input.json' in f for f in run['input_files'])
            assert any('result.csv' in f for f in run['output_files'])
    
    def test_infer_parameters(self):
        """Test parameter inference."""
        importer = DatasetImporter(str(self.test_data_dir))
        importer.discover_directory_structure()
        parameters = importer.infer_parameters()
        
        assert 'param1' in parameters
        assert 'param2' in parameters  
        assert 'param3' in parameters
        assert 'output_file' in parameters
        
        # Check parameter types
        assert parameters['param1']['type'] == 'float'
        assert parameters['param2']['type'] == 'integer'
        assert parameters['param3']['type'] == 'boolean'
        assert parameters['output_file']['type'] == 'string'
        
        # Check parameter ranges
        assert 'min' in parameters['param1']
        assert 'max' in parameters['param1']
        assert 'min' in parameters['param2']
        assert 'max' in parameters['param2']
    
    def test_infer_output_columns(self):
        """Test output column inference."""
        importer = DatasetImporter(str(self.test_data_dir))
        importer.discover_directory_structure()
        output_columns = importer.infer_output_columns()
        
        expected_columns = ['time', 'value', 'error']
        assert all(col in output_columns for col in expected_columns)
    
    def test_create_campaign_from_dataset(self):
        """Test campaign creation from dataset."""
        importer = DatasetImporter(str(self.test_data_dir), "test_campaign")
        importer.discover_directory_structure()
        
        campaign = importer.create_campaign_from_dataset(work_dir=self.temp_dir)
        
        assert campaign.campaign_name == "test_campaign"
        assert len(importer.parameters) > 0
        assert len(importer.output_columns) > 0
        
        # Check that runs were imported
        runs = list(campaign.list_runs())
        assert len(runs) == 3
        
        # Check that we can get collation results
        df = campaign.get_collation_result()
        assert len(df) == 3
        assert 'param1' in df.columns
        assert 'param2' in df.columns
        assert 'time' in df.columns or ('time', 0) in df.columns


class TestConvenienceFunctions:
    """Test cases for convenience functions."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.temp_dir = tempfile.mkdtemp()
        self.create_test_files()
    
    def teardown_method(self):
        """Clean up test fixtures."""
        shutil.rmtree(self.temp_dir)
    
    def create_test_files(self):
        """Create test input and output files."""
        self.input_files = []
        self.output_files = []
        
        for i in range(2):
            # Create input file
            input_file = Path(self.temp_dir) / f"input_{i}.json"
            input_data = {
                "x": 1.0 + i * 0.5,
                "y": 2.0 + i * 0.3,
                "n": 100 + i * 10
            }
            with open(input_file, "w") as f:
                json.dump(input_data, f)
            self.input_files.append(str(input_file))
            
            # Create output file
            output_file = Path(self.temp_dir) / f"output_{i}.csv"
            output_data = pd.DataFrame({
                "result": [10.0 + i, 11.0 + i, 12.0 + i],
                "status": ["ok", "ok", "ok"]
            })
            output_data.to_csv(output_file, index=False)
            self.output_files.append(str(output_file))
    
    def test_create_campaign_from_files(self):
        """Test creating campaign from file lists."""
        campaign = create_campaign_from_files(
            input_files=self.input_files,
            output_files=self.output_files,
            campaign_name="test_files_campaign",
            work_dir=self.temp_dir
        )
        
        assert campaign.campaign_name == "test_files_campaign"
        
        # Check that runs were imported
        runs = list(campaign.list_runs())
        assert len(runs) == 2
        
        # Check collation results
        df = campaign.get_collation_result()
        assert len(df) == 2
        assert 'x' in df.columns
        assert 'y' in df.columns
        assert 'n' in df.columns
    
    def test_create_campaign_from_directory(self):
        """Test creating campaign from directory."""
        # Create a directory structure
        data_dir = Path(self.temp_dir) / "data"
        data_dir.mkdir()
        
        for i in range(2):
            run_dir = data_dir / f"simulation_{i}"
            run_dir.mkdir()
            
            # Input file
            input_data = {"param": 5.0 + i}
            with open(run_dir / "config.json", "w") as f:
                json.dump(input_data, f)
            
            # Output file
            output_data = pd.DataFrame({"output": [1.0 + i, 2.0 + i]})
            output_data.to_csv(run_dir / "results.csv", index=False)
        
        campaign = create_campaign_from_directory(
            root_dir=str(data_dir),
            campaign_name="test_dir_campaign",
            work_dir=self.temp_dir
        )
        
        assert campaign.campaign_name == "test_dir_campaign"
        
        # Check that runs were imported
        runs = list(campaign.list_runs())
        assert len(runs) == 2


class TestCampaignFromExistingData:
    """Test cases for Campaign.from_existing_data method."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.temp_dir = tempfile.mkdtemp()
        self.create_test_files()
    
    def teardown_method(self):
        """Clean up test fixtures."""
        shutil.rmtree(self.temp_dir)
    
    def create_test_files(self):
        """Create test input and output files."""
        self.input_files = []
        self.output_files = []
        
        for i in range(3):
            # Create input file
            input_file = Path(self.temp_dir) / f"params_{i}.json"
            input_data = {
                "temperature": 300.0 + i * 10,
                "pressure": 1.0 + i * 0.1,
                "iterations": 1000 + i * 100
            }
            with open(input_file, "w") as f:
                json.dump(input_data, f)
            self.input_files.append(str(input_file))
            
            # Create output file
            output_file = Path(self.temp_dir) / f"results_{i}.csv"
            output_data = pd.DataFrame({
                "energy": [100.0 + i * 5, 101.0 + i * 5, 102.0 + i * 5],
                "force": [0.1 + i * 0.01, 0.11 + i * 0.01, 0.12 + i * 0.01]
            })
            output_data.to_csv(output_file, index=False)
            self.output_files.append(str(output_file))
    
    def test_from_existing_data(self):
        """Test Campaign.from_existing_data method."""
        campaign = uq.Campaign.from_existing_data(
            name="imported_campaign",
            input_files=self.input_files,
            output_files=self.output_files,
            work_dir=self.temp_dir
        )
        
        assert campaign.campaign_name == "imported_campaign"
        
        # Check that runs were imported
        runs = list(campaign.list_runs())
        assert len(runs) == 3
        
        # Check collation results
        df = campaign.get_collation_result()
        assert len(df) == 3
        assert 'temperature' in df.columns
        assert 'pressure' in df.columns
        assert 'iterations' in df.columns


class TestErrorHandling:
    """Test error handling and edge cases."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.temp_dir = tempfile.mkdtemp()
    
    def teardown_method(self):
        """Clean up test fixtures."""
        shutil.rmtree(self.temp_dir)
    
    def test_nonexistent_directory(self):
        """Test handling of non-existent directory."""
        nonexistent = "/path/that/does/not/exist"
        
        with pytest.raises(ValueError, match="Root directory does not exist"):
            DatasetImporter(nonexistent)
    
    def test_mismatched_file_counts(self):
        """Test handling of mismatched input/output file counts."""
        input_files = ["file1.json", "file2.json"]
        output_files = ["file1.csv"]  # One less than input files
        
        with pytest.raises(ValueError, match="Number of input files must match"):
            create_campaign_from_files(input_files, output_files)
    
    def test_no_runs_discovered(self):
        """Test handling when no runs are discovered."""
        empty_dir = Path(self.temp_dir) / "empty"
        empty_dir.mkdir()
        
        importer = DatasetImporter(str(empty_dir))
        discovered = importer.discover_directory_structure()
        
        assert discovered['structure_type'] == 'unknown'
        assert len(discovered['runs']) == 0
        
        # Should raise error when trying to create campaign
        with pytest.raises(ValueError, match="No runs discovered"):
            importer.create_campaign_from_dataset()
    
    def test_invalid_file_format(self):
        """Test handling of invalid file formats."""
        # Create a file with invalid JSON
        invalid_file = Path(self.temp_dir) / "invalid.json"
        with open(invalid_file, "w") as f:
            f.write("{ invalid json content")
        
        importer = DatasetImporter(str(self.temp_dir))
        # Should handle parsing errors gracefully
        params = importer._parse_input_file(str(invalid_file))
        # Should return empty dict for invalid files
        assert isinstance(params, dict)
