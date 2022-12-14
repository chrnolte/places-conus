Predictors
==========

This is the list of **parcel-level predictors** for our :ref:`Models` of fair market value (FMV).

They are derived from CONUS-wide spatial datasets and geo-located :ref:`parcel boundaries <Parcels>`.

:ref:`Models` are trained on *combinations* of these predictors called :ref:`Predictor sets`. These can also include predictors from :any:`Transactions` (e.g., :any:`date`) and :any:`Parcels` (e.g., :any:`x`, :any:`y`, :any:`ha`).

*******
Terrain
*******

.. attribute:: slope

   Average slope of parcel (degrees).

   :Source: USGS National Elevation Dataset (NED) 1/3 Arc-Second
   :Geoprocessing: Mean of pixel values within parcel (zonal statistics). Slope computed at 30m resolution in Google Earth Engine (EPSG:5070).

.. attribute:: elev

   Average elevation of parcel (meters).

   :Source: USGS National Elevation Dataset (NED) 1/3 Arc-Second
   :Geoprocessing: Mean of pixel values within parcel (zonal statistics). Elevation raster exported at 0.00449 degrees resolution from Google Earth Engine (EPSG:4326).


*********
Hydrology
*********

.. attribute:: cst_50

   Percentage (0-100) of coastal waters within a 50m radius. Used as proxy for beachfront properties and boating access.

   :Source: ESRI North America Water Polygons

.. attribute:: cst_2500

   Percentage (0-100) of coastal waters within a 2500m radius. Used as proxy for ocean proximity for near-ocean properties. Postively associated with distance to coast as well as with the added value of properties surrounded by coastal waters on several sides, such as islands, peninsulas, etc.

   :Source: same as :any:`cst_50`

.. attribute:: lake_frontage

   Estimated total lake frontage of the parcel (in meters).

   :Source: National Hydrographic  waterbodies from the National Hydrographic Database (NHD)NHDPlus High Resolution
   :Access: https://www.usgs.gov/national-hydrography/nhdplus-high-resolution
   :Accessed: Jun 18, 2019
   :Geoprocessing: Total area of intersection of parcel polygon with 50-meter-buffers around NHD lake waterbodies, divided by the buffer width (50m).

.. attribute:: river_frontage

   Estimated total river frontage of the parcel (in meters). Only waterbody polygons from the NHD are included (no lines).

   :Source: same as :any:`lake_frontage`
   :Geoprocessing: Total area of intersection of parcel polygon with 50-meter-buffers around NHD river waterbodies, divided by the buffer width (50m).

.. attribute:: lakefront

   Binary (0/1) indicator for the existence of river frontage.

   :Computation: int(:any:`river_frontage` > 0)

.. attribute:: riverfront

   Binary (0/1) indicator for the existence of river frontage.

   :Computation: int(:any:`river_frontage` > 0)

.. attribute:: water_exposure

   :Computation: (:any:`river_frontage` + :any:`lake_frontage`) / :any:`ha`.

.. attribute:: p_wet

   Percentage (0-100) of parcel area covered by wetland polygons.

   :Source: National Wetlands Inventory (NWI), U.S. Fish & Wildlife Service
   :Access: https://www.fws.gov/program/national-wetlands-inventory/wetlands-data
   :Accessed: Jun 18, 2019

.. attribute:: fld_fr_fath_p100

   Flood risk: average meters of inundation depth within the 1% annual exceedance probability floodplain (pluvial floods).

   :Source: Fathom-US Flood Hazard data (`Wing et al 2018 <https://iopscience.iop.org/article/10.1088/1748-9326/aaac65>`_)
   :Access: https://www.fathom.global/product/flood-hazard-data-maps/fathom-us/ (licensed)
   :Accessed: Mar 26, 2020
   :Geoprocessing: Zonal statistics (mean)

.. attribute:: fld_fr_fath_f100

   Flood risk: average meters of inundation depth within the 1% annual exceedance probability floodplain (fluvial floods).

   :Source: same as :any:`fld_fr_fath_p100`


**********
Land cover
**********

:Source: National Land Cover Database, Year-2011 Land Cover (Edition 2014-10-10)
:Access: `<https://www.mrlc.gov/data>`_


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

All of the following indicators are derived from Microsoft???s open-source `USBuildingFootprints <https://github.com/microsoft/USBuildingFootprints>`_ dataset, which contains polygons of 125.2 million buildings inferred from high-resolution satellite imagery with neural networks.

:Access: `<https://github.com/microsoft/USBuildingFootprints>`_
:Accessed: Dec 6, 2019

.. important::

   Microsoft's building footprints are our preferred open-source metric for the **presence of buildings** in CONUS, as they are more consistently available across CONUS than other indicators (e.g., tax assessor data). However, building footprints introduce new sources of error. For instance, footprints under trees are often missed.

   For more information, please refer to the `USBuildingFootprints documentation <https://github.com/microsoft/USBuildingFootprints>`_.

   Alternative measures of building presence are available in tax assessor and parcel boundary datasets. However, their availability and quality varies across states and counties. See `Nolte et al. (2021) <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3900806>`_ (Fig. S14) for a comparison of CONUS-wide building datasets.


.. attribute:: n_bld_fp

   Count of Microsoft building footprints on the parcel.

   :Geoprocessing: polygon intersections.

.. attribute:: p_bld_fp

   Percentage (0-100) of the area of the parcel that is covered by Microsoft building footprints.

   :Geoprocessing: polygon intersections.

.. aluna:aluna:: p_bld_fp_*

   Percentage of area within the given ``radius`` (integer, meters) that is covered by building footprints. An indicator of nearby building density.

   :Geoprocessing: rasterization of building footprints, pixel-based computation of average building footprint presence within circular neighborhood (2D convolution with moving-window kernel), averaged across all pixels within each parcel (zonal statistics).


.. attribute:: p_bld_fp_500

   See :aluna:ref:`p_bld_fp_*`

.. attribute:: p_bld_fp_5000

   See :aluna:ref:`p_bld_fp_*`



************
Demographics
************

.. attribute:: hh_inc_med_bg_2012-2016

   Median household income at the census block-group level (2012-2016)

   :Source: American Community Survey, via the National Historical Geographic Information System (NHGIS)
   :Access: `<https://www.nhgis.org/>`_
   :Geoprocessing: spatial joins of parcel centroids with reference units.


.. attribute:: bld_pop_exp_c4

   Population gravity.

   :Geoprocessing: block-group population counts are allocated to building footprint areas (Microsoft) on residential parcels (ZTRAX).

   .. note::
      [to be better documented]


**************
Infrastructure
**************

.. aluna:aluna:: rd_dst_pvd+

   Distance to nearest paved road, including highways (meters).

   :Source: TIGER/Line shapefiles from the U.S. Census Bureau for the year 2019
   :Access: `<https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html>`_
   :Accessed: Sept 10, 2020

   .. important ::

      Only computed up to 3km.

.. attribute:: travel

   Travel time to major cities (minutes), ca. 2000

   :Source: European Commission & World Bank (Nelson 2007)
   :Access: `<https://forobs.jrc.ec.europa.eu/products/gam/>`_

   .. important::

         This dataset was computed with different specifications than :any:`travel_weiss`. The two are not intercomparable. Differences do not necessarily reflect change over time.


.. attribute:: travel_weiss

   Travel time to major cities (minutes), ca. 2015

   :Source: Weiss et al. 2017 *Nature*
   :Access: `<https://www.nature.com/articles/nature25181>`_


***************
Land protection
***************

.. attribute:: p_prot_2010_5000

   See :aluna:ref:`p_prot_*_*`

.. attribute:: p_prot_*_*

   Percentage of area within a given <radius> (in meters) that is protected by fee or conservation easement in a given <year>.

   :Sources:
     * Protected Area Database of the United States (PAD-US 2.0)
     * National Conservation Easement Database (NCED)
     * New England Protected Open Space (NEPOS) database
     * Colorado Ownership, Management, and Protection (COMaP) database.

   :Geoprocessing:
     Rasterization of protection polygons, pixel-based computation of average protection within circular neighborhood (2D convolution with moving-window kernel), averaged across all pixels within each parcel (zonal statistics).

   .. warning::

      Clarify access to COMaP-derived indicators.
