Parcels
=======

Parcels are the principal spatial unit in PLACES. They refer to unique, geo-referenced polygons of parcel boundaries in tax assessor maps.


*******************
Parcel data sources
*******************


Parcel boundaries
#################

Parcel boundaries (geo-referenced polygons) are the principal unit of geoprocessing and analysis in PLACES.

In the U.S., most parcel boundary data is created and maintained by county (or town) governments, often by the local tax assessor, to locate **all taxable property** in the county.

Several data aggregators compile these county-level datasets at a national scale and sell licenses, often at high prices. In addition, there are several state-level efforts that compile county-level data into statewide databases (e.g., for tax equalization or planning purposes), some of which are publicly accessible (e.g., Massachusetts' `MassGIS <https://www.mass.gov/info-details/massgis-data-property-tax-parcels>`_, Maryland's `MdProperty View <https://planning.maryland.gov/Pages/OurProducts/PropertyMapProducts/MDPropertyViewProducts.aspx>`_, Florida's `GeoPlan <https://www.fgdl.org/metadata/fgdc_html/parcels_2019.fgdc.htm>`_).

We use **open-source** parcel boundary data wherever we can find a good file online: in approximately one third of CONUS counties.

For most of the remaining counties, we use nationwide parcel data from `Regrid <https://regrid.com>`_. Through their `Data with Purpose <https://regrid.com/purpose>`_ program, Regrid permits non-profit researchers to access their nationwide parcel database on a "pay what you can" basis. Our research would be impossible without this program, as other large-scale parcel providers tend to charge prices that are wildly unaffordable for most researchers in non-profit fields (e.g., environment, equity). Other than enjoying low-cost data access, we have no financial interests in the company.


Tax assessor records
####################

Tax assessor records form the basis of property taxation. They usually contain a table of all properties in a given county (or town), the tax assessor's estimate of their taxable value (often with separate estimates for buildings vs. land), as well as a (locally varying) set of attributes that the tax assessor uses to estimate property value (e.g., size of parcel). Many also contain names and mailing addresses of current owners.

Tax assessor records and parcel boundaries often contain similar data fields. However, the unit of tax assessor records is the property, not the parcel boundary. A single parcel boundary can include multiple properties (e.g. an apartment complex).

Our principal source of tax assessor data is Zillow's `ZTRAX <https://www.zillow.com/research/ztrax/>`_ dataset (see :ref:`Transactions` for more info). As we are not allowed to share these data, we don't use it as predictors, but principally as filters for our training data (e.g., to identify :ref:`Transactions` of vacant parcels).

We link Zillow's ZTRAX data to parcel boundary data using unique parcel identifiers and string pattern matching (regular expressions).


*****************
Parcel attributes
*****************


Parcel boundary attributes
###########################

PLACES uses geoprocessing to obtain a large number of attributes for each parcel (see :ref:`Predictors`).

The following variables are obtained directly from the parcel boundary input data:

.. attribute:: geometry_sha3_224

   This is the unique parcel identifier of the PLACES FMV (CONUS) dataset. It is derived directly from the geo-located parcel boundary data and anonymized with `SHA-3 <https://en.wikipedia.org/wiki/SHA-3>`_  hashing.

   The algorithm is described in :ref:`Data linkage`.

.. attribute:: pid

   Unique parcel identifier internal to PLACES. It currently cannot be shared publicly for parcels whose polygon data we obtain from licensed data sources, as it allows the reverse-engineering of parcel locations and areas.

.. attribute:: apn

   This is the tax Assessor's Parcel Number (APN): a string of characters that the tax assessor uses to identify the parcel in their property records and on a map. The syntax of these numbers varies widely across U.S. counties and New England towns.

   .. note:: Published only for open-access parcels

.. attribute:: apn2

   Some parcel datasets have additional parcel identifiers that the tax assessor or county records office uses to identify the parcel or the taxpayer.

   .. note:: Published only for open-access parcels

.. attribute:: ha

   Total area (hectares) of the parcel polygon (spatial reference: EPSG:5070).

.. attribute:: x

   X coordinate of the parcel centroid (spatial reference: EPSG:5070).

   .. note:: Published only for open-access parcels

.. attribute:: y

   Y coordinate of the parcel centroid (spatial reference: EPSG:5070).

   .. note:: Published only for open-access parcels


Tax assessor attributes
#######################

.. attribute:: mv_b_za

   Market value of buildings in ZTRAX assessor data. Used to identify vacant parcels.


.. attribute:: val_b_za

   Taxable value of buildings in ZTRAX assessor data. Used to identify vacant parcels.


.. attribute:: bld_code

   Standardized land use code for the property. Used to identify vacant parcels.
