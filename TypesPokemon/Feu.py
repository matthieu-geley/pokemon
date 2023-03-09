from Pokemon import Pokemon

class Feu(Pokemon):

	def __init__(self, nomPoke):
		Pokemon.__init__(self, nomPoke)
		self.TypeNom = "feu"
		self.nomPoke = nomPoke
		self.Tpvie = 10
		self.Tpatt = 35
		self.Tpdef = 25
		self.setVie(10)
		self.Typepatt = self.Tpatt + self.attaque
		self.Typedeff = self.Tpdef + self.defense