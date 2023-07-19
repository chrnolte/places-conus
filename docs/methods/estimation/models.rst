Models
======

Models are statistical objects. We train ("fit") them on :ref:`Samples` of sales prices (:math:`y`) and :any:`Predictors` (:math:`X`). Then, we let them make predictions about expected sales prices (:math:`\hat{y}`) of any other :any:`Parcel <Parcels>`.

A PLACES-FMV (CONUS) model is defined by:

* The :any:`Sample <Samples>` for which it is fit
* The :any:`Estimator <Estimators>` the models deploy (linear regression, tree ensembles).
* The :any:`Predictor set <Predictor sets>` they see during fitting (default, with space, with time, with size)

.. toctree::
   :maxdepth: 2
   :caption: Modeling options

   models/estimators
   models/xcolsets


********************
Model specifications
********************

Specifications for currently used models (Jul 16, 2023)

For an interpretation of the content in each column, see :ref:`Geographies`, :ref:`Parcel types`, :ref:`Sale types`, :ref:`Estimators` and :ref:`Predictor sets`.

.. csv-table::
  :file: cfg/model.csv
  :stub-columns: 1
