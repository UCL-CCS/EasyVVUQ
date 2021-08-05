.. _custom_encoder:

Writing a custom encoder or decoder
===================================

EasyVVUQ ships with some relatively generic implementations of encoders and decoders, that can
work for simple codes. For example, GenericEncoder uses text substitution in a user provided template.
You can find examples of using GenericEncoder in previous tutorials
(:doc:`Basic Tutorial <basic\_tutorial>`, :doc:`Cooling Coffee Cup <_cooling_coffee_cup>`).

However, many large, established simulation packages have more complex requirements, such as
multiple input files spread over a multi-layer directory hierarchy, and it is not possible for
to provide a ready-made Encoder adaptable to all cases. It is then necessary to write your own.

Writing a custom encoder
------------------------

In essence, all that is needed is shown in the following snippet: ::

    from easyvvuq.encoders import BaseEncoder

    class MyCustomEncoder(BaseEncoder, encoder_name="my_custom_encoder"):

        def encode(self, params={}, target_dir=''):
            # User code goes here

This subclasses BaseEncoder (the parent class of all EasyVVUQ encoders), to make a new encoder
called, in this case, MyCustomEncoder. Note that this stage *must* pass the *encoder_name* arg. This
determines what EasyVVUQ will call the encoder in error messages etc.

The remaining work is to implement the *encode()* method for the encoder. This method *must* have the
following function signature: ::

    def encode(self, params={}, target_dir=''):

This method will always be passed params - a dict containing the parameters and corresponding values
for a run of this app - and target_dir - the path to the directory in which this encoder's output
should go.

Writing a custom decoder
------------------------

A custom decoder can be created in a very similar manner to the encoder: ::

    from easyvvuq.decoders import BaseDecoder

    class MyCustomDecoder(BaseDecoder, decoder_name="my_custom_decoder"):

        def sim_complete(self, run_info=None):
            # User code goes here (method must return True or False)

        def parse_sim_output(self, run_info={}):
            # User code goes here (method must return a pandas dataframe)

The two methods that must be implemented here are sim_complete(),
which returns True if the simulation has completed (this is handled by
the decoder because it is an application specific issue), and
parse_sim_output(), which returns a dictionary containing the desired
output, distilled from the simulation output files. This dictionary
has to follow the following list of restrictions:


1. Has to be one level deep.
#. All keys are strings signifying output variable names.
#. All the values are either numbers or lists of numbers. Use numbers
   of scalar outputs and lists for vector outputs.

.. code-block:: JSON

  {
    "f1" : 0.3,
    "f2" : [0.2, 0.4],
    "z" : 328
  }
