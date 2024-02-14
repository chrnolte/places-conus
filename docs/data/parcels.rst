Parcels
=======

Parcels are the principal spatial unit in :ref:`PLACES`.

They refer to unique, geo-referenced polygons of parcel boundaries in tax assessor maps.

Parcels can come in all shapes and sizes. Most are private and small, but many owners and sizes exist. Most have buildings, many remain vacant. All are included: small parking lots, golf courses, former mining claims, and public parcels that cover more than half a county.


*******************
Parcel data sources
*******************

Parcel boundaries
#################

Parcel boundaries (geo-referenced polygons) are the principal unit of geoprocessing and analysis in :ref:`PLACES`.

In the U.S., parcel boundary data is created and maintained by county or town governments to locate all taxable property in the county.

There is no federal cadaster in the United States. Commercial data aggregators compile local data nationally and sell data licenses. Some states make statewide databases (e.g., for tax equalization or planning purposes) available for public download (e.g., Massachusetts' `MassGIS <https://www.mass.gov/info-details/massgis-data-property-tax-parcels>`_, Maryland's `MdProperty View <https://planning.maryland.gov/Pages/OurProducts/PropertyMapProducts/MDPropertyViewProducts.aspx>`_, Florida's `GeoPlan <https://www.fgdl.org/metadata/fgdc_html/parcels_2019.fgdc.htm>`_).

We use open-source parcel boundary data wherever we can: in about a third of CONUS counties. For most of the remainder, we use parcel data from `Regrid <https://regrid.com>`_'s `Data with Purpose <https://regrid.com/purpose>`_ program, which offers access to nationwide parcel data for non-profit researchers on a "pay what you can" basis.

Tax assessor records
####################

Tax assessor records ("tax roll" data) are datasets collected by a publicly appointed property tax assessor to assess the taxable value of properties within their jurisdiction (town or county).

They usually contain a table of all (or most) real estate properties in a jurisdiction with a unique property identifier (the "assessor parcel number", or :any:`apn` ), the assessor's estimate of each property's taxable value, and many other attributes that the tax assessor uses to estimate property value, such as lot size, building size and age, bathroom and bedroom counts, etc.

The unit of tax assessor records is the property, not the parcel boundary. A single parcel boundary can include multiple properties (e.g. an apartment complex). A single property can be composed of multiple parcels (e.g., a large ranch)

Until Sep 30, 2023, our main source of tax assessor data was Zillow's `ZTRAX <https://www.zillow.com/research/ztrax/>`_ dataset (see :ref:`Transactions` for more info). We use such data as filters for our training data (e.g., to identify arms-length :ref:`Transactions` or vacant parcels). As we were not allowed to share these data publicly, we did not use it as :ref:`Predictors` in our :ref:`Models`.

We link Zillow's ZTRAX data to parcel boundary data using unique parcel identifiers and string pattern matching (`Nolte 2020 PNAS <https://www.pnas.org/doi/10.1073/pnas.2012865117>`_, `Nolte et al. 2024 Land Economics <https://le.uwpress.org/content/100/1/200>`_).


*****************
Parcel attributes
*****************

Parcel boundary attributes
##########################

PLACES uses geo-referenced parcel boundaries to derive attributes of land, buildings, and people from publicly available spatial data (see :ref:`Predictors`).

We obtain several essential attributes from parcel boundary data:

.. attribute:: geometry_sha3_224

   This is the unique parcel identifier of the PLACES FMV (CONUS) dataset. It is the hashed value of :any:`geometry`,  anonymized using secure `SHA-3 <https://en.wikipedia.org/wiki/SHA-3>`_  hashing. Anyone with access to parcel boundary data can compute it using a short Python code snippet (see :ref:`Data linkage`).

.. attribute:: geometry

   The geospatial parcel boundary (in EPSG:5070 projection).

   Geoprocessing includes: zero-buffers (fixes polygon topology errors), projection into EPSG:5070, and removal of (approximate) duplicates. Empty land areas* are filled with "dummy" parcels (a hexagon layer).

   * As identified by the `National Land Cover Database <https://www.usgs.gov/centers/eros/science/national-land-cover-database>`_, 2019 version, year 2010 estimate.

   .. note:: Published only for parcels from open-access sources (see :ref:`Parcel data sources`).

.. attribute:: pid

   Unique parcel identifier internal to PLACES.

.. attribute:: apn

   Assessor's Parcel Number (APN): a string of characters that the local public tax assessor uses to identify the parcel in their property records and on a map. The syntax of these numbers varies across counties and towns.

.. attribute:: apn2

   Some parcel datasets have additional parcel identifiers that the tax assessor or county records office uses to identify the parcel or the taxpayer.

.. attribute:: ha

   Area (hectares) of the parcel polygon (in EPSG:5070 projection).

.. attribute:: x

   X coordinate of the parcel centroid (in EPSG:5070 projection).

   .. note:: Published only for parcels from open-access sources (see :ref:`Parcel data sources`).

.. attribute:: y

   Y coordinate of the parcel centroid (in EPSG:5070 projection).

   .. note:: Published only for parcels from open-access sources (see :ref:`Parcel data sources`).

.. attribute:: lat_id

   Latitude of parcel centroid in EPSG:4326 projection.

   If the centroid falls outside the parcel boundary, this latitude refers to the parcel's "Pole of Inaccessibility".

   .. note:: Published only for parcels from open-access sources (see :ref:`Parcel data sources`).

.. attribute:: long_id

   Longitude of parcel centroid in EPSG:4326 projection.

   If the centroid falls outside the parcel boundary, this longitude refers to the parcel's "Pole of Inaccessibility".

   .. note:: Published only for parcels from open-access sources (see :ref:`Parcel data sources`).

Tax assessor attributes
#######################

.. note::

   We obtained all tax assessor data from `ZTRAX <https://www.zillow.com/research/ztrax/>`_ (see :ref:`Transactions`). 

   We had to delete it on Sep 30, 2023, as per our data license with Zillow.

   Tax assessor attributes will not be part of the PLACES-FMV (CONUS) data release.

.. attribute:: mv_b_za

   Market value of buildings in ZTRAX assessor data. Used to identify vacant parcels.

.. attribute:: mv_t_za

   Market value of property (both land and buildings) in ZTRAX assessor data. Used to identify :any:`"mostly" vacant parcels <"Mostly" vacant parcels>` and to filter out sales with extremely large discrepancies between sales prices and estimated market value.

.. attribute:: val_b_za

   Taxable value of buildings in ZTRAX assessor data. Used to identify vacant parcels.

.. attribute:: val_t_za

   Taxable value of property (both land and buildings) in ZTRAX assessor data. Used to identify :any:`"mostly" vacant parcels <"Mostly" vacant parcels>`.

.. attribute:: bld_code

   Standardized land use code for the property. Used to identify vacant parcels.
