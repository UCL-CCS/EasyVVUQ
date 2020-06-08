.. _validate_similarities_tutorial:

Validation examples by comparing QoI distributions
==================================================

This tutorial shows how to use a Validation Similarities pattern in EasyVVUQ. 

We test here two analytical functions with Gaussian uncertainties.

The first function is a parabolic function::
  
    mu1 = (y - 50.)**2 / 500.
    sig1 = 0.2
    dist1 = chaospy.Normal(mu1, sig1)

The second function a constant but with changing uncertainty on one side::
  
    mu2 = 2.5
    sig2 = 0.1 + 0.01 * y
    dist2 = chaospy.Normal(mu2, sig2)
    
The variable y is vector
    
Validations metrics
-------------------

The complete code for this example can be found `here <https://github.com/UCL-CCS/EasyVVUQ/blob/dev/docs/tutorial_files/validate_similarities.py>`_.
