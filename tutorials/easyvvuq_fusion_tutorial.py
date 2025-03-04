#! /usr/bin/env python
"""
Run an EasyVVUQ campaign to analyze the sensitivity of the temperature
profile predicted by a simplified model of heat conduction in a
tokamak plasma.

This is done with PCE.
"""
import os
import easyvvuq as uq
import chaospy as cp
from shutil import rmtree
import pickle
import time
import numpy as np
import matplotlib
if not os.getenv("DISPLAY"):
    matplotlib.use("Agg")
import matplotlib.pylab as plt


work_dir = os.path.dirname(os.path.abspath(__file__))
campaign_work_dir = os.path.join(work_dir, "easyvvuq_fusion_tutorial")
# clear the target campaign dir
if os.path.exists(campaign_work_dir):
    rmtree(campaign_work_dir)
os.makedirs(campaign_work_dir)


time_start = time.time()
# Set up a fresh campaign called "fusion_pce."
db_location = "sqlite:///" + campaign_work_dir + "/campaign.db"
my_campaign = uq.Campaign(
    name="fusion_pce.",
    db_location=db_location,
    work_dir=campaign_work_dir
)

# Define parameter space
params = {
    "Qe_tot": {"type": "float", "min": 1.0e6, "max": 50.0e6, "default": 2e6},
    "H0": {"type": "float", "min": 0.00, "max": 1.0, "default": 0},
    "Hw": {"type": "float", "min": 0.01, "max": 100.0, "default": 0.1},
    "Te_bc": {"type": "float", "min": 10.0, "max": 1000.0, "default": 100},
    "chi": {"type": "float", "min": 0.01, "max": 100.0, "default": 1},
    "a0": {"type": "float", "min": 0.2, "max": 10.0, "default": 1},
    "R0": {"type": "float", "min": 0.5, "max": 20.0, "default": 3},
    "E0": {"type": "float", "min": 1.0, "max": 10.0, "default": 1.5},
    "b_pos": {"type": "float", "min": 0.95, "max": 0.99, "default": 0.98},
    "b_height": {"type": "float", "min": 3e19, "max": 10e19, "default": 6e19},
    "b_sol": {"type": "float", "min": 2e18, "max": 3e19, "default": 2e19},
    "b_width": {"type": "float", "min": 0.005, "max": 0.025, "default": 0.01},
    "b_slope": {"type": "float", "min": 0.0, "max": 0.05, "default": 0.01},
    "nr": {"type": "integer", "min": 10, "max": 1000, "default": 100},
    "dt": {"type": "float", "min": 1e-3, "max": 1e3, "default": 100},
    "out_file": {"type": "string", "default": "output.csv"}
}
""" code snippet for writing the template file
str = ""
first = True
for k in params.keys():
    if first:
        str += '{"%s": "$%s"' % (k,k) ; first = False
    else:
        str += ', "%s": "$%s"' % (k,k)
str += '}'
print(str, file=open('fusion.template','w'))
"""


# Create an encoder, decoder and collater for PCE test app

encoder = uq.encoders.GenericEncoder(
    template_fname="fusion.template",
    delimiter="$",
    target_filename="fusion_in.json"
)

decoder = uq.decoders.SimpleCSV(
    target_filename="output.csv",
    output_columns=["te", "ne", "rho", "rho_norm"]
)

execute = uq.actions.ExecuteLocal(
    "python3 {}/fusion_model.py fusion_in.json".format(work_dir)
)

actions = uq.actions.Actions(
    uq.actions.CreateRunDirectory(root=campaign_work_dir, flatten=True),
    uq.actions.Encode(encoder),
    execute,
    uq.actions.Decode(decoder)
)

# Add the app (automatically set as current app)
my_campaign.add_app(
    name="fusion",
    params=params,
    actions=actions
)

time_end = time.time()
print("Time for phase 1 = %.3f" % (time_end - time_start))
time_start = time.time()

# Create the sampler
vary = {
    "Qe_tot":   cp.Uniform(1.8e6, 2.2e6),
    "H0":       cp.Uniform(0.0,   0.2),
    "Hw":       cp.Uniform(0.1,   0.5),
    "chi":      cp.Uniform(0.8,   1.2),
    "Te_bc":    cp.Uniform(80.0,  120.0),
    "b_pos":    cp.Uniform(0.95,  0.99),
    "b_height": cp.Uniform(5e19,  7e19),
    "b_sol":    cp.Uniform(1e19,  3e19),
    "b_width":  cp.Uniform(0.015, 0.025),
    "b_slope":  cp.Uniform(0.005, 0.020)
}
""" other possible quantities to vary
    "a0":       cp.Uniform(0.9,   1.1),
    "R0":       cp.Uniform(2.7,   3.3),
    "E0":       cp.Uniform(1.4,   1.6),
    "b_pos":    cp.Uniform(0.95,  0.99),
    "b_height": cp.Uniform(5e19,  7e19),
    "b_sol":    cp.Uniform(1e19,  3e19),
    "b_width":  cp.Uniform(0.015, 0.025),
    "b_slope":  cp.Uniform(0.005, 0.020)
"""

# Associate a sampler with the campaign
my_sampler = uq.sampling.PCESampler(vary=vary, polynomial_order=1)
my_campaign.set_sampler(my_sampler)

# Will draw all (of the finite set of samples)
my_campaign.draw_samples()
print("Number of samples = %s" % my_campaign.get_active_sampler().count)

time_end = time.time()
print("Time for phase 2 = %.3f" % (time_end - time_start))
time_start = time.time()

# Run and collate the cases
my_campaign.execute().collate()
results_df = my_campaign.get_collation_result()

time_end = time.time()
print("Time for phase 3 = %.3f" % (time_end - time_start))
time_start = time.time()

# Post-processing analysis
my_campaign.apply_analysis(
    uq.analysis.PCEAnalysis(
        sampler=my_campaign.get_active_sampler(),
        qoi_cols=["te", "ne", "rho", "rho_norm"]
    )
)

time_end = time.time()
print("Time for phase 4 = %.3f" % (time_end - time_start))
time_start = time.time()

# Get Descriptive Statistics

results = my_campaign.get_last_analysis()
rho = results.describe("rho", "mean")
rho_norm = results.describe("rho_norm", "mean")

time_end = time.time()
print("Time for phase 5 = %.3f" % (time_end - time_start))
time_start = time.time()


pickle_file = os.path.join(campaign_work_dir, "fusion_results.pickle")
with open(pickle_file, "bw") as f_pickle:
    pickle.dump(results, f_pickle)

time_end = time.time()
print("Time for phase 6 = %.3f" % (time_end - time_start))

plt.ion()

# plot the calculated Te: mean, with std deviation, 10 and 90% and range
te_mean = results.describe("te", "mean")
te_std = results.describe("te", "std")
te_10_pct = results.describe("te", "10%")
te_90_pct = results.describe("te", "90%")
te_min = results.describe("te", "min")
te_max = results.describe("te", "max")

plt.figure()
plt.plot(rho, te_mean, "b-", label="Mean")
plt.plot(rho, te_mean - te_std, "b--", label="+1 std deviation")
plt.plot(rho, te_mean + te_std, "b--")
plt.fill_between(rho, te_mean - te_std, te_mean + te_std,
                 color="b", alpha=0.2)
plt.plot(rho, te_10_pct, "b:", label="10 and 90 percentiles")
plt.plot(rho, te_90_pct, "b:")
plt.fill_between(rho, te_10_pct, te_90_pct, color="b", alpha=0.1)
plt.fill_between(rho, te_min, te_max, color="b", alpha=0.05)

plt.legend(loc=0)
plt.xlabel("rho [m]")
plt.ylabel("Te [eV]")
plt.savefig(os.path.join(campaign_work_dir, "Te.png"))


# plot the first Sobol results
plt.figure()
for k in results.sobols_first()["te"].keys():
    plt.plot(rho, results.sobols_first()["te"][k], label=k)
plt.legend(loc=0)
plt.xlabel("rho [m]")
plt.ylabel("sobols_first")
plt.savefig(os.path.join(campaign_work_dir, "sobols_first.png"))

# plot the second Sobol results
plt.figure()
for k1 in results.sobols_second()["te"].keys():
    for k2 in results.sobols_second()["te"][k1].keys():
        plt.plot(rho, results.sobols_second()["te"][k1][k2],
                 label=k1 + "/" + k2)
plt.legend(loc=0, ncol=2)
plt.xlabel("rho [m]")
plt.ylabel("sobols_second")
plt.savefig(os.path.join(campaign_work_dir, "sobols_second.png"))


# plot the total Sobol results
plt.figure()
for k in results.sobols_total()["te"].keys():
    plt.plot(rho, results.sobols_total()["te"][k], label=k)
plt.legend(loc=0)
plt.xlabel("rho [m]")
plt.ylabel("sobols_total")
plt.savefig(os.path.join(campaign_work_dir, "sobols_total.png"))

# Commented out because we get "GaussianKDE()) has dangling dependencies" error messages
# # plot the distributions
# plt.figure()
# for i, D in enumerate(results.raw_data['output_distributions']['te']):
#     _Te = np.linspace(D.lower[0], D.upper[0], 101)
#     _DF = D.pdf(_Te)
#     plt.loglog(_Te, _DF, 'b-', alpha=0.25)
#     plt.loglog(results.describe('te', 'mean')[i], np.interp(results.describe('te', 'mean')[i], _Te, _DF), 'bo')
#     plt.loglog(results.describe('te', 'mean')[i]-results.describe('te', 'std')[i], np.interp(results.describe('te', 'mean')[i]-results.describe('te', 'std')[i], _Te, _DF), 'b*')
#     plt.loglog(results.describe('te', 'mean')[i]+results.describe('te', 'std')[i], np.interp(results.describe('te', 'mean')[i]+results.describe('te', 'std')[i], _Te, _DF), 'b*')
#     plt.loglog(results.describe('te', '10%')[i],  np.interp(results.describe('te', '10%')[i], _Te, _DF), 'b+')
#     plt.loglog(results.describe('te', '90%')[i],  np.interp(results.describe('te', '90%')[i], _Te, _DF), 'b+')
# plt.xlabel('Te')
# plt.ylabel('distribution function')
# plt.savefig('distribution_functions.png')

te_dist = results.raw_data["output_distributions"]["te"]
for i in [np.maximum(0, int(i - 1))
          for i in np.linspace(0, 1, 5) * rho_norm.shape
          ]:
    plt.figure()
    pdf_raw_samples = cp.GaussianKDE(results_df.te[i])
    pdf_kde_samples = cp.GaussianKDE(te_dist.samples[i])

    plt.hist(
        results_df.te[i], density=True, bins=50,
        label="histogram of raw samples", alpha=0.25
    )
    if hasattr(te_dist, "samples"):
        plt.hist(
            te_dist.samples[i], density=True, bins=50,
            label="histogram of kde samples", alpha=0.25
        )

    plt.plot(
        np.linspace(pdf_raw_samples.lower, pdf_raw_samples.upper),
        pdf_raw_samples.pdf(
            np.linspace(pdf_raw_samples.lower, pdf_raw_samples.upper)
        ),
        label="PDF (raw samples)"
    )
    plt.plot(
        np.linspace(pdf_kde_samples.lower, pdf_kde_samples.upper),
        pdf_kde_samples.pdf(
            np.linspace(pdf_kde_samples.lower, pdf_kde_samples.upper)
        ),
        label="PDF (kde samples)"
    )
    if i == 0:
        t1 = te_dist[i]
        plt.plot(
            np.linspace(t1.lower, t1.upper),
            t1.pdf(np.linspace(t1.lower, t1.upper)),
            label="PDF from EasyVVUQ"
        )
    plt.legend(loc=0)
    plt.xlabel("Te [eV]")
    plt.title("Distributions for rho_norm = %0.4f" % (rho_norm[i]))
    png_file_name = os.path.join(
        campaign_work_dir,
        "distribution_function_rho_norm=%0.4f.png" % (rho_norm[i])
    )
    plt.savefig(png_file_name)
