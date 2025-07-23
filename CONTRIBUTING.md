# Contributing to EasyVVUQ

Thank you for your interest in contributing to EasyVVUQ! This document provides guidelines for contributing to the project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Contributing Process](#contributing-process)
- [Code Style and Standards](#code-style-and-standards)
- [Git Commit Guidelines](#git-commit-guidelines)
- [Testing](#testing)
- [Documentation](#documentation)
- [Submitting Changes](#submitting-changes)
- [Community](#community)

## Code of Conduct

This project adheres to a code of conduct. By participating, you are expected to uphold this code. Please see [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for details.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Git
- Basic knowledge of uncertainty quantification concepts (helpful but not required)

### Areas for Contribution

We welcome contributions in several areas:

- **Bug fixes**: Help us identify and fix issues
- **New features**: Implement new UQ methods or functionality
- **Documentation**: Improve guides, API docs, and examples
- **Testing**: Add test cases and improve test coverage
- **Performance**: Optimize existing algorithms
- **Examples**: Create tutorials and real-world examples

## Development Setup

### 1. Fork and Clone

```bash
# Fork the repository on GitHub, then clone your fork
git clone https://github.com/YOUR_USERNAME/EasyVVUQ.git
cd EasyVVUQ
git remote add upstream https://github.com/UCL-CCS/EasyVVUQ.git
```

### 2. Create Development Environment

```bash
# Create a virtual environment
python -m venv easyvvuq-dev
source easyvvuq-dev/bin/activate  # On Windows: easyvvuq-dev\Scripts\activate

# Install development dependencies
pip install -e .
pip install -r requirements.txt
```

### 3. Install Development Tools

```bash
# Install additional development tools
pip install pytest autopep8 flake8 sphinx
```

### 4. Verify Installation

```bash
# Run tests to ensure everything is working
./run_tests.sh

# Or manually:
python -m pytest tests/
```

## Contributing Process

### 1. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/issue-number-description
```

### 2. Make Changes

- Write clear, well-documented code
- Follow the existing code style
- Add tests for new functionality
- Update documentation as needed

### 3. Test Your Changes

```bash
# Run the full test suite
./run_tests.sh

# Run specific tests
python -m pytest tests/test_specific_module.py

# Check code style
./fix_pep8.sh
```

## Code Style and Standards

### Python Style

- Follow **PEP 8** guidelines
- Use the provided `fix_pep8.sh` script for automatic formatting
- Maximum line length: **100 characters**
- Use meaningful variable and function names
- Add type hints where appropriate

### Code Formatting

Before committing, run:

```bash
# Auto-format code
./fix_pep8.sh

# Check for style issues
flake8 easyvvuq/ tests/ --max-line-length=100
```

### Documentation Style

- Use **Google-style docstrings** for functions and classes
- Include parameter types and return types
- Provide examples where helpful

Example:

```python
def my_function(param1: str, param2: int) -> bool:
    """Brief description of the function.
    
    Longer description if needed.
    
    Args:
        param1: Description of parameter 1.
        param2: Description of parameter 2.
        
    Returns:
        Description of return value.
        
    Raises:
        ValueError: When parameter is invalid.
        
    Example:
        >>> result = my_function("test", 42)
        >>> print(result)
        True
    """
    pass
```

## Git Commit Guidelines

### Commit Message Format

We follow a **simple and practical approach** to commit messages:

- **Use short, concise commit messages** (50 characters or less)
- **Write in imperative mood** (e.g., "Fix bug" not "Fixed bug" or "Fixes bug")
- **Save detailed explanations for the PR description**

### Examples of Good Commit Messages

```bash
git commit -m "Fix sampling bug in MC analysis"
git commit -m "Add Gaussian process surrogate support"
git commit -m "Update installation instructions"
git commit -m "Improve test coverage for encoders"
```

### What NOT to Include in Commit Messages

- Detailed explanations (save these for PR descriptions)
- Multiple unrelated changes (split into separate commits)
- Periods at the end of the message
- Commit messages longer than one line

### Detailed Information Goes in Pull Requests

When creating a PR, include:

- **What** you changed (detailed description)
- **Why** you made the change (motivation/problem solved)
- **How** you implemented it (technical approach)
- **Testing** performed
- **Breaking changes** if any

Example PR description:

```text
## Fix sampling bug in Monte Carlo analysis

### Problem
The MC sampler was incorrectly handling edge cases when the sample size 
was smaller than the number of parameters, causing IndexError.

### Solution
- Added validation for sample size vs parameter count
- Improved error handling with descriptive messages
- Added fallback behavior for small sample sizes

### Testing
- Added unit tests covering edge cases
- Verified existing functionality still works
- Tested with various parameter combinations
```

## Testing

### Running Tests

```bash
# Run all tests
./run_tests.sh

# Run specific test file
python -m pytest tests/test_campaign.py

# Run with coverage
python -m pytest tests/ --cov=easyvvuq --cov-report=html
```

### Writing Tests

- Place tests in the `tests/` directory
- Use descriptive test names: `test_campaign_creation_with_valid_parameters`
- Test both success and failure cases
- Mock external dependencies when appropriate
- Include integration tests for end-to-end workflows

### Test Structure

```python
import pytest
from easyvvuq import Campaign

def test_campaign_creation():
    """Test that a campaign can be created successfully."""
    campaign = Campaign(name="test_campaign")
    assert campaign.name == "test_campaign"

def test_campaign_invalid_input():
    """Test that invalid input raises appropriate error."""
    with pytest.raises(ValueError):
        Campaign(name="")
```

## Documentation

### Building Documentation

```bash
cd docs/
make html
# Documentation will be in docs/build/html/
```

### Adding Examples

- Place example scripts in `tutorials/`
- Include both simple and advanced examples
- Ensure examples are well-commented
- Test that examples run successfully

## Submitting Changes

### 1. Prepare Your Pull Request

```bash
# Ensure your branch is up to date
git fetch upstream
git rebase upstream/dev

# Push to your fork
git push origin your-branch-name
```

### 2. Create Pull Request

- Use a clear, descriptive title
- Reference any related issues (#123)
- Describe what changes you made and why
- Include screenshots for UI changes
- List any breaking changes

### Pull Request Template

```text
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement
- [ ] Other (please describe)

## Testing
- [ ] Tests pass locally
- [ ] Added new tests
- [ ] Updated documentation

## Related Issues
Fixes #123

## Breaking Changes
None / List any breaking changes
```

### 3. Code Review Process

- All PRs require review before merging
- Address reviewer feedback promptly
- Keep PRs focused and reasonably sized
- Maintain a clean commit history

## Community

### Getting Help

- **GitHub Issues**: Report bugs or request features
- **GitHub Discussions**: Ask questions and discuss ideas
- **Documentation**: Check our [API documentation](https://ucl-ccs.github.io/EasyVVUQ/)

### Communication

- Be respectful and constructive in all interactions
- Use clear, descriptive issue titles and descriptions
- Search existing issues before creating new ones
- Provide minimal reproducible examples for bugs

## Recognition

Contributors are recognized in several ways:

- Listed in `CONTRIBUTIONS.md` (credits file)
- Mentioned in release notes for significant contributions
- Co-authorship on relevant publications (for major contributions)

## Questions?

If you have questions not covered in this guide, please:

1. Check existing [GitHub Issues](https://github.com/UCL-CCS/EasyVVUQ/issues)
2. Create a new issue with the "question" label
3. Join the discussion in [GitHub Discussions](https://github.com/UCL-CCS/EasyVVUQ/discussions)

Thank you for contributing to EasyVVUQ!

---

*This contributing guide is inspired by best practices from the Python scientific computing community.*
