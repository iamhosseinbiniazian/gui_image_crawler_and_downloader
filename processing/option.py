from dill.pointers import parent

from processing.LoadEngineFile import engineFile
from processing.configure import Configure
from ui.TreeView import Multicolumn_Listbox
from ui.MenuBar import Menubar
from ui.Pbar import ProcessBar
from ui.customButton import CustomButton
from selenium import webdriver
from tkinter import filedialog
from tkinter import *
import logging
import datetime
import queue
import logging
import signal
import time
import threading
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from imagedownloder.image_downloader import main
from processing.stoppableThread import StoppableThread
from ui.editableTreeview import EditableTreeview
import arabic_reshaper
from bidi.algorithm import get_display
class Clock(threading.Thread):
    """Class to display the time every seconds
    Every 5 seconds, the time is displayed using the logging.ERROR level
    to show that different colors are associated to the log levels
    """

    def __init__(self):
        super().__init__()
        self._stop_event = threading.Event()

    def run(self):
        logger.debug('Clock started')
        previous = -1
        while not self._stop_event.is_set():
            now = datetime.datetime.now()
            if previous != now.second:
                previous = now.second
                if now.second % 5 == 0:
                    level = logging.ERROR
                else:
                    level = logging.INFO
                logger.log(level, now)
            time.sleep(0.2)

    def stop(self):
        self._stop_event.set()


class QueueHandler(logging.Handler):
    """Class to send logging records to a queue
    It can be used from different threads
    The ConsoleUi class polls this queue to display records in a ScrolledText widget
    """
    # Example from Moshe Kaplan: https://gist.github.com/moshekaplan/c425f861de7bbf28ef06
    # (https://stackoverflow.com/questions/13318742/python-logging-to-tkinter-text-widget) is not thread safe!
    # See https://stackoverflow.com/questions/43909849/tkinter-python-crashes-on-new-thread-trying-to-log-on-main-thread

    def __init__(self, log_queue):
        super().__init__()
        self.log_queue = log_queue

    def emit(self, record):
        self.log_queue.put(record)


class ConsoleUi:
    """Poll messages from a logging queue and display them in a scrolled text widget"""

    def __init__(self, frame):
        self.frame = frame
        # Create a ScrolledText wdiget
        self.scrolled_text = ScrolledText(frame, state='disabled', height=12)
        self.scrolled_text.pack(expand=YES,fill=BOTH)
        self.scrolled_text.configure(font='TkFixedFont')
        self.scrolled_text.tag_config('INFO', foreground='black')
        self.scrolled_text.tag_config('DEBUG', foreground='gray')
        self.scrolled_text.tag_config('WARNING', foreground='orange')
        self.scrolled_text.tag_config('ERROR', foreground='red')
        self.scrolled_text.tag_config('CRITICAL', foreground='red', underline=1)
        # Create a logging handler using a queue
        self.log_queue = queue.Queue()
        self.queue_handler = QueueHandler(self.log_queue)
        formatter = logging.Formatter('%(asctime)s: %(message)s')
        self.queue_handler.setFormatter(formatter)
        self.logger = logging.getLogger(__name__)
        self.logger.addHandler(self.queue_handler)
        # Start polling messages from the queue
        self.frame.after(100, self.poll_log_queue)

    def display(self, record):
        msg = self.queue_handler.format(record)
        self.scrolled_text.configure(state='normal')
        self.scrolled_text.insert(tk.END, msg + '\n', record.levelname)
        self.scrolled_text.configure(state='disabled')
        # Autoscroll to the bottom
        self.scrolled_text.yview(tk.END)

    def poll_log_queue(self):
        # Check every 100ms if there is a new message in the queue to display
        while True:
            try:
                record = self.log_queue.get(block=False)
            except queue.Empty:
                break
            else:
                self.display(record)
        self.frame.after(100, self.poll_log_queue)
####################################################3
class Option(object):
    def __init__(self,self2):
        self.root=self2
        logging.basicConfig(level=logging.DEBUG)
        self.engineFile= engineFile()
        self.configure=Configure()
        self.treeViewown=EditableTreeview(self2.frameTreeView)
        self.treeViewown.pack(fill=BOTH,expand=YES)
        self.treeView = Multicolumn_Listbox(self2.frameLabelVeiw, ["index", "Folder", "KeyWord", "Number"],
                                            cell_anchor="center", heading_anchor=W, adjust_heading_to_content=True)
        # self.treeView.interior.pack(fill=BOTH, expand=True)
        #################################################################
        # self.treeViewown.insert('', '0',  tag=get_display(arabic_reshaper.reshape('غیر اخلاقی')),text=get_display(arabic_reshaper.reshape('غیر اخلاقی')))
        # self.treeViewown.insert('', '1', 'item2', text=get_display(arabic_reshaper.reshape('Second Item')))
        # self.treeViewown.insert('', 'end', 'item3', text='Third Item')
        # self.treeViewown.insert('item2', 'end', 'python', text='Python')
        # self.treeViewown.tag_configure(get_display(arabic_reshaper.reshape('غیر اخلاقی')), font=('B Nazanin',10))
        # self.treeViewown.tag_configure(get_display(arabic_reshaper.reshape('غیر اخلاقی')), background='blue')
        # self.treeView.interior.config(height=5)
        # self.treeView.interior.move('item2', 'item1', 'end')
        # self.treeView.interior.item('item1', open=True)
        # self.treeView.interior.item('item2', open=True)
        # print(self.treeView.interior.item('item1', 'open'))
        #
        # self.treeView.interior.detach('item3')
        # self.treeView.interior.move('item3', 'item2', '0')
        # self.treeView.interior.delete('item3')
        #
        self.treeViewown.configure(column=('version'))
        self.treeViewown.column('version', width=50, anchor='center')
        # self.treeView.interior.column('version', width=50, anchor='center')
        self.treeViewown.column('#0', width=150)
        self.treeViewown.heading('#0', text='Version')
        # self.treeView.interior.set('python', 'version', '3.4')
        # self.treeView.interior.item('python', tags=('software'))
        # self.treeView.interior.tag_configure('software', background='yellow')
        ###################################333
        self.treeView.interior.pack(fill=BOTH, expand=True)
        self.menuBar=Menubar(self2.root,self)
        self.messageBox=ConsoleUi(self2.labelFrameRightUpRight)
        self.Pbar=ProcessBar(self2.labelFrameRightDownRight)
        self.treeView.bind('<Delete>',self.deleteAllSelected )
        self.updateMenu()
        self.myRunThread=StoppableThread(target=self.crawlProcessing)
        self.logger = logging.getLogger(__name__)

    def Crawl(self):
        self.messageBox.logger.log(logging.INFO, 'Start Crawling')

        self.myRunThread.start()


        # self.crawlProcessing()

    def crawlProcessing(self):
        self.messageBox.logger.log(logging.INFO,"Your all sellected search engine is="+str(self.configure.option['engine']))

        for i in self.treeView.table_data:
            folder=i[1]
            keyword=i[2]
            numImage=i[3]
            self.messageBox.logger.log(logging.INFO, keyword)
            # self.root.root.update()
            main(sys.argv[1:],folder,keyword,numImage,self.messageBox.logger,self.Pbar)
    def searchImage(self):
        filePath = filedialog.askopenfilename(filetypes=(("JPG File", "*.jpg")
                                   , ("All files", "*.*")))
        url='https://www.google.com/imghp?hl=en&tab=wi'
        driver = webdriver.Chrome('./chromedriver')
        driver.get(url)
        driver.maximize_window()
        element1 = driver.find_element_by_class_name('gsst_e')
        element1.click()

        element1 = driver.find_element_by_xpath("//*[@class='qbtbha qbtbtxt qbclr']")
        element1.click()
        # element1 = driver.find_element_by_id('qbfile')
        fileInput = driver.find_element_by_id('qbfile')
        # fileInput.send_keys('/home/apasai/Desktop/alidaei.jpg')
        fileInput.send_keys(filePath)




        # element1[1].click()
    def LoadExcelFile(self):
        self.engineFile.loadXlsxFile()
        for i in self.engineFile.dataXlsx.keys():
            parent1=self.treeViewown.insert('', 'end',text=get_display(arabic_reshaper.reshape(i)))
            for j in self.engineFile.dataXlsx[i].keys():
                parent2=self.treeViewown.insert(parent1, 'end', text=get_display(arabic_reshaper.reshape(j)))
                for k in self.engineFile.dataXlsx[i][j].keys():
                    self.treeViewown.insert(parent2, 'end', text=get_display(arabic_reshaper.reshape(k)))

    def goConfigureToDefult(self):
        self.configure.goDefult()
    def loadEngineFile(self):
        self.engineFile.loadFile()
        self.updateTreeView()
    def loadConfigureFile(self):
        self.configure.loadConfigure()
    def deleteAllSelected(self,event=None):
        for item in self.treeView.selected_rows:
            del self.engineFile.data[(item[1],item[2])]
        self.treeView.clear()
        self.updateTreeView()
    def selectAll(self):
       for i in range(self.treeView.number_of_rows):
           self.treeView.select_row(i)
    def saveConfigureFile(self):
        self.configure.saveConfigure()
    def saveAsConfigureFile(self):
        self.configure.saveAsConfigure()
    def saveEngineFile(self):
        self.engineFile.saveFile()
    def saveAsEngineFile(self):
        self.engineFile.saveAsFile()
    def NewEngineFile(self):
        self.engineFile.newFile()
        self.treeView.clear()
    def Exit(self):
        self.root.root.destroy()
        self.myRunThread.stop()
    def updateMenu(self):
        for key in self.configure.option['engine']:
            self.configure.engineVariable[key].set(True)
        for key in enumerate(self.configure.engineVariable.items()):
            if key[1][1].get():
                self.menuBar.engineMenu.entryconfig(key[1][0])
    def updateTreeView(self):
        self.treeView.clear()
        for key,value in self.engineFile.data.items():
            self.treeView.insert_row([self.treeView.number_of_rows+1,key[0],key[1],value],index=self.treeView.number_of_rows+1)


