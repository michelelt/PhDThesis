import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import BoxStyle
import pylab as pylab

pylab.rc('font', family="serif")
pylab.rc('text', usetex=True)

def read_file(fname):

    duration_week = []
    duration_week_end = []

    distance_week = []
    distance_week_end = []

    ln = 0
    
    
    infile = open(fname, "r")
    for line in infile:
        if(ln!=0):
            ls = line.strip().split(",") 
            duration=float(ls[1])
            distance=float(ls[2])
            week_day=int(ls[4])
            if(distance==0):
                if(week_day<5):
                    duration_week.append(duration)
                    distance_week.append(distance)
                else:
                    duration_week_end.append(duration)
                    distance_week_end.append(distance)
        ln+=1
    

    return duration_week, duration_week_end, distance_week, distance_week_end
     

def plot(c_data1,c_data2,e_data1,e_data2,xlabel,xmax):
    
    fig, ax = plt.subplots(figsize=(9,5))
    weights1 = np.ones_like(c_data1)/float(len(c_data1))
    weights2 = np.ones_like(e_data1)/float(len(e_data1))

    weights1b = np.ones_like(c_data2)/float(len(c_data1))
    weights2b = np.ones_like(e_data2)/float(len(e_data1))

    n, bins, patches = ax.hist([c_data1,c_data2,e_data1,e_data2], bins=[i for i in range(0,55,5)],histtype='bar',weights=[weights1,weights1b,weights2,weights2b],  color=['b','b','r','r'],
                               label=["Car2Go Week","Car2Go Weekend","Enjoy Week","Enjoy Weekend"])  
    fig, ax = plt.subplots(figsize=(9,5))

    ind = np.arange(len(n[0]))  # the x locations for the groups
    width = 1       # the width of the bars

    user1 = np.array(n[0])
    user2 = np.array(n[1])

    user3 = np.array(n[2])
    user4 = np.array(n[3])

    rects1 = plt.bar(5*ind, user1, 1, color='b', edgecolor='none', linewidth=1.2,  label='Car2Go week')    
    rects2 = plt.bar(5*ind +width, user2, 1, color='b', edgecolor='none', linewidth=1.2,alpha=0.7, hatch="/",  label='Car2Go weekend')    

    rects3 = plt.bar(5*ind+2*width, user3, 1, color='r', edgecolor='none', linewidth=1.2,  label='Enjoy week')    
    rects4 = plt.bar(5*ind +3*width, user4, 1, color='r', edgecolor='none', linewidth=1.2,alpha=0.7, hatch="/",  label='Enjoy weekend')    
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('axes', -0.05))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('axes', -0.03))
    ax.set_xticks([i for i in range(2,100,5)])
    for tick in ax.xaxis.get_major_ticks():
                tick.label.set_fontsize(28)     
    for tick in ax.yaxis.get_major_ticks():
                tick.label.set_fontsize(28)     

    legnew = ax.legend(bbox_to_anchor=(0.4, 1.1), loc=2, numpoints=1, frameon=None, ncol=1, prop={'size':28})
    legnew.draw_frame(False)
    
    ax.grid(True)
    
    ax.set_ylabel("PDF",fontsize=28)
    ax.set_xlabel(xlabel,fontsize=28)
    ax.set_xlim(0,50)
    ax.set_xticklabels([str(i-2)+"-"+str(i+3) for i in range(2,50,5)],rotation=45)
    plt.tight_layout()
    
    fig.savefig("no_rent.pdf")

    
    return


c_duration_week, c_duration_week_end, c_distance_week, c_distance_week_end = read_file("car2go_3_bookings.csv")
e_duration_week, e_duration_week_end, e_distance_week, e_distance_week_end = read_file("enjoy_3_bookings.csv")

plot(c_duration_week,c_duration_week_end,e_duration_week,e_duration_week_end,"Duration[min]",120)



