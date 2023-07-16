Geographies
===========

A **geography** defines the geographic location where the sales data comes from.

Recognized geographies:

* :ref:`counties <Counties>` (with and without neighbors)
* :ref:`regions <Regions>` (with and without neighbors)
* :ref:`states <States>`
* :ref:`contiguous U.S. <CONUS>`.


********
Counties
********

Single-county
#############

Single-county models emulate the point of view of a county's property appraiser. They are run for each county independently, based on sales data from that county only.

:Identifier: 5-digit county FIPS code (:any:`fips`)

:Example: ``06037`` is Los Angeles county, California


County & neighbors
##################

"County & neighbors" models are fit on sales data of each county and its adjacent counties. Adjacent counties are counties whose boundaries are located within 10km or less of the boundaries of the target county.

County-level models with neighbors formed the basis of our first published high-resolution land value map (`Nolte (2020) PNAS <https://doi.org/10.5061/dryad.np5hqbzq9>`_).

:Identifier: 5-digit county FIPS code (:any:`fips`) with :code:`-nb` suffix.

:Example: ``06037-nb`` is Los Angeles county, California, and its five adjacent counties (Ventura, Kern, San Bernardino, Riverside, and Orange)

`Note that we forced the 2020 PNAS model to make predictions for any location, but also required that all training samples had to contain at minimum 1000 sales of large vacant parcels. If a model did not find sufficient sales within a county and its neighbors to meet that requirement, it kept adding sales data from counties located increasingly further away until the requirement was met.`

******
States
******

State models are based on sales data from one state.

:Identifier: 2-letter Alpha state code (:any:`state`)
:Example: ``CA`` is California

*****
CONUS
*****

CONUS models are fit on data for the entire U.S.

Because these models include millions of sales, CONUS models face stronger constrains with respect to the estimators we can fit (OLS regressors are quick, gradient boosting regressors not so much).

:Identifier: ``conus``


*******
Regions
*******

Regions refer to :ref:`core-based regions <Core-based regions>`, an experimental spatial unit derived at the PLACES lab.

We prefer using regions to counties, as counties vary dramatically in size, count, and internal heterogeneity across U.S. states.

Regions seem a little more comparable: they are "grown" from high-value cores (cities, resorts) and meet at lower-value boundaries.

Single-region
#############

Single-region models are based on sales data from one region only.

:Identifier: Unique region identifier (:any:`region_id`)
:Example: ``ca-losa`` is the core-based region around Los Angeles, California. It excludes Lancaster (which is located in LA county), but includes Anaheim, Santa Ana, Irvine (Orange county) as well as Thousand Oaks (Ventura county).

Region & neighbors
##################

"Region & neighbors" models are fit on sales data of each region, but also include sales from adjacent regions.

Adjacent regions are regions whose boundaries are located within 10km or less of the target regions.

:Identifier: Unique region identifier (:any:`region_id`) with :code:`-nb` suffix.
:Example: ``ca-losa-nb`` includes the core-based region for Los Angeles, California, as well as its neighboring core-based regions (OTO, Lancaster, Victorville, Riversidee, San Diego)
