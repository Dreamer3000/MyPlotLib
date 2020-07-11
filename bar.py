import numpy as np
import matplotlib.pyplot as plt

def mybar(y): # takes list of values as  input
    """ Bar graph with y as the heights """
    plt.bar(np.arange(0, len(y), 1), y) # (0, len(y), 1 --> x positions), y --> height of bar
    plt.show() # plot the graph

if __name__ == "__main__": # testing  to see if works, only runs in this program
    print("testing")
    mybar([1,2,3,4])