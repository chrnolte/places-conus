Models
======

Models are statistical objects. We train ("fit") them on :ref:`Samples` of sales prices (:math:`y`) and :any:`Predictors` (:math:`X`). Then, we let them make predictions about expected sales prices (:math:`\hat{y}`) of any other :any:`Parcel <Parcels>`.

A PLACES-FMV (CONUS) model is defined by:

* The :any:`Sample <Samples>` for which it is fit
* The :any:`Estimator <Estimators>` the models deploy (linear regression, tree ensembles).
* The :any:`Predictor set <Predictor sets>` they see during fitting (default, with space, with time, with size)

.. toctree::
   :maxdepth: 2
   :caption: Learn more

   models/estimators
   models/xcolsets
