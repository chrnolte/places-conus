.. _Models_Home:

Estimators
==========

Our research design directly compares the relative predictive accuracy of two common statistical estimators: a structural modeling approach (ordinary least squares (OLS) regressions) and a machine-learning approach (extremely randomized trees).


************************
Linear regressions (OLS)
************************

Linear models, fitted with Ordinary Least Squares (OLS), offer a widely known structural approach to model land values. We use the default specification of ``statsmodels``' ``OLS`` regressor (`OLS documentation <https://www.statsmodels.org/stable/index.html>`_)

**Strengths**

* Interpretability: coefficients can be interpreted as marginal effects, if assumption as satisfied. This allows statements such as: "a 10% increase in wetlands is associated with an X% reduction in property values"
* Extrapolation: an OLS model that is correctly specified and fitted can make predictions outside the range of observed outcomes (:math:`y`) of the observed covariate space (:math:`X`).

**Challenges**

* Knowledge of functional form required: OLS regressions require the definition of a regression equation, which should represent the real-life data-generating process. If the data-generating process is unknown, or varies across space, OLS are easily misspecified and can lead to biased results.
* Lack of flexibility: Unless specified in the regression formula, OLS do not explicitly consider the potentially large number of non-linearities and high-dimensional interactions between variables. Therefore, OLS models are often worse at making predictions than more flexible modeling strategies (e.g., :ref:`Extremely Randomized Trees (ERT)`).

The exact regression specification depends on the :ref:`Predictor set <Predictor sets>`, but generally takes the following formula:

.. math::

   ln(price_{ijt}) = \alpha + X_i \beta + \mu_j + \tau_t + \varepsilon_{ijt}

Where:

* :math:`price_{ijt}` is the sales price of property :math:`i` in region :math:`j` at time :math:`t`
* :math:`\alpha` is the intercept
* :math:`X_i` is a :ref:`Predictor set <Predictor sets>`

  * :any:`ha` - always included
  * :aluna:ref:`hh_inc_med_bg_2012-2016`
  * :aluna:ref:`rd_dst_pvd+`
  * :any:`p_wet`
  * :any:`p_forest`
  * :any:`p_crops`
  * :any:`p_pasture`
  * :any:`fld_fr_fath_f100`
  * :any:`fld_fr_fath_p100`
  * :any:`water_exposure`
  * :any:`cst_2500`
  * :any:`cst_50`
* :math:`\mu_j` are dummies for :ref:`Regions`
* :math:`\tau_t` are year-quarter dummies (always)
* :math:`\varepsilon_{ijt}` is assumed to be a normally distributed error


********************************
Extremely Randomized Trees (ERT)
********************************

The Extremely Randomized Trees (ERT) algorithm is a close cousin of the Random Forest, a popular machine-learning algorithm.

Similar to a Random Forest, an ERT averages predictions of randomized decision trees. In our application, each decision tree is built on a bootstrapped sample of training data. The key difference lies in the way Random Forest and ERT pick the "splits" in the decision trees: a Random Forest searches for the most discriminative split across features and thresholds, whereas ERTs draw random thresholds for each feature and pick whichever happens to be the most discriminative.

We used ERTs to generate our first published estimates of PLACES-FMV for CONUS (*Nolte (2020) PNAS* (`article <https://www.pnas.org/doi/10.1073/pnas.2012865117>`_, `data <https://doi.org/10.5061/dryad.np5hqbzq9>`_). The Supplementary Material of the article goes into more detail on how ERTs outperformed Random Forests in the land value prediction task, possibly due to  overfitting on local idiosyncracies in training data selection (observed sales).

We use ``scikit-learn``'s ``ExtraTreesRegressor`` (`ERT documentation <https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesRegressor.html>`_) with the following modifications:

* ``n_estimators = 500`` to build 500 trees (instead of 100). Larger forests tend to increase accuracy.
* ``bootstrap = True`` to compute out-of-bag (OOB) predictions, i.e. fair-market values for parcels that sold, based only on decision trees that have not seen the parcel in question.
* ``min_samples_leaf = 3`` to average results and to avoid the publication of actual sales data (to comply with the data licensing agreements).

