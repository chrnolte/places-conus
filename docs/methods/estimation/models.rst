Models
======

Models are statistical objects that are fitted to empirical data (logged sales prices :math:`y` and predictors :math:`X`, "training data", here: land sales) to make predictions about the expected values (:math:`\hat{y}`) of new data points (here: any parcel).

A PLACES-FMV (CONUS) models is defined by:

* The :ref:`Submarket <Submarkets>` for which it observes sales and makes predictions.
* The :ref:`Estimator <Estimators>` they deploy.
* The :ref:`Predictor set <Predictor sets>` they can see.


************
CONUS models
************

CONUS models provide a interpretable understanding of the most important drivers of land value across the entire study area. All are fitted on the full :ref:`CONUS` wide sample of vacant land acquisitions (~1.3M sales) using :ref:`OLS <Linear regressions (OLS)>` estimators.

Table of currently fitted models:

.. csv-table:: CONUS models specifications
   :file: fmv_conus.csv
   :header-rows: 1

Table columns:

* **ycol**: Predicted variable
* **xcols**: Variables included "as is".
* **xcols_div**: Variables interacted with census divisions
* **x_dummies**: Variables used as categorical dummies (fixed effects)

***************
Regional models
***************

Current syntax: ``<base_model>_<predictor_set>``


``<base_model>`` refers to the :any:`Estimator <Estimators>` and is either ERT (``v``) or OLS (``vl``).

.. csv-table:: Regional submarkt model specifications
   :file: fmv_regions.csv
   :header-rows: 1

``<predictor_set>`` refers to the :any:`Predictor set <Predictor sets>` thrown into the estimators:

* ``o``: Original covariates (Nolte 2020 PNAS), but excluding space and time (and parcel size).
* ``h``: As ``o``, but adding parcel size (h = hectares)
* ``st``: Original covariates, including space and time (same as Nolte 2020 PNAS)
* ``sth``: As ``st``, but adding parcel size.
* ``o_s``: Predictor set selected through forward feature selection in spatial cross-validation, using predictors from ``o`` as an input.
* ``h_s``: Predictor set selected through forward feature selection in spatial cross-validation, using predictors from ``h`` as an input.
* ``o_s+st``: Predictor set from ``o_s``, but adding space and time
* ``o_s+sth``: Predictor set from ``o_s``, but adding space, time and parcel size.

**Example**: ``v_st``: ERT estimators with original predictor set.


*************
County models
*************

.. note::
   Under development
