import pytest
import os
from easyvvuq.encoders.copy_encoder import CopyEncoder


def test_copy_encoder():
    with pytest.raises(RuntimeError):
        CopyEncoder('axcd', 'axcd')


def test_copy_encoder_encode(tmpdir):
    filename1 = os.path.join(tmpdir, 'test1.txt')
    filename2 = 'test2.txt'
    open(os.path.join(filename1, 'a')).close()
    encoder = CopyEncoder(filename1, filename2)
    with pytest.raises(RuntimeError):
        encoder.encode({}, 'axcd')
    encoder.encode(tmpdir)
    assert(os.path.isfile(os.path.join(tmpdir, filename2)))
