Parcels
=======

Parcels are the principal spatial unit in :ref:`PLACES`.

They refer to unique, geo-referenced polygons of parcel boundaries in tax assessor maps.

Parcels can come in all shapes and sizes. Most are private and small, but many combinations of ownership and size exist. Most have buildings, but many are vacant. But they are a simplification of the real world, so they include it all: small parking lots, golf courses, former mining claims, and very large parcels that can contain half or more of a county's area (usually federal, state, or Native American-owned land, mostly in the West).

We keep small parcels small and large parcels large. Expect considerable spatial heterogeneity between and within them.


*******************
Parcel data sources
*******************

Parcel boundaries
#################

Parcel boundaries (geo-referenced polygons) are the principal unit of geoprocessing and analysis in :ref:`PLACES`.

In the U.S., parcel boundary data is created and maintained by local (county or town) governments to locate **all taxable property** in the county.

There is no federal cadaster in the United States. Commercial data aggregators compile local datasets at a national scale and sell data licenses. Some states compile statewide databases (e.g., for tax equalization or planning purposes), a subset of which is publicly accessible (e.g., Massachusetts' `MassGIS <https://www.mass.gov/info-details/massgis-data-property-tax-parcels>`_, Maryland's `MdProperty View <https://planning.maryland.gov/Pages/OurProducts/PropertyMapProducts/MDPropertyViewProducts.aspx>`_, Florida's `GeoPlan <https://www.fgdl.org/metadata/fgdc_html/parcels_2019.fgdc.htm>`_).

We use **open-source** parcel boundary data wherever we can find a good file online: in approximately one third of CONUS counties.

For most of the remaining counties, we use nationwide parcel data from `Regrid <https://regrid.com>`_. Through their `Data with Purpose <https://regrid.com/purpose>`_ program, Regrid permits non-profit researchers to access their nationwide parcel database on a "pay what you can" basis.

We're grateful for that program: our research would be impossible without it. Licenses to nationwide parcel data from other parcel data providers tend to be unaffordable for many non-profit researchers working in public-interest areas with limited funding (e.g., environmental, rural, equity-focused). Other than enjoying this low-cost data access, we have no financial interests in the company.

Tax assessor records
####################

Tax assessor records (or **tax roll** data) refer to datasets collected by a publicly appointed property tax assessor to assess the taxable value of all properties within their jurisdiction (town or county).

The centerpiece of these records is a table of all real estate properties in the jurisdiction. It usually contains a unique property identifier (the "assessor parcel number", or :`apn`:) the tax assessor's estimate of their taxable value, sometimes with separate estimates for buildings vs. land, as well as locally varying sets of attributes that the tax assessor uses to estimate property value (e.g., lot size of parcel). Many also contain names and mailing addresses of current owners.

Tax assessor records and parcel boundaries often contain similar data fields. However, the unit of tax assessor records is the property, not the parcel boundary. A single parcel boundary can include multiple properties (e.g. an apartment complex).

Up until Sep 30, 2023, our main source of tax assessor data is Zillow's `ZTRAX <https://www.zillow.com/research/ztrax/>`_ dataset (see :ref:`Transactions` for more info). As we are not allowed to share these data, we do not use it as predictors of models we want to be able to publish. However, we use it extensively as filters for our training data (e.g., to identify arms-length :ref:`Transactions` or vacant parcels).

We link Zillow's ZTRAX data to parcel boundary data using unique parcel identifiers and string pattern matching described in `Nolte 2020 PNAS <https://www.pnas.org/doi/10.1073/pnas.2012865117>`_ and `Nolte et al. 2023 Land Economics <https://le.uwpress.org/content/early/2023/06/09/le.100.1.102122-0090R>`_.


*****************
Parcel attributes
*****************

Parcel boundary attributes
##########################

PLACES uses geo-referenced parcel boundaries to derive a wide range of attributes from publicly available spatial data using (see :ref:`Predictors`).

In addition, a few important variables are obtained directly from the parcel boundary input data:

.. attribute:: geometry_sha3_224

   This is the unique parcel identifier of the PLACES FMV (CONUS) dataset. It is the hashed value of :any:`geometry`,  anonymized using secure `SHA-3 <https://en.wikipedia.org/wiki/SHA-3>`_  hashing. Anyone with access to parcel boundary data can compute using a short Python code snippet provided in the :ref:`Data linkage` section.

.. attribute:: geometry

   The geospatial parcel boundary (by default in EPSG:5070 projection)

   We apply minimal geospatial manipulations to the originally imported geometries: zero-buffers (a common fix for polygon topology errors), projection into EPSG:5070, removal of duplicates (approximate). Empty land areas (as identified by the National Land Cover Database, year 2010, 2019 version) are filled with a hexagon layer.

   .. note:: Published only for parcels from open-access sources (see :ref:`Parcel data sources`).

.. attribute:: pid

   Unique parcel identifier internal to PLACES. It currently cannot be shared publicly for parcels whose polygon data we obtain from licensed data sources, as it allows the reverse-engineering of parcel locations and areas.

.. attribute:: apn

   This is the tax Assessor's Parcel Number (APN): a string of characters that the tax assessor uses to identify the parcel in their property records and on a map. The syntax of these numbers varies widely across U.S. counties and New England towns.

.. attribute:: apn2

   Some parcel datasets have additional parcel identifiers that the tax assessor or county records office uses to identify the parcel or the taxpayer.

.. attribute:: ha

   Total area (hectares) of the parcel polygon (spatial reference: EPSG:5070).

.. attribute:: x

   X coordinate of the parcel centroid (spatial reference: EPSG:5070).

   .. note:: Published only for parcels from open-access sources (see :ref:`Parcel data sources`).

.. attribute:: y

   Y coordinate of the parcel centroid (spatial reference: EPSG:5070).

   .. note:: Published only for parcels from open-access sources (see :ref:`Parcel data sources`).


Tax assessor attributes
#######################

.. note::

   We obtain all tax assessor data from `ZTRAX <https://www.zillow.com/research/ztrax/>`_ (see :ref:`Transactions`).

   Tax assessor attributes will not be part of the PLACES-FMV (CONUS) data release. We can only share it until Sep 30, 2023, and only with researchers that already have a license to ZTRAX. Future research projects will have to obtain data for these variables independently from their local county records office or from aggregators of such data.

.. attribute:: mv_b_za

   Market value of buildings in ZTRAX assessor data. Used to identify vacant parcels.

.. attribute:: mv_t_za

   Market value of property (both land and buildings) in ZTRAX assessor data. Used to identify :any:`Mostly vacant` parcel types and to filter out sales with extremely large discrepancies between sales prices and estimated market value.

.. attribute:: val_b_za

   Taxable value of buildings in ZTRAX assessor data. Used to identify vacant parcels.

.. attribute:: val_t_za

   Taxable value of property (both land and buildings) in ZTRAX assessor data. Used to identify :any:`Mostly vacant` parcel types.

.. attribute:: bld_code

   Standardized land use code for the property. Used to identify vacant parcels.
