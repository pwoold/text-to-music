import pysynth as ps


''' 
Four variables
	- scale degree
	- tonal center
	- scale
	- note length
'''


#scales

scale_dict = {'13': ionian, '14': dorian}

ionian = [1,3,4,6,8,10,11]
dorian = []

#notes
notes_list = ['a','a#','b','c','c#','d','d#','e','f','f#','g','g#']


sample_string = [1,23,2,5,8,22,5,7,9,3,7]



for item in sample_string:
	if item (between 1 and 12):
		note = item
	if item (between 13 and 23):
		scale = scale_dict(item)
	if item (between 24 and 26):
		length = length_dict(item)
	if item (between 27 and 38):
		length = root_dict(item)

		#now append the (note,length)?

#test tuple of notes
test = (('c', 4), ('e', 4), ('g', 4),
		('c5', -2), ('e6', 8), ('d#6', 2))


#creates the wav file from the tuple
ps.make_wav(test, fn = "test.wav")