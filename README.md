# pyvim
Use vim to edit and execute commands and files from the Python interpreter

editor:
    calls vim from Python console, opening a temp file
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
