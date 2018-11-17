def get_source(filename):
	text = []
	for line in open(filename, "r"):
		if line[-1:] == "\n":
			text.append(line[:-1])
		else:
			text.append(line)
	return text

def lex(code):
	code1 = 0
	if code[0] == "\"" or code[0] == "'" and code[-1:] == "\"" or code[-1:] == "'":
		try:
			code1 = int(code[2:][:-2])
		except:
			return code[2:][:-2]
		return code1

def parse(lexcode_strings):
	#lexcode = lexcode_strings[0]
	#strings = lexcode_strings[1]
	return lexcode_strings



def main():
	test = get_source("test.nut")
	for line in test:
		print parse(lex(line))




if __name__ == '__main__':
	main()