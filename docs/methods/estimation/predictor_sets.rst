Predictor sets
==============

Predictors sets are named sets (combinations) of :any:`Predictors` used in estimation.

Each `Model <#Models>`_ is trained on a specific predictor set. Because the choice of predictor set affects predictions and model performance, our approach compares several predictor selection strategies (top-down choices vs. forward-feature selection through cross-validation).

.. note::

   This section is still very much under development.


********************
Groups of Predictors
********************

Public
######

* Terrain: :any:`elev`, :any:`slope`
* Water access: :any:`water_exposure`, :any:`cst_50`, :any:`cst_2500`, :any:`p_wet`
* Land cover: :any:`p_forest`, :any:`p_crops`, :any:`p_pasture`, :any:`p_grassland`, :any:`p_shrub`, :any:`p_barren`
* Demographics: :aluna:ref:`hh_inc_med_2012-2016`, :any:`bld_pop_exp_c4` (population gravity)
* Road access: :aluna:ref:`rd_dist_pvd+` :any:`travel`
* Nearby development: :any:`p_bld_fp_500`, :any:`p_bld_fp_5000`
* Nearby protection: :any:`p_prot_2010_5000`

Public for open-source parcels
##############################

* Parcel coordinates: :any:`x`, :any:`y`
* Parcel size: :any:`ha` - from parcel boundary data

Non-public
##########

* Flood risk: :any:`p_bld_fp_500`, :any:`p_bld_fp_5000` - from Fathom
* Time: :any:`year_cont` - from sales data




*******************
Predictor selection
*******************

To improve the spatial and temporal prediction capacities of the Predictor sets, we use an algorithm proposed by `Meyer et al. 2018 <https://www.sciencedirect.com/science/article/pii/S1364815217310976>`_ to select Predictor sets through target-oriented cross-validation.

The algorithm iteratively selects and adds predictors to the set as a function of how well the addition improve predictive accuracy.


Currently implemented:

* Spatial cross-validation (3 x 3 in-region quantiles of sales data)

.. warning::

   No temporal cross-validation yet.


Omitted
#######

For non-vacant parcels ("PLACES FMV: all" in `Nolte (2020) <https://www.pnas.org/doi/10.1073/pnas.2012865117>`_):

* Land cover: ``dev_intensity`` (was part of the  model that included non-vacant parcels)
* Buildings on parcel (0 for all vacant parcels): ``p_bld_fp``

