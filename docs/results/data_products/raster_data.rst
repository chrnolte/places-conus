Raster data
===========

:Folder: ``rasters/``
:Format: GeoTIFF
:Projection: Conus Albers (`EPSG:5070 <https://epsg.io/5070-1252>`_)
:Resolution: 480 x 480 meters (snapped to the `National Land Cover Database <https://www.mrlc.gov/data>`_)

*******************************
Rasterized land value estimates
*******************************

Parcel-level land value estimates for the contiguous United States.

:Folder: ``rasters/estimates/``
:File syntax:
 ``<unit>_<model>_<prediction_year>.tif``

:Example:
 ``lnusd-ha-16_conus_mv_lm_2010.tif`` is a land value raster that

 * Uses the unit ``lnusd-ha-16`` (logged per-hectare dollars * 16)
 * Estimates were made by the model ``conus_mv_lm``
 * Estimates are made for the year ``2010``

:Unit:
 Natural logarithm of U.S. dollars (deflated to Jan 2022) per hectare

 To save space, we converted the `float` values into `uint8` by multiplying the ``ln($/ha)`` unit with 16.

 `The multiplication with 16 allows us to save the rasters as integers instead of floats (saves space) without too much loss of information (i.e. integers cover most of the range of the data)`


******************************
Rasterized statistical support
******************************

Indicators of statistical support: how different from the training sample are the parcels for which the predictions are made?

Our "Area of Applicability" (AOA) indicator is based on `Meyer & Pebesma 2021 <https://besjournals.onlinelibrary.wiley.com/doi/full/10.1111/2041-210X.13650>`_.



:Folder: ``rasters/support/``
:File syntax:
 ``AOA_<model>_<prediction_year>_<cross-validation type>.tif``
:Example:
 ``AOA_conus_mv_lm_2010_bg.tif`` is a raster of Meyer & Pebesma's distance index:

 * For the model ``conus_mv_lm``
 * For predictions made in the year ``2010``
 * Based on cross-validation blocked by census block groups ``bg``

:Unit:
 Unitless distance

 Rasterized AOA maps are created by dividing the distance index by the AOA threshold, and taking the natural logarithm. As a result, pixels with values < 0 are within the AOA, pixels with values > 0 are outside.

 To save space, we converted the `float` values into `uint8` using the following conversion: (x + 4) * 25.
