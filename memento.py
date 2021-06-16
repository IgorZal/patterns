class Git:

	def __init__(self,something):
		self.something=something

	def checkout(self):
		return self.something

class Redactor:

	def __init__(self):
		self.something=''

	def write(self,text):
		self.something+=text

	def show_text(self):
		return self.something

	def save(self):
		return Git(self.something)

	def restore(self,memento):
		self.something=memento.checkout()


word=Redactor()
word.write('random fact...')
save=word.save()
word.write('travel to the month is 3 days transfer')
word.restore(save)
print(word.show_text())
