#! /usr/bin/env python
import os
import easyvvuq as uq
import chaospy as cp
import pickle
import time
import numpy as np
import matplotlib.pylab as plt

# Read an old campaign
old_campaign = uq.Campaign(state_file="campaign_state.json", work_dir=".")
results_df = old_campaign.get_collation_result()

# Post-processing analysis
analysis = uq.analysis.PCEAnalysis(sampler=old_campaign.get_active_sampler(), qoi_cols=["te", "ne", "rho", "rho_norm"])
old_campaign.apply_analysis(analysis)

# Get Descriptive Statistics
results = old_campaign.get_last_analysis()
rho = results.describe('rho', 'mean')
rho_norm = results.describe('rho_norm', 'mean')

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
for i in [np.maximum(0, np.int(i-1)) for i in np.linspace(0,1,5) * rho_norm.shape]:
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
