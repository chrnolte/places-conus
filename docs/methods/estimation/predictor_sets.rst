Predictor sets
==============

Predictors sets are named sets (combinations) of :any:`Predictors` used in estimation.

Each `Model <#Models>`_ is trained on a specific predictor set. Because the choice of predictor set affects predictions and model performance, our approach compares several predictor selection strategies (top-down choices vs. forward-feature selection through cross-validation).

.. note::

   This section is still very much under development.


*********************
Default predictor set
*********************

Our starting point is the predictor set from `Nolte (2020) PNAS <https://www.pnas.org/doi/10.1073/pnas.2012865117>`_:


.. caution ::

   Two predictors from this set (Fathom flood data) are currently not for public use


********************************************
Predictor selection through cross-validation
********************************************

To improve the spatial prediction capacities of Predictor set, we an algorithm proposed by `Meyer et al. 2018 <https://www.sciencedirect.com/science/article/pii/S1364815217310976>`_ to select Predictor sets through target-oriented cross-validation.

The algorithm iteratively selects and adds predictors to the set as a function of how well the addition improve predictive accuracy.


Currently implemented:

* Spatial cross-validation (3 x 3 in-region quantiles of sales data)

.. warning::

   No temporal cross-validation yet.
