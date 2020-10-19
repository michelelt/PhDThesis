import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import BoxStyle
import pylab as pylab

pylab.rc('font', family="serif")
pylab.rc('text', usetex=True)

def read_file(fname,):

    values = []
    

    print("start")
    ln = 0    
    infile = open(fname, "r")
    for line in infile:
        if(ln!=0):
            ls = line.strip().split(",") 
            google_bus=float(ls[3])

            values.append(google_bus)
        ln+=1
    

    return values
     

def plot(c_data1,e_data1):
    
    fig, ax = plt.subplots(figsize=(9,5))
    weights1 = np.ones_like(c_data1)/float(len(c_data1))

    weights2 = np.ones_like(e_data1)/float(len(e_data1))

    n, bins, patches = ax.hist([c_data1,e_data1], bins=[i for i in range(0,55,5)],histtype='bar',weights=[weights1,weights2])  
    fig, ax = plt.subplots(figsize=(9,5))

    ind = np.arange(len(n[0]))  # the x locations for the groups
    width = 1       # the width of the bars

    user1 = np.array(n[0])
    user2 = np.array(n[1])


    rects1 = plt.bar(5*ind, user1, 1, color='b', edgecolor='none', linewidth=1.2,  label='Car2Go')    
    rects2 = plt.bar(5*ind +width, user2, 1, color='r', edgecolor='none', linewidth=1.2,  label='Enjoy')    

    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('axes', -0.05))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('axes', -0.03))
    ax.set_xticks([i for i in range(1,55,5)])
    for tick in ax.xaxis.get_major_ticks():
                tick.label.set_fontsize(28)     
    for tick in ax.yaxis.get_major_ticks():
                tick.label.set_fontsize(28)     

    legnew = ax.legend(bbox_to_anchor=(0.6, 1.185), loc=2, numpoints=1, frameon=None, ncol=1, prop={'size':28})
    legnew.draw_frame(False)
    
    ax.grid(True)
    
    ax.set_ylabel("Booking Probability [\%]",fontsize=28)
    ax.yaxis.set_label_coords(-0.15,0.29)

    ax.set_xlabel("Public Tranportation Time [min]",fontsize=28)
    ax.set_xlim(0,50)
    ax.set_xticklabels([str(i-2)+"-"+str(i+3) for i in range(2,50,5)],rotation=45)
    #plt.tight_layout()
    plt.subplots_adjust(left=0.17, bottom=0.35, right=0.97, top=0.94, wspace=0, hspace=0)
    fig.savefig("public.pdf")

    
    return


c_public_tranport = read_file("car2go_6.csv")
e_public_tranport = read_file("enjoy_6.csv")


plot(c_public_tranport,e_public_tranport)



