from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfile 
from imageProcessing import *
from PIL import Image,ImageTk
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg)
class Gui(Tk):
    def __init__(self):
        super().__init__()
        self.title("DIP")#project name
        self.resizable(False, False)
        self.geometry("800x600")#default dimensions
        self.leftHalf= Frame(self,width=400,height=600)
        self.leftHalf.grid(row=0,column=0)
        self.rightHalf= Frame(self,width=400,height=600)
        self.rightHalf.grid(row=0,column=1)
        self.pointProcessing= Button(self.leftHalf, text="Point Processing",command=self.createPointProcessing,borderwidth = 1)
        self.neighborhoodProcessing = Button(self.leftHalf, text="Neighborhood Processing",command=self.createNeighborhoodProcessing,borderwidth= 1)
        self.pointProcessing.grid(row=0,column=0)
        self.neighborhoodProcessing.grid(row=0, column=1)
        self.processingSelector= ttk.Combobox(self.leftHalf,width=30,state="readonly")
        self.createPointProcessing()
        self.processingSelector.grid(row=1, column=0, padx=(10, 0), pady=(20, 0), columnspan=2)
        self.upload = Button(self.leftHalf, text='Upload Image', command= self.uploadImage)
        self.upload.grid(row=5,column=0,pady=(10,0))
        self.imageProcessing=None
        self.imagePath=None
        self.image = None
        self.process = Button(self.leftHalf, text='Process', command= self.performProcessing)
        self.process.grid(row=5,column=1)
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
    def uploadImage(self):
        file = askopenfile(mode='r', filetypes=[('Image Files', '*.jpg'),('Image Files', '*.png')])
        if (file==None):
            return
        self.imagePath=file.name
        self.imageProcessing = ImageProcessing(self.imagePath)
        self.updateDisplay()
    def updateDisplay(self):
        fig = plt.figure(figsize=(5,4))
        self.image=self.imageProcessing.get()
        plt.imshow(self.image)
        self.display = FigureCanvasTkAgg(fig, master=self)
        print(self.display)
        self.display.draw ()
        self.display.get_tk_widget().grid(row=0,column=1)
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
    def selectedProcess(self,processName):
       
        processMap = {
        "grayIntensityScaling" : self.imageProcessing.adjustIntensityLevel  ,
        "subSampling" : self.imageProcessing.subSample  ,
        "contrastStretching" : self.imageProcessing.contrastStretching ,
        "thresholding" : self.imageProcessing.threshold  ,
        "logTransformation" : self.imageProcessing.logTransform  ,
        "inverseLogTransformation" : self.imageProcessing.inverseLogTransform,
        "powerLawTransformation" : self.imageProcessing.powerLawTransform ,
        "grayLevelSlice" : self.imageProcessing.grayLevelSlicing ,
        "median filter" : self.imageProcessing.medianFilter ,
        "minmax filter" : self.imageProcessing.minmaxFilter,
        "average filter" : self.imageProcessing.averageFilter,
        "laplacian filter": self.imageProcessing.lablacianFilter,
        "Ideal Highpass Filter" : self.imageProcessing.IHPF,
        "Ideal Lowpass Filter" : self.imageProcessing.ILPF,
        "Butterworth Highpass Filter (BHPF)" : self.imageProcessing.BHPF,
        "Butterworth Lowpass Filter (BHPF)" : self.imageProcessing.BLPF,
        "Gaussian Highpass Filter (GHPF)" : self.imageProcessing.GHPF,
        "Gaussian Lowpass Filter (GHPF)" : self.imageProcessing.GLPF
        }
        return processMap[processName]
    def performProcessing(self):
        operation = self.selectedProcess(self.processingSelector.get())
        self.updateDisplay(operation())
        



root = Gui()
root.mainloop()

