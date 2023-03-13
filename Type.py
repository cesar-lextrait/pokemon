from pokemon import Pokemon


class Type(Pokemon):
    def __init__(self, nom, level, defense, PV, puissance, type):
        super().__init__(nom, level, defense, PV, puissance, type)
        self.type_feu = "Feu"
        self.type_eau = "Eau"
        self.type_terre = "Terre"
        self.type_normal = "Normal"
  