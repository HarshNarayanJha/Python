




# Sole Objective(s):

# >>> To stress the brains of my careless friends (who are currently unaware that they are in 12th now)
# >>> To test their basic knowledge of python that they tasted in class 11th...
# >>> and maybe to scare them a little bit too (no!, kidding...)


# A dict with all sorts of datatypes and expressions and methods as keys and values (DISASTER Looming!!!)
d = {
	1: 'a',
	'2': '95',
	'[3]': (67+45)*2,
	(4,): None,
	None: (4,),
	(5, 4, 3): {
		'1': [1, [], {1: 99}, [3], (4,)],
		2: [1, "[], {2: 98},[4,5], 4"],
	},
	'<>': "[56, 67, 75, 85]".replace(', ', ':'),

	(): "ThIs iS PythON".swapcase(),
	123: "ThIs iS PythON".swapcase().endswith('oN'),
	'val': "butterfly".upper().count('T', 3, 4),
	456: '1'.isdigit() and 'a'.isalpha() and 'a12b'.isalnum() or ''.isdecimal(),
	'ABCD'.lower(): "AbCD".split('b'),
}

d['[3]'] /= 2
d['abcd'].extend([1, 2, 3, 4, 5])
d['abcd'].insert(4, 5)

#Q1: Find the output (and type) (or error, if any) of:
#(a) >>> d[1].upper()
#(b) >>> d[()]
#(c) >>> d[3]
#(d) >>> d['[3]'] + 34
#(e) >>> d["ABCD"]
#(f) >>> d["abcd"]
#(g) >>> d["abcd"][1][0][0][0][0]
#(h) >>> d["abcd"][7]
#(i) >>> d[(4)]
#(j) >>> d[(4,)]
#(k) >>> d[123] or d[456]
#(l) >>> d.keys()

#Q2: From d, fetch:
#(a) >>> 95 as int
#(b) >>> []
#(c) >>> 99
#(d) >>> [3]
#(e) >>> 75
#(f) >>> 'python' (in LOWERCASE!)
#(g) >>> 'CD' (in uppercase!)

# Q last (DIASATER Looming): what is the output of
# >>> str(d[(5, 4, 3)['1'][4][0]]) + str(d[(5, 4, 3)][2][0]) + str(d['abcd'][0]) + str(d['abcd'][6])