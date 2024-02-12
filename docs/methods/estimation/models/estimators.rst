Estimators
==========

Estimators are algorithms that compute statistical estimates (fair market value) from data (of sales transactions).

Our research design compares the predictive accuracy of linear regressions (ordinary least squares, OLS) and tree ensemble methods (extremely randomized trees, gradient boosting, histogram-based gradient boosting).

************************
Linear regressions (OLS)
************************

Linear models  offer a simple parametric approach to model land values.

We use the default specification of ``statsmodels``' `OLS <https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.OLS.html#statsmodels.regression.linear_model.OLS>`_ (ordinary least squares) regressor.

**Strengths**

* Interpretability: coefficients can be interpreted as marginal effects, if assumption are satisfied. This allows statements such as: "a 10% increase in wetlands is associated with an X% reduction in property values"
* Extrapolation: an OLS model that is correctly specified and fitted can make predictions outside the range of observed sales prices or predictors.

**Challenges**

* Analysts need to know the functional form: OLS regressions require the definition of a regression equation, which should represent the real-life data-generating process. If the data-generating process is unknown, or varies across space, it is easy to misspecify OLS models, leading to biased results.
* Lack of flexibility: Unless specified in the regression formula, OLS do not explicitly consider the potentially large number of non-linearities and high-dimensional interactions between variables. Therefore, OLS models often offer lower predictive accuracy than more flexible modeling strategies (e.g., :ref:`Extremely Randomized Trees <Extremely Randomized Trees (ERT)>`).

The exact regression specification depends on the :ref:`predictor set <Predictor sets>`, but generally takes the following formula:

.. math::

   ln(price_{ijt}) = \alpha + X_i \beta + \mu_j + \tau_t + \varepsilon_{ijt}

Where:

* :math:`price_{ijt}` is the sales price of property :math:`i` in region :math:`j` at time :math:`t`
* :math:`\alpha` is the intercept
* :math:`X_i` is a :ref:`predictor set <Predictor sets>`
* :math:`\mu_j` are dummies for :ref:`regions`
* :math:`\tau_t` are year-quarter dummies
* :math:`\varepsilon_{ijt}` is a normally distributed error


********************************
Extremely Randomized Trees (ERT)
********************************

The Extremely Randomized Trees (ERT) algorithm (`Geurts et al 2006 <https://link.springer.com/article/10.1007/s10994-006-6226-1>`_) is a close cousin of the Random Forest, a popular machine-learning algorithm.

Similar to a Random Forest, ERTs average predictions of randomized decision trees, and decision trees are built on bootstrapped samples of training data (in our specification). While a Random Forest searches for the "best" split across features and thresholds, ERTs draw random thresholds for each feature and pick whichever happens to be the most discriminative.

We used ERTs to generate our first published estimates of PLACES-FMV for CONUS (*Nolte (2020) PNAS* (`article <https://www.pnas.org/doi/10.1073/pnas.2012865117>`_, `data <https://doi.org/10.5061/dryad.np5hqbzq9>`_).

We use ``scikit-learn``'s `ExtraTreesRegressor <https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesRegressor.html>`_ with the following modifications:

* ``n_estimators=500`` to build 500 trees (instead of 100). Larger forests tend to increase accuracy.
* ``bootstrap=True`` to compute out-of-bag (OOB) predictions, i.e. fair-market values for parcels that sold, based only on decision trees that have not seen the parcel in question.
* ``min_samples_leaf=3`` to average results and to avoid the publication of actual sales data (to comply with the data licensing agreements).

We vary parameters such as ``min_samples_leaf`` and ``n_estimators`` to study trade-offs between resource usage, privacy, and predictive performance.


*********************************
Gradient Boosting Regressor (GBR)
*********************************

A tree ensemble algorithm, but this one "boosts" (serial improvements) and doesn't "bag" (parallel predictions, as in random forests).

We use ``scikit-learn``'s `GradientBoostingRegressor <https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor>`_.


***************************************
Histogram-based Gradient Boosting (HGB)
***************************************

A tree ensemble algorithm that promises superior efficiency (faster predictions).

Uses ``scikit-learn``'s `HistGradientBoostingRegressor <https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html>`_.


**************
Stacked models
**************

Stacked models use predictions of other models as inputs. We let first-level :ref:`models <Models>` make predictions during cross-validation, then use predictions from several different models as independent variables in second-level models.


************************
Estimator specifications
************************

.. csv-table::
  :file: ../cfg/estimator.csv
  :stub-columns: 1
