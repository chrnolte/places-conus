.. _Methods_Home:

Methods
=======

PLACES-FMV (CONUS) contains parcel-level estimates of the fair market value (FMV) of vacant and :ref:`"mostly" vacant<"Mostly" vacant parcels>` properties in the contiguous United States (see :ref:`data products <Data products>`).

The :ref:`estimation <Estimation>` component develops these estimates from statistical :ref:`models <Models>`. Our models are trained on :ref:`samples <Samples>` of private land transactions at various :ref:`geographic scales <Geographies>` using simple :ref:`estimators <Estimators>` (linear regressions, tree ensembles) and publicly available :ref:`predictors<Predictor sets>`.

The :ref:`validation <Validation>` component examines the strength of correlations between the resulting FMV estimates and the observed cost of public land acquisitions and conservation easements in the contiguous United States.

.. figure:: methods.png
   :width: 800
   :alt: Overview of methods

.. toctree::
   :maxdepth: 3

   methods/estimation
   methods/validation
