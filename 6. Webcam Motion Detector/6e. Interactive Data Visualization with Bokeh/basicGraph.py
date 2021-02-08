# Making a basic Bokeh line graph

from bokeh.plotting import figure
from bokeh.io import output_file, show

# Prepare some data
x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]

# Prepare the output file
output_file("Line.html")

# Create figure object
f = figure()

# Create line plot.  line can be changed to circle / triangle etc for different plots
f.line(x, y)

show(f)
