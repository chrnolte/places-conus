Parcel data
===========

Folder: ``parcels``

Parcel-level data for all parcels that are either vacant or larger than one hectare: fair market value (FMV) predictions, :any:`Predictor sets`, and indicators of statistical support.

All parcel-level data is provided in the `Apache Parquet <https://parquet.apache.org/docs/overview/>`_ format. Developed for big-data applications, Parquet is efficient in space consumption and has exceptional reading and writing speed. Support exists for Python and R, as well as other languages (but not Stata).

Tables are by county in a hierarchical file structure. For instance, parcel-level predictors for Franklin county, Massachusetts (FIPS code: 25011) can be found in::

  /parcels/MA/25011/25011_parcel_predictors_pqt.zip

All parcel-level datasets use the parcel identifier :any:`geometry_sha3_224` (see :ref:`Data linkage`).

.. _parcel_data_yhat:

*************
FMV estimates
*************

Filename syntax: ``<county_fips>_parcel_predictions_<model>_pqt.zip``

Parcel-level estimates of fair market value from :ref:`Models`.

Tables currently exist for the following modeling approaches:

* ``conus``: Predictions from CONUS-wide OLS regressions.

  For an interpretation of model names, please refer to :ref:`CONUS models`.

* ``regions``: Predictions from regional models (note that not all regional markets have sufficient vacant sales).
* ``pnas2020``: Predictions using the same algorithm as in Nolte 2020 PNAS.


.. _parcel_data_X:

**************
Predictor data
**************

Filename convention: ``<county_fips>_parcel_predictors_pqt.zip``

Parcel-level dataset of :ref:`Predictor sets` (:math:`X`) used in :ref:`Models`.

For an interpretation of column names, refer to :ref:`Predictors <Predictors>`.

.. _parcel_data_support:

***************
Quality metrics
***************

.. note::
    Not yet published.

Parcel-level indicators of statistical support for each parcel-level FMV estimate. Examples include (1) the estimated likelihood that a parcel sales is observed and (2) the "area of applicability" of each parcel from the training dataset (see :ref:`Uncertainty`).
