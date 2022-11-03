Regions
=======

"Regions" are our data-driven attempt to subdivide the CONUS landscape into mutually exclusive and exhaustive blocks of land parcels where land values are driven by a shared "high-value" gravity center (core).

We use these core-based regions as spatial units in our land value models:

* for region-specific valuation models (where sufficient data is available).
* for region-specific uncertainty and error metrics.
* in OLS models: for regional fixed effects or regionally varying coefficients.
* in data-scarce regions: for the imputation of models behavior, using regions with similar characteristics.


**********
Principles
**********

Regions are defined by their high-value core
********************************************

Cores are centers of attraction that drives nearby land prices up. This is usually a city center (metropolitan or micropolitan areas), but also includes recreational locations (e.g., major resorts near mountains and lakes).


Regions are separated by low land values
****************************************

Which land area is attributed to a "core" is determined by two-dimensional rent gradients, i.e., observed changes in estimated land values in space. Such shapes are neither circular, nor do they follow administrative boundaries. Instead, they can be idiosyncratic as a function of geography and infrastructure (e.g., around a lake, within a long valley, etc.). The underlying assumption is that a local minimum in the rent gradient indicates that we're at a location where two cores have a similarly strong influence, i.e., a boundary between core-based areas.


.. _Regions_Methods:

*******
Methods
*******

Use CBSAs to generate cores
###########################

We start with the population centers of the U.S. Census Core-Based Statistical Areas (CBSAs). CBSAs refer to counties or groups of counties and include both metropolitan statistical areas (MSA) and micropolitan statistical areas.

Within each CBSA, we find the population gravity center by allocating census-block-level data to Microsoft building footprints, smoothing them with a Gaussian filter, and then selecting the pixel with the highest value in the county.

Manual additions of cores
#########################

Recreational::

    CORES_REC = {'AZ': ['Lake Powell', 'Sedona', 'Lakeside'],
                 'CA': ['Mendocino'],
                 'CO': ['Aspen', 'Estes Park', 'Granby', 'Telluride',
                        'Pagosa Springs'],
                 'GA': ['Lake Oconee', 'Lake Chatuga'],
                 'MA': ['Nantucket'],
                 'ME': ['Desert Island'],
                 'MD': ['Deep Creek Lake'],
                 'NC': ['Lake Norman', 'Highlands'],
                 'NH': ['Littleton', 'North Conway'],
                 'NY': ['The Hamptons', 'Eagle Bay', 'Saranac Lake'],
                 'OK': ['Hochatown'],
                 'VA': ['Smith Mountain Lake', 'Cape Charles'],
                 'WI': ['Woodruff'],
                }

Added towns and cities (that did not have their own CBSA)::

    CORES_CITY = {'AR': ['Conway'],
                  'AZ': ['Bullhead City', 'Kingman'],
                  'CA': ['Bishop', 'Lancaster', 'Monterey', 'Palm Springs',
                         'Paso Robles', 'Ridgecrest', 'Santa Barbara',
                         'Victorville', 'Walnut Creek'],
                  'CT': ['Danbury', 'Bristol'],
                  'LA': ['Covington', 'Slidell'],
                  'MA': ['New Bedford', 'Fitchburg', 'Amherst'],
                  'ME': ['Augusta', 'Presque Isle'],
                  'MD': ['Frederick', 'Annapolis', 'Ocean City'],
                  'MI': ['Port Huron'],
                  'NC': ['Waynesville'],
                  'NH': ['Nashua', 'Portsmouth'],
                  'NJ': ['Long Branch'],
                  'NY': ['Middletown'],
                  'PA': ['Hazleton'],
                  'SC': ['Anderson'],
                  'VA': ['Bristol', 'Fredericksburg', 'Hampton'],
                  'VT': ['Middlebury'],
                 }

**************
Region growing
**************

We use the ``watershed`` image segmentation algorithm from the Python package ``scikit-image``, using a slightly blurred and inverted (negative values) version of our published land value raster (Nolte 2020 PNAS) as the indicator for the land value gradient.
