class Personne:
    def __init__(self, T, P, A):
        self.taille= T
        self.poids= P
        self.age= A
    def IMC (self):
        imc_calcul= self.poids/(self.taille**2)
        return imc_calcul
    def interpretation (self, imc_calcul):
        if imc_calcul<=18.5 :
            return "Insuffisance pondérale"
        elif 18.5 < imc_calcul <= 24.9:
            return "Imc normal"
        elif imc_calcul>=30:
            return "Obésité"
aziz= Personne(1.67, 63 , 18 )
imc_de_ghita= ghita.IMC()

print(f"L'IMC de Ghita est : {imc_de_ghita:.1f}")

print(f"Interprétation : {ghita.interpretation(imc_de_ghita)}")
