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

Here the specified :code:`polynomial_order`, and the number of inputs in :code:`vary`, determine the
number of samples, which increases exponentially fast with an increasing amount of inputs. This
is the so-called *curse of dimensionality*. Sparse grids do **not** circumvent the curse of 
dimensionality, although they can postpone its effect to higher dimensions. In the case of a standard
EasyVVUQ Canpaign, by setting :code:`polynomial_order=3` we create a sampling through a 
single tensor product of one-dimensional quadrature rules with order 3 for every input. It is this tensor 
product construction that leads to the exponential rise in cost. Sparse grids on the other hand, do not
create a single tensor product, but build the sampling plan from the ground up by using a linear combination
of tensor products involving 1D quadrature rules of different orders. For two inputs, we might for instance 
consider using 1D quadrature rules of order [1, 1], [1, 2] and [2, 1], whereas a standard EasyVVUQ campaign
with :code:`polynomial_order=2` uses just [2,2]. If the chosen quadrature rule generates 1 point for order 1 
and 3 points for order 2, then [2, 2] (the 2nd order rule for both dimensions) will generate 3*3 = 9 points.




