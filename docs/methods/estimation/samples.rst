Samples
=======

Samples define the sets of property transaction records that are used to train :any:`models <Models>`.

Samples contain sales prices (the dependent variable) and :any:`predictors <Predictor sets>`.

A sample is defined by:

* Its :any:`geography <Geographies>`: a county, a region (with or without neighbors), a state, or the contiguous U.S.
* The :any:`parcel type <Parcel types>` of the transacted properties (e.g., vacant or mostly vacant, urban or rural).
* The :any:`type of sale <Sale types>`, reflecting our confidence that the sales price reveals market value.


.. toctree::
   :maxdepth: 2
   :caption: Sampling: details

   samples/geographies
   samples/parceltypes
   samples/saletypes
