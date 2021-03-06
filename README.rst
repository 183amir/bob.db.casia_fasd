.. vim: set fileencoding=utf-8 :
.. Manuel Guenther <manuel.guenther@idiap.ch>
.. Fri Oct 31 14:18:57 CET 2014

.. image:: http://img.shields.io/badge/docs-stable-yellow.png
   :target: http://pythonhosted.org/bob.db.casia_fasd/index.html
.. image:: http://img.shields.io/badge/docs-latest-orange.png
   :target: https://www.idiap.ch/software/bob/docs/latest/bioidiap/bob.db.casia_fasd/master/index.html
.. image:: https://travis-ci.org/bioidiap/bob.db.casia_fasd.svg?branch=master
   :target: https://travis-ci.org/bioidiap/bob.db.casia_fasd?branch=master
.. image:: https://coveralls.io/repos/bioidiap/bob.db.casia_fasd/badge.svg?branch=master
   :target: https://coveralls.io/r/bioidiap/bob.db.casia_fasd?branch=master
.. image:: https://img.shields.io/badge/github-master-0000c0.png
   :target: https://github.com/bioidiap/bob.db.casia_fasd/tree/master
.. image:: http://img.shields.io/pypi/v/bob.db.casia_fasd.png
   :target: https://pypi.python.org/pypi/bob.db.casia_fasd
.. image:: http://img.shields.io/pypi/dm/bob.db.casia_fasd.png
   :target: https://pypi.python.org/pypi/bob.db.casia_fasd
.. image:: https://img.shields.io/badge/original-data--files-a000a0.png
   :target: http://www.cbsr.ia.ac.cn/english/FaceAntiSpoofDatabases.asp

=====================================================
 CASIA Face Anti-Spoofing Database Interface for Bob
=====================================================

The CASIA-FASD database is a spoofing attack database which consists of three types of attacks: warped printed photographs, printed photographs with cut eyes and video attacks.
The samples are taken with three types of cameras: low quality, normal quality and high quality.

This package contains the Bob_ accessor methods to use the DB directly from python, with our certified protocols.
The actual raw data for `CASIA FASD`_ database should be downloaded from the original URL

Reference::

  Z. Zhang, J. Yan, S. Lei, D. Yi, S. Z. Li: "A Face Antispoofing Database with Diverse Attacks", In proceedings of the 5th IAPR International Conference on Biometrics (ICB'12), New Delhi, India, 2012.


Installation
------------
To install this package -- alone or together with other `Packages of Bob <https://github.com/idiap/bob/wiki/Packages>`_ -- please read the `Installation Instructions <https://github.com/idiap/bob/wiki/Installation>`_.
For Bob_ to be able to work properly, some dependent packages are required to be installed.
Please make sure that you have read the `Dependencies <https://github.com/idiap/bob/wiki/Dependencies>`_ for your operating system.

Documentation
-------------
For further documentation on this package, please read the `Stable Version <http://pythonhosted.org/bob.db.casia_fasd/index.html>`_ or the `Latest Version <https://www.idiap.ch/software/bob/docs/latest/bioidiap/bob.db.casia_fasd/master/index.html>`_ of the documentation.
For a list of tutorials on this or the other packages ob Bob_, or information on submitting issues, asking questions and starting discussions, please visit its website.

.. _bob: https://www.idiap.ch/software/bob
.. _casia fasd: http://www.cbsr.ia.ac.cn/english/FaceAntiSpoofDatabases.asp
