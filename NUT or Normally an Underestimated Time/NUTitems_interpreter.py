import pickle


lexed_data = []
parsed_data = []
possible_types = ["TRAIT","ITEM","INSTANCE"]
possible_info_types = ["TRAIT INFO","ITEM INFO","INSTANCE INFO"]
mode = ""
line_num = 1

def lexer(data):
	global mode
	if data[:1] == "#":
		return {"COMMENT":data[1:-1]}
	elif data[0] == "\t":
		return {mode+" INFO":data[1:-1]}
	elif data.split(" ")[0] == "trait":
		mode = "TRAIT"
		return {"TRAIT":data.split(" ")[1][:-2]}
	elif data.split(" ")[0] == "item":
		mode = "ITEM"
		return {"ITEM":data.split(" ")[1][:-2]}
	elif data.split(" ")[0] == "instance":
		mode = "INSTANCE"
		return {"INSTANCE":data.split(" ")[1][:-2]}


def parser(lexeddata):
	global parsed_data
	data_type = "".join(lexeddata.keys())
	value = "".join(lexeddata.values())
	if data_type == "COMMENT":
		return None
	elif data_type in possible_types:
		return {data_type:[value]}
	elif data_type in possible_info_types:
		if parsed_data[-1] != None:
			parsed_data[-1].values()[0].append(value)
		else:
			pass
		

def export(filname, code):
	outfile = open(filname, 'wb')
	pickle.dump(code, outfile)
	outfile.close()


			
def main():
	global line_num
	for line in open("NUTitems_test.nuti", "r"):
		if line[-1:] != "\n":
			lexed_data.append(lexer(line+"\n"))
		else:
			lexed_data.append(lexer(line))
		line_num += 1
	for item in lexed_data:
		parsed = parser(item)
		if parsed != None:
			parsed_data.append(parsed)
	parsed_data2 = []
	for item in parsed_data:
		parsed_data2.append({item.keys()[0]:{item.values()[0][0]:item.values()[0][1:]}})
	for item in parsed_data2:
		print item
	export("export.pickle", parsed_data2)


if __name__ == '__main__':
	main()