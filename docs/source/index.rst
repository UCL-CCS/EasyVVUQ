.. EasyVVUQ documentation master file, created by
   sphinx-quickstart on Tue May 28 17:54:08 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

EasyVVUQ: Uncertainty intervals for everyone!
=============================================

EasyVVUQ is a Python library designed to facilitate verification, validation 
and uncertainty quantification (VVUQ) for a wide variety of simulations.
It was conceived and developed within the EU funded `VECMA <http://www.vecma.eu/>`_ 
(Verified Exascale Computing for Multiscale Applications) project.

A good introduction can be found in the paper by D. Suleimenova *et al.*, “Tutorial applications for Verification, Validation and Uncertainty Quantification using VECMA toolkit”, J. Comput. Sci. 53, 101402 (2021), `DOI:10.1016/j.jocs.2021.101402 <https://doi.org/10.1016/j.jocs.2021.101402>`_.

.. _goals:

Goals
=====

The purpose of EasyVVUQ is to make it as easy as possible to implement 
advanced techniques for uncertainty quantification for existing 
application codes (or workflows).
We do not intend to re-invent the wheel, and plan on always building 
upon existing libraries such as
`Chaospy <https://chaospy.readthedocs.io/>`_ which focus on providing
statistical functionality.
Our aim is to expose these features in as accessible a way for users 
of scientific codes, in particular simulation software targeting HPC 
machines.

For technical details please see :ref:`api-ref`.

We also provide a range of interactive tutorials within the repository. 
This collection changes over time, but can be found 
here: https://github.com/UCL-CCS/EasyVVUQ/tree/dev/tutorials .

Another point of reference point are the non-regression tests which
can be found at https://github.com/UCL-CCS/EasyVVUQ/tree/dev/tests .
These are often useful in showing how pieces of the software work.


.. _toc:

Table of contents
-----------------

.. toctree::
   :maxdepth: 2
   :caption: Contents

   installation
   concepts
   

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
* :doc:`_autodoc/modules`
