#-----------------------------------------------------------------------------------------#
# Text to Music 

# Framework:
# Read in a string of characters
# Every four spaces causes the root to change randomly
# Vowels cause the scale to shift
# The scale degree added (1-7) depends on the letter
#
# bc -   1
# df -   2
# ghj -  3
# klm -  4
# npq -  5
# rst -  6
# vwxz - 7

#-----------------------------------------------------------------------------------------#
import pysynth as ps
import numpy as np


# Defines scales relative to a root note being 1, using the 12 chromatic notes
# For example if the root is C, then C:1, E:3, etc...
ionian = [1,3,5,6,8,10,12]
dorian = [1,3,4,6,8,10,11]
phrygian = [1,2,4,6,8,9,11]
lydian = [1,3,5,7,8,10,12]
mixolydian = [1,3,5,6,8,10,11]
aeolian = [1,3,4,6,8,9,11]

#Vowels define scale changes
scale_dict = {'a': ionian, 'e': dorian,'i': phrygian, 'o': lydian,'u': mixolydian, 'y': aeolian}

#notes
notes_list = np.array(['a','a#','b','c','c#','d','d#','e','f','f#','g','g#'])

#generates lists for the 12 chromatic scales and stores it in [keys]
keys=[]
for i in range(0,12):
	temp=(np.roll(notes_list,i))
	keys.append(temp.tolist())

#Reverse the list
keys = keys [::-1]

def letter_to_degree(letter):
	if letter in "bc":
		degree = 0
	elif letter in "df":
		degree = 1
	elif letter in "ghj":
		degree = 2
	elif letter in "klm":
		degree = 3
	elif letter in "npq":
		degree = 4
	elif letter in "rst":
		degree = 5
	elif letter in "vwxz":
		degree = 6
	return degree

def changeKey(counter):
	new_key= keys[counter]
	return new_key

def changeScale(letter):
	return scale_dict[letter]

def addNote(letter, current_scale, current_key):
	# subtract 1 bc array indices start at 0
	this_scale = [x-1 for x in current_scale]

	val = this_scale[letter_to_degree(letter)]

	note_letter = current_key[val] 
	note = note_letter + '3'
	return note

#This loop builds the note string from the input string

test_string = '''Shall I compare thee to a summer's day?
Thou art more lovely and more temperate:
Rough winds do shake the darling buds of May,
And summer's lease hath all too short a date:
Sometime too hot the eye of heaven shines,
And often is his gold complexion dimmed,
And every fair from fair sometime declines,
By chance, or nature's changing course untrimmed:
But thy eternal summer shall not fade,
Nor lose possession of that fair thou ow'st,
Nor shall death brag thou wander'st in his shade,
When in eternal lines to time thou grow'st,
   So long as men can breathe, or eyes can see,
   So long lives this, and this gives life to thee.'''

note_list = []
the_scale = ionian
the_key = keys[0]
space_counter = 0
key_counter = 0
for char in test_string.lower():

	#change key randomly if spaces is > 4
	if space_counter > 4:
		space_counter = 0
		key_counter = key_counter +1
		if key_counter == 11:
			key_counter = 0
		the_key = changeKey(key_counter)
	#keeps track of spaces 
	if char == ' ':
		space_counter = space_counter + 1
	#change scale if a vowel passes through
	if char in 'aeiouy':
		the_scale = changeScale(char)
	#adds notes if neither vowel nor space
	if char not in 'aeiouy ' and char in 'abcdefghijklmnopqrstuvwxyz':
		note_list.append(addNote(char,the_scale,the_key))


tuple_list = []
for note in note_list:
	tuple_list.append((note,8))


#test tuple of notes
test2 = tuple(tuple_list)


#creates the wav file from the tuple
ps.make_wav(test2, fn = "shake.wav")



