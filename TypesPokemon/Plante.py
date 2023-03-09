from Pokemon import Pokemon

class Plante(Pokemon):

	def __init__(self, nomPoke):
		Pokemon.__init__(self, nomPoke)
		self.TypeNom = "plante"
		self.nomPoke = nomPoke
		self.Tpvie = 25
		self.Tpatt = 10
		self.Tpdef = 35
		self.setVie(25)
		self.Typepatt = self.Tpatt + self.attaque
		self.Typedeff = self.Tpdef + self.defense