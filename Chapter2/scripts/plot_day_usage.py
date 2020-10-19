#!/usr/bin/python
import datetime
import pylab as plt
import matplotlib.ticker as ticker
import matplotlib.dates as mdates
import pylab as pylab


pylab.rc('font', family="serif")
pylab.rc('text', usetex=True)

def plot_data(bins,bookings_enjoy,bookings_car2go,rentals_enjoy,rentals_car2go):

    fig, ax = plt.subplots(figsize=(9,5))

    #print(bookings)
    ax.plot(bins, bookings_enjoy, color= 'r', label="Bookings Enjoy")
    ax.plot(bins, rentals_enjoy, color= 'r', linestyle="--", label="Rentals Enjoy")
    ax.plot(bins, bookings_car2go, color= 'b',  label="Bookings CarGo")
    ax.plot(bins, rentals_car2go, color= 'b', linestyle="--", label="Rentals CarGo")
    
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
    
    
    legnew = ax.legend(bbox_to_anchor=(0.07, 1.135), loc=2, numpoints=1, frameon=None, ncol=2, prop={'size':28})
    legnew.draw_frame(False)
    
    ax.xaxis.set_major_locator(ticker.MultipleLocator(7))
    yearsFmt = mdates.DateFormatter('%d-%m-%Y')
    ax.xaxis.set_major_formatter(yearsFmt)
    plt.xticks(rotation='45')
    ax.grid(True)
    
    ax.set_ylabel("#Rentals/#Bookings",fontsize=28)
    ax.set_xlabel("Data",fontsize=28)
    
    
    plt.tight_layout()
    
    fig.savefig("bookings.pdf")
    #plt.show()

    
    return

def read_file(fname):

    bookings = []    
    rentals = []    
    bins = []
    ln = 0
    index=0
    
    
    infile = open(fname, "r")
    for line in infile:
        if(ln!=0):
            ls = line.strip().split(",") 
            if(index%2==0):
                rentals.append(int(ls[1]))
                bookings.append(int(ls[2]))                
                str_date = ls[0].split("-")
                str_hour = ls[0].split()[1].split(":")[0]
                dt = datetime.datetime(int(str_date[0]),int(str_date[1]), int(str_date[2].split()[0]), int(str_hour), 0)
                bins.append(dt)
            else:
                rentals[len(bookings)-1]+=int(ls[1])
                bookings[len(bookings)-1]+=int(ls[2])  
            index+=1              

        ln+=1
    
    
    return bins, bookings, rentals

def main():
    
    bins,bookings_enjoy,rentals_enjoy = read_file("enjoy_1.csv")
    bins,bookings_car2go,rentals_car2go = read_file("car2go_1.csv")
    
        
        
    plot_data(bins,bookings_enjoy,bookings_car2go,rentals_enjoy,rentals_car2go)
    
    print("end reading")


       
    print("End.")

if __name__ == "__main__":
    main()
