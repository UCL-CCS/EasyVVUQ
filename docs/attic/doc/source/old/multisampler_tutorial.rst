.. _multisampler_tutorial:

Combining multiple samplers using Multisampler
==============================================

There may be cases in which you want to generate runs using a combination of samplers, each acting
on a subset of the parameters.
For example, one may wish to carry out a Polynomial Chaos Expansion on some parameters (x and y), but for a set sequence of some other parameter (z).
In such a case you would want a sampler that combines a PCE sampler (for x and y) and a Sweep sampler (cycling through values of z).
There are, of course, far more complex situations than this too.

In EasyVVUQ such a case is addressed using a `Multisampler`.
For example, the following code creates a new sampler which combines three existing samples (`sampler1`, `sampler2` and `sampler3`): ::

    my_multisampler = uq.sampling.MultiSampler(sampler1, sampler2, sampler3)


Whilst this example involves 3 samplers, any number of samplers can be combined in the same manner.
Note that the ordering of the samplers *does* matter.
The last sampler in the list updates 'fastest' while the first sampler updates 'slowest'.
Furthermore, every sampler in a multisampler must be finite (contain a finite number of samples).

Once created, this sampler can be added to the campaign object and used like any other: ::

    my_campaign.set_sampler(my_multisampler)
    my_campaign.draw_samples()


