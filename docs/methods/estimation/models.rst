Models
======

Land value models are trained on :ref:`samples <Samples>` of sales prices and :any:`predictors <Predictors>` to make predictions about expected sales prices all :any:`parcels <Parcels>`.

A model is defined by:

* The :any:`sample <Samples>` it sees, defined by :ref:`geography <Geographies>`, :ref:`parcel type <Parcel types>`, and :ref:`sale type <Sale types>`. 
* The :any:`estimator <Estimators>` it uses (linear regression, tree ensembles).
* The :any:`predictor set <Predictor sets>` it sees during fitting (independent variables).

.. toctree::
   :maxdepth: 2
   :caption: Modeling: details

   models/estimators
   models/xcolsets


********************
Model specifications
********************

To interpret columns, see :ref:`geographies <Geographies>`, :ref:`parcel types <Parcel types>`, :ref:`sale types <Sale types>`, :ref:`estimators <Estimators>` and :ref:`predictor sets <Predictor sets>`.

.. csv-table::
  :file: cfg/model.csv
  :stub-columns: 1
