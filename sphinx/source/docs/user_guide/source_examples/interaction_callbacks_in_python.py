
from bokeh.io import vplot
from bokeh.models import CustomJS, ColumnDataSource, Slider
from bokeh.plotting import Figure, output_file, show

output_file("callbacks_in_python.html")

x = [x * 0.005 for x in range(0, 200)]
y = x

source = ColumnDataSource(data=dict(x=x, y=y))

plot = Figure(plot_width=400, plot_height=400)
plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)


def callback(source=source):
    data = source.get('data')
    f = slider.get('value')
    x, y = data['x'], data['y']
    for i in range(len(x)):
        y[i] = Math.pow(x[i], f)
    source.trigger('change')

callback = CustomJS.from_py_func(callback)

slider = Slider(start=0.1, end=4, value=1, step=.1, title="power", callback=callback)
callback.args['slider'] = slider

layout = vplot(slider, plot)

show(layout)
