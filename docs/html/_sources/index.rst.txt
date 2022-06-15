Welcome to AmberFD's documentation!
===================================

AmberFD is a C++ and Python based library that adds a fluctuating density model to OpenMM for
molecular dynamics simulations.

Here you can find all the information needed to compile, run, and possibly edit the AmberFD Library. 
This page is VERY MUCH under construction, and documentation (but hopefully not API usage) 
is bound to change!

This documentation is broken down into three parts:

First, to learn how to compile and use AmberFD with an OpenMM Python script, please read the :ref:`Introduction`. 
For most users, this will be all that is necessary

Second, If you want to make changes to the OpenMM simulation or system forces, the :ref:`Submodules`
should contain all the information needed to adjust force settings and such.

Finally, :ref:`C++ Library` contains finer details about the library guts. 
Those that wish to adjust how AmberFD forces operate should use this as a map of the code.

.. toctree::
   :maxdepth: 4
   :caption: Contents:
   
   Introduction
   modules
    
   cpp/library_root

   
Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
