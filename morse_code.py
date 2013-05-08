import fileinput
import sys

dict_char = {}
words = {}
morris_chars = [] #key = English ASCII | value = morse code

def LookupFirst(first):
	for k,v in words.iteritems():
		if first == v:
			return k


def ConvertMorse(line):
	print 'ConvertMorse got, ', line #make sure it is on right line
	line = file.next()
	for line in file: #read each line
		if line.startswith('*'): #check for delimiter
			print 'we out' #end of file. we out, we gone. peace.
			file.close()
			sys.exit()

		for k,v in words.iteritems():
			if v == line:
				print k
			else:
				for char in line:
					if char == ' ':
					#line.split()
					#print 'line after split', line.split()
						first, second = line.split()

#						print 'first', first
#						print 'second', second
					
#						print 'words.iteritems() ', words.iteritems()
						
						print LookupFirst(first)
						
						for k,v in words.iteritems():
							if v == second:
			 					print  k
								break

def ConvertWords(line):
	if line.startswith('*'): #check we don't hit next section of file containing morse code
		print 'hit the last *, time to convert morse words!' #hit the delimiter
		ConvertMorse(line) #convert morse words to English
	for char in line: #convert each character in each line
		if char == ' ' or char.isspace():#dont convert spaces, no point
			break
		else:
			morris_chars.append(dict_char[char]) #add char to end of morris_code list
	words[line[:-1]] = "".join(morris_chars) #-1 for newline char, add English ASCII to morris_chars list

	del morris_chars[0:len(morris_chars)] #dispose of newline char
	line = file.next() #go to next line
	ConvertWords(line) #recursive call, same function for next line :)
	

with open('input.txt') as file:
    for line in file: #read text file line by line
		if line.startswith('*'): #check if line equals ' * ' this is the delimiter
			line = file.next() #read line after *
			ConvertWords(line)	#convert English words to ASCII and save in list	
			break
		(key,value) = line.split() #split column of English ASCII and Morse code conversion
		dict_char[(key)] = value #create dict: key=English ASCII | value=morse code
file.close() #close file
