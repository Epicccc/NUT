import re

def get_source(filename):
	return open(filename, "r").read()

def lex(code):

	strings = re.findall('\"(.*)\"', code)
	code_nostr = code
	for i in strings:
		code_nostr = code_nostr.replace("\""+i+"\"","|STRING|")


	return (code_nostr.split(" "), strings)


	




def parse(lexcode_strings):
	lexcode = lexcode_strings[0]
	strings = lexcode_strings[1]

	current = ""
	mode = ""
	for i in lexcode:
		if i == "|STRING|":
			continue
		current = i.lower()
		current = list(current)
		try:
			current.remove(",")
		except:
			continue
		current = "".join(current)
		if current == "display":
			mode = "print"
		if i == "|STRING|" and mode == "print":
			return strings
	return lexcode




def main():
	print parse(lex(get_source("test.nut")))




if __name__ == '__main__':
	main()