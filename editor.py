#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
from readline import get_history_item as histitem
from readline import get_current_history_length as histlen

def editor(path=None):
    """editor:
    calls vim from python console, opening a temp file
    with filetype set to Python, enabling the use of 
    highlighting and indentation. 
    
    Useful for multiline command editing without having 
    to leave the Python interactive console. 
    
    The line previous to the editor being called will be 
    written to the temp file and should just be deleted 
    if not wanted.
    
    Code will be executed on save/exit and any objects 
    defined will be saved as globals.
    
    Existing files can also be opened and edited. The 
    file will be executed on exit.
    
    Examples:
        editor()
        editor('myfile.py')
    """

    import sys, tempfile, os
    from subprocess import call
    with tempfile.NamedTemporaryFile(suffix=".tmp") as tf:
        if not path == None:
            with open(path, 'rb') as f:
                initstr = f.read()
            tf.write(initstr)
        else:
            initstr = bytes(histitem(histlen()-1), "utf-8")
            tf.write(initstr)
        tf.flush()
        call(['vim', '-c', 'set filetype=python', tf.name])
        tf.seek(0)
        s = tf.read()
        print(s.decode("utf-8"))
        exec(s, globals())
