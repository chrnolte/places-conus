Parcel data
===========

Folder: ``parcels``

Tabular data for :any:`Parcels`:

* Fair market value (FMV) estimates (:math:`\hat{y}`)
* :any:`Predictor sets` (:math:`X`)
* Uncertainty estimates
* Dissimilarity from training sample

Parcel data is provided in the `Apache Parquet <https://parquet.apache.org/docs/overview/>`_ format. Parquet is efficient in space consumption with fast reading and writing speeds. Support exists for Python and R, as well as other languages.

Parcel data is provided by county. Each county's data is in: ``parcels/``:any:`state` ``/``:any:`fips`.

Example: parcel-level predictors for Franklin county, Massachusetts (FIPS: 25011) are in::

  /parcels/MA/25011/25011_parcel_predictors_pqt.zip

All parcel-level datasets can be joined on the parcel identifier (:any:`geometry_sha3_224`), which can also be derived from the parcel geometries (see :ref:`Data linkage`).


.. _parcel_data_yhat:

*********************************
Fair Market Value (FMV) estimates
*********************************

Filename syntax: ``<fips>_parcel_predictions_pqt.zip``

Parcel-level estimates of property value from :ref:`Models`.


.. _parcel_data_X:

**************
Predictor data
**************

Filename convention: ``<fips>_parcel_predictors_pqt.zip``

Parcel-level dataset of all :ref:`Predictors` contained in :ref:`Predictor sets` (:math:`X`) of active :ref:`Models`.

For an interpretation of column names, see :ref:`Predictors <Predictors>`.


.. _parcel_data_uncertainty:

*********************
Uncertainty estimates
*********************

Parcel-level uncertainty estimate (not yet computed)


.. _parcel_data_support:

**********************************
Dissimilarity from training sample
**********************************

Dissimilarity index of predicted observation from training sample in importance-weighted feature space (see "Area of applicability" / :ref:`Uncertainty`).
