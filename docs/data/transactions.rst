Transactions
============

Our estimates of fair market value (FMV) are derived from **observed prices of land sales** and the characteristics of the parcels that were sold (:ref:`predictors <Predictors>`).


************************
Transaction data sources
************************

All our transaction data was provided by `Zillow, Inc <https://www.zillowgroup.com/>`_, a real estate marketplace company.

.. note::
   Data for the first phase of this grant (Aug 1, 2022 - Sep 30, 2023) was provided by `Zillow <https://www.zillowgroup.com/>`_ through the Zillow Transaction and Assessment Dataset (ZTRAX). More information can be found at `<http://www.zillow.com/ztrax>`_. The results and opinions are those of the author(s) and do not reflect the position of Zillow Group.

Zillow ended the ZTRAX program on Sep 30, 2023. We had to delete ZTRAX from our systems at that date, including derivatives from which one could reverse-engineer the original data.

Similar datasets are available from other real estate data aggregators. However, high price tags mean that access to such data is out of reach for most small research teams: nationwide datasets can cost ≥$50K for a single research project and ≥$100K for a multi-project license.


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

Transactions and parcels have a "many-to-many" (:math:`n-m`) relationship. Each transaction can have multiple parcels and each parcel can transact more than once.

Linkages between parcels and sales are therefore saved in separate tables containing parcel identifiers (:any:`pid`) and sales transaction identifiers (:any:`sid`).
