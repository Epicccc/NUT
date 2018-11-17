tokens = []


def open_file(filename):
	data = open(filename, "r").read()
	data += "<EOF>"
	return data

def lex(filedata):
	tok = ""
	state = 0
	isexpr = 0
	string = ""
	expr = ""
	n = ""
	filedata = list(filedata)
	for char in filedata:
		tok += char
		if tok == " ":
			if state == 0:
				tok = ""
			elif state == 1:
				tok = " "
		elif tok == "\n" or tok == "<EOF>":
			if expr != "" and isexpr ==1:
				tokens.append("EXPR:"+ expr)
				expr = ""
			elif expr != "" and isexpr == 0:
				tokens.append("NUM:"+ expr)
				expr = ""
			tok = ""
		elif tok == "PRINT" or tok == "print":
			tokens.append("PRINT")
			tok = ""
		elif tok in ["1","2","3","4","5","6","7","8","9"]:
			expr += tok
			tok = ""
		elif tok == "+" or tok == "-" pr:
			isexpr = 1
			expr += tok
			tok = ""
		elif tok == "\"":
			if state == 0:
				state = 1
			elif state == 1:
				tokens.append("STRING:"+string+"\"")
				string = ""
				state = 0
				tok = ""
		elif state == 1:
			string += tok
			tok = ""

	return tokens

def parse(toks):
	i = 0
	while i < len(toks):
		if toks[i] + " " + toks[i+1][0:6] == "PRINT STRING":
			print toks[i+1][7:]
			i += 2

def run():
	data = open_file("test.nut")
	toks = lex(data)
	parse(toks)

run()