Datasets
========

The following datasets will be shared via ICPSR.


***********
Parcel data
***********

.. _hans:

.. _parcel_data_X:

Predictors (X)
##############

Parcel-level dataset of :any:`Predictors` used in :ref:`Models`.


.. _parcel_data_fmv:

FMV estimates (:math:`\hat{y}`)
###############################

Parcel-level estimates of fair market value from all :any:`Models`, with associated confidence intervals.


.. _parcel_data_support:

Support
#######

Parcel-level indicators of statistical support, such as likelihood that a similar sale would be selected, as well as an index of dissimilarity with the training data.

**********
Model data
**********

Accuracy
########

Model-level accuracy estimates from each model and/or region.


Data linkage
############

We will make a Python algorithm available that generates a unique parcel identifier from the parcel polygon. This should allow you to link up the data, as long as your parcel polygons are the same as ours (and if not, let's check out both and figure out which one's better).

.. note::

   There has to be a perfect match in the geospatial polygons.
