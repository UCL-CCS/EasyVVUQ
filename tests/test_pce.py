import numpy    as np
import chaospy  as cp
import easyvvuq as uq

# ... The model
def model(x, c1, c2):
    def c(x):
        if x < 0.5:
            return c1
        else:
            return c2

    N = len(x)
    u = np.zeros(N)

    u[0] = c1
    for n in range(N-1):
        dx = x[n+1] -x[n]
        K1 = -dx*u[n]*c(x[n])
        K2 = -dx*u[n] + K1/2*c(x[n]+dx/2)
        u[n+1] = u[n] + K1 + K2

    return u
# ...

# Uncertain parameter
c1 = cp.Normal(0.5, 0.15)
c2 = cp.Uniform(0.5, 2.5)

# Create the campaign
my_campaign = uq.Campaign()
my_campaign.params_info = {"c": {"type":"array"}}

# Create the sampler
my_sampler  = uq.elements.sampling.PCESampler(my_campaign, [c1, c2])

#
my_campaign.add_runs(my_sampler)

x = np.linspace(0, 1, 101)
#samples = [model(x, nd[0], nd[1]) for nd in nds.T]




