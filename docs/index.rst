.. EasyVVUQ documentation master file, created by
   sphinx-quickstart on Tue May 28 17:54:08 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

EasyVVUQ: Error bars for everyone!
====================================

EasyVVUQ is a Python library designed to facilitate verification, validation 
and uncertainty quantification (VVUQ) for a wide variety of simulations.
It was conceived and developed within the EU funded `VECMA <http://www.vecma.eu/>`_ 
(Verified Exascale Computing for Multiscale Applications) project.

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

.. _toc:

Table of contents
-----------------

.. toctree::
   :maxdepth: 1

   installation
   concepts
   basic_tutorial
   cooling_coffee_cup
   multisampler_tutorial
   restartable_campaign_tutorial
   custom_encoder

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
