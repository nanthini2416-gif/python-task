from datetime import datetime as d
x=d.now()
y=x.timetuple()
print("Time tuple",y)
print("Time tuple Year",y[0])
