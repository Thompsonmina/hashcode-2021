# Write Unit Tests

class Reader():
	"""
		This is a generic input parser for hashcode, from the previous trends the input file is normally 
		n lines of data
		each line is made up of 1 or more space separated values 
	"""
	def __init__(self, filename):
		self.filename = filename
		with open(filename, "r") as file:
			self.lines = file.readlines()

	def get_first_line(self):
		""" 
			returns the the first line of the input
			which is normally a string of space separated values that will most likely dictate how the remaining
			input will look like
		"""
		return self.lines[0][:-1]

	def get_first_n_lines(self, n):
		"""
			return the first n lines as a list, sometimes the lines that will dictate what the rest of the data will look 
			like is more tham one 
		"""
		if n == 1:
			return [self.get_first_line()]
		else:
			if n > len(self.lines):
				raise ValueError(f"The total lines in input is not up to {n}")
			return [line[:-1] for line in self.lines[:n]]

	def get_n_sections(self, sectionsize, start, n):
		""" 
			return the first n sections from a starting point as a list of list of size sectionsize
			a section is a group of lines that gives all the relevant details for a primary unit of data 
		"""
		sections = []

		# start is one-indexed so need it to be zero indexed
		for i in range(start - 1, n * sectionsize + 1, sectionsize):
			try:
				# do not fret for althougn this is a nested loop its still O(n) time
				section = []
				for j in range(i, i + sectionsize):
					section.append(self.lines[j][:-1])
				sections.append(section)
			except IndexError:
				raise IndexError(f"Something may be wrong with your parameters")

		return sections


# an example
# inputreader = Reader("a_example.in")

# print(inputreader.get_first_n_lines(1))
# print(inputreader.get_first_n_lines(2))


# anotherreader = Reader("b_small.in")
# print(anotherreader.get_first_line())

# print(anotherreader.get_n_sections(sectionsize = 2, start = 2, n =3))
# print(anotherreader.get_n_sections(sectionsize = 3, start = 2, n =2))	


