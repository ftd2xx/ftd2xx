======
FTD2XX
======

|package| |lint|

|python| |black|

ftd2xx is a simple python wrapper around the `D2XX DLL`_ from FTDI using
ctypes. The API based on Pablo Bleyer Kocik's d2xx_ extension.

Requires Python 3.8 minimum. Please ensure you have FTDI drivers installed or
available where the linker looks for shared libraries (e.g., PATH on windows,
LD_LIBRARY_PATH or standard library directories on Linux)

I don't have time to maintain this project, so I am looking for a maintainer.

There is another library by pyftdi_ that looks more actively maintained, has support for newer device, and may fit your needs better.

Also, Jeremy Bentham wrote a blog_ about using this library.

.. _d2xx: http://bleyer.org/pyusb/
.. _pyftdi: https://github.com/eblot/pyftdi
.. _D2XX DLL: http://www.ftdichip.com/Drivers/D2XX.htm
.. _blog: https://iosoft.blog/2018/12/02/ftdi-python-part-1/

.. |black|
    image:: https://img.shields.io/badge/code%20style-black-000000.svg
        :target: https://github.com/psf/black
.. |python|
    image:: https://img.shields.io/pypi/pyversions/ftd2xx.svg
        :target: https://pypi.org/project/ftd2xx/
.. |package|
    image:: https://github.com/snmishra/ftd2xx/workflows/Python%20package/badge.svg
.. |lint|
    image:: https://github.com/snmishra/ftd2xx/workflows/Lint/badge.svg
