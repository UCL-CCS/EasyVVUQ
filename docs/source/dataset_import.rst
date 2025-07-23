.. _dataset_import:

Dataset Import Guide
====================

Overview
--------

This guide addresses **GitHub Issue #116: "Add functionality to pick up existing datasets"** by providing **two distinct approaches** for working with existing simulation data in EasyVVUQ:

1. **Campaign Creation**: Import data to create full EasyVVUQ campaigns
2. **Analysis-Only**: Direct analysis without campaign overhead

Quick Start: Choose Your Approach
---------------------------------

Decision Matrix
~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - **Your Goal**
     - **Recommended Approach**
   * - Quick analysis of existing results
     - **Analysis-Only**
   * - Building UQ workflow
     - **Campaign Creation**
   * - Need both flexibility and organization
     - **Hybrid**
   * - Maximum performance
     - **Analysis-Only**
   * - Collaborative project
     - **Campaign Creation**
   * - Custom analysis + future expansion
     - **Hybrid**

Approach 1: Campaign Creation + Analysis
----------------------------------------

When to Use
~~~~~~~~~~~

- Building ongoing UQ workflows
- Need to add more runs or resample
- Want full parameter management
- Using EasyVVUQ sampling methods
- Collaborative projects (shared database)

Basic Example
~~~~~~~~~~~~~

.. code-block:: python

    from easyvvuq.utils import dataset_importer

    # Method 1: From directory structure
    campaign = dataset_importer.create_campaign_from_directory(
        root_dir="/path/to/simulation/data",
        campaign_name="my_campaign",
        work_dir="/path/to/work/dir"
    )

    # Method 2: From file lists
    campaign = dataset_importer.create_campaign_from_files(
        input_files=["run1/input.json", "run2/input.json"],
        output_files=["run1/output.csv", "run2/output.csv"],
        campaign_name="my_campaign",
        work_dir="/path/to/work/dir"
    )

    # Method 3: Campaign class method
    campaign = uq.Campaign.from_existing_data(
        name="my_campaign",
        input_files=input_files,
        output_files=output_files,
        work_dir="/path/to/work/dir"
    )

Advanced Features
~~~~~~~~~~~~~~~~~

.. code-block:: python

    # Get collated results
    df = campaign.get_collation_result()

    # Apply EasyVVUQ analysis
    analysis = uq.analysis.EnsembleBoot(
        qoi_cols=[('output_column', 0)],
        stat_func=np.mean
    )
    campaign.apply_analysis(analysis)
    results = campaign.get_last_analysis()

    # Extend campaign with more runs
    campaign.add_external_runs(new_runs)
    campaign.draw_samples(num_samples=50)
    campaign.execute().collate()

Benefits
~~~~~~~~

- Full parameter space management
- Can add more runs and resample
- Database storage and retrieval
- Run status tracking
- Integration with EasyVVUQ sampling methods
- Suitable for ongoing UQ workflows

Considerations
~~~~~~~~~~~~~~

- Higher memory usage
- Campaign database overhead
- Requires parameter definitions

Approach 2: Analysis-Only (Direct DataFrame Analysis)
------------------------------------------------------

When to Use
~~~~~~~~~~~

- Quick analysis tasks
- Custom analysis methods
- Integration with other tools
- Maximum performance needed
- Exploratory data analysis

Basic Example
~~~~~~~~~~~~~

.. code-block:: python

    import pandas as pd
    import numpy as np
    import easyvvuq as uq

    # Load your data directly into DataFrame
    df = pd.DataFrame({
        ('run_id', 0): range(100),
        ('x1', 0): np.random.uniform(0, 1, 100),
        ('x2', 0): np.random.uniform(0, 1, 100),
        ('output', 0): np.random.normal(0, 1, 100)
    })

    # Method 1: Direct pandas/numpy analysis
    mean_output = np.mean(df[('output', 0)])
    std_output = np.std(df[('output', 0)])
    correlation = np.corrcoef(df[('x1', 0)], df[('output', 0)])[0, 1]

    # Method 2: Use EasyVVUQ analysis classes directly
    ensemble_analysis = uq.analysis.EnsembleBoot(
        qoi_cols=[('output', 0)],
        stat_func=np.mean
    )
    results = ensemble_analysis.analyse(df)

Advanced Custom Analysis
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    # Custom sensitivity analysis
    def elementary_effects(df, param_col, output_col):
        median_val = df[param_col].median()
        high_group = df[df[param_col] > median_val][output_col]
        low_group = df[df[param_col] <= median_val][output_col]
        return high_group.mean() - low_group.mean()

    # Statistical tests
    from scipy import stats
    t_stat, p_value = stats.ttest_ind(group1, group2)

    # Machine learning
    from sklearn.linear_model import LinearRegression
    model = LinearRegression()
    model.fit(X, y)
    coefficients = model.coef_

Benefits
~~~~~~~~

- No campaign overhead - maximum performance
- Direct DataFrame manipulation
- Custom analysis methods easy to implement
- Works with any DataFrame structure
- Easy integration with pandas, numpy, scipy, sklearn
- Suitable for quick analysis and exploration

Considerations
~~~~~~~~~~~~~~

- No parameter management
- Can't easily add more runs
- Manual data organization

Approach 3: Hybrid (Best of Both Worlds)
-----------------------------------------

When to Use
~~~~~~~~~~~

- Complex workflows
- Need both organization and flexibility
- Production UQ pipelines
- Mixed analysis requirements

Example
~~~~~~~

.. code-block:: python

    # Create campaign for organization
    campaign = dataset_importer.create_campaign_from_files(
        input_files=input_files,
        output_files=output_files,
        campaign_name="hybrid_campaign"
    )

    # Extract DataFrame for custom analysis
    df = campaign.get_collation_result()

    # Custom analysis
    custom_results = my_custom_analysis(df)

    # Campaign analysis
    campaign.apply_analysis(uq.analysis.EnsembleBoot(qoi_cols=[('output', 0)]))
    campaign_results = campaign.get_last_analysis()

    # Still can extend campaign
    campaign.add_external_runs(new_runs)

Benefits
~~~~~~~~

- Organized campaign management
- Custom analysis flexibility
- Can combine EasyVVUQ tools with custom methods
- Extensible for future work
- Best choice for complex workflows

Data Format Requirements
------------------------

Campaign Creation Approach
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Requires both input parameters AND output results:

**Input Files** (JSON, YAML, or CSV):

.. code-block:: json

    {
      "parameter1": 1.0,
      "parameter2": 2.0,
      "parameter3": "string_value"
    }

**Output Files** (CSV, JSON, or YAML):

.. code-block:: csv

    time,temperature,pressure
    0,300.0,1.0
    1,301.0,1.01
    2,302.0,1.02

Analysis-Only Approach
~~~~~~~~~~~~~~~~~~~~~~

Works with any pandas DataFrame structure:

.. code-block:: python

    # Flexible DataFrame format
    df = pd.DataFrame({
        'param1': [1.0, 2.0, 3.0],
        'param2': [10.0, 20.0, 30.0],
        'output1': [100.0, 150.0, 200.0],
        'output2': [0.1, 0.2, 0.3]
    })

    # Or EasyVVUQ multi-index format
    df = pd.DataFrame({
        ('param1', 0): [1.0, 2.0, 3.0],
        ('param2', 0): [10.0, 20.0, 30.0],
        ('output1', 0): [100.0, 150.0, 200.0]
    })

Directory Structure Support
---------------------------

Supported Structures
~~~~~~~~~~~~~~~~~~~~~

**Run Directories**:

.. code-block:: text

    data/
    ├── run_001/
    │   ├── input.json
    │   └── output.csv
    ├── run_002/
    │   ├── input.json
    │   └── output.csv
    └── ...

**File Lists**:

.. code-block:: text

    data/
    ├── inputs/
    │   ├── params_001.json
    │   ├── params_002.json
    │   └── ...
    └── outputs/
        ├── results_001.csv
        ├── results_002.csv
        └── ...

File Format Support
--------------------

Input Files
~~~~~~~~~~~

- **JSON**: Parameter definitions
- **YAML**: Configuration files
- **CSV**: Tabular parameter data

Output Files
~~~~~~~~~~~~

- **CSV**: Simulation results (most common)
- **JSON**: Structured output data
- **YAML**: Configuration outputs

Analysis Classes Compatibility
------------------------------

Works with Both Approaches
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``EnsembleBoot``: Bootstrap analysis
- ``BasicStats``: Basic statistics

Requires Campaign (with proper samplers)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``PCEAnalysis``: Polynomial Chaos Expansion
- ``SCAnalysis``: Stochastic Collocation
- ``QMCAnalysis``: Quasi-Monte Carlo

Analysis-Only Compatible
~~~~~~~~~~~~~~~~~~~~~~~~

- Direct pandas/numpy operations
- scipy.stats functions
- sklearn models
- Custom analysis functions

Performance Comparison
----------------------

.. list-table::
   :header-rows: 1
   :widths: 20 20 20 20

   * - **Aspect**
     - **Campaign Creation**
     - **Analysis-Only**
     - **Hybrid**
   * - **Memory Usage**
     - Higher
     - Lower
     - Medium
   * - **Setup Time**
     - Longer
     - Shorter
     - Medium
   * - **Analysis Speed**
     - Medium
     - Fastest
     - Medium
   * - **Extensibility**
     - High
     - Low
     - High
   * - **Flexibility**
     - Medium
     - High
     - High

Error Handling
--------------

Campaign Creation
~~~~~~~~~~~~~~~~~

.. code-block:: python

    try:
        campaign = dataset_importer.create_campaign_from_directory(
            root_dir="/path/to/data",
            campaign_name="my_campaign"
        )
    except FileNotFoundError:
        print("Data directory not found")
    except ValueError as e:
        print(f"Invalid data format: {e}")

Analysis-Only
~~~~~~~~~~~~~

.. code-block:: python

    try:
        df = pd.read_csv("results.csv")
        analysis = uq.analysis.EnsembleBoot(qoi_cols=[('output', 0)])
        results = analysis.analyse(df)
    except Exception as e:
        print(f"Analysis failed: {e}")
        # Fallback to direct pandas analysis
        mean_val = df['output'].mean()

Code Examples
-------------

The documentation above provides comprehensive code examples for all approaches. Users can copy and adapt these examples for their specific use cases. The test suite in ``tests/test_dataset_importer.py`` also provides practical examples of how to use the functionality.

Best Practices
--------------

Campaign Creation
~~~~~~~~~~~~~~~~~

- Use consistent parameter names across runs
- Ensure all required parameters are present
- Use appropriate file formats (JSON for parameters, CSV for results)
- Test with small datasets first

Analysis-Only
~~~~~~~~~~~~~

- Use pandas DataFrame best practices
- Handle missing data appropriately
- Use vectorized operations for performance
- Consider memory usage for large datasets

Hybrid
~~~~~~

- Start with campaign creation for organization
- Extract DataFrame for custom analysis
- Use campaign features for extension
- Document both approaches in your workflow

Migration from Existing Workflows
---------------------------------

From Manual Analysis
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    # Before: Manual file loading
    for file in files:
        data = pd.read_csv(file)
        # manual analysis...

    # After: Analysis-Only approach
    df = load_all_data_to_dataframe(files)
    results = uq.analysis.EnsembleBoot(qoi_cols=['output']).analyse(df)

From Other UQ Tools
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    # Convert existing data to EasyVVUQ format
    df_easyvvuq = convert_to_easyvvuq_format(external_data)
    campaign = dataset_importer.create_campaign_from_dataframe(df_easyvvuq)

Troubleshooting
---------------

Common Issues
~~~~~~~~~~~~~

**Campaign Creation**:

- *File not found*: Check file paths and permissions
- *Parameter mismatch*: Ensure consistent parameter names
- *Invalid format*: Verify JSON/CSV syntax

**Analysis-Only**:

- *Column not found*: Check DataFrame column names
- *Analysis failed*: Verify data types and ranges
- *Memory error*: Consider chunking large datasets

Getting Help
~~~~~~~~~~~~

1. Check the error message carefully
2. Review the demo scripts for examples
3. Check the EasyVVUQ documentation
4. Use the test suite for reference implementations
