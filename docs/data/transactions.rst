Transactions
============

Our estimates of fair market value (FMV) are derived from **observed prices of land sales** and associated characteristics of sold land.


************************
Transaction data sources
************************

All our transaction data is provided by the real estate marketplace company `Zillow, Inc <https://www.zillowgroup.com/>`_.

.. note::
   Data for the first phase of this grant (Aug 1, 2022 - Sep 30, 2023) is provided by `Zillow <https://www.zillowgroup.com/>`_ through the Zillow Transaction and Assessment Dataset (ZTRAX). More information can be found at `<http://www.zillow.com/ztrax>`_. The results and opinions are those of the author(s) and do not reflect the position of Zillow Group.

We are not allowed to share any of this transaction data.

ZTRAX sunset
############

The ZTRAX program **sunsets on Sep 30, 2023**. All researchers that had access, including our research team, will have to delete all ZTRAX data from all devices on that date, including any derivatives from which one could reverse-engineer the original data.

We are grateful that Zillow allowed us to work with this dataset. Its absence will be felt in the research community. Researchers with interests in traditionally underfunded research fields (e.g. environmental policy and justice) will likely find it difficult to obtain access to similar "big" sales transaction data:

* Commercial sales data aggregators exist, but can cost upwards of $50,000 for a project. This is out of the reach for most academic institutions.
* Many public tax assessor datasets contain last sales dates and prices. If combined with reliable approaches to identify arms-length sales, such datasets can be promising replacements for transaction data.

We promised to build a few publicly shareable datasets across some U.S. states for future research. We would gladly join, advise, or lead a larger-scale joint effort to build these types of datasets for academic use.


**********************
Transaction attributes
**********************

The following transaction attributes are derived directly from the transaction data.


.. attribute:: sid

   Unique identifier of transactions


.. attribute:: price

   Nominal transaction price.


.. attribute:: date

   Nominal date of transaction.


.. aluna:aluna:: zf_*

   Arms-length filters for ZTRAX (see `Nolte et al. 2023 Land Economics <https://le.uwpress.org/content/early/2023/06/09/le.100.1.102122-0090R>`_)


.. attribute:: year_cont

   Continuous time of sale (in years).

   :Computation: :any:`date` . ``year`` + :any:`date` . ``dayofyear`` / 365


******************
Linkage to parcels
******************

Transactions and parcels have a "many-to-many" (:math:`n-m`) relationship. Each transaction can have multiple parcels and each parcel can transact more than once. Linkages between parcels and sales are based on a separate table of :any:`sid` - :any:`pid` links.

