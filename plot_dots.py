from matplotlib import pyplot as plt
import numpy as np

class PlotDots():
    def __init__(self, figsize=(10,10), markersize=25, marker='.'):
        self.figsize = figsize
        self.markersize = markersize
        self.marker = marker
    
    def plot(self, XY, x_range, y_range):
        plt.figure(figsize=self.figsize)
        for xy in XY:
            x,y = xy
            plt.xlim(x_range[0], x_range[1])
            plt.ylim(y_range[0], y_range[1])
            plt.plot([x], [y], marker=self.marker, markersize=self.markersize)
        plt.show()