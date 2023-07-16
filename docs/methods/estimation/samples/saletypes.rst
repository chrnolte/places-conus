Sale types
==========

A `saletype` identifies a types of sales document.


****
deed
****

Identifier: ``deed``

Deeds are our standard source of price information: they refer to :ref:`Transactions` that have passed our "high-confidence" arms-length filters.

Required selection criteria include:

- Transaction records passes all of our "high-confidence" arms-length filters (:aluna:ref:`zf_*`) (`Nolte et al. (2023) Land Economics <https://le.uwpress.org/content/early/2023/06/09/le.100.1.102122-0090R>`_)


********
deed-zf1
********

Also includes medium-confidence sales


****
full
****

Also includes last sales information from tax assessor records, which does not permit the application of our arms-length sales filters (`Nolte et al. (2023) Land Economics <https://le.uwpress.org/content/early/2023/06/09/le.100.1.102122-0090R>`_)
