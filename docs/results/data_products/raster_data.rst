Raster data
===========


*******************************
Fair market value (FMV) rasters
*******************************



Parcel-level estimates of "fair market value" (FMV) for the contiguous United States, rasterized.

:Folder: ``rasters/estimates/``

:File syntax:
 ``fmv_<model_id>_<prediction_year>.tif``, where ``model_id`` identifies the :ref:`model <Model specifications>`.

:Example:
 ``fmv_region-nb_2010.tif`` is a land value raster with estimates from the model ``region-nb`` for the year ``2010``.

:Unit:
 Natural logarithm of U.S. dollars per hectare (deflated to Jan 2022), divided by 16 and rounded to save space (``uint8``).

 .. math::
 
   \frac{ln(\frac{$}{hectare})}{16}

:Geoprocessing:
 Parcel-level estimates are assigned to their :ref:`parcel boundary polygons <Parcels>` and rasterized.

:Format: GeoTIFF
:Projection: Conus Albers (`EPSG:5070 <https://epsg.io/5070-1252>`_)
:Resolution: 480 x 480 meters (snapped to the `National Land Cover Database <https://www.mrlc.gov/data>`_)

.. image:: raster_fmv.png
  :width: 800
  :alt: Fair market value rasters


***********************************
Area of applicability (AOA) rasters
***********************************


Parcel-level indicators of statistical support for the FMV estimates, rasterized.

We use the :ref:`Area of Applicability (AOA)` proposed by `Meyer & Pebesma 2021 <https://besjournals.onlinelibrary.wiley.com/doi/full/10.1111/2041-210X.13650>`_.

In a nutshell, the AOA is a metric of how dissimilar the predicted parcel is from the parcels on which the :ref:`model <Models>` was trained, in comparison to how dissimilar the parcels were to each other in the cross-validation of the model (from which the uncertainties are derived).

Dissimilarity is computed as the distance in the predictor space, where predictors are scaled (weighted) according to their importance in the model.

:Folder: ``rasters/support/``

:File syntax:
 ``aoa_<model_id>_<prediction_year>_<cross-validation type>.tif``, where ``model_id`` identifies the :ref:`model <Model specifications>` and ``cross-validation type`` identifies the type of :ref:`cross-validation <Cross-validation>`.

:Example:
 ``aoa_region-nb_2010_bg.tif`` is a raster of Meyer & Pebesma's distance index:

 * For the model ``region-nb``
 * For predictions made in the year ``2010``
 * Cross-validation blocked by census block groups ``bg``

:Unit:
 Unitless distance, converted.

 We picked a conversion that would result in values ≤100 being within the AOA, and values ≥100 being outside the AOA, while preserving as much of the heterogeneity in AOA as possible within a space-saving `uint8` raster.

  .. math::
   
    (ln(AOA) - 4) * 25

:Format: GeoTIFF
:Projection: Conus Albers (`EPSG:5070 <https://epsg.io/5070-1252>`_)
:Resolution: 480 x 480 meters (snapped to the `National Land Cover Database <https://www.mrlc.gov/data>`_)


.. image:: raster_aoa.png
  :width: 800
  :alt: Area of applicability rasters
