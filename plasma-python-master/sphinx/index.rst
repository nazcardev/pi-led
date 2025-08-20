.. role:: python(code)
   :language: python

.. toctree::
   :titlesonly:
   :maxdepth: 0

Welcome
-------

This documentation will guide you through the methods available in the Plasma Python library.

* More information - https://shop.pimoroni.com/products/plasma
* Get the code - https://github.com/pimoroni/plasma
* Get started - https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-plasma
* Get help - http://forums.pimoroni.com/c/support

At A Glance
-----------

.. automoduleoutline:: plasma
   :members:

Set A Single Pixel
------------------

The bread and butter of Plasma is setting pixels. Your Plasma LED string will always have
4x more pixels than buttons. You can set these to any one of around 16 million colours!

The :python:`brightness` argument is completely optional. Omit it to keep the last
brightness value set for that particular pixel.

.. automodule:: plasma
   :noindex:
   :members: set_pixel

Set All Pixels
--------------

Sometimes you need to set all the pixels to the same colour. This convinience method
does just that!

.. automodule:: plasma
   :noindex:
   :members: set_all

Show
----

None of your pixels will appear on Plasma until you :python:`show()` them. This method writes
all the pixel data out to your device.

.. automodule:: plasma
   :noindex:
   :members: show

Clear
-----

Exactly the same as calling :python:`set_all(0,0,0)`, clear sets all the pixels to black.

You must also call :python:`show()` if you want to turn Plasma off.

.. automodule:: plasma
   :noindex:
   :members: clear

Enable/Disable Clear On Exit
----------------------------

Sometimes you want a script that runs and quits, leaving a pattern up on Plasma

.. automodule:: plasma
   :noindex:
   :members: set_clear_on_exit

Get A Single Pixel
------------------

.. automodule:: plasma
   :noindex:
   :members: get_pixel

Constants
---------

Plasma has 8 pixels. Simple. Use the constant :python:`plasma.NUM_PIXELS` when you're iterating over pixels,
so you can avoid a *magic number* in your code.

:python:`plasma.NUM_PIXELS = 8`
