Parcel data
===========

Parcel data can be joined on the parcel identifier (:any:`geometry_sha3_224`, see :ref:`data linkage <Data linkage>`).


.. _parcel_data_yhat:

*********************************
Fair market value (FMV) estimates
*********************************

Parcel-level estimates of property value from :ref:`models <Models>`.

:Example:
 ``25011_parcel_predictions.pqt`` is a table of parcel-level predictor data for Franklin county, Massachusetts.

:Location:
 ``parcels/<state>/<county>/<county>_parcel_predictions_pqt.zip``

 * ``state`` is the 2-letter Alpha code of the state (see :any:`state`).
 * ``county`` is the 5-letter FIPS code of the county (see :any:`fips`).

:Columns:
 ``fmv_<model_id>_<year>``

 * ``model_id`` identifies the :ref:`model <Model specifications>`, and
 * ``year`` is the year for which the prediction was made.

:Unit:
 Natural logarithm of U.S. dollars (real, deflated to Jan 2022)

:Format:
  Compressed `Parquet <https://parquet.apache.org/docs/overview/>`_ table


.. _parcel_data_X:

**************
Predictor data
**************

Parcel-level table of all :ref:`predictors <Predictors>` used by :ref:`models <Models>`.

:Example:
 ``25011_parcel_predictors.pqt`` is a table of parcel-level predictor data for Franklin county, Massachusetts

:Location:
 ``parcels/<state>/<county>/<county>_parcel_predictions_pqt.zip``

 * ``state`` is the 2-letter Alpha code of the state (see :any:`state`).
 * ``county`` is the 5-letter FIPS code of the county (see :any:`fips`).

:Columns:
  For an interpretation of column names and units, see :ref:`predictors <Predictors>`.

:Format:
  Compressed `Parquet <https://parquet.apache.org/docs/overview/>`_ table


.. _parcel_data_support:

********************************
Area of applicability (AOA) data
********************************

Parcel-level indicator of the :ref:`Area of Applicability (AOA)` for the FMV estimates, standardized.

This a measure of **dissimilarity**: how "different" is each predicted parcel sale from the sales in the :ref:`sample <Samples>` that the predicting :ref:`model <Models>` was trained on?

It can be used to identify "audacious" (incomparable) predictions in the :ref:`land value rasters <Fair market value (FMV) rasters>`, such as for parcels that rarely sell (such as unique or very large parcels) in parts of the landscape where sales data is unobserved (undisclosed or not digitized).

Computationally, it is the Euclidean distance in weighted predictor space, where predictors are weighted by their importance in the model (see `Meyer & Pebesma 2021 <https://besjournals.onlinelibrary.wiley.com/doi/full/10.1111/2041-210X.13650>`_).

:Example:
 ``25011_parcel_predictors.pqt`` is a table of parcel-level AOA measures data for Franklin county, Massachusetts

:Location:
 ``parcels/<state>/<county>/<county>_parcel_support_pqt.zip``

 * ``state`` is the 2-letter Alpha code of the state (see :any:`state`).
 * ``county`` is the 5-letter FIPS code of the county (see :any:`fips`).

:Columns:
 ``aoa_<model_id>_<year>_<cross-validation_type>``

 * ``model_id`` identifies the :ref:`model <Model specifications>`.
 * ``year`` is the year for which the prediction was made.
 * ``cross-validation_type`` identifies the type of :ref:`cross-validation <Cross-validation>` used to find the AOA threshold.

:Unit:
 Unitless distance, rescaled

 Values ≤0 are within the threshold of the :ref:`AOA <Area of Applicability (AOA)>`, values ≥0 are outside.

  .. math::
   
    ln(\frac{dissimilarity\;index}{AOA\;threshold})

:Format:
  Compressed `Parquet <https://parquet.apache.org/docs/overview/>`_ table
