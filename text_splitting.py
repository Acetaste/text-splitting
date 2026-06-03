from tkinter import *
from tkinter import ttk
import re
from name_split_library import *


root = Tk()
root.title("Text Splitting Tool")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

StrToReplace            = StringVar()
StrToReplaceWith        = StringVar()


BoolNewline             = BooleanVar()
BoolURL                 = BooleanVar()

def switch_callback():
    Input               = inputtextentry.get("1.0","end")
    Output              = outputtextentry.get("1.0","end")
    
    inputtextentry.delete("1.0","end")
    outputtextentry.delete("1.0","end")
    
    inputtextentry.insert(chars = Output, index = "1.0")
    outputtextentry.insert(chars = Input, index = "1.0")
    
def replace_callback():
    Input               = inputtextentry.get("1.0","end")
    if BoolNewline.get():
        Input           = f"{StrToReplaceWith.get()}".join(Input.splitlines())
        Input           = Input.replace(f"\n",f"")
    
    Input               = Input.replace(f"{StrToReplace.get()}",f"{StrToReplaceWith.get()}")
    
    outputtextentry.delete("1.0","end")
    outputtextentry.insert(chars = Input, index = "1.0")    
    

def clean_callback():
    input_string        = inputtextentry.get("1.0","end")
    
    processed_string    = remove_characters(input_string)
    processed_string    = replace_characters_with_comma(processed_string)
    processed_string    = remove_index(processed_string)
    processed_string    = normalizes_separator(processed_string)   
    if BoolURL.get():
        processed_string = remove_url(processed_string)
    
    outputtextentry.delete("1.0","end")
    outputtextentry.insert(chars = processed_string, index = "1.0") 
 
def name_split_callback(): 
    input_string        = inputtextentry.get("1.0","end")
    input_string        = f"".join(input_string.splitlines())
    input_string        = input_string.replace(f"\n",f"")
    
    output_string       = name_split(input_string)
    
    outputtextentry.delete("1.0","end")
    outputtextentry.insert(chars = output_string, index = "1.0") 
    
def clean_and_split_callback():
    input_string        = inputtextentry.get("1.0","end")
    processed_string    = f"".join(input_string.splitlines())
    processed_string    = processed_string.replace(f"\n",f"")
    
    processed_string    = remove_characters(processed_string)
    processed_string    = replace_characters_with_comma(processed_string)
    processed_string    = remove_index(processed_string)
    processed_string    = normalizes_separator(processed_string)   
    processed_string    = remove_url(processed_string)
    
    output_string       = name_split(processed_string)
    
    outputtextentry.delete("1.0","end")
    outputtextentry.insert(chars = output_string, index = "1.0") 
    

#mainframe

mainframe = ttk.Frame(root, padding = (3, 3, 12, 12))
mainframe.grid(column = 0, row  = 0, sticky = "NWSE")
mainframe.rowconfigure(0, weight=1)
mainframe.columnconfigure(0, weight=1)
mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=1)

controlframe = ttk.Frame(mainframe)
controlframe.grid(column = 0, row = 0, columnspan =1, sticky = (N, W, E), padx =10, pady =10)
controlframe.columnconfigure(0, weight=1)

inputtextframe = ttk.Frame(mainframe)
inputtextframe.grid(column = 1, row = 0, sticky = (N, W, S, E), padx =10, pady =10)
inputtextframe.rowconfigure(1, weight=1)
inputtextframe.columnconfigure(0, weight=1)

outputtextframe = ttk.Frame(mainframe)
outputtextframe.grid(column = 2, row = 0, sticky = (N, W, S, E), padx =10, pady =10)
outputtextframe.rowconfigure(1, weight=1)
outputtextframe.columnconfigure(0, weight=1)


#controlframe

controlframetext = ttk.Label(controlframe, text = "Control:")
controlframetext.grid(column = 0, row = 0, sticky = (N, W, E))

switchframe = ttk.Frame(controlframe)
switchframe.grid(column = 0, row = 1, columnspan= 2, sticky = (W, E))
switchframe.columnconfigure(0, weight = 1)


replaceframe = ttk.Frame(controlframe)
replaceframe.grid(column = 0, row = 2,columnspan=2, sticky = (W, E))
replaceframe.columnconfigure(0, weight = 1)
replaceframe.columnconfigure(1, weight = 1)

cleanframe = ttk.Frame(controlframe)
cleanframe.grid(column =0, row = 3, sticky = (W, E))
cleanframe.columnconfigure(0, weight = 1)
cleanframe.columnconfigure(1, weight = 1)


nameframe = ttk.Frame(controlframe)
nameframe.grid(column = 0, row = 4, sticky = (W, E))
nameframe.columnconfigure(0, weight = 1)
nameframe.columnconfigure(1, weight = 1)



#switchframe

switchbutton = ttk.Button(switchframe, text = "Switch", command = switch_callback)
switchbutton.grid(column = 0, row = 0, sticky = (W, E))

#nameframe

namesplitbutton = ttk.Button(nameframe, text = "Name Split", command = name_split_callback)
namesplitbutton.grid(column = 0, row = 0, sticky = (W, E))

cleanandsplitbutton = ttk.Button(nameframe, text = "Clean 'N Split", command = clean_and_split_callback)
cleanandsplitbutton.grid(column = 1, row = 0, sticky = (W, E))

#cleanframe

cleanbutton = ttk.Button(cleanframe, text = "Clean", command = clean_callback)
cleanbutton.grid(column = 0, row = 0, sticky = (W, E))

cleancheck = ttk.Checkbutton(cleanframe, text = "Remove Email/URL", variable = BoolURL)
cleancheck.grid(column=1, row = 0, sticky = (W, E))

#replaceframe

replacebutton = ttk.Button(replaceframe, text = "Replace", command = replace_callback)
replacebutton.grid(column = 0, row = 0, sticky = (W, E))

newlinecheck = ttk.Checkbutton(replaceframe, text = "Replace Newline", variable = BoolNewline)
newlinecheck.grid(column=1, row = 0, sticky = (W, E))

replaceentry = ttk.Entry(replaceframe, textvariable=StrToReplace)
replaceentry.grid(column = 0, row = 1, sticky = (W, E))

replacewithentry = ttk.Entry(replaceframe, textvariable=StrToReplaceWith)
replacewithentry.grid(column = 1, row = 1, sticky = (W, E))



#textframe

inputframetext = ttk.Label(inputtextframe, text = "Input:")
inputframetext.grid(column = 0, row = 0, sticky = (N, W, E))

inputtextentry = Text(inputtextframe)
inputtextentry.grid(column = 0, row = 1, sticky = (N, S , W, E))

outputframetext = ttk.Label(outputtextframe, text = "Output:")
outputframetext.grid(column = 0, row = 0, sticky = (N, W, E))

outputtextentry = Text(outputtextframe)
outputtextentry.grid(column = 0, row = 1, sticky = (N, S , W, E))





root.mainloop()