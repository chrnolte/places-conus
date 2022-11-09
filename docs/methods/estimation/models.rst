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

:Submarket: CONUS
:Estimator: OLS
:Predictor set: Nonspatial default; regional dummies.


***************
Regional models
***************

:Submarket: Regions
:Estimators: ERT
:Predictor set: PNAS 2020
