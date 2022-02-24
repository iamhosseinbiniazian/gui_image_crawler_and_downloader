from tkinter import *
from tkinter import ttk
from ui.customButton import CustomButton
from processing.controler import Controler
from ui.resizingcanvas import ResizingCanvas
class Gui:
    def __init__(self,root):
        self.root=root
        self.root.option_add('*tearOff', False)
        root.attributes('-zoomed', True)
        self.root.title("NDC")
        ###########################shortcut bar################################
        self.shortcut_bar = Frame(self.root, height=25, background='light sea green')
        self.shortcut_bar.pack(expand=NO, fill=X)
        self.status_bar_frame = Frame(self.root, height=25, background='light green')
        self.status_label=Label(self.status_bar_frame,text="Hello dear, the program was started!!!",background='light green')
        self.status_label.pack(expand=YES,fill=X)
        self.status_bar_frame.pack(expand=NO, fill=X,side=BOTTOM)
        ##############################################################
        self.mainPanedWindow = ttk.Panedwindow(root, orient=HORIZONTAL)
        self.mainPanedWindow.pack(fill=BOTH, expand=True)
        self.frameLeft = ttk.Frame(self.mainPanedWindow, width=120, height=300, relief=SUNKEN)
        self.frameRight = ttk.Frame(self.mainPanedWindow, width=400, height=400, relief=SUNKEN)
        self.mainPanedWindow.add(self.frameLeft, weight=1)
        self.mainPanedWindow.add(self.frameRight, weight=10)
        #########################################################################
        self.NDCPanedWindow = ttk.Panedwindow(self.frameLeft, orient=HORIZONTAL)
        self.NDCPanedWindow.pack(fill=BOTH, expand=True)
        self.frameTree = ttk.Frame(self.NDCPanedWindow, width=100, height=self.root.winfo_screenheight(), relief=SUNKEN)
        self.frameNDC = ttk.Frame(self.NDCPanedWindow, width=100, height=self.root.winfo_screenheight(), relief=SUNKEN)
        self.NDCPanedWindow.add(self.frameTree, weight=1)
        self.NDCPanedWindow.add(self.frameNDC, weight=0)
        ##############################################################
        self.NDCTreePanedWindow = ttk.Panedwindow(self.frameTree, orient=VERTICAL)
        self.NDCTreePanedWindow.pack(fill=BOTH, expand=True)
        self.frameTreeView = ttk.Frame(self.NDCTreePanedWindow, width=100, height=100, relief=SUNKEN)
        self.frameLabelVeiw = ttk.Frame(self.NDCTreePanedWindow, width=100, height=100, relief=SUNKEN)
        self.NDCTreePanedWindow.add(self.frameTreeView, weight=1)
        self.NDCTreePanedWindow.add(self.frameLabelVeiw, weight=1)
        ###########################################################
        #U=Up
        #B=Between
        #D=Down
        #L=Left
        #R=Right
        self.NDCCPanedWindow1 = ttk.Panedwindow(self.frameNDC, orient=HORIZONTAL)
        self.NDCCPanedWindow1.pack(fill=BOTH, expand=True)
        canvas_width =self.NDCPanedWindow.winfo_screenmmwidth()//3
        print(canvas_width)
        canvas_height =self.NDCCPanedWindow1.winfo_screenheight()
        print(canvas_height)
        python_green = "#476042"
        # canvasU = Canvas(self.NDCCPanedWindow,width=canvas_width,height=canvas_height)
        self.canvasU = ResizingCanvas(self.NDCCPanedWindow1 , width=canvas_width, height=canvas_height, bg="gray", highlightthickness=0)
        self.canvasU.pack(fill=BOTH, expand=YES)
        canvas_height=canvas_height/2
        newh=canvas_height
        canvas_height=canvas_height-20
        points = [0, 0,
                  canvas_width, 0,
                  canvas_width, canvas_height,
                  ######################
                  canvas_width-(canvas_width/3), canvas_height,
                  ###############################
                  canvas_width - ((canvas_width / 3)+((canvas_width )/18)), canvas_height-canvas_height/8,
                  (canvas_width / 3) + ((canvas_width ) / 18), canvas_height -canvas_height/8,
                  (canvas_width / 3), canvas_height,
                  0, canvas_height]
        canvas_height=newh

        points1 = [
            0,canvas_height,
            (canvas_width / 3),canvas_height,
            (canvas_width / 3)+((canvas_width ) / 18),canvas_height/8+canvas_height,
            canvas_width-((canvas_width / 3)+((canvas_width ) / 18)),canvas_height/8+canvas_height,
            canvas_width - (canvas_width/3), canvas_height,
            canvas_width,canvas_height,
            canvas_width, canvas_height*2,
            0, canvas_height*2,
        ]
        # canvas_height = canvas_height - 20
        points21 = [
            (canvas_width / 3), canvas_height,
            (canvas_width / 3) + ((canvas_width) / 18), canvas_height / 8 + canvas_height,
            canvas_width - ((canvas_width / 3) + ((canvas_width) / 18)), canvas_height / 8 + canvas_height,
            canvas_width - (canvas_width / 3), canvas_height,


        ]
        canvas_height = canvas_height - 20
        points22=[
            canvas_width - (canvas_width / 3), canvas_height,
            ###############################
            canvas_width - ((canvas_width / 3) + ((canvas_width) / 18)), canvas_height - canvas_height / 8,
            (canvas_width / 3) + ((canvas_width) / 18), canvas_height - canvas_height / 8,
            (canvas_width / 3), canvas_height,

        ]
        points2=points21+points22
        rectanglepoint=[
            (canvas_width / 3) + ((canvas_width) / 18), canvas_height - canvas_height / 8,
            points2[4] ,points2[5],
        ]
        self.canvasU.create_polygon(points, outline=python_green,
                          fill='blue', width=3)

        self.canvasU.create_polygon(points1, outline=python_green,
                           fill='red', width=3)
        self.canvasU.create_polygon(points2, outline=python_green,
                           fill='yellow', width=3,tags='obj2Tag')

        ###############################################################
        self.rightPanedWindow = ttk.Panedwindow(self.frameRight, orient=VERTICAL)
        self.rightPanedWindow.pack(fill=BOTH, expand=True)
        self.frameRightUp = ttk.Frame(self.rightPanedWindow, width=100, height=400, relief=SUNKEN)
        self.frameRightDown = ttk.Frame(self.rightPanedWindow, width=400, height=100, relief=SUNKEN)
        self.rightPanedWindow.add(self.frameRightUp, weight=4)
        self.rightPanedWindow.add(self.frameRightDown, weight=1)
        ##################################################################
        self.rightUpPanedWindow=ttk.Panedwindow(self.frameRightUp, orient=HORIZONTAL)
        self.frameRightUpLeftStyle = ttk.Style()
        self.frameRightUpLeftStyle.configure('My.TFrame', background='white')
        self.rightUpPanedWindow.pack(fill=BOTH, expand=True)
        self.frameRightUpLeft = ttk.Frame(self.rightUpPanedWindow,style='My.TFrame', width=100, height=300, relief=SUNKEN)
        self.frameRightUpRight = ttk.Frame(self.rightUpPanedWindow, width=400, height=400, relief=SUNKEN)
        self.rightUpPanedWindow.add(self.frameRightUpLeft,weight=1)
        self.rightUpPanedWindow.add(self.frameRightUpRight,weight=4)
        ####################################################################
        self.rightUpRightPanedWindow = ttk.Panedwindow(self.frameRightUpRight, orient=VERTICAL)
        self.rightUpRightPanedWindow.pack(fill=BOTH, expand=True)
        self.frameMbox = ttk.Frame(self.rightUpRightPanedWindow, width=100, height=400, relief=SUNKEN)
        self.framePbar = ttk.Frame(self.rightUpRightPanedWindow, width=400, height=100, relief=SUNKEN)
        self.rightUpRightPanedWindow.add(self.frameMbox, weight=4)
        self.rightUpRightPanedWindow.add(self.framePbar, weight=1)
        self.labelFrameRightUpRight=LabelFrame(self.frameMbox,text="Logs",relief = RIDGE)
        self.labelFrameRightUpRight.pack(fill=BOTH,expand=True)
        self.labelFrameRightUpRight.config()
        self.labelFrameRightDownRight = LabelFrame(self.framePbar, text="Download Process", relief=RIDGE)
        self.labelFrameRightDownRight.pack(fill=BOTH, expand=True)
        self.labelFrameRightDownRight.config()
        ############################################################
        self.controler=Controler(self)
        self.buttonCrawl=CustomButton(self.canvasU,rectanglepoint,"crawl",self.controler.option)
        self.controler.option.treeView.bind('<Double-Button-1>', self.addNewtoTreeView)
        self.entry1 = Entry(self.canvasU)
        self.entry2=Entry(self.canvasU)
        self.entry3=Entry(self.canvasU)
        self.label1 = Label(self.canvasU,text='Folder')
        self.label2 = Label(self.canvasU,text='KeyWord')
        self.label3 = Label(self.canvasU,text='Number')
        self.buttonadd=Button(self.canvasU,text="Add New KeyWord",command=self.unpackEntry)
        self.buttoncancel=Button(self.canvasU,text="Cancel",command=self.deleteEntry)
        self.ide1 = 0
        self.ide2 = 0
        self.ide3 = 0
        self.idl1 = 0
        self.idl2 = 0
        self.idl3 = 0
        self.idb1=0
        self.idb2=0
        # self.buttonadd.bind('<Return>', self.unpackEntry)
        # self.buttonCrawl.config(command=lambda: self.Crawl(self))

    def addNewtoTreeView(self, event=None):
        self.ide1=self.canvasU.create_window(100, 60, window = self.entry1)
        self.ide2=self.canvasU.create_window(100, 85, window=self.entry2)
        self.ide3=self.canvasU.create_window(100, 110, window=self.entry3)
        self.idl1=self.canvasU.create_window(250, 60, window = self.label1)
        self.idl2=self.canvasU.create_window(250, 85, window=self.label2)
        self.idl3=self.canvasU.create_window(250, 110, window=self.label3)
        self.idb1=self.canvasU.create_window(160,200, window=self.buttonadd)
        self.idb2 = self.canvasU.create_window(160, 250, window=self.buttoncancel)



    def unpackEntry(self):
        if self.entry1.get()!="" and self.entry2.get()!="":
            if str.isnumeric(self.entry3.get()):
                self.controler.option.engineFile.data[(self.entry1.get(),self.entry2.get())] = int(self.entry3.get())
                self.controler.option.treeView.insert_row(
                    [self.controler.option.treeView.number_of_rows + 1, self.entry1.get(),self.entry2.get(), int(self.entry3.get())],
                    index=self.controler.option.treeView.number_of_rows + 1)
            else:
                self.controler.option.engineFile.data[(self.entry1.get(), self.entry2.get())] = -1
                self.controler.option.treeView.insert_row(
                    [self.controler.option.treeView.number_of_rows + 1, self.entry1.get(),self.entry2.get(),-1],
                    index=self.controler.option.treeView.number_of_rows + 1)
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        self.canvasU.delete(self.ide1)
        self.canvasU.delete(self.ide2)
        self.canvasU.delete(self.ide3)
        self.canvasU.delete(self.idl1)
        self.canvasU.delete(self.idl2)
        self.canvasU.delete(self.idl3)
        self.canvasU.delete(self.idb1)
        self.canvasU.delete(self.idb2)

    def deleteEntry(self):
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        self.canvasU.delete(self.ide1)
        self.canvasU.delete(self.ide2)
        self.canvasU.delete(self.ide3)
        self.canvasU.delete(self.idl1)
        self.canvasU.delete(self.idl2)
        self.canvasU.delete(self.idl3)
        self.canvasU.delete(self.idb1)
        self.canvasU.delete(self.idb2)




