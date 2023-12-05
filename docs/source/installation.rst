.. _installation:

EasyVVUQ installation
=====================

Installation
------------

.. note:: To use the library you will need Python 3.8+.

Installation should be straight forward::

    pip install easyvvuq

To update an existing installation::

    pip install easyvvuq --upgrade
  
Alternatively, to get the most current version, the code can be installed from
Github as follows::

    git clone https://github.com/UCL-CCS/EasyVVUQ.git
    cd EasyVVUQ
    bash install_EasyVVUQ.sh

.. note:: The `install_EasyVVUQ.sh` script above assumes that your default `python`
          is Python 3. If that is not the case replace `python` with `python3` and
          `pip` with `pip3`.

Depending on your setup you may not have permission to install packages.
In that case, we recommend creating a virtual environment using  
`conda <https://docs.conda.io/projects/conda/en/latest/user-guide/install/>`_
or `pipenv <https://docs.pipenv.org>`_.

Questions & Troubleshooting
---------------------------

For any problems and questions you might have related to ``EasyVVUQ``, please
feel free to file an `<https://github.com/UCL-CCS/EasyVVUQ/issues>`_.
