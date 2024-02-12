Predictor sets
==============

Predictors sets are sets of :any:`predictors <Predictors>` (independent variables) seen by :ref:`models <Models>`.

Changing predictor sets across models allows us to study how predictor selection affects model performance and biases.

****************************
Predictor set specifications
****************************

The following table contains the full list of predictors of each predictor set used in :ref:`model specifications <Model specifications>`.

Predictors in the column `continuous`` are used "as is". Predictors in ``dummied`` are first transformed into categorical dummies (e.g., for year-quarter or regional fixed effects).

For an interpretation of the meaning of each variables, see :ref:`Predictors`.

Stacked (second-level) models use the predictions of first-level models as predictors: ``lnusd-ha_<model identifier>``.

.. csv-table::
  :file: ../cfg/xcolset.csv
  :stub-columns: 1
