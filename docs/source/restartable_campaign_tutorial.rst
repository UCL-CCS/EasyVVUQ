.. _restartable_campaign_tutorial:

Restarting a Campaign
=====================

This tutorial shows a simple case of saving and reloading a Campaign in
EasyVVUQ.
Restarting a Campaign can be useful in a number of cases, such as when
the execution phase takes so long we can't (or don't want to) have our
python workflow script running the whole time. This example uses the same
Gauss test case as in the :doc:`Basic Tutorial <basic\_tutorial>`.

EasyVVUQ Script Overview
------------------------

The full script can be found here: (:download:`easyvvuq_restart_campaign_tutorial.py <../../tutorials/easyvvuq_restart_campaign_tutorial.py>`)

To run the script execute the following command ::

    python3 easyvvuq_restart_campaign_tutorial.py

The first 9 steps are identical to those detailed in the `Basic Tutorial <basic_tutorial>`, so we will begin at step 10 in the script.

Section 10. Print the list of runs
----------------------------------

Before doing anything else, let's first print out the list of runs that have already been added to our `Campaign`. The following should display a (nicely formatted) list of the 15 runs present. ::

    pprint(my_campaign.list_runs())

Section 11. Save the Campaign
-----------------------------

Now we want to save the state of our campaign so that we can reload it at a later time. 
Here we have chosen to save it in a file called 'campaign_state.json' ::

    my_campaign.save_state("campaign_state.json")

At this point we could in principle end the script, and reload the campaign in a different script at a later time.

Section 12. Load state in new campaign object
---------------------------------------------

We can now make a new campaign object, which we shall call `reloaded_campaign` to make the distinction clearer. By specifying the state_file parameter, we can make this load the state of the previously saved campaign (stored in `campaign_state.json`). ::

    reloaded_campaign = uq.Campaign(state_file="campaign_state.json", work_dir=".")

`reloaded_campaign` is now a campaign object with the same state, and with a link to the same database of runs etc. as we had before. It has automatically loaded the app, encoder, decoder and sampler we had set previously. We can now continue from where we left off.

Section 13. Do some more runs...
--------------------------------

In the following we draw some more samples, execute the runs, and collate the results into the existing dataframe. ::

    reloaded_campaign.draw_samples(num_samples=1, replicas=5)
    reloaded_campaign.populate_runs_dir()
    my_campaign.apply_for_each_run_dir(uq.actions.ExecuteLocal(cmd, interpret='python3'))
    reloaded_campaign.collate()

Section 14. Print the list of runs again
----------------------------------------
Finally, we can print the list of runs in the campaign again. ::

    pprint(reloaded_campaign.list_runs())

At which point we see there are now 20 of them.

Section 15. Run Analysis
------------------------

As in the basic tutorial, we can now carry out a bootstrap analysis on these 20 runs. ::

    stats = uq.analysis.EnsembleBoot(groupby=["mu"], qoi_cols=["Value"])
    my_campaign.apply_analysis(stats)
    print("stats:\n", my_campaign.get_last_analysis())
