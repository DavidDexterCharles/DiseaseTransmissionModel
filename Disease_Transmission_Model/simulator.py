#ID:811000385
#COMP3950
import random, numpy as np
from numpy.matlib import rand
#from scipy.stats import poisson
#from matplotlib import pyplot as plt
from pieChart import pieChart
from Linegraph import LineGraph
popsize=1000          #population size
numinfected=2               #number of infected individuals
numsus=popsize-numinfected #number of susceptible individuals
ip=0.2                     #infection probability

popsize=int(raw_input("Please enter population size"))
if popsize!=-12345:
    numinfected=int(raw_input("Please enter Number of Infected Citizens"))
    numsus=popsize-numinfected #number of susceptible individuals
    ip=float(raw_input("Please enter the infection probability"))
    while(ip>1 or ip<=0 ):
        print "Probability value must be less than 1 but greater than 0"
        ip=float(raw_input("Please enter the infection probability"))
    print "The time between infection and infectiousness"                     #1
    n_infectedtoinfectious=int(raw_input("Please enter number of trials"))
    p_infectedtoinfectious=float(raw_input("Please enter Probability Value"))
    while(p_infectedtoinfectious>1 or p_infectedtoinfectious<=0 ):
        print "Probability value must be less than 1 but greater than 0"
        p_infectedtoinfectious=float(raw_input("Please enter Probability Value"))
    print "The time between infectiousness and Onset of symptoms"             #2
    n_infectioustosymptomatic=int(raw_input("Please enter number of trials"))
    p_infectioustosymptomatic=float(raw_input("Please enter Probability Value"))
    while(p_infectioustosymptomatic>1 or p_infectioustosymptomatic<=0 ):
        print "Probability value must be less than 1 but greater than 0"
        p_infectioustosymptomatic=float(raw_input("Please enter Probability Value"))
    print "The time between Onset of symptoms and Immunity"                       #3
    n_symptomatictoimmune=int(raw_input("Please enter number of trials"))
    p_symptomatictoimmune=float(raw_input("Please enter Probability Value"))
    while(p_symptomatictoimmune>1 or p_symptomatictoimmune<=0 ):
        print "Probability value must be less than 1 but greater than 0"
        p_symptomatictoimmune=float(raw_input("Please enter Probability Value"))
else:
    print "Debug Mode......"
    popsize=3000 
    numinfected=2              
    numsus=popsize-numinfected
    ip=0.2 
    n_infectedtoinfectious=5
    p_infectedtoinfectious=.5
    n_infectioustosymptomatic=5
    p_infectioustosymptomatic=.5
    n_symptomatictoimmune=5
    p_symptomatictoimmune=.5

def getContactSize(): 
    n_contact=5
    p_contact=.5
    contact=np.random.binomial(n_contact, p_contact,1)[0]#number of people person meets
    return contact

#, p = 5, .2 # number of trials, probability of each trial
#s = np.random.binomial(n, p,1)
# result of flipping a coin 10 times, tested 1000 times.)
def initTimeline(): 
        timeline={}  
        timeline["status"]=0                
        timeline["infectious"]=0  
        timeline["symptomatic"]=0
        timeline["max_infection_time"]=0
        return timeline
def getTimeline(): 
        timeline={}  
        
        timeline["status"]=1                 
        global n_infectedtoinfectious#=5
        global p_infectedtoinfectious#=.5
        infectedtoinfectious=0#time between infection and infectiousness
        while(infectedtoinfectious==0):infectedtoinfectious=np.random.binomial(n_infectedtoinfectious, p_infectedtoinfectious,1)[0]
        timeline["infectious"]=infectedtoinfectious +1 
        #print "infectedtoinfectious" 
        #print infectedtoinfectious+1
        global n_infectioustosymptomatic#=5
        global p_infectioustosymptomatic#=.5
        infectioustosymptomatic=0
        while(infectioustosymptomatic==0):infectioustosymptomatic=np.random.binomial(n_infectioustosymptomatic, p_infectioustosymptomatic,1)[0]#time between infectiousness and the onset of symptoms 
        timeline["symptomatic"]= int(timeline["infectious"])+ int(infectioustosymptomatic)
        #print "infectioustosymptomatic"
        #print infectioustosymptomatic
        global n_symptomatictoimmune#=5
        global p_symptomatictoimmune#=.5
        symptomatictoimmune=0
        while(symptomatictoimmune==0):symptomatictoimmune=np.random.binomial(n_symptomatictoimmune, p_symptomatictoimmune,1)[0]#time between onset of symptoms and immunity 
        timeline["max_infection_time"]= int(timeline["symptomatic"])+int(symptomatictoimmune)
        #print "symptomatictoimmune"
        #print symptomatictoimmune
        return timeline

def getEvent(population):
    recovered=0
    susceptible=0
    infectious=0
    noninfectious=0
    symptomatic=0
    timeEvent={}
    for i in range(0,len(population)):
        if population[i]['status']==-1:
            recovered=recovered+1
        elif population[i]['status']==0:
            susceptible=susceptible+1
        elif population[i]['status']>=1:
            if population[i]['status']>=population[i]['infectious']:
                infectious=infectious+1
                if population[i]['status']>=population[i]['symptomatic']:
                    symptomatic=symptomatic+1
            elif population[i]['status']<population[i]['infectious']:
                noninfectious=noninfectious+1
    timeEvent['recovered']= recovered 
    timeEvent['infectious']= infectious
    timeEvent['noninfectious']= noninfectious
    timeEvent['symptomatic']= symptomatic
    timeEvent['susceptible']= susceptible
        
    return timeEvent   

    
#pieChart()  
templist=[]
population=[]
count=check=0
for i in range(0,popsize):
        population.insert(i,initTimeline())
        #print i
        #print population[i]

#print population

while(count<numinfected):
    check=random.randrange(0,popsize)
    if check not in templist:
        
        #print"pop :", check
        population[check]= getTimeline()
        #print population[check]
        templist.insert(count, check)
        #print templist
        count=count+1

def pop():        
    for i in range(0,popsize):
        print i, population[i]
'''
print "Random"
temp=float(random.randrange(1,100))/100
print temp
'''

#pop()

print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"

templist=[]
count=0
r=0
check=0
#while(r<popsize):
# r =int(raw_input("Please enter number"))
#print population
timestep=0
time=[]
immune=0
checker=0
#time.insert(timestep,getEvent(population))
while True:
   
    for i in range(0,popsize):
        #print"i ",i

        if population[i]['status']==0:
            numContacts=getContactSize()
            #print"NumContacts", numContacts
            
            while(count<numContacts):
                check=random.randrange(0,popsize)
                if check not in templist:
                    templist.insert(count, check)
                    count=count+1
            #print "Templist", templist
            
            for x in range(0,len(templist)):
                
                if population[templist[x]]['status']>=population[templist[x]]['infectious'] and population[templist[x]]['status']!=0:
                    #print "population[templist[x]]['status']", population[templist[x]]['status']
                    #print "population[templist[x]]['infectious']",population[templist[x]]['infectious']
                    v=float(random.randrange(1,100))/100
                    if v<=ip:
                        #print "Rand vavlue",v
                        #print"pop :", i
                        #print"Infector :", templist[x]
                        population[i]=getTimeline()
                        if checker==0:
                            numsus=numsus-1
                            checker=1
                            # print "NUMSUS: &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&", numsus
        
        elif population[i]['status']>=1:
            if population[i]['status']==population[i]['max_infection_time']:
                population[i]['status']=-1 #recovered
                immune=immune+1
                # print "COUNT@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",immune
            else: population[i]['status']=population[i]['status']+1
         
        count=0   
        templist=[]
        checker=0
   
    #d =int(raw_input("Please enter number"))
    #pop()
    time.insert(timestep,getEvent(population))
    if numsus+immune==popsize:
        pieChart(numsus,immune,population)
        break
    timestep=timestep+1
    
    if timestep%500==0: pieChart(numsus,immune,population)
    
    
    
LineGraph(time)
def tgo():
    for i in range(0,len(time)):
        print i,time[i]

#pop()
#tgo()
#print population


