import pytest
import chaospy as cp
from easyvvuq.sampling import QMCSampler


def test_init():
    vary = {'a': cp.Uniform(-5, 3), 'b': cp.Uniform(2, 10)}
    with pytest.raises(RuntimeError):
        QMCSampler({}, 100)
    
