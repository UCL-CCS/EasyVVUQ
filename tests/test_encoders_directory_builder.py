from easyvvuq.encoders.directory_builder import DirectoryBuilder
import pytest
import os


@pytest.fixture
def builder():
    return DirectoryBuilder({'a': {'b': {'c': None, 'd': None}}, 'e': {'f': None}})


def test_init(builder):
    assert(builder.tree == {'a': {'b': {'c': None, 'd': None}}, 'e': {'f': None}})


def test_encoder(builder, tmp_path):
    with pytest.raises(RuntimeError):
        builder.encode()


def test_create_dir_tree(builder, tmp_path):
    builder.create_dir_tree(builder.tree, tmp_path)
    assert(os.path.isdir(os.path.join(tmp_path, 'a', 'b', 'c')))
    assert(os.path.isdir(os.path.join(tmp_path, 'a', 'b', 'd')))
    assert(os.path.isdir(os.path.join(tmp_path, 'e', 'f')))


def test_get_restart_dict(builder):
    restart_dict = builder.get_restart_dict()
    assert(restart_dict['tree'] == {'a': {'b': {'c': None, 'd': None}}, 'e': {'f': None}})


def test_element_version(builder):
    assert(isinstance(builder.element_version(), str))
