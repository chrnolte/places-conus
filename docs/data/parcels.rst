Parcels
=======

Parcels are the principal spatial unit in PLACES. They refer to unique, geo-referenced polygons of parcel boundaries in tax assessor maps.

*******************
Parcel data sources
*******************

We use **open-source** parcel boundary data wherever we could find a good file: in approximately one third of CONUS counties.

For the remaining counties, we use nationwide parcel data from **Regrid**. Through their `Data with Purpose <https://regrid.com/purpose>`_ program, Regrid provides access to their parcel data for non-profit researchers on a "pay what you can" basis. We have no financial interests in the company, and are glad they do this.


**********************
Parcel data attributes
**********************

PLACES generates hundreds of variables for each parcel (see :ref:`Features`)

We only obtain a few directly from the parcel boundary input data:

.. attribute:: pid

   This is the unique parcel identifier of the PLACES FMV (CONUS) dataset. It is derived from the parcel boundary data using our own hashing function.

.. attribute:: apn

   This is the tax Assessor's Parcel Number (APN): a string of characters that the tax assessor uses to identify the parcel in their property records and on a map. The syntax of these numbers varies widely across U.S. counties and New England towns.

.. attribute:: apn2

   Some parcel datasets have additional parcel identifiers that the tax assessor or county records office uses to identify the parcel or the taxpayer.

.. attribute:: ha

   Total area (hectares) of the parcel polygon (spatial reference: EPSG:5070).

.. attribute:: x

   X coordinate of the parcel centroid (spatial reference: EPSG:5070).

.. attribute:: y

   Y coordinate of the parcel centroid (spatial reference: EPSG:5070).
