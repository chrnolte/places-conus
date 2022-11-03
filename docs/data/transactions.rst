Transactions
============

We estimate fair market value (FMV) from observed prices of land sales and associated characteristics of sold land.

This requires observations of geo-located, land right transactions between unrelated sellers and buyers, neither under the pressure to buy or sell. Data needed include prices, dates, parcel identifiers, document types, and names of sellers and buyers (to algorithmically check similarity and exclude public actors).

************************
Transaction data sources
************************

All our sales transaction data comes from Zillow, Inc.

.. note::
   Data for the first phase of this research (Aug 1, 2022 - Sep 30, 2023) provided by `Zillow <https://www.zillowgroup.com/>`_ through the Zillow Transaction and Assessment Dataset (ZTRAX). More information can be found at `<http://www.zillow.com/ztrax>`_. The results and opinions are those of the author(s) and do not reflect the position of Zillow Group.

We are not allowed to share this transaction data.

After the sunset of the ZTRAX program (Sep 30, 2023), researchers with interests in environmental policy and justice might find it frustratingly difficult to obtain access to large-scale sales transaction data:

* Commercial sales data aggregators exist, but can cost upwards of $50,000 for a project, which is out of the reach for most academic institutions.
* Many public tax assessor datasets contain last sales dates and prices. If combined with reliable approaches to identify arms-length sales, such datasets can be promising replacements for transaction data.


**********************
Transaction attributes
**********************


.. attribute:: sid

   Unique identifier of transactions


.. attribute:: price

   Nominal transaction price.


.. attribute:: date

   Nominal date of transaction.


.. attribute:: zf_<filter>

   Arms-length filters for ZTRAX (see `Nolte et al. 2011 <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3900806>`_)


:: note:
   In progress



******************
Linkage to parcels
******************

Transactions and parcels have a "many-to-many" (:math:`n-m`) relationship in PLACES, because each transaction can have multiple parcels and each parcel can transact more than once. Linkages between parcels and sales are therefore usually based on a separate table of :any:`sid` - :any:`pid` links.
