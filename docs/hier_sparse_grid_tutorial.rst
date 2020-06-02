.. _hier_sparse_grid_tutorial:

Hierarchical sparse grid tutorial
==============

This tutorial shows how to use a sparse Stochastic Collocation (SC) sampler
in EasyVVUQ. We will assume you are familiar with the basic building
blocks of an EasyVVUQ Campaign. If not, see the basic tutorial 
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
EasyVVUQ Canpaign, by setting :code:`polynomial_order=3` we create a sampling plan through a 
single tensor product of one-dimensional quadrature rules with order 3 for every input. It is this tensor 
product construction that leads to the exponential rise in cost. Sparse grids on the other hand, do not
create a single tensor product, but build the sampling plan from the ground up by using a linear combination
of tensor products involving 1D quadrature rules of different orders. For two inputs, we might for instance 
consider using 1D quadrature rules of order [1, 1], [1, 2] and [2, 1], whereas a standard EasyVVUQ campaign
with :code:`polynomial_order=2` uses just [2,2]. If the chosen quadrature rule generates 1 point for order 1 
and 3 points for order 2, then [2, 2] (the 2nd order rule for both dimensions) will generate 3*3 = 9 points.
For the sparse grid we have a linear combination of:

    * [1, 1]: a single point in the 2D domain (X, Y)
    * [1, 2]: a line of 3 points with constant X
    * [2, 1]: a line of 3 points with constant Y

In the case of sparse grids it is common to select a *nested* quadrature rule. This means that the quadrature
rule of order p contains all points of the same rule of order p-1. When taking the linear combinations, a nested rule ensures that many points will conincide, which yields efficient sampling 
plans, especially in higher dimensions. If our 1D rule of order 1 and 2 generates the points [0.5] and [0, 0.5, 1]
we obtain a sampling plan consisting of

    * [1, 1]: [0.5, 0.5]
    * [1, 2]: [0.5, 0.0], [0.5, 0.5], [0.5, 1.0]
    * [2, 1]: [0.0, 0.5], [0.5, 0.5], [1.0, 0.5],

which gives a total of 5 unique points, compared to the 9 points of [2, 2]. 

Create a sparse SC sampler
--------------------------

An example sparse SC sampler is given by::

    my_sampler = uq.sampling.SCSampler(vary=vary, polynomial_order=poly_order,
                                       quadrature_rule="C", sparse=True,
                                       growth=True)
                                       
Here :code:`"C"` stands for the Clenshaw Curtis rule, which can be made nested by turning on the :code:`growth`
flag. You can also select other quadrature rules, e.g. the standard Gaussian option (:code:`"G"`). Not all
rules can be made nested though, see the Chaospy `documentation <https://chaospy.readthedocs.io/en/master/quadrature.html>`_
for a list of all quadrature rules and their properties.

The rest of the Campaign proceed exactly as it would in the non-sparse case. The only exception is in the case of
a nested rule, in which case the sampling plan can be isotropically refined. This is done with the following command::

    #update the sparse grid to the next level
    my_sampler.next_level_sparse_grid()

    #draw the new samples
    my_campaign.draw_samples()
    my_campaign.populate_runs_dir()

In the `example <https://github.com/UCL-CCS/EasyVVUQ/blob/dev/tests/test_hierarchical_sparse_grid_sc.py>`_ the grid 
is refined once, after which the Sobol sensitivity indices are calculated and compared against the reference.
