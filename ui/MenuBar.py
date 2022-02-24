from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

class Menubar:
    def __init__(self,root,option):
        self.root = root
        self.color_schemes = {
        'Default': '#000000.#FFFFFF',
        'Greygarious': '#83406A.#D1D4D1',
        'Aquamarine': '#5B8340.#D1E7E0',
        'Bold Beige': '#4B4620.#FFF0E1',
        'Cobalt Blue': '#ffffBB.#3333aa',
        'Olive Green': '#D1E7E0.#5B8340',
        'Night Mode': '#FFFFFF.#000000',}
        self.new_file_icon = PhotoImage(file='ui/icons/new_file.gif')
        self.open_file_icon = PhotoImage(file='ui/icons/open_file.gif')
        self.save_file_icon = PhotoImage(file='ui/icons/save.png')
        self.save_as_file_icon = PhotoImage(file='ui/icons/save_as.png')
        self.cut_icon = PhotoImage(file='ui/icons/cut.gif')
        self.copy_icon = PhotoImage(file='ui/icons/copy.gif')
        self.paste_icon = PhotoImage(file='ui/icons/paste.gif')
        self.undo_icon = PhotoImage(file='ui/icons/undo.gif')
        self.redo_icon = PhotoImage(file='ui/icons/redo.gif')
        self.google_icon = PhotoImage(file='ui/icons/google.png')
        self.bing_icon = PhotoImage(file='ui/icons/bing.png')
        self.flickr_icon = PhotoImage(file='ui/icons/flicker.png')
        self.engine_icon = PhotoImage(file='ui/icons/engine.png')
        self.safe_search_icon = PhotoImage(file='ui/icons/safesearch.png')
        self.yes_icon = PhotoImage(file='ui/icons/yes.png')
        self.no_icon = PhotoImage(file='ui/icons/no.png')
        self.defults_icon = PhotoImage(file='ui/icons/defults.png').subsample(32,32)

        self.deletedulicate_icon = PhotoImage(file='ui/icons/Duplicate-icon.png')
        self.engine =  [
            ("Google", 1,self.google_icon),
            ("Bing", 2,self.bing_icon),
            ("Flickr", 3,self.flickr_icon)
        ]
        ###########################################################
        self.mainMenu=self.createMainMenu()
        self.fileMenu=self.createFileMenu(option)
        (self.optionMenu,self.engineMenu,self.safeSearchMenu,self.deleteDuplicateMenu)=self.createOptionMenu(option)
        self.editMenu=self.createEditMenu(option)
        self.viewMenu=self.createViewMenu(option)
        self.imageMenu=self.createImageMenu(option)
        self.aboutMenu=self.createAboutMenu()
    def createViewMenu(self,option):
        view_menu = Menu(self.mainMenu, tearoff=0)
        view_menu.add_checkbutton(label='Show Line Number', variable=option.configure.show_line_number)
        view_menu.add_checkbutton(
            label='Show Cursor Location at Bottom', variable=option.configure.show_cursor_info)

        view_menu.add_checkbutton(label='Highlight Current Line', onvalue=1,
                                  offvalue=0, variable=option.configure.highlight_line)
        themes_menu = Menu(view_menu, tearoff=0)
        view_menu.add_cascade(label='Themes', menu=themes_menu,command=lambda :self.get_theme(option))
        for k in sorted(self.color_schemes):
            themes_menu.add_radiobutton(label=k, variable=option.configure.theme_choice,value=k)
        self.mainMenu.add_cascade(label='View', menu=view_menu)
        return view_menu

    def get_theme(self,option):
        print(option.configure.theme_choice)
    def changeOtionMenu(self,option):
        self.optionMenu=self.createOptionMenu(option)
    def createMainMenu(self):
        #########################Main Menu#############################
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        return menubar
    def createOptionMenu(self,option):
        optionM = Menu(self.mainMenu)
        self.mainMenu.add_cascade(menu=optionM, label='Option')
        engine = Menu(optionM)
        optionM.add_cascade(menu=engine, label='Engine',image=self.engine_icon,compound=LEFT)
        for val, eng in enumerate(self.engine):
            engine.add_checkbutton(label=eng[0], image=eng[2], compound=LEFT,
                                   variable=option.configure.engineVariable[eng[0]],
                                   command=option.configure.EngineChoose)
        optionM.add_separator()
        safeSearch = Menu(optionM)
        optionM.add_cascade(menu=safeSearch, label='Safe Search',image=self.safe_search_icon,compound=LEFT)
        safeSearch.add_radiobutton(label='Yes', variable=option.configure.option['safe search'], value=True,image=self.yes_icon,compound=LEFT)

        safeSearch.add_radiobutton(label='No', variable=option.configure.option['safe search'], value=False,image=self.no_icon,compound=LEFT)
        optionM.add_separator()
        deleteDuplicate = Menu(optionM)
        optionM.add_cascade(menu=deleteDuplicate, label='Delete Duplicate', image=self.deletedulicate_icon, compound=LEFT)
        deleteDuplicate.add_radiobutton(label='Yes', variable=option.configure.option['deletedup'], value=True,
                                   image=self.yes_icon, compound=LEFT)

        deleteDuplicate.add_radiobutton(label='No', variable=option.configure.option['deletedup'], value=False,
                                   image=self.no_icon, compound=LEFT)
        optionM.add_separator()
        defults = Menu(optionM)
        optionM.add_cascade(menu=defults, label='Defults', image=self.defults_icon, compound=LEFT)
        defults.add_radiobutton(label='Yes', variable=option.configure.option['defaults'], value=True,
                                        image=self.yes_icon, compound=LEFT)

        defults.add_radiobutton(label='No', variable=option.configure.option['defaults'], value=False,
                                        image=self.no_icon, compound=LEFT)
        return (optionM,engine,safeSearch,deleteDuplicate)

####################################################################################################################################
    def createFileMenu(self,option):
        file = Menu(self.mainMenu)
        configure = Menu(file)
        file.add_cascade(menu=configure, label="Configure")
        configure.add_command(label='Defult',compound=LEFT,image=self.new_file_icon,command=option.goConfigureToDefult)
        configure.add_command(label='Load',compound=LEFT,image=self.open_file_icon ,command=option.loadConfigureFile)
        configure.add_command(label="Save",compound=LEFT,image=self.save_file_icon,command=option.saveConfigureFile)
        configure.add_command(label="Save As",compound=LEFT,image=self.save_as_file_icon,command=option.saveAsConfigureFile)
        self.mainMenu.add_cascade(menu=file, label='File')
        loadEngineFile = Menu(file)
        file.add_cascade(menu=loadEngineFile, label="Load Engine File")
        loadEngineFile.add_command(label='New',compound=LEFT,image=self.new_file_icon,command=option.NewEngineFile)
        loadEngineFile.add_command(label='Load',compound=LEFT,image=self.open_file_icon , command=option.loadEngineFile)
        loadEngineFile.add_command(label='Load xlsx',compound=LEFT,image=self.open_file_icon , command=option.LoadExcelFile)
        loadEngineFile.add_command(label="Save",compound=LEFT,image=self.save_file_icon,command=option.saveEngineFile)
        loadEngineFile.add_command(label="Save As",compound=LEFT,image=self.save_as_file_icon,command=option.saveAsEngineFile)
        file.add_command(label='Exit', command=option.Exit)
        file.entryconfig('Exit', accelerator='Alt+F4')
        return file
###########################################################################################################################################
    def createEditMenu(self,option):
        edit_menu = Menu(self.mainMenu, tearoff=0)
        edit_menu.add_command(label='Undo', accelerator='Ctrl+Z', compound='left', image=self.undo_icon, command=self.undo)
        edit_menu.add_command(label='Redo', accelerator='Ctrl+Y', compound='left', image=self.redo_icon, command=self.redo)
        edit_menu.add_separator()
        edit_menu.add_command(label='Cut', accelerator='Ctrl+X', compound='left', image=self.cut_icon, command=self.cut)
        edit_menu.add_command(label='Copy', accelerator='Ctrl+C', compound='left', image=self.copy_icon, command=self.copy)
        edit_menu.add_command(label='Paste', accelerator='Ctrl+V', compound='left', image=self.paste_icon, command=self.paste)
        edit_menu.add_separator()
        edit_menu.add_command(label='Find', underline=0, accelerator='Ctrl+F')
        edit_menu.add_separator()
        edit_menu.add_command(label='Select All', underline=7, accelerator='Ctrl+A',command=option.selectAll)
        self.mainMenu.add_cascade(label='Edit', menu=edit_menu)
        return edit_menu
################################################################################################################
    def createImageMenu(self, option):
        image_menu = Menu(self.mainMenu, tearoff=0)
        image_menu.add_command(label='Load Image',command=option.searchImage)
        image_menu.add_command(label='Help')
        self.mainMenu.add_cascade(label='Search', menu=image_menu)
        return image_menu
#########################################################################################################################################
    def createAboutMenu(self):
        about_menu = Menu(self.mainMenu, tearoff=0)
        about_menu.add_command(label='About')
        about_menu.add_command(label='Help')
        self.mainMenu.add_cascade(label='About', menu=about_menu)
#########################################################################################################################################
    def Exit(self):
        self.root.destroy()
    def cut(self):
        # content_text.event_generate("<<Cut>>")
        return "break"

    def copy(self):
        # content_text.event_generate("<<Copy>>")
        return "break"

    def paste(self):
        # content_text.event_generate("<<Paste>>")
        return "break"

    def undo(self):
        # content_text.event_generate("<<Undo>>")
        return "break"

    def redo(self,event=None):
        # content_text.event_generate("<<Redo>>")
        return 'break'



