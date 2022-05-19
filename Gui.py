from tkinter import *
from tkinter import ttk
from tkinter import simpledialog
from tkinter.filedialog import askopenfile
from imageProcessing import *
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg)


class Gui(Tk):
    def __init__(self):
        super().__init__()
        self.w = None
        self.title("DIP")  # project name
        self.resizable(False, False)
        self.geometry("800x300")  # default dimensions
        self.configure(bg='white')
        self.leftHalf = Frame(self, width=400, height=300, bg='white')
        self.leftHalf.grid(row=0, column=0, padx=(30, 0), rowspan=3)
        self.rightHalf = Frame(self, width=450, height=300, bg='white')
        self.rightHalf.grid(row=0, column=1)
        self.pointProcessing = Button(self.leftHalf, text="Point Processing", width=30,
                                      command=self.createPointProcessing,
                                      borderwidth=0, bg='#e7e7e7', pady=5)
        self.neighborhoodProcessing = Button(self.leftHalf, text="Neighborhood Processing",
                                             command=self.createNeighborhoodProcessing, borderwidth=0, width=30,
                                             bg='#e7e7e7', pady=5)
        self.pointProcessing.grid(row=2, column=0, padx=(0, 0))
        self.neighborhoodProcessing.grid(row=3, column=0)
        self.processingSelector = ttk.Combobox(self.leftHalf, width=30, state="readonly")
        self.createPointProcessing()
        self.processingSelector.grid(row=4, column=0, pady=(10, 10))
        self.upload = Button(self.leftHalf, text='Upload Image', command=self.uploadImage, width=30, borderwidth=0,
                             bg='#008CBA', pady=5, fg='white')
        self.upload.grid(row=5, column=0)
        self.reset = Button(self.leftHalf, text='Reset', command=self.resetImage, width=30, borderwidth=0,
                            bg='#e7e7e7', pady=5)
        self.reset.grid(row=7, column=0)
        self.imageProcessing = None
        self.imagePath = None
        self.image = None
        self.process = Button(self.leftHalf, text='Process', command=self.performProcessing, width=30, borderwidth=0,
                              bg='#4CAF50', pady=5, fg='white')
        #   self.parameterLabel = Label(self.leftHalf,text="Please enter desired values ")
        #  self.parameterLabel.grid(row=6,column=1)
        # self.input= Entry(self.leftHalf)
        #  self.input.grid(row=7,column=0,pady=(20,0),padx=(100,0))
        self.process.grid(row=6, column=0)

    def createPointProcessing(self):
        values = ("grayIntensityScaling",
                  "subSampling",
                  "contrastStretching",
                  "thresholding",
                  "logTransformation",
                  "inverseLogTransformation",
                  "powerLawTransformation",
                  "grayLevelSlice",
                  "bitPlaneSlicing")
        self.processingSelector['values'] = values

    def resetImage(self):
        self.image = self.imageProcessing.resetChanges().get()
        self.updateDisplay()

    def uploadImage(self):
        file = askopenfile(mode='r', filetypes=[('Image Files', '*.jpg'), ('Image Files', '*.png')])
        if file == None:
            return
        self.imagePath = file.name
        self.imageProcessing = ImageProcessing(self.imagePath)

        self.image = self.imageProcessing.get()
        self.updateDisplay()

    def updateDisplay(self):
        fig = plt.figure(figsize=(5, 3))
        # self.image=self.imageProcessing.get()
        plt.imshow(self.image, cmap='gray')
        self.display = FigureCanvasTkAgg(fig, master=self)
        print(self.display)
        self.display.draw()
        self.display.get_tk_widget().grid(row=0, column=1, padx=90)

    def createNeighborhoodProcessing(self):
        values = ("median filter",
                  "minmax filter",
                  "average filter",
                  "laplacian filter",
                  "Ideal Highpass Filter",
                  "Ideal Lowpass Filter",
                  "Butterworth Highpass Filter (BHPF)",
                  "Butterworth Lowpass Filter (BLPF)",
                  "Gaussian Highpass Filter (GHPF)",
                  "Gaussian Lowpass Filter (GHPF)"
                  )
        self.processingSelector['values'] = values

    def selectedProcess(self, processName):
        processMap = {
            "Reset": self.imageProcessing.resetChanges,
            "grayIntensityScaling": self.adjustIntensityLevel,
            "subSampling": self.subSample,
            "contrastStretching": self.contrastStretching,
            "thresholding": self.threshold,
            "logTransformation": self.logTransform,
            "inverseLogTransformation": self.inverseLogTransform,
            "powerLawTransformation": self.powerLawTransform,
            "grayLevelSlice": self.grayLevelSlicing,
            "median filter": self.imageProcessing.medianFilter,
            "minmax filter": self.minmaxFilter,
            "average filter": self.averageFilter,
            "laplacian filter": self.lablacianFilter,
            "Ideal Highpass Filter": self.imageProcessing.IHPF,
            "Ideal Lowpass Filter": self.imageProcessing.ILPF,
            "Butterworth Highpass Filter (BHPF)": self.imageProcessing.BHPF,
            "Butterworth Lowpass Filter (BLPF)": self.imageProcessing.BLPF,
            "Gaussian Highpass Filter (GHPF)": self.imageProcessing.GHPF,
            "Gaussian Lowpass Filter (GHPF)": self.imageProcessing.GLPF
        }
        return processMap[processName]

    def performProcessing(self):
        operation = self.selectedProcess(self.processingSelector.get())
        self.image = operation().get()
        self.updateDisplay()

    def adjustIntensityLevel(self):
        k_param = simpledialog.askinteger(title="Field Input", prompt="Input K")
        return self.imageProcessing.adjustIntensityLevel(k_param)

    def subSample(self):
        factor_param = simpledialog.askinteger(title="Field Input", prompt="Input Factor")
        return self.imageProcessing.subSample(factor_param)

    def contrastStretching(self):
        smin_param = simpledialog.askinteger(title="Field Input", prompt="Input SMin")
        smax_param = simpledialog.askinteger(title="Field Input", prompt="Input SMax")
        return self.imageProcessing.contrastStretching(smin=smin_param, smax=smax_param)

    def threshold(self):
        threshold_param = simpledialog.askinteger(title="Field Input", prompt="Input Threshold")
        return self.imageProcessing.threshold(threshold_param)

    def grayLevelSlicing(self):
        min_param = simpledialog.askinteger(title="Field Input", prompt="Input Min")
        max_param = simpledialog.askinteger(title="Field Input", prompt="Input Max")
        new_val_param = simpledialog.askinteger(title="Field Input", prompt="Input New Value")
        keep_param = simpledialog.askinteger(title="Field Input", prompt="Input Keep")
        return self.imageProcessing.grayLevelSlicing(min_param, max_param, new_val_param, keep_param)

    def logTransform(self):
        c_param = simpledialog.askinteger(title="Field Input", prompt="Input C")
        return self.imageProcessing.logTransform(c_param)

    def inverseLogTransform(self):
        c_param = simpledialog.askinteger(title="Field Input", prompt="Input C")
        return self.imageProcessing.inverseLogTransform(c_param)

    def powerLawTransform(self):
        gamma_param = simpledialog.askfloat(title="Field Input", prompt="Input Gamma")
        c_param = simpledialog.askinteger(title="Field Input", prompt="Input C")
        return self.imageProcessing.powerLawTransform(gamma_param, c_param)

    def minmaxFilter(self):
        mode_param = simpledialog.askstring(title="Field Input", prompt="Input Mode")
        return self.imageProcessing.minmaxFilter(mode_param)

    def averageFilter(self):
        sigma_param = simpledialog.askfloat(title="Field Input", prompt="Input Sigma")
        return self.imageProcessing.averageFilter(sigma_param)

    def lablacianFilter(self):
        neighbors_param = simpledialog.askinteger(title="Field Input", prompt="Input Neighbors")
        sign_param = simpledialog.askinteger(title="Field Input", prompt="Input Sign")
        composite_param = simpledialog.askinteger(title="Field Input", prompt="Input Composite")
        return self.imageProcessing.lablacianFilter(neighbors_param, sign_param, composite_param)


root = Gui()
root.mainloop()
