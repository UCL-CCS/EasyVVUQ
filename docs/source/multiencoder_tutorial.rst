.. _multiencoder_tutorial:

Creating complex encoders using MultiEncoder and DirectoryBuilder
=================================================================

While a user is always free to write their own, custom encoder (as discussed in the :doc:`Custom Encoder tutorial <custom\_encoder>`)
it is generally easier to use existing encoders whenever possible. In some cases a single encoder may not be sufficient, but combining
multiple encoders together can achieve the desired effect.

For example, consider an application which takes *two* input files, `A` and `B`, but `A` can be generated using `encoder1` and `B`
with a (generally) different encoder, `encoder2`. In such a case, EasyVVUQ provides the `MultiEncoder` element, which can combine
any number of encoders into a single encoder: ::
    my_multiencoder = uq.encoders.MultiEncoder(encoder1, encoder2, ...)

Once created, this encoder can be set for an app, as with any other encoder.

This is particularly useful when used in conjunction with the `DirectoryBuilder` encoder.
For example, the following code will create a particular directory structure (as specified by `directory_tree`),
and then encode two files from template (using `GenericEncoder`), placing each file into a different
part of the created directory tree: ::

    directory_tree = {'dir1': {'dir2': {'dir3': None, 'dir4': None}}, 'dir5': {'dir6': None}}

    multiencoder = uq.encoders.MultiEncoder(

        uq.encoders.DirectoryBuilder(tree=directory_tree),

        uq.encoders.GenericEncoder(
            template_fname='template1.xml',
            delimiter='#',
            target_filename='dir1/dir2/dir3/app1input.xml'
        ),

        uq.encoders.GenericEncoder(
            template_fname='template2.csv',
            delimiter='$',
            target_filename='dir5/dir6/app2input.csv'
        )
    )
