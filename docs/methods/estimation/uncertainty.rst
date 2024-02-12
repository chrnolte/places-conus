Uncertainty
===========

***********************
Model-level uncertainty
***********************

We compute the following uncertainty metrics for each :ref:`model <Models>`:

* Count of observations (``n``)
* Mean prediction residual (``mean`` bias)
* Standard deviation of prediction error (``std``)
* Root mean squared error (``rmse``)
* Explained variance (``r2``: :math:`R^2`)
* Skew (``skew``)
* Kurtosis (``kurtosis``)


Cross-validation
****************

Model-level uncertainty metrics are derived via cross-validation.

We use mainly three blocking strategies reflecting different prediction tasks:

  * random folds (``r``)
  * blocking by census block groups (``bg``)
  * blocking by census block groups, next-year forecasting (``tbg``)

Variations include:

  * next-year forecasting (``t``)
  * spatially blocked (``s``)
  * blocked by census tracts (``tract``)


************************
Parcel-level uncertainty
************************

We compute the following uncertainty metrics for each :ref:`Parcel <Parcels>`:


Statistical support
*******************

Parcel-level metrics that offer users a measure of statistical support, i.e., an answer to the question: to which extent is each parcel for which we develop FMV estimates similar to the parcels in the training data used to fit their corresponding :ref:`Model <Models>`?


Area of Applicability (AOA)
***************************

An indicator of how "different" a given parcel is from the sample of parcel sales that were used to train the model (training data).

We use the "Area of Applicability" (AOA) metric proposed by Meyer & Pebesma (2021) [#mp]_. The AOA identifies observations for which prediction errors are expected to fall within the empirically derived prediction uncertainties obtained through cross-validation.

The purpose of the Area of Applicability is to help analysts identify parcels whose :ref:`Predictor set <Predictor sets>` is so **different** ("far away") from the predictor sets of the training data (sales data) that we cannot make the assumption that our approach to estimate parcel-level prediction uncertainties (prediction errors in cross-validation) works for them. In other words, such estimates are distant extrapolations, have weak statistical support, and should be considered speculative.

For our AOA estimates, we compute Meyer & Pebesma's distance index, and divide it by the threshold they propose to define the (binary) Area of Applicability (AOA) (outlier-removed upper dissimilarity index of the training data).

This means that an AOA of ≤1 (or a ln(AOA) of 0) marks predictions that are considered to be sufficiently "similar" to the training sample to trust estimated uncertainties, whereas an AOA of >1 identifies estimates for which the predictive model might be more biased or imprecise than our performance statistics suggest.

.. [#mp] Meyer H, Pebesma E (2021) Predicting into unknown space? Estimating the area of applicability of spatial prediction models. Methods in Ecology and Evolution. `doi: 10.1111/2041-210X.13650 <https://doi.org/10.1111/2041-210X.13650>`_
