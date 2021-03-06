dynplot
=======

Extends matplotlib's pyplot.plot() to allow for repetitive plotting to the same figure

There is no simple way to update multiple lines repetitively and continuously of an existing figure in `matplotlib <https://matplotlib.org/>`_. Using this class as drop-in replacement for matplotlib's pyplot, the figure's line will be updated upon every call of the ``plot()`` method and create thus a dynamic plot, constantly refreshing.

**Current limitations:**

- Only the ``plot`` function is supported.
- The figure and axes are only configurable via the internal ``fig`` and ``ax`` attribute, i.e. the following call will _fail_:

  >>> dplt.title('Will fail!')

  In this case, instead use the following:

  >>> _ = dplt.ax.set_title('Will work!')

**Examples:**

Single call during one repetition, could also contain multiple ``x``/``y`` data pairs.

>>> from dynplot import dynplot
>>> from math import sin, pi
>>>
>>> dplt = dynplot()
>>> for i in range(100):
>>>     x = range(i, i+20)
>>>     y = [sin(2*pi*x/20) for x in x]
>>>     dplt.plot(x, y)
>>>     _ = dplt.ax.set_title('Wave')
>>>     dplt.show()

Multiple calls (i.e. multiple lines) during one repetition

>>> from dynplot import dynplot
>>> from math import sin, pi
>>>
>>> dplt = dynplot()
>>> for i in range(100):
>>>     x = range(i, i+20)
>>>     y1 = [sin(2*pi*x/20) for x in x]
>>>     y2 = [sin(2*pi*x/10) for x in x]
>>>     dplt.plot(y1)
>>>     dplt.plot(y2)
>>>     dplt.show()


Installation
------------

The module is build in a way to be installable with `pip <https://pypi.org/project/pip/>`_:

1. Clone this repository and enter it
2. Type ``pip install .`` to install it

In order to add it to a requirements file as normally obtained from ``pip freeze``, use the following line:

``-e git+https://github.com/lorenzschmid/dynplot.git#egg=dynplot==1.0.0``
