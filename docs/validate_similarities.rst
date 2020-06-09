.. _validate_similarities_tutorial:

Validation by comparing QoI distributions
=========================================

This tutorial shows how to use a Validation Similarities pattern in EasyVVUQ.

We test here two quantities of interest (QoI) represented by two analytical functions with Gaussian uncertainties.

The first function is a parabolic function::
  
    mu1 = (y - 50.)**2 / 500.
    sig1 = 0.2
    dist1 = chaospy.Normal(mu1, sig1)

The second function a constant but with changing uncertainty on one side::
  
    mu2 = 2.5
    sig2 = 0.1 + 0.01 * y
    dist2 = chaospy.Normal(mu2, sig2)
    
Here you see how these functions look, when we are varing :code:`y` in the intervalle :code:`[0, 100]`:

.. figure:: images/val_qoi_1.png

Validations metrics
-------------------

In EasyVVUQ, we implemented the calculation of four different divergence measures:
Hellinger, Jensen-Shannon, Wasserstein-1 and Wasserstein-2 (cf. Refenrces below for more details). This allows us to computes distances between two probability distributions. 

QoI distributions
-----------------

We can use Chaospy to compute the probability densities and the cummulative distributions functions needed for the above-mentioned  metrics::

    # Probabily densities: for Hellinger and Jensen-Shannon
    p1 = dist1.pdf(x)
    p2 = dist2.pdf(x)

    # Cummulative distributions (w/ weight): for Wasserstein
    dx = x[-1] - x[0]
    c1 = dx * dist1.cdf(x)
    c2 = dx * dist2.cdf(x)
    
The sampling values :code:`x` can be computed using the min/max values of a common large support of QoI distrubtions, for example::

    x = np.linspace(min_value, max_value, 1000, endpoint=True)
    
**Note**: the min/max values can be obtained from lower and upper bound of the distributions. In case of univarainte distribution, we can use: :code:`dist.lower[0]` and :code:`dist.upper[0]`.



The complete code for this example can be found `here <https://github.com/UCL-CCS/EasyVVUQ/blob/dev/docs/tutorial_files/validate_similarities.py>`_.


References
----------

