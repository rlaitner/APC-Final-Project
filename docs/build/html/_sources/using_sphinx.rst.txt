Using Sphinx for Documentation
==========================================================

Overview
______________________________________

Documentation for this project can be built using `Sphinx <sphinx-doc.org/en/master/index.html>`_.

The files are provided in the ``main/source`` directory and can build 
both html documentation and PDF files (through LaTeX).  

Sphinx-autodoc has provided the Makefile and make.bat in the ``main`` 
repository. Use the follow commands when located in ``main`` for quick build:


	* ``make html``
	* ``make latexpdf``

To manually build the documentation, use ``sphinx-build``. 

See `sphinx-build <sphinx-doc.org/en/master/man/sphinx-build.html>`_ 
for more detailed explanation. 
