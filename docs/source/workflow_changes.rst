.. _workflow_changes:

Workflow Changes
================

Recently (since release v0.7.3) there have been some changes in the workflow of EasyVVUQ 
which means that some existing scripts that use EasyVVUQ will need to be altered. There are 
many changes, in fact, but here we will only concentrate on the changes that mean you will 
have to change your existing scripts. I will try to summarise them below.

No More Collaters
-----------------

You don't need to explicitly create a collater anymore. The code that imports collaters will
fail with an import error. The rest did not change. You still need to call ``campaign.collate()``
in order to collect all the simulation data from the decoders. You also don't need to and can't
specify a collater when adding an app to a campaign. So, for example ::
    my_campaign.add_app(name="gauss",
                        params=params,
                        encoder=encoder,
                        decoder=decoder,
                        collater=collater)



would now become 
::
    my_campaign.add_app(name="gauss",
                        params=params,
                        encoder=encoder,
                        decoder=decoder)
                        
The call to ``campaign.get_collation_result()`` will return a pandas DataFrame as before. The resulting
DataFrame is now `multi-indexed <https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html>`_. 
The main difference here would be that each column is treated as if holding a vector argument. This is
probably best illustrated with an example.

Here is a valid example of such a DataFrame. ::

       run_id        x1        x2         g                    
            0         0         0         0         1         2
    0       0  0.046910  0.046910  0.046910  0.046910  0.093820
    1       1  0.046910  0.230765  0.046910  0.230765  0.277675
    2       2  0.046910  0.500000  0.046910  0.500000  0.546910
    3       3  0.046910  0.769235  0.046910  0.769235  0.816145
    4       4  0.046910  0.953090  0.046910  0.953090  1.000000
    5       5  0.230765  0.046910  0.230765  0.046910  0.277675
    6       6  0.230765  0.230765  0.230765  0.230765  0.461531
    7       7  0.230765  0.500000  0.230765  0.500000  0.730765
    8       8  0.230765  0.769235  0.230765  0.769235  1.000000
    9       9  0.230765  0.953090  0.230765  0.953090  1.183855
    10     10  0.500000  0.046910  0.500000  0.046910  0.546910
    11     11  0.500000  0.230765  0.500000  0.230765  0.730765
    12     12  0.500000  0.500000  0.500000  0.500000  1.000000
    13     13  0.500000  0.769235  0.500000  0.769235  1.269235
    14     14  0.500000  0.953090  0.500000  0.953090  1.453090
    15     15  0.769235  0.046910  0.769235  0.046910  0.816145
    16     16  0.769235  0.230765  0.769235  0.230765  1.000000
    17     17  0.769235  0.500000  0.769235  0.500000  1.269235
    18     18  0.769235  0.769235  0.769235  0.769235  1.538469
    19     19  0.769235  0.953090  0.769235  0.953090  1.722325
    20     20  0.953090  0.046910  0.953090  0.046910  1.000000
    21     21  0.953090  0.230765  0.953090  0.230765  1.183855
    22     22  0.953090  0.500000  0.953090  0.500000  1.453090
    23     23  0.953090  0.769235  0.953090  0.769235  1.722325
    24     24  0.953090  0.953090  0.953090  0.953090  1.906180

It has two input variables ``x1`` and ``x2`` and one vector valued qoi (quantity of interest) 
`g` with three elements. Any scalar is treated as a vector with one element. This is mainly of interest for people
developing analysis classes but probably useful to know to users too. If you want to access
the columns of the qoi you can do so (assuming ``df`` is collation result) ``df[g]`` would
return a data frame with the three columns that make up ``g``. You can also call ``df[g, 1]`` to
get a particular element. In which case it will return a corresponding column (second one in this 
case).

Decoders Must Return Dictionaries
---------------------------------
 
Decoders are now required to return dictionaries. These dictionaries must contain qoi's as keys 
and the values can be either float or lists. In case the values are lists the qoi will be interpreted 
as a vector. If your simulation produces more complex output you need to pre-process it to fit into this format.
An example of a valid dictionary that could be returned by a decoder could be ::

    {'y1': 3.14, 'y2': [1, 2]}

You can also enforce checking the output of your decoders using `Cerberus <https://docs.python-cerberus.org/en/stable/>`_. 
To this end you need to create a validation dictionary in the Cerberus format. You then need to specify this when 
calling ``add_app`` on a campaign. For example, if the ouput of the decoder is the dictionary above, you can
use the following validator ::

    validator = {
        'y1' : {'type': 'float', 'required': True}, 
        'y2' : {'type': 'list', required: True, minlength: 2, maxlength: 2}
    }
    campaign.add_app(name="gauss",
                     params=params,
                     encoder=encoder,
                     decoder=decoder,
                     decoderspec=validator)
                    
Each time the decoder output is read it will be checked using this specification. This can be used for 
debugging and validation purposes. For more information for how to write the validator please consult
the Cerberus project website.

Analysis Classes Return an AnalysisResults Instance
---------------------------------------------------

In an effort to provide a consistent interface to the user, all classes must return the results in the same
way. The idea is that the users would not need to modify their code if they want to swap the analysis method
for another one. Of course, this is to some extent not possible because different analysis methods have different
capabilities in terms of what information they can provide. But we must strive for a consistent interface
as much as possible. So from now on when you call ``campaign.get_last_analysis()`` or when you use the ``analyse()``
method of an analysis class explicitly it will return an instance of ``AnalysisResults``. In order to get sobol 
indices from this object see the example: ::

    >>> results = campaign.get_last_analysis()
    >>> results.sobols_first()
    {'f': {'x1': array([0.610242]), 'x2': array([0.26096511])}}
    >>> results.sobols_first('f')
    {'x1': array([0.610242]), 'x2': array([0.26096511])}
    >>> results.sobols_first('f', 'x1')
    array([0.610242])

If ``f`` is one your qois and ``x1`` and ``x2`` are your input variables you can get the first order sobol indices for
all qois and all inputs by calling ``results.sobols_first()``, you can get sobol indices for ``f`` by calling 
``results.sobols_first(f)`` and you can get the index for one of the quantities by calling ``results.sobols_first(f, x2)``.
Also implemented in some of the classes are ``results.sobols_second()`` and ``results.sobols_total()`` which work in a similar way.
Where make sense the classes will also provide a ``surrogate()`` method which will return an object that will act
as a surrogate for your simulation.

You can get descriptive statistcs by calling ``results.describe()``.
