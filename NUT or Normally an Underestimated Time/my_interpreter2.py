parsed_data = []
variables = []
keywords = ["append","range","print", "var", "def", "return","if","is","not","try","open","with","close","except","continue","break","in","for","while"]
symbols = ["\"","=","(",")",":","%","+","-","/","*",">","<","==",">=","<=",".","{","}","[","]","+=","-=","++","*=","/="]
bools = ["True","False"]
mode = "NONE"
def lex(data):
    toks = []
    got_tok = False
    for i in data:
        got_tok = False
        if i == "":
            continue
        try:
            toks.append({"INT":int(i)})
            got_tok = True
            continue
        except:
            for word in keywords:
                if word.lower() == i:
                    toks.append({"KEYWORD":i})
                    got_tok = True
                    break
            for symbol in symbols: 
                if symbol == i:
                    toks.append({"SYMBOL":i})
                    got_tok = True
                    break
            for boolean in bools:
                if boolean == i:
                    toks.append({"BOOL":i})
                    got_tok = True
                    break
        if not got_tok:
            toks.append({"VAR":i})
    return toks
        

def parse(data):
    global mode
    tasks = []
    curr_list = []
    curr_str = []
    varname = ""
    forloop_iter_var = ""
    forloop_var = ""
    index = 0
    strings = []
    lists = []
    mode2 = ""
    for tok in data:
        if tok == {"SYMBOL", "\""} and mode2 != "STR":
            mode2 = "STR"
            curr_str = []
            continue
        elif tok == {"SYMBOL", "\""} and mode == "STR":
            strings.append({index:" ".join(curr_str)})
            mode2 = "NONE"
            continue
        elif mode2 == "STR":
            curr_str.append(tok.values()[0])
        elif tok == {"SYMBOL", "["} and mode2 != "STR":
            mode2 = "LIST"
        elif tok == {"SYMBOL", "]"} and mode2 == "LIST":
            mode2 = "NONE"
            lists.append({index:curr_list})
            continue
        elif mode2 == "LIST":
            curr_list.append(tok.values()[0])
        index += 1
    index = 0
    for tok in data:
        dataT = tok.keys()[0]
        dataStr = tok.values()[0]
        if mode == "VARSEARCH":
            if dataT == "VAR":
                mode = "VARVALUE"
                varname = dataStr
        elif mode == "VARVALUE":
            if dataT == "SYMBOL" and dataStr == "=":
                continue
            else:
                if dataT == "SYMBOL" and dataStr == "[":
                    variables.append({varname:lists[index].values()[0]})
                elif dataT == "SYMBOL" and dataStr == "\"":
                    variables.append({varname:strings[index].values()[0]})
                else:
                    try:
                        variables.append({varname:int(dataStr)})
                    except:
                        if dataStr == "True":
                            variables.append({varname:True})
                        elif dataStr == "False":
                            variables.append({varname:False})
                        else:
                            variables.append({varname:dataStr})
                    mode = "NONE"
                    continue
        elif mode == "PRINT":
            if dataT == "INT":
                tasks.append({"PRINT":dataStr})
                mode = "NONE"
                continue
            elif dataT == "BOOL":
                tasks.append({"PRINT":dataStr})
            elif dataT == "VAR":
                for variable in variables:
                    if variable.keys()[0] == dataStr:
                        tasks.append({"PRINT":variable.values()[0]})
                        mode = "NONE"
                        continue
            elif tok == {"SYMBOL":"["}:
                tasks.append({"PRINT":lists[index].values()[0]})
                mode = "NONE"
                continue
            elif dataT == "SYMBOL" and dataStr == "\"":
                try:
                    tasks.append({"PRINT":lists[index].values()[0]})
                    mode = "NONE"
                    continue
                except:
                    pass
        elif mode == "FORLOOP_VAR1" and dataT == "VAR":
            forloop_iter_var = dataStr
            mode = "FORLOOP_VAR2"
            continue
        elif mode == "FORLOOP_VAR2" and dataT == "VAR":
            forloop_var = dataStr
            mode = "FORLOOP"
            continue
        elif mode == "FORLOOP" and tok != {"SYMBOL":"-"} and index == 0:
            mode = "NONE"
        if dataT == "KEYWORD" and dataStr == "var":
            mode = "VARSEARCH"
        elif dataT == "KEYWORD" and dataStr == "print":
            mode = "PRINT"
        #elif dataT == "KEYWORD" and dataStr == "for":
        #    mode = "FORLOOP_VAR1"
        index += 1
    task_type = ""
    for i in tasks:
        task_type = i.keys()[0]
        task_info = i.values()[0]
        if task_type == "PRINT":
            return task_info
            

with open("test.nut", "r") as f:
    for line in f:
        data = parse(lex(line[:-1].split(" ")))
        if line[-1:] == "\n":
            if data == None:
                pass
            else:
                parsed_data.append(data)
        else:
            parsed_data.append(parse(lex(line.split(" "))))
for i in parsed_data:
    print i