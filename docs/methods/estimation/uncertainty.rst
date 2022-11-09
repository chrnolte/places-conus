Uncertainty
===========

.. note::

   This section is still very much under development.

===============================
Model-level uncertainty metrics
===============================

Uncertainty metrics we plan to publish for each :ref:`Model <Models>` include:

* Akaike Information Criterion (AIC)
* Explained variance (:math:`R^2`)
* Root mean squared error (RMSE) of predictions

  * in random cross-validation
  * in spatially blocked cross-validation
  * in temporally blocked cross-validation


========================
Parcel-level uncertainty
========================

Uncertainty metrics we plan to publish for each :ref:`Parcel <Parcels>` include:


Prediction uncertainty
######################

We plan to compute prediction intervals at confidence levels of 50%, 75%, 90%, 95%, and 99%.

.. caution ::

   Parcel-level prediction intervals are currently only defined and computed for the OLS :ref:`Estimator <Estimators>`. We don't have a formal approach to estimate these error quantiles for regression tree ensembles, unless we use a quantile regression tree, which needs larger numbers of observations in leaf, and thus involves larger bias.


Statistical support
###################

Parcel-level metrics that offer users a measure of statistical support, i.e., an answer to the question: how similar is the parcel for which this estimate was predicted from the parcels on which the :ref:`Model <Models>` was trained.


Selection probability
*********************

Likelihood of being selected into sales data.


Distance Index
**************

Our "Distance Index" (DI) is an indicator of how "different" a given parcel is from the sample of parcel sales that were used to train the model (training data).

The purpose of this distance index is to help analysts identify parcels whose :ref:`Predictor set <Predictor sets>` is so **different** ("far away") from the predictor sets of the training data (sales data) that we cannot make the assumption that our approach to estimate parcel-level prediction uncertainties (prediction errors in cross-validation) works for them. In other words, such estimates are distant extrapolations, have therefore weak statistical support, and should be considered speculative.

The DI is derived from the "Area of Applicability" algorithm proposed by Meyer & Pebesma (2021) [#mp]_. The AOA identifies observations for which prediction errors are expected to fall within the empirically derived prediction uncertainties (obtained through cross-validation).

Our distance index computed as the ratio of Meyer & Pebesma's "Dissimilarity Index" (:math:`{DI_k}`) and the threshold they propose to define the (binary) Area of Applicability (AOA) (outlier-removed maximum dissimilarity index of the training data).

This means that a DI of ≤1 marks predictions that are considered to be sufficiently "similar" to the training sample to trust estimated uncertainties, whereas a DI of >1 identifies estimates for which the predictive model might be more biased or imprecise than our performance statistics suggest.

.. [#mp] Meyer H, Pebesma E (2021) Predicting into unknown space? Estimating the area of applicability of spatial prediction models. Methods in Ecology and Evolution. `doi: 10.1111/2041-210X.13650 <https://doi.org/10.1111/2041-210X.13650>`_
