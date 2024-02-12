Sale types
==========

A **saletype** identifies a types of sales document.

The sale types we define reflect our confidence that sales prices reveal market value.

* ``deed``: deeds are our standard source of price information across most models: they refer to :ref:`transactions <Transactions>` that have passed all of our "high-confidence" arms-length filters (`Nolte et al. 2024 Land Economics <https://le.uwpress.org/content/100/1/200>`_).

* ``deed-zf1``: also includes medium-confidence sales

* ``deed-zf0``: also includes low-confidence sales

* ``full``: includes last sales information from tax assessor records (which does not permit the application of any arms-length sales filters).
