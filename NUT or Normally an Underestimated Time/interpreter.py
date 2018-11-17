def interpret(strings, tok, subject):
	if tok == "var":
		variables[strings[0]] = "".join(strings[1:])
		print variables
	elif tok == "run":
		func = subject.split(" ")[1]
		params = subject.split(" ")[2:]
		if func == "print":
			if "".join(params)[1:][:-1] == "".join(strings):
				print "".join(params)
			else:
				for i in variables:
					if i in params:
						print variables[i]










def parse(subject):
	if subject[:1] == "#" or subject == "\n" or subject == "	":
		pass
	else:
		tok = subject.split(" ")[0]
		strings = []
		chars = list(subject)
		state = ""
		for char in chars:
			if state == "string":
				if char == "\"":
					state = ""
					continue
				strings[len(strings)-1] += char
				continue
			if char == "\"":
				state = "string"
				strings.append("")
		interpret(strings, tok, subject)



lines = []
variables = {}
with open("test.nut", "r") as f:
	for line in f:
		lines.append(line)

for i in lines:
	parse(i)