from easyvvuq.analysis.ensemble_boot import confidence_interval, bootstrap
from easyvvuq.analysis.ensemble_boot import ensemble_bootstrap, EnsembleBoot
import os
import numpy as np
import pandas as pd
import pytest

VALUES = np.array([-0.15290645, -0.06603495, -1.15918081, -0.69664801, -0.15575749,
                   2.35229204, -0.06865014, -0.54273057, -1.02611451, -0.06726835,
                   -1.44265619, -0.07376992, 0.15329612, 0.22452796, -0.43804867,
                   -0.57410222, 0.73160321, 0.47333579, 0.99045532, 0.0610611,
                   -0.68175712, 1.44167141, 1.41131026, 0.04405738, -0.62093876,
                   -0.10847473, -0.51871589, -0.7083068, -1.19355452, 0.34581233,
                   0.4186337, -1.50122848, -0.02000289, 0.8692544, 0.00630065,
                   0.06573571, -0.13717114, -0.49024436, 0.45795243, -1.75480644,
                   -0.03456317, -0.31055375, 0.42796229, 0.46150687, -1.39604062,
                   -0.8399575, 1.58534212, -0.2266236, -0.49377649, 2.1317957,
                   -0.25232935, -0.96146138, 1.07657868, -0.45800046, -1.17446575,
                   -0.76133007, -0.08153581, -0.31169611, -0.52160229, 0.62211079,
                   -0.11015225, 0.00509996, 1.03970295, 1.54558691, 1.2175904,
                   1.2350817, -0.33833554, 0.35622358, 1.91426417, 1.37448159,
                   -1.31821785, 0.27282303, -0.02054649, 0.77370705, -1.46905703,
                   1.17037632, -1.42858642, 0.81286204, -0.2679725, -1.43849903,
                   -0.10667022, 1.05864374, -0.03691869, 0.28838373, -1.22270076,
                   -0.38587169, -0.06953894, -0.04007896, 1.90438598, 0.47908424,
                   0.55914129, 0.31623038, -0.90755982, -0.73807981, -1.79903777,
                   -0.65874425, 0.3829014, -1.05095023, -0.32223138, 1.55394379])


def test_confidence_interval():
    dist = np.array([])
    with pytest.raises(ValueError):
        stat, low, high = confidence_interval(dist, 0.0, 0.05)
    dist = np.array([0.0])
    stat, low, high = confidence_interval(dist, 0.0, 0.05)
    assert(stat == low == high == 0.0)
    stat, low, high = confidence_interval(dist, 0.0, 0.05, pivotal=True)
    assert(stat == low == high == 0.0)
    stat, low, high = confidence_interval(VALUES, 0.0, 0.05)
    assert(stat == -0.06909454)
    assert(low == -1.4859470412500002)
    assert(high == 1.90957202975)
    stat, low, high = confidence_interval(VALUES, 0.0, 0.05, pivotal=True)
    assert(stat == 0.0)
    assert(low == -1.90957202975)
    assert(high == 1.4859470412500002)


def test_bootstrap():
    with pytest.raises(RuntimeError):
        bootstrap(pd.DataFrame({}), np.mean)
    stat, low, high = bootstrap(pd.DataFrame({'a': [0.0]}), np.mean)
    assert(stat == 0.0)
    assert(low == 0.0)
    assert(high == 0.0)


def test_ensemble_bootstrap():
    df = pd.DataFrame({
        'a': np.concatenate((VALUES, VALUES)),
        'b': ['group1'] * VALUES.shape[0] + ['group2'] * VALUES.shape[0]})
    results = ensemble_bootstrap(df, groupby=['b'], qoi_cols=['a'])
    assert(not results.empty)
    assert(results.values.shape == (2, 3))
    with pytest.raises(RuntimeError):
        ensemble_bootstrap(df, groupby=['b'], qoi_cols=['c'])
    results = ensemble_bootstrap(df, qoi_cols=['a'])
    assert(results.values.shape == (1, 3))


def test_ensemble_boot():
    analysis = EnsembleBoot()
    assert(analysis.element_name() == 'ensemble_boot')
    assert(analysis.element_version() == '0.1')
    with pytest.raises(RuntimeError):
        analysis.analyse()
    with pytest.raises(RuntimeError):
        analysis.analyse(pd.DataFrame({}))
    analysis = EnsembleBoot(groupby=['b'], qoi_cols=['a'], stat_func=np.mean)
    df = pd.DataFrame({
        'a': np.concatenate((VALUES, VALUES)),
        'b': ['group1'] * VALUES.shape[0] + ['group2'] * VALUES.shape[0]})
    results = analysis.analyse(df)
    assert(not results.empty)
