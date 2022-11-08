Uncertainty
===========

.. note::

   This section is still very much under development.

===============================
Model-level uncertainty metrics
===============================

* AOC
* R2
* ...

Cross-validation
****************

* Spatial
* Temporal


================================
Parcel-level uncertainty metrics
================================


Distance Index
**************

The "Distance Index" (DI) is an indicator of how "different" a given parcel is from the sample of parcel sales that were used to train the model (training data).

The purpose of the distance index is to help analysts identify parcel-level land value estimates for which predictor values are so different ("far away") from the distribution of predictors in the training data (sales data) that we cannot assume that our estimated prediction uncertainties (derived from the training data) accurately estimate the their prediction error. In other words, such estimates are extrapolations, have weak statistical support, and should therefore be considered speculative.

The DI is directly derived from the "Area of Applicability" algorithm proposed by `Meyer & Pebesma (2021) <https://besjournals.onlinelibrary.wiley.com/doi/full/10.1111/2041-210X.13650>`_, which identifies observations for which prediction errors are expected to fall within the empirically derived prediction uncertainties (obtained via internal cross-validation). We compute our distance index based on Meyer & Pebesma's "Dissimilarity Index" (:math:`{DI_k}`), divided by the threshold for the Area of Applicability (AOA).

This means that a DI of ≤1 marks predictions that are considered to be sufficiently "similar" to the training sample to estimate uncertainties, whereas a DI of >1 identifies estimates for which the predictive model might be more biased or imprecise than our model performance statistics suggest.
