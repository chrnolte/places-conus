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

.. csv-table:: Table Title
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

.. note::
   Under development

*************
County models
*************

.. note::
   Under development
