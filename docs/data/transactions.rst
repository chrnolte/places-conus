Transactions
============

Our estimates of fair market value (FMV) are derived from **observed prices of land sales** and associated characteristics of sold land.


************************
Transaction data sources
************************

All our transaction data was provided by the real estate marketplace company `Zillow, Inc <https://www.zillowgroup.com/>`_.

.. note::
   Data for the first phase of this grant (Aug 1, 2022 - Sep 30, 2023) was provided by `Zillow <https://www.zillowgroup.com/>`_ through the Zillow Transaction and Assessment Dataset (ZTRAX). More information can be found at `<http://www.zillow.com/ztrax>`_. The results and opinions are those of the author(s) and do not reflect the position of Zillow Group.

The ZTRAX program ended on Sep 30, 2023. We had to delete ZTRAX from our systems at that date, including derivatives from which one could reverse-engineer the original data.

We are grateful that Zillow allowed us to work with this data. Its absence will be felt. Researchers with interests in traditionally underfunded research fields (e.g. environmental policy and justice) will likely find it difficult to obtain access to similar "big" sales transaction data in the immediate future.


**********************
Transaction attributes
**********************

We obtain several attributes from the transaction data:


.. attribute:: sid

   Unique identifier of transactions


.. attribute:: price

   Nominal transaction price.


.. attribute:: date

   Nominal date of transaction.


.. aluna:aluna:: zf_*

   Arms-length filters for ZTRAX (see `Nolte et al. 2024 Land Economics <https://le.uwpress.org/content/100/1/200>`_)


.. attribute:: year_cont

   Continuous time of sale (in years).

   :Computation: :any:`date` . ``year`` + :any:`date` . ``dayofyear`` / 365


******************
Linkage to parcels
******************

Transactions and parcels have a "many-to-many" (:math:`n-m`) relationship. Each transaction can have multiple parcels and each parcel can transact more than once. Linkages between parcels and sales are based on a separate table of :any:`sid` - :any:`pid` links.

