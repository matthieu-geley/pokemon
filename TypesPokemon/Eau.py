from Pokemon import Pokemon

class Eau(Pokemon):

	def __init__(self, nomPoke):
		Pokemon.__init__(self, nomPoke)
		self.TypeNom = "eau"
		self.nomPoke = nomPoke
		self.Tpvie = 50
		self.Tpatt = 5
		self.Tpdef = 15
		self.setVie(50)
		self.Typepatt = self.Tpatt + self.attaque
		self.Typedeff = self.Tpdef + self.defense