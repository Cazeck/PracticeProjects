# Web-based Financial Graph
# Collecting and presenting Stock Market Data using Python
import datetime
from pandas_datareader import data
from bokeh.plotting import figure, show, output_file

start = datetime.datetime(2016, 3, 1)
end = datetime.datetime(2016, 3, 10)

# Grabbing Stock data from Yahoo
df = data.DataReader(name="GOOG", data_source="yahoo", start=start, end=end)

# Indexing
date_increase = df.index[df.Close > df.Open]
date_decrease = df.index[df.Close < df.Open]

# determining whether a stocks price went up or down for the day
def inc_dec(close_c, open_c):
    if close_c > open_c:
        value = "Increase"
    elif close_c < open_c:
        value = "Decrease"
    else:
        value = "Equal"
    return value

# Adding a new Status column to our dataset with the info from inc_dec
df["Status"] = [inc_dec(c, o) for c, o in zip(df.Close, df.Open)]

# Calculating middle of the box chart (Average between open and close)
df["Middle"] = (df.Open + df.Close) / 2

# Height of the rectangle for the data frame
df["Height"] = abs(df.Close - df.Open)

print(df)

# building figure object
p = figure(x_axis_type='datetime', width=1000, height=300)
p.title.text = "Candlestick Chart"

# 12 Hours in milliseconds
hours_12 = 12*60*60*1000

# When price closes higher than when it started
p.rect(df.index[df.Status == "Increase"], df.Middle[df.Status == "Increase"], hours_12,
       df.Height[df.Status == "Increase"], fill_color="green", line_color="black")

# When price closes lower than when it started
p.rect(df.index[df.Status == "Decrease"], df.Middle[df.Status == "Decrease"], hours_12,
       df.Height[df.Status == "Decrease"], fill_color="red", line_color="black")

output_file("CS.html")
show(p)