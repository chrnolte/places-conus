.. _Methods_Home:

Methods
=======

PLACES-FMV (CONUS) data are parcel-level **estimates** of fair market value (FMV) and associated uncertainties.

The :ref:`Estimation` component develops these estimates from data on private land transactions.

Estimates are predictions (conditional means) created by :ref:`Models`.

Our models are trained on samples from different :ref:`geographic areas <Geographies>` (counties, regions, states, CONUS) and :ref:`parcel types <Parcel types>` (vacant, mostly vacant). They employ different statistical regression :ref:`estimators <Estimators>` (linear, tree ensembles) and see different :ref:`sets of predictors<Predictor sets>`.

The :ref:`Validation` component examines the strength of correlations between FMV estimates and the actual cost of public land acquisitions and conservation easements in CONUS.

.. image:: methods.png
   :width: 800
   :alt: Methods overview


.. toctree::
   :maxdepth: 2
   :caption: Learn more

   methods/estimation
   methods/validation
