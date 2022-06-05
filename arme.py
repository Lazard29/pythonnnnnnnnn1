#/usr/bin/python3
# coding: utf-8


class Batiment:
    def __init__(self, portes, toilettes, bureau):
        self.portes = portes
        self.toilettes = toilettes
        self.bureau = bureau

    def avoir_porte(self):
        return self.portes

    def avoir_toilettes(self):
        return self.toilettes

    def avoir_bureau(self):
        return self.bureau


class Immeubles(Batiment):
    def __init__(self, portes, toilettes, bureau):
        super().__init__(portes, toilettes, bureau)



class Supermache(Batiment):
    def __init__(self, portes, toilettes, bureau):
        super().__init__(portes, toilettes, bureau)


    





