import numpy as np
import matplotlib.pyplot as plt
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
            if(week_day<5):
                duration_week.append(duration)
                distance_week.append(distance)
            else:
                duration_week_end.append(duration)
                distance_week_end.append(distance)
        ln+=1
    

    return duration_week, duration_week_end, distance_week, distance_week_end
     

def plot(c_data1,c_data2,e_data1,e_data2,xlabel,xmax,outname):
    
    fig, ax = plt.subplots(figsize=(9,5))
    
    sorted_data = np.sort(c_data1)    
    yvals=np.arange(len(sorted_data))/float(len(sorted_data)-1)
    ax.plot(sorted_data,yvals, color= 'b',  label="Car2Go Week")

    sorted_data = np.sort(c_data2)    
    yvals=np.arange(len(sorted_data))/float(len(sorted_data)-1)
    ax.plot(sorted_data,yvals, color= 'b', linestyle="--", label="Car2Go Weekend")

    sorted_data = np.sort(e_data1)    
    yvals=np.arange(len(sorted_data))/float(len(sorted_data)-1)
    ax.plot(sorted_data,yvals, color= 'r',  label="Enjoy Week")

    sorted_data = np.sort(e_data2)    
    yvals=np.arange(len(sorted_data))/float(len(sorted_data)-1)
    ax.plot(sorted_data,yvals, color= 'r', linestyle="--", label="Enjoy Weekend")
    
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('axes', -0.05))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('axes', -0.03))
    for tick in ax.xaxis.get_major_ticks():
                tick.label.set_fontsize(36)     
    for tick in ax.yaxis.get_major_ticks():
                tick.label.set_fontsize(36)     
        
    legnew = ax.legend(bbox_to_anchor=(0.3, 0.8), loc=2, numpoints=1, frameon=None, ncol=1, prop={'size':30})
    legnew.draw_frame(False)
    
    ax.grid(True)
    
    ax.set_ylabel("ECDF",fontsize=30)
    ax.set_xlabel(xlabel,fontsize=30)
    ax.set_xlim(0,xmax)
    
    plt.tight_layout()
    
    fig.savefig(outname)
    
    return


c_duration_week, c_duration_week_end, c_distance_week, c_distance_week_end = read_file("car2go_3_rentals.csv")
e_duration_week, e_duration_week_end, e_distance_week, e_distance_week_end = read_file("enjoy_3_rentals.csv")

plot(c_duration_week,c_duration_week_end,e_duration_week,e_duration_week_end,"Duration [min]",120,"duration.pdf")

plot(c_distance_week,c_distance_week_end,e_distance_week,e_distance_week_end,"Distance [Km]",20,"distance.pdf")


