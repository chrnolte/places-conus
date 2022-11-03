.. _Models_Home:

Models
======

Our research design will directly compares the relative predictive accuracy of at least two different types of models:

****************************
Ordinary Least Squares (OLS)
****************************

The OLS framework offers a widely known, interpretable, and structured approach to model land values.

Regression formula:

.. math::

   ln(price_{ijk}) = \alpha + X_i \beta + \mu_j + \tau_t + \varepsilon_{ijt}

Where:

* :math:`\alpha` is an intercept
* :math:`X_i` is a set of :ref:`Predictors`

  * :py:attr:`hh_inc_med_bg_2012-2016`
  * :any:`rd_dist_pvd` +
  * :py:attr:`p_wet`
  * :any:`p_forest`
  * :any:`p_crops`
  * :any:`p_pasture`
  * :any:`fld_fr_fath_f100`
  * :any:`fld_fr_fath_p100`
  * :py:attr:`water_exposure`
  * :any:`cst_2500`
  * :any:`cst_50`

* :math:`\mu_j` are dummies for :ref:`Regions`
* :math:`\tau_t` are year-quarter dummies.
* :math:`\varepsilon_{ijt}` is assumed to be a normally distributed error

********************************
Extremely Randomized Trees (ERT)
********************************

Very similar to random forest algorithms, ERTs are ensembles of decision trees.

We use ``scikit-learn`` implementation of the ``ExtraTreesClassifier`` with the following specifications: ``n_estimators=500``, ``bootstrap=True``, and ``min_samples_leaf=3``.

