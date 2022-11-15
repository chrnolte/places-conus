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

CONUS models provide a interpretable understanding of the most important drivers of land value across the full study area. All are fitted on the full :ref:`CONUS` wide sample of vacant land acquisitions (~1.3M sales) using :ref:`OLS <Linear regressions (OLS)>` estimators.

.. note ::

   Notes to self:
   - Population gravity: might require 3-4 B-splines

.. todo:: There's something here

***************
Regional models
***************

:Submarket: Regions
:Estimators: ERT
:Predictor set: PNAS 2020
