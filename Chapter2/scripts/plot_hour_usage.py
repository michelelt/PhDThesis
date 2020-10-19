#!/usr/bin/python
import pylab as plt
import numpy as np
from builtins import range
import pylab as pylab


pylab.rc('font', family="serif")
pylab.rc('text', usetex=True)

def plot_data(aggregate_week_bookings_enjoy,aggregate_weekend_bookings_enjoy,aggregate_week_bookings_car2go,aggregate_weekend_bookings_car2go):

    fig, ax = plt.subplots(figsize=(9,5))

    bins=[i for i in range(0,24)]
    ax.plot(bins, aggregate_week_bookings_enjoy, color= 'r', label="Enjoy Week")
    ax.plot(bins, aggregate_weekend_bookings_enjoy, color= 'r', linestyle="--", label="Enjoy Weekend")
    ax.plot(bins, aggregate_week_bookings_car2go, color= 'b',  label="Car2Go Week")
    ax.plot(bins, aggregate_weekend_bookings_car2go, color= 'b', linestyle="--", label="Car2Go Weekend")
    
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('axes', -0.05))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('axes', -0.03))
    for tick in ax.xaxis.get_major_ticks():
                tick.label.set_fontsize(28)     
    for tick in ax.yaxis.get_major_ticks():
                tick.label.set_fontsize(28)        
    
    legnew = ax.legend(bbox_to_anchor=(-0.216, 1.47), loc=2, numpoints=1, frameon=None, ncol=2, prop={'size':28})
    legnew.draw_frame(False)
    
    ax.grid(True)
    
    ax.set_ylabel("#Bookings",fontsize=28)
    ax.set_xlabel("Hour of Day",fontsize=28)
    ax.set_xlim(0,23.01)
    ax.set_ylim(0,130)
    ax.xaxis.set_ticks(np.arange(0,24, 2))
    plt.subplots_adjust(left=0.15, bottom=0.22, right=0.97, top=0.79, wspace=0, hspace=0)

    #plt.tight_layout()
    
    fig.savefig("bookings_day.pdf")

    
    return

def read_file(fname):

    week_bookings = [[] for i in range(0,24)]
    weekend_bookings = [[] for i in range(0,24)]
    ln = 0
    
    
    infile = open(fname, "r")
    for line in infile:
        if(ln!=0):
            ls = line.strip().split(",") 
            bookings_num=int(ls[1])
            my_hour = int(ls[9])
            week_day=int(ls[4])
            if(week_day<5):
                week_bookings[my_hour].append(bookings_num)
            else:
                weekend_bookings[my_hour].append(bookings_num)
        ln+=1
    
    
    return week_bookings, weekend_bookings

def main():
    
    week_bookings_enjoy, weekend_bookings_enjoy = read_file("enjoy_2-3.csv")

    aggregate_week_bookings_enjoy=[np.mean(week_bookings_enjoy[i]) for i in range(0,24)]
    

    week_bookings_car2go, weekend_bookings_car2go = read_file("car2go_2-3.csv")
    
        
    aggregate_weekend_bookings_enjoy=[np.mean(weekend_bookings_enjoy[i]) for i in range(0,24)]

    aggregate_week_bookings_car2go=[np.mean(week_bookings_car2go[i]) for i in range(0,24)]
    aggregate_weekend_bookings_car2go=[np.mean(weekend_bookings_car2go[i]) for i in range(0,24)]


    plot_data(aggregate_week_bookings_enjoy,aggregate_weekend_bookings_enjoy,aggregate_week_bookings_car2go,aggregate_weekend_bookings_car2go)
    
    print("end reading")


       
    print("End.")

if __name__ == "__main__":
    main()
