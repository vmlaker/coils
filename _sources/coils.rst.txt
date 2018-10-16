.. _api:

The Coils programming API
=========================

Functions
---------

.. autofunction:: coils.string2time
.. autofunction:: coils.time2string
.. autofunction:: coils.time2levels
.. autofunction:: coils.time2dir
.. autofunction:: coils.time2fname
.. autofunction:: coils.user_input


Classes
-------

.. autoclass:: coils.Averager
    :members: add, __len__
    :undoc-members:

----

.. autoclass:: coils.MapSockServer
    :members: run
    :undoc-members:

.. autoclass:: coils.MapSockClient
    :members: send
    :undoc-members:

.. autoclass:: coils.MapSockRequest
    :members:
    :undoc-members:

----

.. autoclass:: coils.RateTicker
    :members: tick
    :undoc-members:

----

.. autoclass:: coils.Ring
    :members: __getitem__, turn, first, last, __len__
    :undoc-members:

----

.. autoclass:: coils.SocketTalk
    :members: pair, server, client, put, get, close
    :undoc-members:

----

.. autoclass:: coils.SortedList
    :members: add, getCountLT, getCountGT, removeLT
    :undoc-members:

----

.. autoclass:: coils.Timer
    :members: get, getTotal
    :undoc-members:
