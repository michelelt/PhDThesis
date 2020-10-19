import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import BoxStyle
import pylab as pylab

pylab.rc('font', family="serif")
pylab.rc('text', usetex=True)

def read_file(fname,cnum):

    matrix = [[0 for i in range(0,51)] for j in range(0,51)]
    

    print("start")
    ln = 0    
    infile = open(fname, "r")
    for line in infile:
        if(ln!=0):
            ls = line.strip().split(",") 
            duration=int(float(ls[1]))
            google=int(float(ls[cnum]))
            x_val=50
            y_val=50
            if(google<51): y_val=google
            if(duration<51): x_val=duration
            matrix[x_val][y_val]+=1
            
        ln+=1
    

    return matrix
     

def plot(data1,xlabel,outname):
    
    fig, ax = plt.subplots(figsize=(11,9))
    
    a=np.matrix(data1)
    heatmap = ax.imshow(a, cmap='Reds', interpolation='nearest')
    ax.plot([i for i in range(0,52)],[i for i in range(0,52)],color="k",linestyle="--")
    ax.invert_yaxis()

    ax.set_xlim(0,50)
    ax.set_ylim(0,50)
    cb=plt.colorbar(heatmap)
    cb.set_label(label='Number of Elements',fontsize=30)
    cb.ax.tick_params(labelsize=36)    
    
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
        
    
    ax.grid(True)
    
    ax.set_ylabel("Rental Time [min]",fontsize=30)
    ax.set_xlabel(xlabel,fontsize=30)
    
    plt.tight_layout()
    
    fig.savefig(outname)
    
    return


c_matrix = read_file("car2go_6.csv",2)
plot(c_matrix,"Driving Google [min]","car2go_faster_driving.pdf")
c_matrix = read_file("car2go_6.csv",3)
plot(c_matrix,"Public Transport [min]","car2go_faster_public.pdf")

e_matrix = read_file("enjoy_6.csv",2)
plot(e_matrix,"Driving Google [min]","enjoy_faster_driving.pdf")

e_matrix = read_file("enjoy_6.csv",3)
plot(e_matrix,"Public Transport [min]","enjoy_faster_public.pdf")


