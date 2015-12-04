"""
Make a pie chart - see
http://matplotlib.sf.net/matplotlib.pylab.html#-pie for the docstring.

This example shows a basic pie chart with labels optional features,
like autolabeling the percentage, offsetting a slice with "explode",
adding a shadow, and changing the starting angle.

"""
from pylab import *
import matplotlib.pyplot as pyplot
#from simulator import time
# make a square figure and axes
#figure(1, figsize=(8,8))
#ax = axes([0.1, 0.1, 0.8, 0.8])



# The slices will be ordered and plotted counter-clockwise.
labels = 'Immune', 'Infectious', 'Non-infectious', 'Susceptible'






def pieChart(numsus,immune,population):
    infectious=0
    noninfectious=0
    #symptomatic=[]
    
    for x in range(0,len(population)):
        if population[x]['status']>=population[x]['infectious'] and population[x]['status']!=0:
            infectious=infectious+1
        elif population[x]['status']<population[x]['infectious']and population[x]['status']>=1:
            noninfectious=noninfectious+1
    
    
    
    
    fracs = [immune, infectious, noninfectious, numsus]
    explode=(0, 0.05, 0.05, 0)
    
   
    
    pie(fracs, explode=explode, 
                    autopct='%1.f%%', shadow=True, startangle=90)
                    # The default startangle is 0, which would start
                    # the Frogs slice on the x-axis.  With startangle=90,
                    # everything is rotated counter-clockwise by 90 degrees,
                    # so the plotting starts on the positive y-axis.
    
    
    pyplot.plot(fracs[0], label='Immune')
    pyplot.plot(fracs[1], label='Infectious')
    pyplot.plot(fracs[2], label='Non-Infectious')
    pyplot.plot(fracs[3], label='Susceptible')
    pyplot.legend(loc='best')
    
    title('Population Composition', bbox={'facecolor':'0.8', 'pad':5})
    
    show()
    
