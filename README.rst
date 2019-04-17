dynplot
=======

Extends matplotlib's pyplot.plot() to allow for repetitive plotting

There is no simple way to update multiple lines repetitively and continuously of an existing figure in `matplotlib <https://matplotlib.org/>`_. Using this class as drop-in replacement for matplotlib's pyplot, the figure's line will be updated upon every call of the ``plot()`` method and create thus a dynamic plot, constantly refreshing.

**Current limitations**:

- Only the ``plot`` function is supported.
- The figure and axes are only configurable via the internal ``fig`` and ``ax`` attribute, i.e. the following call will _fail_:

  >>> dplt.title('Will fail!')

- ``dynplot.plot()`` only accepts plotting if x and y data are given

**Example**:

.. code-block:: python
   :linenos:

   from dynplot import dplt
   from math import sin, pi

   dplt = dplt()
   for i in range(100):
       x = range(i, i+20)
       y = [sin(2*pi*x/20) for x in x]
       dplt.plot(x, y)
       _ = dplt.ax.set_title('Wave')
       dplt.show()
