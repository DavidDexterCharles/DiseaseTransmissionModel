from pylab import *
import matplotlib.pyplot as pyplot
#from simulator import time


def LineGraph(time):
    recovered=[]
    susceptible=[]
    infectious=[]
    noninfectious=[]
    symptomatic=[]
    T=[]
    for x in range(0,len(time)):
        susceptible.insert(x, time[x]['susceptible'])
        infectious.insert(x, time[x]['infectious'])
        noninfectious.insert(x, time[x]['noninfectious'])
        symptomatic.insert(x, time[x]['symptomatic'])
        recovered.insert(x, time[x]['recovered'])
        T.insert(x,int(x))    
    
    x = T
    y1 =recovered
    y2=susceptible
    y3=infectious
        
    pyplot.title('Population Status at each time interval.',bbox={'facecolor':'0.8', 'pad':5})
    
    pyplot.xlabel('Time')
    pyplot.ylabel('Population')
    
    
    # pyplot.plot(x, recovered, label='Immune')

    pyplot.line = pyplot.plot(x,y2, label='Susceptible')
    pyplot.legend()
    pyplot.line = pyplot.plot(x,y1, label='Immune')
    pyplot.legend()
    pyplot.line = pyplot.plot(x,y3, label='Infectious')
    pyplot.legend(loc='center right')
   
    #pyplot.plot(x,y1)
    #pyplot.plot(x,y2)
    #pyplot.plot(x,y3)
    pyplot.show()
    print "process completed..........."
