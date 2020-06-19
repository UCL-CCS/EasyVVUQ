# Configure Google Cloud Kubernetes Engine

Here we describe how to configure remote access to a remote Kubernetes
cluster hosted on Google Cloud. Some of the instructions should
transfer to other providers. For this tutorial you need to have a
Google Cloud account, and Google Cloud SDK installed on your
computer. You also probably need to enable Google Cloud Kubernetes
Engine enabled in your Google Cloud console.

.. code-block:: shell

   gcloud auth login

Will log you in to your Google account. It will open a browser window
where you will allow access to google cloud.

.. code-block:: shell

   gcloud config set project PROJECT_ID

.. code-block:: shell

   gcloud init

This will set the project id. Too access google cloud from your
computer you need to do this. Note that you may not have to specify
zone during the init stage which I foolishly didn't.

.. code-block:: shell
   
   gcloud container clusters create easyvvuq --zone=us-central1-c

Now this should be all that you need to start accessing the
cluster. It is now configured in your ~/.kube/config file. This file
can also (probably) be used as a template when using other services
(not Google Cloud). And we can start using it to run Dask on.

Now if you run

.. code-block:: shell

   kubectl get nodes

You should see something similar to:

.. code-block::
   
   NAME                                      STATUS   ROLES    AGE   VERSION
   gke-easyvvuq-default-pool-b5d5204c-4lx0   Ready    <none>   44s   v1.14.10-gke.36
   gke-easyvvuq-default-pool-b5d5204c-tnpz   Ready    <none>   41s   v1.14.10-gke.36
   gke-easyvvuq-default-pool-b5d5204c-trwr   Ready    <none>   44s   v1.14.10-gke.36

So let us start Python and try to create a Kubernetes cluster and get
dask and EasyVVUQ running on it.

.. literalinclude:: worker-spec.yml
   :language: YAML
