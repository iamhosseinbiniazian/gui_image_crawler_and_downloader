import collections
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import io
import json
class Configure:
    def __init__(self,path="./config"):
        '''
        :param path:
        '''
        self.path=path
        self.option = collections.OrderedDict()
        self.allengine=["Google","Flickr","Bing"]
        #self.option['engine'] = ["Google","Flickr","Bing"]
        self.option['engine'] = ['Google']
        self.option['safe search']=BooleanVar(False)
        self.option['exclude'] = ["*/.svn", "*/.bzr"],
        self.option['dry_run'] = None
        self.option['prefer'] = []
        self.option['defaults'] = BooleanVar(False)
        self.option['exact'] = BooleanVar(False)
        self.option['min_size'] = 25
        self.option['noninteractive'] = None
        self.option['deletedup'] = BooleanVar(False)
        self.option['dir'] ='/home/apasai'
        self.option['face-only'] = BooleanVar(False)
        self.option['timeout'] = 25
        self.option['num-threads'] = 50
        self.option['max-number'] = -4
        self.option['output'] ="./download_imagess"
        self.option['proxy_http'] = None
        self.option['numImage'] = 500
        self.option['proxy_socks5'] = None
        self.engineVariable = dict()
        for i in self.allengine:
            self.engineVariable[i]=BooleanVar()
        for key ,_ in self.engineVariable.items():
            self.engineVariable[key].set(False)
        # initializing the choice, i.e. Python
        self.show_line_number = IntVar()
        self.show_line_number.set(1)
        self.show_cursor_info = IntVar()
        self.show_cursor_info.set(1)
        self.theme_choice = StringVar()
        self.theme_choice.set('Default')
        self.highlight_line = IntVar()
        self.backup=self.option
    def EngineChoose(self):
        self.option['engine']=[]
        for key,value in self.engineVariable.items():
            if value.get():
                self.option['engine'].append(key)
        print(self.option['engine'])
    def saveConfigure(self):
        filePath =self.path
        self._SaveConfigure(self.option,filePath)
        messagebox.showinfo("save configure", "configure saved as '%s'"%filePath)
        self.path=filePath

    def saveAsConfigure(self):
        filePath = filedialog.asksaveasfilename(filetypes=(("Json File", "*.json")
                                   , ("All files", "*.*")))
        self._SaveConfigure(self.option,filePath)
        messagebox.showinfo("save configure", "configure saved as '%s'"%filePath)
        self.path=filePath

    def goDefult(self,path="./config"):
        answer=messagebox.askyesno("Defult","Are you sure?")
        # try:
        if answer:
            for key, _ in self.engineVariable.items():
                self.engineVariable[key].set(False)
            self.option=self.backup
            for key in self.option['engine']:
                self.engineVariable[key].set(True)
            self.path = './config'
            self._SaveConfigure(self.option)
            messagebox.showinfo("Load defult configure", "Defult configure loaded(./config.json)")
        # except:
            # messagebox.showerror("Load defult configure", "Defult configure unloaded" )
    def _SaveConfigure(self,data,path='./config.json'):
        self.savedictionary=collections.OrderedDict()
        for key , value in data.items():
            if isinstance(value,(BooleanVar)):
                self.savedictionary[key]=int(value.get())
            elif value == None:
                self.savedictionary[key] = "None"
            else:
                self.savedictionary[key] = value
        with open(path, 'w') as fp:
            json.dump(self.savedictionary, fp)
    def loadConfigure(self):
        for key ,_ in self.engineVariable.items():
            self.engineVariable[key].set(False)
        filePath=filedialog.askopenfilename(filetypes = (("Jason File", "*.json")
                                              ,("All files", "*.*")))
        if filePath:
            try:
                print('read:',filePath)
                with io.open(filePath,mode='r') as file:
                    data = json.load(file)
                    for key , value in data.items():
                            if value in [0,1]:
                                self.changeOption(bool(value), optionname=key)
                            elif value == 'None':
                                self.changeOption(None, optionname=key)
                            else:
                                self.changeOption(value, optionname=key)
                for key in self.option['engine']:
                    self.engineVariable[key].set(True)
                self.path=filePath
            except:
                messagebox.showerror("Open Source File", "Failed to read file \n'%s'" % filePath)
    def changeOption(self,value,optionname='engine'):
        if value in [True,False]:
            self.option[optionname].set(value)
        else:
            self.option[optionname]=value




