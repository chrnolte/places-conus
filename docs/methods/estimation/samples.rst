Samples
=======

Samples define the sets of property transaction records that are used to train :any:`Models`.

Samples contain sales prices (:math:`y`) and :any:`Predictor sets` (:math:`X`).

A sample is defined by:

* Its :any:`geography <Geographies>` (a county, a region, a state, with or without neighbors, the whole country.)
* The :any:`parcel type <Parcel types>` of the transacted properties (vacant, mostly vacant, single-family home)
* The :any:`type of sale <Sale types>`, reflecting our degree of confidence that the recorded price reveals something about a property's market value.


.. toctree::
   :maxdepth: 2
   :caption: Learn more

   samples/geographies
   samples/parceltypes
   samples/saletypes
