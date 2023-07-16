Predictor sets
==============

Predictors sets are named sets (combinations) of :any:`Predictors` used in estimation.

Each `Model <#Models>`_ is trained on a given predictor set.

We vary predictor sets across models to study how predictor selection affects model performance and predictions.


*********
Reference
*********

:Identifier: ``ref``

* Terrain: :any:`elev`, :any:`slope`
* Water access: :any:`water_exposure`, :any:`cst_50`, :any:`cst_2500`
* Flood risk and wetlands: :any:`fld_fr_fath_f100`, :any:`fld_fr_fath_p100`, :any:`p_wet`
* Land cover: :any:`p_forest`, :any:`p_crops`, :any:`p_pasture`, :any:`p_grassland`, :any:`p_shrub`, :any:`p_barren`
* Demographics: :aluna:ref:`hh_inc_med_2012-2016`, :any:`bld_pop_exp_c4` (population gravity)
* Road access: :aluna:ref:`rd_dist_pvd+` :any:`travel`
* Nearby development: :any:`p_bld_fp_500`, :any:`p_bld_fp_5000`
* Nearby protection: :any:`p_prot_2010_5000`
* Population gravity: :any:`bld_pop_exp_c4`

