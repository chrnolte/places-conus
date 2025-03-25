Predictor sets
==============

Predictors sets are sets of :any:`predictors <Predictors>` (independent variables) seen by :ref:`models <Models>`.

Changing predictor sets across models allows us to study how predictor selection affects model performance and biases.

****************************
Predictor set specifications
****************************

The below table contains the full list of predictor sets used in :ref:`model specifications <Model specifications>`.

For an interpretation of the meaning of each variable, see the full :ref:`list of predictors <Predictors>`.

Predictors in the column ``continuous`` are used *as is*. Predictors in ``dummied`` are first transformed into categorical dummies (e.g., for year-quarter or regional fixed effects). Stacked (second-level) models use the predictions of first-level models as predictors: ``lnusd-ha_<model identifier>``.

.. csv-table::
  :file: ../cfg/predictor_sets.csv
  :stub-columns: 1
