Data linkage
============

In order to join our parcel data to yours, you will need to generate the correct parcel identifiers.

Our published datasets use the parcel identifier :any:`geometry_sha3_224` to identify individual parcels. This unique identifier is derived from geo-referenced parcel geometries (polygons) using a secure hash algorithm (SHA 224).

We have chosen this approach because:

* it is **easy to generate**. You only need a parcel geometry dataset and rudimentary Python knowledge.
* it is **unambiguous**. If our parcel identifiers match, you know we're referring to exactly the same tract of land. If the parcel boundary is not identical, you won't get a match.
* it is **secure**. Access to the published parcel identifiers does not allow anyone to re-create the parcel geometries. This was an essential precondition for publishing datasets derived from licensed parcel boundary data (Regrid).


*****************
Linkage algorithm
*****************

The following Python code snippet allows you to generate :any:`geometry_sha3_224` from your parcel boundary polygons (geo-referenced vector data).

It requires the Python package ``geopandas``, which provides functionality for vector data processing in Python (`installation instructions <https://geopandas.org/en/stable/getting_started/install.html>`_).

Replace ``FILEPATH`` with the filepath to your parcel data file. Any format supported by the Python package `fiona <https://fiona.readthedocs.io/en/latest/index.html>`_ will work (e.g. .shp, .gpkg, .gdb). If the vector data is not provided in the required projection (`EPSG 5070 <https://geopandas.org/en/stable/getting_started/install.html>`_), it will be automatically reprojected::

   import hashlib
   import geopandas as gpd

   # Filepath
   FILEPATH = '/folder_to_my_parcel_data/25011_parcels.gpkg'

   pc = gpd.read_file(FILEPATH)
   print('Load')

   if not pc.crs == 'epsg:5070':
       pc = pc.to_crs('epsg:5070')
       print('Reproject')

   def to_sha3_224(x):
       m = hashlib.sha3_224()
       m.update(bytes(str(x), encoding='utf-8'))
       return m.hexdigest()

   pc['geometry_sha3_224'] = pc['geometry'].apply(to_sha3_224)
   t('Hash')

   pc[['geometry', 'geometry_sha3_224']]

The result should look similar to this one (from Franklin county, Massachusetts):

.. image:: linkage_results.png
  :width: 800
  :alt: Regions
