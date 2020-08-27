import pytest
from easyvvuq.sampling import QMCSampler


def test_init(self):
    vary = {'a': cp.Uniform(-5, 3), 'b': cp.Uniform(2, 10)}
    with pytest.raises(RuntimeError):
        QMCSampler(vary)
