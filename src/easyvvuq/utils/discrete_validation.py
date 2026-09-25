"""
Utilities for handling discrete distribution validation in EasyVVUQ.

This module provides enhanced validation capabilities for discrete distributions
when used with Stochastic Collocation (SC) and Polynomial Chaos Expansion (PCE) methods.
"""
import chaospy as cp
from typing import Any, Dict, Union


def is_integer_valued(value: Any) -> bool:
    """
    Check if a value represents an integer, even if it's stored as a float.
    
    This is crucial for handling chaospy output where discrete distributions
    may return float arrays for numerical consistency with continuous distributions.
    
    Parameters
    ----------
    value : Any
        The value to check
        
    Returns
    -------
    bool
        True if the value represents an integer
    """
    try:
        # Handle numpy arrays and scalars
        if hasattr(value, '__iter__') and not isinstance(value, (str, bytes)):
            # For arrays, check if all elements are integer-valued
            return all(is_integer_valued(v) for v in value)
        
        # Convert to float first to handle various numeric types
        float_val = float(value)
        
        # Check if it's close to an integer
        return abs(float_val - round(float_val)) < 1e-10
    except (ValueError, TypeError):
        return False


def convert_to_integer(value: Any) -> Union[int, Any]:
    """
    Convert a value to integer if it represents an integer, otherwise return as-is.
    
    Parameters
    ----------
    value : Any
        The value to convert
        
    Returns
    -------
    Union[int, Any]
        Integer value if conversion is valid, otherwise the original value
    """
    if is_integer_valued(value):
        return int(round(float(value)))
    return value


def validate_discrete_parameter(value: Any, param_def: Dict[str, Any]) -> bool:
    """
    Validate a parameter value for discrete distributions.
    
    This function handles the case where chaospy returns float values
    for discrete distributions, especially in mixed discrete/continuous scenarios.
    
    Parameters
    ----------
    value : Any
        The parameter value to validate
    param_def : Dict[str, Any]
        Parameter definition from the campaign
        
    Returns
    -------
    bool
        True if the value is valid for this parameter
    """
    param_type = param_def.get('type', 'float')
    
    # For integer parameters, check if the value is integer-valued
    if param_type == 'integer':
        if not is_integer_valued(value):
            return False
        
        # Check bounds if specified
        int_val = convert_to_integer(value)
        if 'min' in param_def and int_val < param_def['min']:
            return False
        if 'max' in param_def and int_val > param_def['max']:
            return False
    
    return True


def is_discrete_distribution(distribution) -> bool:
    """
    Check if a distribution is discrete.
    
    Parameters
    ----------
    distribution
        A chaospy distribution object
        
    Returns
    -------
    bool
        True if the distribution is discrete
    """
    return isinstance(distribution, cp.DiscreteUniform)


def get_discrete_parameter_info(vary: Dict[str, Any]) -> Dict[str, bool]:
    """
    Identify which parameters use discrete distributions.
    
    Parameters
    ----------
    vary : Dict[str, Any]
        Dictionary of parameter names to chaospy distributions
        
    Returns
    -------
    Dict[str, bool]
        Dictionary mapping parameter names to whether they are discrete
    """
    discrete_info = {}
    for param_name, distribution in vary.items():
        discrete_info[param_name] = is_discrete_distribution(distribution)
    return discrete_info


def process_sampler_output(run_dict: Dict[str, Any], params_spec, vary: Dict[str, Any]) -> Dict[str, Any]:
    """
    Process sampler output to handle discrete distributions properly.
    
    This function converts float values to integers for parameters that should be integers
    but were returned as floats by chaospy due to mixed distribution scenarios.
    
    Parameters
    ----------
    run_dict : Dict[str, Any]
        Dictionary of parameter values from the sampler
    params_spec : ParamsSpecification
        Parameter specification object
    vary : Dict[str, Any]
        Dictionary of parameter names to chaospy distributions
        
    Returns
    -------
    Dict[str, Any]
        Processed run dictionary with correct types
    """
    processed_run = run_dict.copy()
    
    # Get discrete parameter information
    discrete_info = get_discrete_parameter_info(vary)
    
    for param_name, value in run_dict.items():
        if param_name in params_spec.params_dict:
            param_def = params_spec.params_dict[param_name]
            param_type = param_def.get('type', 'float')
            
            # Convert float to int for integer parameters from discrete distributions
            if param_type == 'integer' and discrete_info.get(param_name, False):
                if is_integer_valued(value):
                    processed_run[param_name] = convert_to_integer(value)
    
    return processed_run
