from Pokemon import Pokemon

class Sol(Pokemon):

	def __init__(self, nomPoke):
		Pokemon.__init__(self, nomPoke)
		self.TypeNom = "Sol"
		self.nomPoke = nomPoke
		self.Tpvie = 10
		self.Tpatt = 15
		self.Tpdef = 55
		self.setVie(10)
		self.Typepatt = self.Tpatt + self.attaque
		self.Typedeff = self.Tpdef + self.defense