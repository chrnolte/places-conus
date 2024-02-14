Model data
==========

Measures of :ref:`model-level uncertainty <Model-level uncertainty>`:

:Location:
 ``models/model_performance_pqt.zip``

:Rows:
  :ref:`models <Models>`, identified by their ``model_id`` (see :ref:`model specifications <Model specifications>`)

:Columns:
  ``<statistic>_<cross-validation>``

  * ``statistic`` is a statistic of the prediction error (residuals), such as ``mean`` or ``rmse`` (see :ref:`model-level uncertainty <Model-level uncertainty>` for a list)
  * ``cross-validation`` is the type of :ref:`cross-validation <Cross-validation>` to derive the statistic.

  :Example: ``rmse_bg`` is the root mean squared error (RMSE, ``rmse``) derived via cross-validation blocked by census block groups (``bg``).

:Format:
  Compressed `Parquet <https://parquet.apache.org/docs/overview/>`_ table
