Parcel types
============

A `parceltype` identifies types of parcels for which sales data is observed.


**************
Vacant parcels
**************

Vacant parcels are parcels for which our available indicators suggest that it contains no building.

Required selection criteria include:

- No detected building footprint :any:`p_bld_fp`
- No recorded positive building assessed value (:any:`val_b_za`) in linked tax assessor data.
- No recorded building market value (:any:`mv_b_za`) in linked tax assessor data.
- No standardized property land use code (:any:`bld_code`) that indicates the presence of a building (e.g. "single-family home")

:Identifier: ``v``


***********************
"Mostly" vacant parcels
***********************

"Mostly vacant" parcels are parcels that might have some buildings, but mostly consist of vacant land (in terms of area or property value).

Required selection criteria include:

- Detected building footprint (:any:`p_bld_fp`) covers <0.1% of the parcel area.
- Recorded building assessed value (:any:`val_b_za`) is ≤0.1% of the total assessed value (:any:`val_t_za`)
- Recorded building market value (:any:`mv_b_za`) is ≤0.1% of the total assessed value (:any:`mv_t_za`)

:Identifier: ``mv``


*******************
Single-family homes
*******************

Single-family homes are one of the most-studied property type in valuation studies in the United States and included here for comparison.

Required selection criteria include:

- Standardized property land use code (:any:`bld_code`) needs to indicate the presence of a single-family home or similar (in ZTRAX: ``RR000``, ``RR101``, ``RR102``, ``RR999``)
- One or two building footprints have to have been detected on the parcel (:any:`n_bld_fp`)

:Identifier: ``sfh``


*******************
Additional criteria
*******************

* Some model samples are restricted to subsections of the rural-urban gradient ("rural", "exurban", "urban"). The cutoffs between these regions are based on our experimental "population gravity" raster (:any:`bld_pop_exp_c4`): 0.09 to separate urban from exurban areas and 0.008 to separate exurban from rural areas. These are arbitrary values.

* Some model samples apply custom filters, e.g. for floodplains, wetlands, forests, coastlines. See below.

* All samples exclude properties with known conservation easements (:any:`p_e` > 20%, to avoid including encumbered purchases).

* All samples exclude properties that were part of a publicly financed land acquisition included in the :ref:`Validation` data (:any:`ct_p` > 20%, to avoid including validation data in the training sample).

* "Vacant" and "mostly vacant" models drop sales smaller than one acre.

********************
Parcel type: details
********************

Specifications for currently used parcel types (Jul 16, 2023)

.. csv-table::
  :file: ../cfg/parceltype.csv
  :stub-columns: 1

