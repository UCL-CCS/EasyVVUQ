import easyvvuq as uq

def test_lhc():
    vary = {'a' : (-5, 3), 'b' : (2, 10)}
    sampler = uq.sampling.quasirandom.LHCSampler(vary, 5)
    
