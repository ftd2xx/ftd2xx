======
FTD2XX
======

ftd2xx is a simple python wrapper around the `D2XX DLL`_ from FTDI using
ctypes. The API based on Pablo Bleyer Kocik's d2xx_ extension.

Version 1.1.0 is compatible with Python 3. Please ensure you have FTDI
drivers installed or available where the linker looks for shared
libraries (e.g., PATH on windows, LD_LIBRARY_PATH or standard library
directories on Linux)

I don't have time to maintain this project, so I am looking for a maintainer. 

There is another library by Ben Bass called pylibftdi_ that may fit your needs better.

Also, Jeremy Bentham wrote a blog_ about using this library.

.. _d2xx: http://bleyer.org/pyusb/
.. _pylibftdi: https://bitbucket.org/codedstructure/pylibftdi
.. _D2XX DLL: http://www.ftdichip.com/Drivers/D2XX.htm
.. _blog: https://iosoft.blog/2018/12/02/ftdi-python-part-1/
