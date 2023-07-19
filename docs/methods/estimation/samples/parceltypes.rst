Parcel types
============

A `parceltype` identifies types of parcels for which sales data is observed.


******
vacant
******

``v``

Vacant parcels are parcels for which our available indicators suggest that it contains no building.

Required selection criteria include:

- No detected building footprint :any:`p_bld_fp`
- No recorded positive building assessed value (:any:`val_b_za`) in linked tax assessor data.
- No recorded building market value (:any:`mv_b_za`) in linked tax assessor data.
- No standardized property land use code (:any:`bld_code`) that indicates the presence of a building (e.g. "single-family home")


*************
mostly vacant
*************

Identifier: ``mv``

"Mostly vacant" parcels are parcels that might have some buildings, but mostly consist of vacant land (in terms of area or property value).

Required selection criteria include:

- Detected building footprint (:any:`p_bld_fp`) covers <0.1% of the parcel area.
- Recorded building assessed value (:any:`val_b_za`) is ≤0.1% of the total assessed value (:any:`val_t_za`)
- Recorded building market value (:any:`mv_b_za`) is ≤0.1% of the total assessed value (:any:`mv_t_za`)


*******************
single-family homes
*******************

``sfh``

Single-family homes are one of the most-studied property type in valuation studies in the United States and included here for comparison.

Required selection criteria include:

- Standardized property land use code (:any:`bld_code`) needs to indicate the presence of a single-family home or similar (in ZTRAX: ``RR000``, ``RR101``, ``RR102``, ``RR999``)
- One or two building footprints have to have been detected on the parcel (:any:`n_bld_fp`)


********************
Parcel type: details
********************

Specifications for currently used parcel types (Jul 16, 2023)

.. csv-table::
  :file: ../cfg/parceltype.csv
  :stub-columns: 1

