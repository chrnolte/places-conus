Raster data
===========

:Folder: ``rasters/``
:Format: GeoTIFF
:CRS: Conus Albers (`EPSG:5070 <https://epsg.io/5070-1252>`_
:Resolution: 480 x 480 meters, snapped to National Land Cover Database

*******************************
Rasterized land value estimates
*******************************

Parcel-level land value estimates for the contiguous United States.

These are the rasters we use when making maps such as the one published in Nolte 2020 PNAS

:Folder: ``rasters/estimates/``
:File syntax:
 ``<unit>_<model>_<prediction_year>.tif``

:Example:
 ``lnusd-ha-16_conus_mv_lm_2010.tif`` is a land value raster that

 * Uses the unit ``lnusd-ha-16`` (logged per-hectare dollars * 16)
 * Estimates were made by the model ``conus_mv_lm``
 * Estimates are made for the year ``2010``

:Unit:
 Natural logarithm of U.S. dollars (deflated to Jan 2022) per hectare, multiplied by 16 (``ln($/ha) * 16``).

 `The multiplication with 16 allows us to save the rasters as integers instead of floats (saves space) without too much loss of information (i.e. integers cover most of the range of the data)`


******************************
Rasterized statistical support
******************************

Indicators of statistical support: how different from the training sample are the parcels for which the predictions are made?

:Folder: ``rasters/support/``
:File syntax:
 ``distance_<model>_<prediction_year>.tif``
:Example:
 ``distance_conus_mv_lm_2010.tif`` is a raster of Meyer & Pebesma's distance index:

 * For the model ``conus_mv_lm``
 * For predictions made in the year ``2010``

:Unit:
 Unitless distance (`Meyer & Pebesma 2021 <https://besjournals.onlinelibrary.wiley.com/doi/full/10.1111/2041-210X.13650>`_)
