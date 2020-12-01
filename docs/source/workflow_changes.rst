.. _workflow_changes:

Recently (today is 01.12.2020) there have been some changes in the workflow of EasyVVUQ 
which means that some existing workflows will need to be altered. There are many changes, 
in fact, but here we will only concentrate on the changes that mean you will have to change 
your existing scripts. I will try to summarise them here.

No More Collaters
=================

You don't need to explicitly create a collater anymore. The code that imports collaters will
fail with an import error. The rest did not change. You still need to call ``campaign.collate()``
in order to collect all the simulation data from the decoders. You also don't need to and can't
specify a collater when adding an app to a campaign. So, for example ::
    my_campaign.add_app(name="gauss",
                        params=params,
                        encoder=encoder,
                        decoder=decoder,
                        collater=collater)



would then become 
::
    my_campaign.add_app(name="gauss",
                        params=params,
                        encoder=encoder,
                        decoder=decoder,
                        collater=collater)
 
Decoders Must Return Dictionaries
=================================
 
Decoders are now required to return dictionaries. These dictionaries must contain qoi's as keys 
and the values can be either flow or lists. In case the values are lists the qoi will be interpreted 
as a vector. In fact, internally, all qois are now treated as vectors. This is done for consistency
reasons. So if your simulation returns a single scalar value it will be treated as a vector in one
dimension. An example of a valid dictionary that could be returned by a decoder could be ::

    {'y1': 3.14, 'y2': [1, 2]}

You can also enfore checking the output of your decoders using Cerberus. To this end you need to create
a validation dictionary in the Cerberus format. You then need to specify this when calling ``add_app`` 
on a campaign. For example, using the output above ::

    validator = {
        'y1' : {'type': 'float', 'required': True}, 
        'y2' : {'type': 'list', required: True, minlength: 2, maxlength: 2}
    }
    campaign.add_app(name="gauss",
                     params=params,
                     encoder=encoder,
                     decoder=decoder,
                     decoderspec=validator,
                     collater=collater)
                    
Each time the decoder output is read it will be checked using this specification. This can be used for 
debugging and validation purposes.

Analysys Classes Return an AnalysisResults Instance
===================================================

In an effort to provide a consistent interface to the users all classes must return the results in the same
way. The idea is that the users would not need to modify their code if they want to swap the analysis method
for another one. Of course this is to some extent not possible because different analysis methods have different
capabilities in terms of what information they can provide. But we must strive for a consistent interface
as much as possible. So from now on when you call ``campaign.get_last_analysis()`` or when you use the ``analyse()``
method of an analysis class explicitly it will return an instance of AnalysisResults. In order to get values of
interest to you see the examples below ::

    >>> results = campaign.get_last_analysis()
    >>> results.sobols_first()
    {'f': {'x1': array([0.610242]), 'x2': array([0.26096511])}}
    >>> results.sobols_first('f')
    {'x1': array([0.610242]), 'x2': array([0.26096511])}
    >>> results.sobols_first('f', 'x1')
    array([0.610242])

If, say, `f` is one your qois and `x1` and `x2` are your input variables you can get the first order sobol indices for
both all qois and all inputs by calling `results.sobols_first()`, you can get sobol indices for `f` by calling 
`results.sobols_first(f)` and you can get the index for one of the quantities by calling `results.sobols_first(f, x2)`.
Also implemented in some of the classes are `results.sobols_second()` and `results.sobols_total()` which work in a similar way.

You can get descriptive statistcs by calling `results.describe()`.
