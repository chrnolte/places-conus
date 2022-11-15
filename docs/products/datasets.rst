Datasets
========

The following datasets will be shared via ICPSR.


***********
Parcel data
***********

Parcel-level datasets (:any:`Predictor sets`, fair market value (FMV) predictions, and indicators of statistical support) will be made available as data tables in the `Apache Parquet <https://parquet.apache.org/docs/overview/>`_ format.


.. _parcel_data_X:

Predictors (:math:`X`)
#########################

Parcel-level dataset of :any:`Predictor sets` used in :ref:`Models`.


.. _parcel_data_yhat:

FMV estimates (:math:`\hat{y}`)
###############################

Parcel-level estimates of fair market value from all :any:`Models`, with associated confidence intervals.


.. _parcel_data_support:

Quality metrics
###############

Parcel-level indicators of statistical support. Examples include (1) the estimated likelihood that a parcel sales is observed and (2) the "distance" of each parcel from the training dataset (see :ref:`Uncertainty`).


**********
Model data
**********

We will also publish our :ref:`Model-level uncertainty`, such as AIC, R2, and RMSEs in cross-validation

Accuracy
########

Model-level accuracy estimates from each model and/or region.



***********
Raster data
***********

We will also publish rasterized estimates of our FMV predictions at 480m resolution, similar to the ones `we already published <https://placeslab.org/fmv-usa>`_.
