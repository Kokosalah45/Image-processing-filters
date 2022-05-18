from tkinter import *
from tkinter import ttk

class Gui(Tk):
    def __init__(self):
        super().__init__()
        self.title("DIP")#project name
        self.resizable(False, False)
        self.geometry("800x600")#default dimensions
        self.pointProcessing= Button(self, text="Point Processing",command=self.createPointProcessing,borderwidth = 1)
        self.neighborhoodProcessing = Button(self, text="Neighborhood Processing",command=self.createNeighborhoodProcessing,borderwidth= 1)
        self.pointProcessing.grid(row=0,column=0)
        self.neighborhoodProcessing.grid(row=0, column=1)
        self.processingSelector= ttk.Combobox(self,width=30,state="readonly")
        self.createPointProcessing()
        self.processingSelector.grid(row=1, column=0, padx=(10, 0), pady=(20, 0), columnspan=2)
    def createPointProcessing(self):
        values = ("grayIntensityScaling" ,
"subSampling"  ,
"contrastStretching" ,
"thresholding" ,
"logTransformation" ,
"inverseLogTransformation" ,
"powerLawTransformation" ,
"grayLevelSlice" ,
"bitPlaneSlicing" )
        self.processingSelector['values']= values
    def createNeighborhoodProcessing(self):
        values = ("median filter",
 "minmax filter"  ,
"average filter" ,
"laplacian filter" ,
"robert's operator " ,
"Butterworth Highpass Filter (BHPF)" ,
"Gaussian Highpass Filter (GHPF)",
"Butterworth Lowpass Filter (BLPF)",
"Gaussian Lowpass Filter (GLPF)",
"Ideal HighPass Filter (IHPF)",
"Ideal LowPass Filter (ILPF)"

                  )
        self.processingSelector['values'] =  values



root = Gui()
root.mainloop()

