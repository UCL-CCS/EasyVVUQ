.. _multiencoder_tutorial:

Combining multiple encoders using MultiEncoder
==============================================

While a user is always free to write their own, custom encoder (as discussed in the :doc:` Custom Encoder tutorial <custom\_encoder>`
it is generally easier to use existing encoders whenever possible. In some cases a single encoder may not be sufficient, but combining
multiple encoders together can achieve the desired effect.

For example, consider an application which takes *two* input files, `A` and `B`, but `A` can be generated using `encoder1` and `B`
with a (generally) different encoder, `encoder2`. In such a case, EasyVVUQ provides the `MultiEncoder` element, which can combine
any number of encoders into a single encoder: ::
    my_multiencoder = uq.encoders.MultiEncoder(encoder1, encoder2, ...)

Once created, this encoder can be set for an app, as with any other encoder.

