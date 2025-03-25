Models
======

Land value models are trained on :ref:`samples <Samples>` of sales prices and :any:`predictors <Predictors>` to estimate expected sales prices across all :any:`parcels <Parcels>` in CONUS.

A model is defined by:

* The :any:`sample <Samples>` it sees, which is a function of :ref:`geography <Geographies>`, :ref:`parcel type <Parcel types>`, and :ref:`sale type <Sale types>`. 
* The :any:`estimator <Estimators>` it uses (linear regression, tree ensembles).
* The :any:`predictor set <Predictor sets>` it sees during fitting (independent variables).

.. toctree::
   :maxdepth: 2
   :caption: Modeling: details

   models/estimators
   models/predictor_sets


********************
Model specifications
********************

This table provides an overview of **all models** tested by Sep 30, 2023.

For an interpretation of the first five columns, refer to the documentation of :ref:`geographies <Geographies>`, :ref:`parcel types <Parcel types>`, :ref:`sale types <Sale types>`, :ref:`estimators <Estimators>` and :ref:`predictor sets <Predictor sets>`.

* ``ycol`` is the predicted variable. In most models, it is ``lnusd-j001``: the natural logarithm of the deflated sales price, with random jitter added (standard deviation: 0.01). ``lnusd-ha-*`` refers to the natural logarithm of the deflated per-area (per-hectare) sales price. ``*-jsd01`` and ``*-jsd10`` refer to jitter with a standard deviation of 0.1 and 1.0, respectively.
* ``weights`` refer to the weight given to each observation. ``recip``, ``rihs``, and ``rsqrt`` refer to different approaches to downweigh sales appearing in clusters (e.g. subdevelopments)
* ``disclosure`` refers to the minimum amount of county-level sales data required to include the county's data in the :ref:`sample <Samples>`. ``all`` includes all counties, ``medium`` and ``high`` include only counties with rich sales data: ``medium`` for counties with ≥1% sales of single-family homes per year, ``high`` for counties with ≥2% sales of single-family homes per year.


.. csv-table::
  :file: cfg/model.csv
  :stub-columns: 1

