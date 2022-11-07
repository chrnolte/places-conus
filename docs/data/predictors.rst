Predictors
==========

This is the list of variables used as predictors in the estimation of fair market value.

*******
Terrain
*******

.. attribute:: slope

   Average slope of parcel (degrees).

   Source: USGS National Elevation Dataset (NED) 1/3 Arc-Second [deprecated]

   Geoprocessing: zonal statistics mean of pixel-level values of slope (in degrees), computed at 30m resolution in Google Earth Engine (EPSG:5070).

.. attribute:: elev

   Average elevation of parcel (meters).

   Source: USGS National Elevation Dataset (NED) 1/3 Arc-Second [deprecated]

   Geoprocessing: mean of pixel values of elevation (in meters) within parcels, at 0.00449 degrees resolution (EPSG:4326).


*********
Hydrology
*********

.. attribute:: cst_50

   Percentage (0-100) of coastal waters within a 50m radius. Used as proxy for beachfront properties and boating access.

   Source: ESRI North America Water Polygons

.. attribute:: cst_2500

   Percentage (0-100) of coastal waters within a 2500m radius. Used as proxy for ocean proximity for near-ocean properties. Postively associated with distance to coast as well as with the added value of properties surrounded by coastal waters on several sides, such as islands, peninsulas, etc.

.. attribute:: lake_frontage

   Estimated total frontage (in meters) of the parcel along lake waterbodies from the National Hydrographic Database (NHD).

   Geoprocessing: total area of intersections of the parcel polygon with 50-meter-buffers around NHD lakes, divided by the buffer width (50m).

.. attribute:: river_frontage

   Estimated lake frontage (in meters) to the closest lake waterbody in the National Hydrographic Database (NHD).

   Geoprocessing: total area of intersections of the parcel polygon with 50-meter-buffers around NHD lakes, divided by the buffer width (50m).

.. attribute:: water_exposure

   Sum of river and lake frontage, normalized by parcel size

   :any:`river_frontage` / :any:`ha` + :any:`lake_frontage` / :any:`ha`

.. attribute:: p_wet

   Percentage (0-100) of parcel area covered by wetland polygons from the US Fish and Wildlife Service National Wetlands Inventory (39).

.. attribute:: fld_fr_fath_p100

   Flood risk: average meters of inundation depth within the 1% annual exceedance probability floodplain (pluvial floods).

   Source: Fathom

   .. warning::

      Licensed. Not for publication.

.. attribute:: fld_fr_fath_f100

   Flood risk: average meters of inundation depth within the 1% annual exceedance probability floodplain (fluvial floods).

   Source: Fathom

   .. warning::

      Licensed. Not for publication.


**********
Land cover
**********

Source: National Land Cover Database, Year-2011 Land Cover (edition: 2014-10-10)


.. attribute:: p_forest

   Percentage (0-100) of NLCD pixels classified as forest (deciduous, evergreen, or mixed) in 2011.


.. attribute:: p_crops

   Percentage (0-100) of NLCD pixels classified as cropland in 2011.


.. attribute:: p_pasture

   Percentage (0-100) of NLCD pixels classified as pasture in 2011.


.. attribute:: p_grassland

   Percentage (0-100) of NLCD pixels classified as grassland in 2011.


.. attribute:: p_shrub

   Percentage (0-100) of NLCD pixels classified as shrubland in 2011.


.. attribute:: p_barren

   Percentage (0-100) of NLCD pixels classified as barren land in 2011.


*********
Buildings
*********

Microsoft’s open-source building footprint dataset contains polygons of 125.2 million buildings.

.. attribute:: n_bld_fp

   Count of Microsoft building footprints on the parcel.

   Geoprocessing: polygon intersections.

.. attribute:: p_bld_fp

   Percentage (0-100) of the area of the parcel that is covered by Microsoft building footprints.

   Geoprocessing: polygon intersections.

.. attribute:: p_bld_fp_<radius>

   Percentage of area within the given ``radius`` (integer, meters) that is covered by building footprints. An indicator of nearby building density.

   Geoprocessing: rasterization of building footprints, pixel-based computation of average building footprint presence within circular neighborhood (2D convolution with moving-window kernel), averaged across all pixels within each parcel (zonal statistics).


************
Demographics
************

.. attribute:: hh_inc_med_bg_2012_2016

   Median household income at the census block-group level (2012-2016)

   Source: American Community Survey, via the National Historical Geographic Information System (NHGIS)

   Geoprocessing: spatial joins.

   .. note::

      The actual name of this variable in the PLACES database is ``hh_inc_med_bg_2012-2016``. Leaving this here until I figure out how to let reStructuredText accept the '-' in the variable name.


.. attribute:: bld_pop_exp_c4

   Population gravity.

   Geoprocessing: block-group population counts are allocated to building footprint areas (Microsoft) on residential parcels (ZTRAX).

   .. note::
      [to be better documented]


**************
Infrastructure
**************

.. _rd_dist_pvd+:

.. attribute:: rd_dist_pvd

   Distance to nearest paved road **excluding** highways (meters).

   ``rd_dist_pvd+``: Distance to nearest paved road **including** highways (meters).

   Source: TIGER/Line shapefiles from the U.S. Census Bureau.


.. attribute:: travel

   Travel time to major cities (minutes), ca. 2000

   Source: European Commission & World Bank. Download: `Nelson 2007 <https://forobs.jrc.ec.europa.eu/products/gam/>`_

   .. note::

         This dataset was computed with different specifications than :any:`travel_weiss`. The two are not intercomparable. Differences do not necessarily reflect change over time.


.. attribute:: travel_weiss

   Travel time to major cities (minutes), ca. 2015

   Source: `Weiss et al. 2017 Nature <https://www.nature.com/articles/nature25181>`_


***************
Land protection
***************

.. attribute:: p_prot_<radius>_<year>


   Percentage of area within a given <radius> (in meters) that is protected by fee or conservation easement in a given <year>.

   Sources:

   * Protected Area Database of the United States (PAD-US 2.0)
   * National Conservation Easement Database (NCED)
   * New England Protected Open Space (NEPOS) database
   * Colorado Ownership, Management, and Protection (COMaP) database.

   .. warning::

      Clarify access to COMaP-derived indicators.

   Geoprocessing: rasterization of protection polygons, pixel-based computation of average protection within circular neighborhood (2D convolution with moving-window kernel), averaged across all pixels within each parcel (zonal statistics).
