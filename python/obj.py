class Adaptor():
	color = "Black"
	size="Small"
	power ="90W"

	def __init__(self, c, s, p):
		self.color =c
		self.size = s
		self.power = p

	def print(self):
		print(self.color + ' ' + self.size + ' ' + self.power) 


	def __str__(self):
		return self.color + ' ' + self.size + ' ' + self.power


a = Adaptor("Red", "Small", "865W")
b = Adaptor("Green", "Big", "90W")


print(a)
print(b)


adapators = [a, b]
#adapators.append(Adaptor("Red", "Small", "865W"))
#adapators.append(a)
print(len(adapators))


		
		

w = [1, 2]
r= {2,3}