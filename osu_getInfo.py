import sys

def search(input):
	with open(sys.argv[1], 'r') as my_file:
		lines = my_file.readlines()
		line_iter = iter(lines)
		find = False
		target = "[" + input + "]"
		for line in line_iter:
			if target in line:
				find = True
				break
		if (find):
			for line in line_iter:
				if len(line.strip()) != 0:
					print( line)
				else: 
					break			
		else:
			print("No such infomation in file")

def searchSublevel(x, y):
	with open(sys.argv[1], 'r') as my_file:
		lines = my_file.readlines()
		line_iter = iter(lines)
		find = False
		target = "[" + x + "]"
		for line in line_iter:
			if target in line:
				find = True
				break
		if (find):
			for line in line_iter:
				if len(line.strip()) != 0:
					if y in line:
						l, r = line.split(':')
						print( r)
				else: 
					"No such infomation in " + x
					break			
		else:
			print( "No such infomation in file")


if __name__ == "__main__":
	if len(sys.argv) != 2:
		print( "usage: inputfile outputfile")
		exit(-1)
	print( "please enter the search information using the following format:")
	print( "e.g. General")
	print( "e.g. General-AudioFilename")
	x =  raw_input().split('-')
	if len(x) == 1:
		search(x[0])
	elif len(x) == 2:
		searchSublevel(x[0], x[1])

