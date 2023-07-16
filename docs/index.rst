PLACES-FMV (CONUS)
==================

.. note::
   This is a draft document to facilitate communications with the research team, collaborator panel, data partners, and early data adopters. Please report errors to `chrnolte@bu.edu <mailto:chrnolte@bu.edu>`_.

Welcome to the documentation and user's guide for the PLACES-FMV (CONUS) data volume.

PLACES-FMV (CONUS) is a data volume containing parcel-level estimates of the "fair market value" (FMV) of vacant and mostly-vacant lands in the contiguous United States (CONUS).

The estimates are derived from training data of millions of vacant and mostly-vacant property sales (2000-2021). Our statistical :ref:`Models` are simple and scalable, fitted at both local (county) and larger scales, and use exclusively public data as predictors.

We created this data volume to facilitate the development of actionable multi-objective land conservation scenarios for the United States at the spatial resolution of individual parcels.

The research is conducted at Boston University's `PLACES lab <https://placeslab.org>`_ and supported by the National Science Foundation's (NSF) Human-Environment and Geographical Sciences program [#f1]_.

.. important::

   * Jul 19/20, 2023: :ref:`Collaborator panel` & :ref:`Early adopters` webinar
   * Aug 11, 2023: deadline for feedback (on data, models, performance metrics.)
   * Sep 30, 2023: Boston University has to delete all training data.

.. toctree::
   :maxdepth: 2
   :caption: Overview

   about
   data
   methods
   results

:ref:`genindex`

.. rubric:: Footnotes

.. [#f1] Award `#2149243 <https://www.nsf.gov/awardsearch/showAward?AWD_ID=2149243>`_, Human-Environment and Geographical Sciences, National Science Foundation (NSF). PLACES is also supported by NSF's "Coastlines and People" program (`#2209190 <https://www.nsf.gov/awardsearch/showAward?AWD_ID=2209190>`_) and the National Aeronautics and Space Administration's (NASA) Water Resources Applications program (#21-WATER21-2-0027). In the past, we have received research support from The Nature Conservancy and Boston University's Rafik B. Hariri Institute for Computing and Computational Science and Engineering.

.. note::
   Data for the first phase of this research (Aug 1, 2022 - Sep 30, 2023) provided by `Zillow <https://www.zillowgroup.com/>`_ through the Zillow Transaction and Assessment Dataset (ZTRAX). More information can be found at `<http://www.zillow.com/ztrax>`_. The results and opinions are those of the author(s) and do not reflect the position of Zillow Group.

.. note::
   We thank Regrid's `Data with Purpose <https://regrid.com/purpose>`_ program, which provides access to nonprofit researchers on a "pay what you can" basis. For two thirds of CONUS counties, PLACES-FMV (CONUS) is based on Regrid parcel data. For the remaining counties, parcel boundary data was downloaded from publicly available sources.

.. important::
   The data comes without any legal warranties or formal guarantees. Errors in data entry, processing, and interpretation can occur when governmental and satellite data is synthesized and interpreted across such a vast and incredibly diverse continent.

.. important::
   All data shared inherit the **data use licenses** from the most conservative of their input sources (see :ref:`Data`). We are working on an agreement that allows us to share our final data volume at no cost with government, academic, and non-profit analysts through the Inter-university Consortium for Political and Social Research (`ICPSR <https://www.icpsr.umich.edu/web/pages/>`_).
