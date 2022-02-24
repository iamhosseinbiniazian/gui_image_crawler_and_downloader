# ctext.py - Copyright (c) 2017 Pat Thoyts <patthoyts@users.sourceforge.net>
#
# SPDX-License-Identifier: BSD-3-Clause

'''Python wrapper for the Tklib ctext widget.
See the Tk documentation for complete details of the use of this widget.
'''

import tkinter as tk

class Ctext(tk.Text):
    '''Python wrapper for the Tklib ctext widget'''
    def __init__(self, master=None, cnf={}, **kwargs):
        '''Initialize the ctext wrapper.'''
        if master:
            self.master = master
        else:
            self.master = tk._default_root
        self.version = self.master.tk.call('package', 'require', 'ctext')
        tk.Widget.__init__(self, master, 'ctext', cnf, kwargs)

    def highlight(self, start_index, end_index):
        '''Highlight the text between start_index and end_index.'''
        self.tk.call(self._w, 'highlight', start_index, end_index)

    def fastdelete(self, index, index2=None):
        '''Delete the text range specified without updating the highlighting.
        Arguments are identical to the delete method.'''
        self.tk.call(self._w, 'fastdelete', index, index2)

    def fastinsert(self, index, *args):
        '''Insert text without updating the highlighting.
        Arguments are identical to the insert method.'''
        self.tk.call(self._w, 'fastinsert', index, *args)

    def copy(self):
        '''Copy the selected text from this widget to the clipboard.'''
        self.tk.call('tk_textCopy', self._w)

    def cut(self):
        '''Copy the selected text from this widget to the clipboard and then delete it from the widget.'''
        self.tk.call('tk_textCut', self._w)

    def paste(self):
        '''Paste the contents of the clipboard to the insertion point of the ctext widget.'''
        self.tk.call('tk_textPaste', self._w)

    def append(self):
        '''Append the selected text from this widget to the clipboard.'''
        self.tk.call(self._w, 'append')

    def add_highlight_class(self, classname, color, wordlist):
        '''Add a highlighting class `classname` to the widget using the given color
        containing all the words in the `wordlist`.'''
        self.tk.call('ctext::addHighlightClass', self._w, classname, color, wordlist)

    def add_highlight_prefix(self, classname, color, char):
        '''Add a highlighting class that matches any word that starts with the specified `char`.'''
        self.tk.call('ctext::addHighlightClassWithOnlyCharStart', self._w, classname, color, char)

    def add_highlight_chars(self, classname, color, chars):
        '''Add a highlighting class that matches any of the characters contained in `chars`.'''
        self.tk.call('ctext::addHighlightClassForSpecialChars', self._w, classname, color, chars)

    def add_highlight_regexp(self, classname, color, pattern):
        '''Add a highlighting class that matches a regular expression to apply the chosen color.'''
        self.tk.call('ctext::addHighlightClassForRegexp', self._w, classname, color, pattern)

    def clear_highlight_classes(self):
        '''Remove all highlight classes from this widget.'''
        self.tk.call('ctext::clearHighlightClasses', self._w)

    def get_highlight_classes(self):
        '''Return a list of all the highlight class names defined for this widget.'''
        return self.tk.call('ctext::getHighlightClasses', self._w)

    def delete_highlight_class(self, classname):
        '''Delete the selected highlight class from the widget.'''
        self.tk.call('ctext::deleteHighlightClass', self._w, classname)

    def enable_c_comments(self, enable):
        '''Enable C comment highlighting.
        The class for c-style comments is `_cComment`. This highlighting is disabled by default.'''
        if enable:
            cmd = 'ctext::enableComments'
        else:
            cmd = 'ctext::disableComments'
        self.tk.call(cmd, self._w)