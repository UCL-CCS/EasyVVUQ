.. _concepts:

Conceptual Basis
================

EasyVVUQ was created as part of the `VECMA <http://www.vecma.eu/>`_ project.
The aim of this project was to make state of the art VVUQ algorithms 
available for use in HPC applications (and specifically multiscale models).
The basis of making generic tools within VECMA is the idea of *Patterns*,
which are:

    “abstractions that describe, in a non-application and non-domain 
    specific manner, a workflow or algorithm for conducting validation, 
    verification, uncertainty quantification or sensitivity analysis”

Making use of Patterns in practice requires that they are decomposed into 
components which can be flexibly combined to implement a range of algorithms.

.. figure:: images/vecma-algorithms.svg
   :scale: 50 %
   :alt: VVUQ algorithm as connected elements.

   Figure 1: Decomposition of generalized VVUQ workflow into different 
   functions.
   These are implemented as 'Elements' in EasyVVUQ.
   Rounded boxes are specified by users to tailor general workflows to thier
   particular use case


Elements
--------

Sampler
-------

Decoders
--------

Encoders
--------

Collation
---------

Analysis
--------
