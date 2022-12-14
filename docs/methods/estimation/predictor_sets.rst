Predictor sets
==============

Predictors sets are named sets (combinations) of :any:`Predictors` used in estimation.

Each `Model <#Models>`_ is trained on a given predictor set.

We vary predictor sets across models to study how predictor selection affects model performance and predictions.


********************
Groups of Predictors
********************

Public
######

* Terrain: :any:`elev`, :any:`slope`
* Water access: :any:`water_exposure`, :any:`cst_50`, :any:`cst_2500`, :any:`p_wet`
* Flood risk: :any:`fld_fr_fath_f100`, :any:`fld_fr_fath_p100`
* Land cover: :any:`p_forest`, :any:`p_crops`, :any:`p_pasture`, :any:`p_grassland`, :any:`p_shrub`, :any:`p_barren`
* Demographics: :aluna:ref:`hh_inc_med_2012-2016`, :any:`bld_pop_exp_c4` (population gravity)
* Road access: :aluna:ref:`rd_dist_pvd+` :any:`travel`
* Nearby development: :any:`p_bld_fp_500`, :any:`p_bld_fp_5000`
* Nearby protection: :any:`p_prot_2010_5000`
* Population gravity: :any:`bld_pop_exp_c4`

Partially public
################

The following predictors are derived from the parcel boundary data. They are publicly accessible only for counties in which we have access to open-source parcel data (see :any:`Parcel data sources`).

* Parcel coordinates: :any:`x`, :any:`y`
* Parcel size: :any:`ha` - from parcel boundary data

Non-public
##########

* Time: :any:`year_cont` - from sales data


*******************
Predictor selection
*******************

To improve the spatial and temporal prediction capacities of the Predictor sets, we use an algorithm proposed by `Meyer et al. 2018 <https://www.sciencedirect.com/science/article/pii/S1364815217310976>`_ to select Predictor sets through target-oriented cross-validation.

The algorithm iteratively selects and adds predictors to the set as a function of how well the addition improve predictive accuracy.

.. todo:: Explain use of spatial predictors.

Implemented:

* Spatial cross-validation (3 x 3 in-region quantiles of sales data)

Not yet implemented:

* Temporal (predictive) cross-validation.
* Spatiotemporal cross-validation.


Omitted
#######

For non-vacant parcels ("PLACES FMV: all" in `Nolte (2020) <https://www.pnas.org/doi/10.1073/pnas.2012865117>`_):

* Land cover: ``dev_intensity`` (was part of the  model that included non-vacant parcels)
* Buildings on parcel (0 for all vacant parcels): ``p_bld_fp``

