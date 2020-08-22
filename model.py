class Matrika:

    def __init__(self, matrika):
        self.vrstice = len(matrika)
        self.stolpci = len(matrika[0])
        self.matrika = matrika

    def __repr__(self):
        return f' {self.matrika}'

    def __add__(self, other):
        if self.stolpci == other.stolpci:
            if self.vrstice == other.vrstice:
                vsota_matrik = []
                for i in range(self.vrstice):
                    vrstica_nove = []
                    for j in range(self.stolpci):
                        vrstica_nove.append(self.matrika[i][j] + other.matrika[i][j])
                    vsota_matrik.append(vrstica_nove)
                return Matrika(vsota_matrik)
        return print("Matriki nimata enakih dimenzij")

    def __sub__(self, other):
        if self.stolpci == other.stolpci:
            if self.vrstice == other.vrstice:
                razlika_matrik = []
                for i in range(self.vrstice):
                    vrstica_nove = []
                    for j in range(self.stolpci):
                        vrstica_nove.append(self.matrika[i][j] - other.matrika[i][j])
                    razlika_matrik.append(vrstica_nove)
                return Matrika(razlika_matrik)
        return print("Matriki nimata enakih dimenzij")
                        
    def transponiraj(self):
        matrika = []
        A = self.matrika
        for i in range(len(A[0])):
            vrstica = []
            for j in range(len(A)):
                vrstica.append(A[j][i])
            matrika.append(vrstica)            
        return Matrika(matrika)

    def __mul__(self, other):
        if self.stolpci == other.vrstice:
            sez1 = Matrika(self.matrika).v_navadno()
            sez2 = Matrika(other.matrika).v_navadno()
            skupek_matrik =[]
            for i in range(len(sez2)):
                za_sestet_stolpci = []
                for j in range(len(sez1)):
                    za_sestet_stolpci.append(mnozenje_stevilo_seznam(sez1[j],sez2[i][j]))
                skupek_matrik.append(za_sestet_stolpci)
            return Matrika(Matrika(sesteva_stolpce(skupek_matrik)).v_navadno())
        return print("Matriki nimata ustreznih dimenzij za množenje")
  
    def kvadrat_matrike(self):
        if self.ali_je_matrika_kvadratna() == True:
            transponirana = self.transponiraj()
            produkt_matrik = []
            for i in range(self.vrstice):
                vrstica_v_produktu = []
                for j in range(self.stolpci):
                    vsota_produktov = 0
                    for clen in zip(self.matrika[i], transponirana.matrika[j]):
                        produkt = clen[0] * clen[1]
                        vsota_produktov += produkt 
                        produkt = 0
                    vrstica_v_produktu.append(vsota_produktov)
                produkt_matrik.append(vrstica_v_produktu)
            return Matrika(produkt_matrik)
        
    def ali_je_matrika_kvadratna(self):
        return self.vrstice == self.stolpci

    def sled_matrike(self):
        if self.ali_je_matrika_kvadratna() == True:
            sled = 0
            A = self.matrika
            for i in range(self.vrstice):
                sled += A[i][i]
            return sled
        else:
            return print("Matrika nima sledi, saj ni kvadratna")

    def zmnozek_matrika_s_skalarjem(self, s = 1):
        matrika_pomnozena = []
        A = self.matrika
        for i in range(self.vrstice):
            vrstica = []
            for j in range(self.stolpci):
                zmnozek = s * A[i][j]
                vrstica.append(zmnozek)
                zmnozek = 0
            matrika_pomnozena.append(vrstica)
        return Matrika(matrika_pomnozena)

    def ali_je_matrika_podana(self):
        if self.matrika == [[]]:
            return False
        else: 
            return True

    def dolzine_vrstic(self):
        dolzine = []
        A = self.matrika
        for vrstica in self.matrika:
            dolzina = len(vrstica)
            dolzine.append(dolzina)
        return dolzine
    
    def v_navadno(self):
        """Sestavi matriko seznama vrstic v 
        seznam stolpcev in obratno  """
        seznam_vrstic = []
        for i in range(self.stolpci): # gre po vrsticah
            vrstica = []
            for j in range(self.vrstice): # gre po stolpcih
                vrstica.append(self.matrika[j][i])
            seznam_vrstic.append(vrstica)
        return seznam_vrstic


def mnozenje_stevilo_seznam(sez, n):
    nov_sez = []
    for i in range(len(sez)):
        novo_st = sez[i] * n
        nov_sez.append(novo_st)
    return nov_sez

def vsota_stolpcev(sez1, sez2):
    """sešteje seznama"""
    nov_stolpec = []
    for i in range(len(sez1)):
        vsota = 0
        vsota += sez1[i] + sez2[i]
        nov_stolpec.append(vsota)
    return nov_stolpec

def sesteva_stolpce(seznam_seznamov_stolpcev):
    """sešteje vse 'stolpce' v posameznem podseznamu """
    matrika_stolpcev = []
    for i in range(len(seznam_seznamov_stolpcev)):
        sez = seznam_seznamov_stolpcev[i]
        stolpec11 = sez[0]
        while len(sez) > 1:
            i = 0
            stolpec22 = sez[1]
            stolpec11 = vsota_stolpcev(stolpec11, stolpec22)
            sez = sez[i+1:]
        matrika_stolpcev.append(stolpec11)
    return matrika_stolpcev

def razumevanje_matrike(matrika):
    matrika = matrika.split(",") 
    matrika1 = []
    for vrstica in matrika:
        vrstica = vrstica.split()
        vrstica1 = []
        for znak in vrstica:
            vrstica1.append(float(znak))
        matrika1.append(vrstica1)
    return Matrika(matrika1)

def razumevanje_skalarja(skalar):
    return(float(skalar))

def pravilnost_vnosa_skalarja(skalar):
    """Zapise skalar prejet iz vnosa v
    obliko za uporabo v spodnjih definicijah"""
    return skalar

def ali_je_skalar_podan(skalar):
    if skalar == '':
        return False
    else:
        return True

def ali_so_vrstice_enako_dolge(sez):
    """ Definicija sprejme seznam, katerega 
    elementi so dolzine vsake vrstice """
    for element in sez:
        if len(sez) == 0:
            return False
        elif len(sez) == 1:
            return True
        elif sez[0] != sez[1]:
            return False
        else:
            return ali_so_vrstice_enako_dolge(sez[1:])
    return False

