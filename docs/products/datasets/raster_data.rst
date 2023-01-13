Raster data
===========

Folder: ``rasters``

CONUS-wide rasters of predicted fair market values and other rasterized measures (distance index) in EPSG:5070 projection at 480m resolution.

Unit of all FMV estimates is: ln($/ha), where $ refers to January 2022 dollars

In all published raster names, the ``16`` refers to the raster resolution in units of 30m, the width of a pixel in our base raster reference (USGS NLCD). ``16`` translates to an aggregation of 16 x 16 pixels and thus a resolution of 480m.

*******************
CONUS model rasters
*******************

Folder and filename syntax: ``rasters/conus/ln_rprc_ha_pred_<model_name>_16_<version>.tif``

For an interpretation of ``<model_name>``, see :any:`CONUS models`

``<version>`` tracks consecutive updates.

**************
Region rasters
**************

Rasters derived from models for submarkets within regions. Each model is fit on either urban, exurban, or remote sales within each region. Not all submarkets have sufficient sales to produce predictions.

FMV predictions
###############

Folder and filename syntax: ``rasters/regions/fmv_<model_name>_16_<version>.tif``

*[rename to `ln_rprc_ha_pred` for consistency]*

For an interpretation of ``<model_name>``, see :any:`Regional models`.

``<version>`` tracks consecutive updates.

Distance index
##############

For a definition and computation, see :any:`Distance index (DI)`.

Filename convention: ``rasters/regions/DI_<model_name>_16_<version>.tif``

