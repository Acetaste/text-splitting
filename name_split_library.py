def remove_characters(inputString):
    characters = [  "✉",
                    "corresponding author",
                    "Corresponding Author",
                    "#",
                    "*",
                    "‖",
                    "§",
                    "¶",
                    "∗",
                    "‡",
                    "†",
                    "ORCID",
                    "ORCID logo",
                    ""
                    ]
    for character in characters:
        inputString = inputString.replace(character,"")
    return inputString
    
def replace_characters_with_comma(inputString):
    characters = [  "&",
                    ";",
                    " and",
                    "∙",
                    ]
    for character in characters:
        inputString = inputString.replace(character,",")
    return inputString
    
def normalizes_separator(inputString):
    
    for i in range(0,10):
            inputString = inputString.replace("  "," ")
            inputString = inputString.replace(" ,",",")
            inputString = inputString.replace(",,",",")
        
    
    if inputString[len(inputString)-1] == ",":
        inputString     = inputString[:-1]
        
    inputString         = inputString.replace(",",", ")
    
    for i in range(0,10):
            inputString = inputString.replace("  "," ")
            inputString = inputString.replace(" ,",",")
            inputString = inputString.replace(",,",",")
            
    return inputString
    
def trim_string(inputString):
    processed_string    = f"".join(inputString.splitlines())
    processed_string    = processed_string.replace(f"\n",f"")
    processed_string    = processed_string.strip()
    return processed_string
    
def normalize_space(inputString):
    for i in range(0,10):
            inputString = inputString.replace("  "," ")
            
    if inputString[0] == " ":
        inputString= inputString[1:]
        
    if inputString[len(inputString)-1] == " ":
        inputString= inputString[:-1]
        
    return inputString
    
def remove_index(inputString):
    for i in range(0,10):
        inputString = inputString.replace(str(i),",")
    for i in range(1,4):
        for lower_case_letter in range(ord("a"), ord("z")):
            inputString = inputString.replace(f" {chr(lower_case_letter)},",",")
        for upper_case_letter in range(ord("A"), ord("Z")):
            inputString = inputString.replace(f" {chr(upper_case_letter)},",",")
    return inputString
    
def remove_url(inputString):
    inputList = inputString.split(", ")
    temp = list()
    for i in inputList:
        if (not ("http" in i)) and (not("@" in i)):
            temp.append(i)
    return ", ".join(temp)
    
def name_split(inputString):
    inputList          = inputString.split(", ")
    outputList         = list()
    for author in inputList:
        Jr_Flag             = False
        if (" Jr." in author) or("Jr." in author[0:3]): 
            author          = author.replace("Jr.", "")
            Jr_Flag         = True
        elif (" Jr" in author)or("Jr" in author[0:2]):
            author          = author.replace("Jr", "")
            Jr_Flag         = True
        
        author              = normalize_space(author)
        author_split        = author.rsplit(" ",1)

        
        author_split[0]     = author_split[0].replace(" ","-")
        author_split[0]     = author_split[0].replace(".","")
        firstname_count     = author_split[0].count("-")
        for i in range(1, firstname_count+2):
            
            if (i == firstname_count+1):
                author_split[0]    = author_split[0][:i]
            else:
                author_split[0]    = author_split[0][:i] + author_split[0][author_split[0].find("-")+1:]
        if Jr_Flag:
            author_split.append("Jr")
        
        author = " ".join(author_split)
        outputList.append(author)
        
    outputString = ", ".join(outputList)
    return outputString

def write_out(inputString, textWidget):
    textWidget['state'] = 'normal'
    textWidget.delete("1.0","end")
    textWidget.insert(chars = inputString, index = "1.0") 
    textWidget['state'] = 'disabled'