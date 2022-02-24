#!/usr/bin/env python3


import sys

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
class TestApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.wm_title('Ctext test app')
        self.ctext = Ctext(self, background="black", foreground="white")
        self.ctext.pack(expand=True, fill='both')
        self.after_idle(self.create)

    def create(self):
        self.ctext.add_highlight_class('keyword', 'cyan', ['printf','return'])
        self.ctext.add_highlight_regexp('include', 'red', "<.*>")
        self.ctext.add_highlight_prefix('preprocessor', 'yellow', '#')
        self.ctext.add_highlight_chars('exclamation', 'magenta', '!')
        self.ctext.add_highlight_chars('punctuation', 'green', "\n\"\'")
        self.ctext.enable_c_comments(True)
        for line in (
                '/* this is a comment',
                ' */',
                '#include <stdio.h>',
                'int main(int argc, char *argv[])',
                '{',
                '    printf("Hello, World!\\n");',
                '    return 0;',
                '}'):
            self.ctext.insert('end', line, '', "\n", '')
        self.after_idle(self.rehighlight)
        self.after(2000, self.delete_class)
        self.after(5000, self.clearall)

    def delete_class(self):
        print("*** delete class")
        print(self.ctext.get_highlight_classes())
        self.ctext.delete_highlight_class('exclamation')
        print("'exclamation' class deleted.")
        print(self.ctext.get_highlight_classes())
        self.after_idle(self.rehighlight)

    def clearall(self):
        print("*** clearall")
        print(self.ctext.get_highlight_classes())
        self.ctext.clear_highlight_classes()
        print(self.ctext.get_highlight_classes())
        self.after_idle(self.rehighlight)

    def rehighlight(self):
        self.ctext.highlight('1.0', 'end - 1 line')


def main():
    """Program entry."""
    app = TestApp()
    app.mainloop()
    return 0

if __name__ == '__main__':
    sys.exit(main())