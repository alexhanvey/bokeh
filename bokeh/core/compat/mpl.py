"Supporting objects and functions to convert Matplotlib objects into Bokeh."
#-----------------------------------------------------------------------------
# Copyright (c) 2012 - 2014, Continuum Analytics, Inc. All rights reserved.
#
# Powered by the Bokeh Development Team.
#
# The full license is in the file LICENSE.txt, distributed with this software.
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

from __future__ import absolute_import

import matplotlib.pyplot as plt

from .bokeh_exporter import BokehExporter
from .bokeh_renderer import BokehRenderer

#-----------------------------------------------------------------------------
# Classes and functions
#-----------------------------------------------------------------------------

def to_bokeh(fig=None, use_pandas=True, xkcd=False):
    """ Uses bokeh to display a Matplotlib Figure.

    You can store a bokeh plot in a standalone HTML file, as a document in
    a Bokeh plot server, or embedded directly into an IPython Notebook
    output cell.

    Parameters
    ----------

    fig: matplotlib.figure.Figure
        The figure to display. If None or not specified, then the current figure
        will be used.

    name: str (default=None)
        If this option is provided, then the Bokeh figure will be saved into
        this HTML file, and then a web browser will be used to display it.

    server: str (default=None)
        Fully specified URL of bokeh plot server. Default bokeh plot server
        URL is "http://localhost:5006" or simply "default"

    notebook: bool (default=False)
        Return an output value from this function which represents an HTML
        object that the IPython notebook can display. You can also use it with
        a bokeh plot server just specifying the URL.

    use_pandas: bool (default=True)
        The implementation should try to use Pandas for processing datetime
        data (if it is installed). Set to False to plot the datetime xaxis
        with other non-pandas interfaces.

    xkcd: bool (default=False)
        If this option is True, then the Bokeh figure will be saved with a
        xkcd style.
    """

    if fig is None:
        fig = plt.gcf()

    renderer = BokehRenderer(use_pandas, xkcd)
    exporter = BokehExporter(renderer)

    exporter.run(fig)

    return renderer.fig
