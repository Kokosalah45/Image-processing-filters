from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfile 
from imageProcessing import *
from PIL import Image,ImageTk
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
        self.display =Canvas(self.rightHalf, width= 600, height= 400)
        self.display.grid(row=0,column=0)
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
        self.image= PhotoImage(file=file.name)
        self.updateDisplay()
    def updateDisplay(self):
        self.display.create_image(0,0,anchor=NW,image=self.image)
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
    def onProcessingSelection(self):
        process= self.processingSelector.get()
        operations = {
            
            
            }
        



root = Gui()
root.mainloop()

