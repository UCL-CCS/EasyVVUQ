.. _hier_sparse_grid_tutorial:

Hierarchical sparse grid tutorial
==============

This tutorial shows how to use a sparse Stochastic Collocation sampler
in EasyVVUQ. We will assume you are familiar with the basic building
block of an EasyVVUQ Campaign. If not, see the basic tutorial 
`here <https://github.com/UCL-CCS/EasyVVUQ/blob/dev/docs/basic_tutorial.rst>`_.

The complete code for this example can be found `here <https://github.com/UCL-CCS/EasyVVUQ/blob/dev/tests/test_hierarchical_sparse_grid_sc.py>`__. This file 
demonstates the sparse grid using a analytic test function, for which we compute
exact reference statistics.

Sparse grids
------------

Let us briefly describe the concept behind sparse grids. In a standard EasyVVUQ
Campaign, an SC sampler object might be created via::

    my_sampler = uq.sampling.SCSampler(vary=vary, polynomial_order=3,
                                       quadrature_rule="G")

Here the specified polynomial_order, and the number of inputs in vary, determine the
number of samples. 

