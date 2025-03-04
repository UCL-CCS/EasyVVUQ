#! /usr/bin/env python
import easyvvuq as uq
import chaospy as cp
import time
import numpy as np
import matplotlib.pylab as plt
import os

def sobols(P, coefficients):
    A = np.array(P.coefficients)!=0
    multi_indices = np.array([P.exponents[A[:,i]].sum(axis=0) for i in range(A.shape[1])])
    sobol_mask = multi_indices != 0
    _, index = np.unique(sobol_mask, axis=0, return_index=True)
    index = np.sort(index)
    sobol_idx_bool = sobol_mask[index]
    sobol_idx_bool = np.delete(sobol_idx_bool, [0], axis=0)
    n_sobol_available = sobol_idx_bool.shape[0]
    if len(coefficients.shape) == 1:
        n_out = 1
    else:
        n_out = coefficients.shape[1]
    n_coeffs = coefficients.shape[0]
    sobol_poly_idx = np.zeros([n_coeffs, n_sobol_available])
    for i_sobol in range(n_sobol_available):
        sobol_poly_idx[:, i_sobol] = np.all(sobol_mask == sobol_idx_bool[i_sobol], axis=1)
    sobol = np.zeros([n_sobol_available, n_out])
    for i_sobol in range(n_sobol_available):
        sobol[i_sobol] = np.sum(np.square(coefficients[sobol_poly_idx[:, i_sobol] == 1]), axis=0)
    idx_sort_descend_1st = np.argsort(sobol[:, 0], axis=0)[::-1]
    sobol = sobol[idx_sort_descend_1st, :]
    sobol_idx_bool = sobol_idx_bool[idx_sort_descend_1st]
    sobol_idx = [0 for _ in range(sobol_idx_bool.shape[0])]
    for i_sobol in range(sobol_idx_bool.shape[0]):
        sobol_idx[i_sobol] = np.array([i for i, x in enumerate(sobol_idx_bool[i_sobol, :]) if x])
    var = ((coefficients[1:]**2).sum(axis=0))
    sobol = sobol / var
    return sobol, sobol_idx, sobol_idx_bool


# Read an old campaign
time_start = time.time()
DIR = os.getenv('DIR')   ## use the environment variable DIR to store the previous campaign directory path
old_campaign = uq.Campaign(name="fusion_pce.", db_location= f'sqlite:///{os.path.abspath(os.curdir)}/{DIR}/campaign.db')
time_end = time.time()
print('Time for phase 1 = %.3f' % (time_end-time_start))

time_start = time.time()
results_df = old_campaign.get_collation_result()
time_end = time.time()
print('Time for phase 2 = %.3f' % (time_end-time_start))

# Post-processing analysis
time_start = time.time()
analysis = uq.analysis.PCEAnalysis(sampler=old_campaign.get_active_sampler(), qoi_cols=["te", "ne", "rho", "rho_norm"], sampling=False)
old_campaign.apply_analysis(analysis)
time_end = time.time()
print('Time for phase 3 = %.3f' % (time_end-time_start))

# Get Descriptive Statistics
time_start = time.time()
results = old_campaign.get_last_analysis()
rho = results.describe('rho', 'mean')
rho_norm = results.describe('rho_norm', 'mean')
time_end = time.time()
print('Time for phase 4 = %.3f' % (time_end-time_start))

plt.ion()

# plot the calculated Te: mean, with std deviation, 10 and 90% and range
plt.figure()
plt.plot(rho, results.describe('te', 'mean'), 'b-', label='Mean')
plt.plot(rho, results.describe('te', 'mean')-results.describe('te', 'std'), 'b--', label='+1 std deviation')
plt.plot(rho, results.describe('te', 'mean')+results.describe('te', 'std'), 'b--')
plt.fill_between(rho, results.describe('te', 'mean')-results.describe('te', 'std'), results.describe('te', 'mean')+results.describe('te', 'std'), color='b', alpha=0.2)
plt.plot(rho, results.describe('te', '10%'), 'b:', label='10 and 90 percentiles')
plt.plot(rho, results.describe('te', '90%'), 'b:')
plt.fill_between(rho, results.describe('te', '10%'), results.describe('te', '90%'), color='b', alpha=0.1)
plt.fill_between(rho, results.describe('te', '1%'), results.describe('te', '99%'), color='b', alpha=0.05)
plt.legend(loc=0)
plt.xlabel('rho [m]')
plt.ylabel('Te [eV]')
plt.title(old_campaign.campaign_dir)
plt.savefig('Te.png')

# plot the first Sobol results
plt.figure()
for k in results.sobols_first()['te'].keys(): plt.plot(rho, results.sobols_first()['te'][k], label=k)
plt.legend(loc=0)
plt.xlabel('rho [m]')
plt.ylabel('sobols_first')
plt.title(old_campaign.campaign_dir)
plt.savefig('sobols_first.png')

# plot the second Sobol results
plt.figure()
for k1 in results.sobols_second()['te'].keys():
    for k2 in results.sobols_second()['te'][k1].keys():
        plt.plot(rho, results.sobols_second()['te'][k1][k2], label=k1+'/'+k2)
plt.legend(loc=0, ncol=2)
plt.xlabel('rho [m]')
plt.ylabel('sobols_second')
plt.title(old_campaign.campaign_dir+'\n');
plt.savefig('sobols_second.png')

# plot the total Sobol results
plt.figure()
for k in results.sobols_total()['te'].keys(): plt.plot(rho, results.sobols_total()['te'][k], label=k)
plt.legend(loc=0)
plt.xlabel('rho [m]')
plt.ylabel('sobols_total')
plt.title(old_campaign.campaign_dir)
plt.savefig('sobols_total.png')


# plot the distributions
plt.figure()
for i, D in enumerate(results.raw_data['output_distributions']['te'].samples):
    pdf_kde_samples = cp.GaussianKDE(D)
    _Te = np.linspace(pdf_kde_samples.lower, pdf_kde_samples.upper[0], 101)
    plt.loglog(_Te, pdf_kde_samples.pdf(_Te), 'b-', alpha=0.25)
    plt.loglog(results.describe('te', 'mean')[i], pdf_kde_samples.pdf(results.describe('te', 'mean')[i]), 'bo')
    plt.loglog(results.describe('te', 'mean')[i]-results.describe('te', 'std')[i], pdf_kde_samples.pdf(results.describe('te', 'mean')[i]-results.describe('te', 'std')[i]), 'b*')
    plt.loglog(results.describe('te', 'mean')[i]+results.describe('te', 'std')[i], pdf_kde_samples.pdf(results.describe('te', 'mean')[i]+results.describe('te', 'std')[i]), 'b*')
    plt.loglog(results.describe('te', '10%')[i],  pdf_kde_samples.pdf(results.describe('te', '10%')[i]), 'b+')
    plt.loglog(results.describe('te', '90%')[i],  pdf_kde_samples.pdf(results.describe('te', '90%')[i]), 'b+')
    plt.loglog(results.describe('te', '1%')[i],  pdf_kde_samples.pdf(results.describe('te', '1%')[i]), 'bs')
    plt.loglog(results.describe('te', '99%')[i],  pdf_kde_samples.pdf(results.describe('te', '99%')[i]), 'bs')
plt.xlabel('Te')
plt.ylabel('distribution function')
plt.title(old_campaign.campaign_dir)
plt.savefig('distribution_functions.png')

te_dist = results.raw_data['output_distributions']['te']
for i in [np.maximum(0, int(i-1)) for i in np.linspace(0,1,5) * rho_norm.shape]:
    plt.figure()
    pdf_raw_samples = cp.GaussianKDE(results_df.te[i])
    pdf_kde_samples = cp.GaussianKDE(te_dist.samples[i])
    plt.hist(results_df.te[i], density=True, bins=50, label='histogram of raw samples', alpha=0.25)
    if hasattr(te_dist, 'samples'):
        plt.hist(te_dist.samples[i], density=True, bins=50, label='histogram of kde samples', alpha=0.25)

    plt.plot(np.linspace(pdf_raw_samples.lower, pdf_raw_samples.upper), pdf_raw_samples.pdf(np.linspace(pdf_raw_samples.lower, pdf_raw_samples.upper)), label='PDF (raw samples)')
    plt.plot(np.linspace(pdf_kde_samples.lower, pdf_kde_samples.upper), pdf_kde_samples.pdf(np.linspace(pdf_kde_samples.lower, pdf_kde_samples.upper)), label='PDF (kde samples)')
    
#    t1 = te_dist[i]
#    plt.plot(np.linspace(t1.lower, t1.upper), t1.pdf(np.linspace(t1.lower,t1.upper)), label='PDF')

    plt.legend(loc=0)
    plt.xlabel('Te [eV]')
    plt.title('Distributions for rho_norm = %0.4f' % (rho_norm[i]))
    plt.savefig('distribution_function_rho_norm=%0.4f.png' % (rho_norm[i]))


# Compare new and old ways of calculating statistical quantities
sobol, sobol_idx, _ = sobols(old_campaign.get_active_sampler().P, results.raw_data['Fourier_coefficients']['te'])

varied = [_ for _ in analysis.sampler.vary.get_keys()]
S1 = {_: np.zeros(sobol.shape[-1]) for _ in varied}
ST = {_: np.zeros(sobol.shape[-1]) for _ in varied}
S2 = {_ : {__: np.zeros(sobol.shape[-1]) for __ in varied} for _ in varied}
for v in varied: del S2[v][v]
for n, si in enumerate(sobol_idx):
    if len(si) == 1:
        v = varied[si[0]]
        S1[v] = sobol[n]
    elif len(si) == 2:
        v1 = varied[si[0]]
        v2 = varied[si[1]]
        S2[v1][v2] = sobol[n]
        S2[v2][v1] = sobol[n]
    for i in si:
        ST[varied[i]] += sobol[n]

plt.figure()
plt.plot(rho, results.describe('te', 'mean') - results.raw_data['Fourier_coefficients']['te'][0], label='Difference in mean')
plt.plot(rho, results.describe('te', 'std') - np.sqrt(np.sum(results.raw_data['Fourier_coefficients']['te'][1:]**2, axis=0)), label='Difference in std')
plt.legend(loc=0)
plt.xlabel('rho [m]')
plt.title('Comparison between chaospy sampling\nand fourier coefficients evaluations')
plt.savefig('Difference_in_mean_and_std.png')


plt.figure()
for k in S1.keys():
    plt.plot(rho, results.sobols_first()['te'][k] - S1[k], label='Difference in sobol firsts %s' % (k))
for k1 in S2.keys():
    for k2 in S2[k1].keys():
        plt.plot(rho, results.sobols_second()['te'][k1][k2] - S2[k1][k2], label='Difference in sobol seconds %s/%s' % (k1, k2))
for k in S1.keys():
    plt.plot(rho, results.sobols_total()['te'][k] - ST[k], label='Difference in sobol totals %s' % (k))
plt.legend(loc=0, ncol=3, fontsize=4)
plt.xlabel('rho [m]')
plt.ylabel('sobols')
plt.title('Comparison between chaospy sampling\nand fourier coefficients evaluations')
plt.savefig('Difference_in_sobols.png')

