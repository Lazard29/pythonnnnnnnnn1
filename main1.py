#/usr/bin/python3
# coding: utf-8

class joueur:
    def __init__(self, pseudo, mail,nom,prenom, vie, mort):
        self.pseudo = pseudo
        self.mail = mail
        self.nom = nom 
        self.prenom = prenom
        self.vie = 12
        self.mort = 100
        


        print("welcome to the player", pseudo, "ton mail est", mail, "ton nom est", nom)


    def avoir_pseudo(self):
        return self.pseudo

    def avoir_mail(self):
        return self.mail

    def avoir_nom(self):
        return self.nom

    def avoir_prenom(self):
        return self.prenom

    def dommage(self, dommage):
        self.vie -= dommage



personne1 = joueur("aldo", "ad.iiiii5@gmail.com", "jourdain", "arno")
personne2 = joueur("phiol", "iiiiiiooo@hotmail.fr", "leguen", "marc")


# ----------------------------------------------------------------------------------


class guerrier(joueur):
    def __init__(self, pseudo, mail,nom,prenom, vie, mort):

        super().__init__(pseudo, mail,nom,prenom, vie, mort)

        self.armor = 3


        print("welcome to the player", pseudo, "ton mail est", mail, "ton nom est", nom)



    def avoir_prenom(self):
        return self.prenom



    def dommage(self, dommage):
        if self.mort > 0:
            self.mort -= 1
            dommage = 0
        super().dommage(dommage)




personne1 = joueur("aldo", "ad.iiiii5@gmail.com", "jourdain", "arno")
personne2 = joueur("phiol", "iiiiiiooo@hotmail.fr", "leguen", "marc")



if issubclass (guerrier,joueur):
    print("le guerrier est bien un sous domaine de la classe parent f {joueur}")