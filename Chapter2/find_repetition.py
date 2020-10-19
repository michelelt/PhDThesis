import sys


def main():
    
    
    files = sys.argv
    if(len(files)<2): 
        print("reqire at least 1 file as input")
        exit(0)
        
    print("start")
    for i in range(1,len(files)):
        fname = files[i]
        
        fin = open(fname,"r")
        ln=0
        for line in fin:
            ls = line.split()
            for i in range(1,len(ls)):
                if(ls[i-1].strip(",.|!?;:")==ls[i].strip(",.|!?;:")):
                    print("Repetion in file "+files[i]+" on line: %d"%ln + " words: ", ls[i])

            ln +=1
            
        
    
    
    
    
    
    
    return


main()
