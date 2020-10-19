import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import BoxStyle
import pylab as pylab

pylab.rc('font', family="serif")
pylab.rc('text', usetex=True)

def read_file(fname,cnum):

    difference = []

    ln = 0
    
    
    infile = open(fname, "r")
    for line in infile:
        if(ln!=0):
            ls = line.strip().split(",") 
            diffval=float(ls[cnum])
            if(diffval<0):
                difference.append(diffval*-1)
        ln+=1
    

    return difference
     

def plot(c_data1,e_data1,xlabel,xmax,outname):
    
    print(c_data1)
    fig, ax = plt.subplots(figsize=(9,5))
    
    sorted_data = np.sort(c_data1)    
    yvals=np.arange(len(sorted_data))/float(len(sorted_data)-1)
    ax.plot(sorted_data,yvals, color= 'b',  label="Car2Go Week")

    sorted_data = np.sort(e_data1)    
    yvals=np.arange(len(sorted_data))/float(len(sorted_data)-1)
    ax.plot(sorted_data,yvals, color= 'r',  label="Enjoy Week")

    
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


c_difference = read_file("car2go_6.csv",5)
e_difference = read_file("enjoy_6.csv",5)

plot(c_difference,e_difference,"Faster [min]",30,"faster_driving.pdf")



