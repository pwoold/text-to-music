add_list = [2, 2, 2, 1, 2, 2]
scale_list = [1]
counter = 0

for item in add_list:

	scale_list.append(scale_list[counter]+item)
	counter = counter +1

print(scale_list)
	

# C C# D D# E F F# G G# A  A# B
# 1 2  3 4  5 6 7  8 9  10 11 12

# D D# E F F# G G# A  A# B C  C#
# 1 2  3 4 5  6 7  8  9 10 11 12