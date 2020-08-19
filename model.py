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
            transponirana = other.transponiraj()
            produkt_matrik = []
            for i in range(self.vrstice):
                vrstica_v_produktu = []
                for j in range(other.stolpci):
                    vsota_produktov = 0
                    for clen in zip(self.matrika[i], transponirana.matrika[j]):
                        produkt = clen[0] * clen[1]
                        vsota_produktov += produkt 
                        produkt = 0
                    vrstica_v_produktu.append(vsota_produktov)
                produkt_matrik.append(vrstica_v_produktu)
            return Matrika(produkt_matrik)
        else:
            print("Matriki nimata ustreznih dimenzij za množenje")

    
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






def razumevanje_matrike(matrika):
    matrika = matrika.split(",") #razdelim niz na dele v seznam pri vsakem znaku za vejico
    matrika1 = []
    for vrstica in matrika:
        vrstica = vrstica.split()
        vrstica1 = []
        for x in vrstica: #gledam po en clen niza 
            vrstica1.append(float(x)) #niz pretvorim v stevilo in dodam v seznam
        matrika1.append(vrstica1)
    return Matrika(matrika1)


def razumevanje_skalarja(skalar):
    return(float(skalar))

def pravilnost_vnosa_skalarja(skalar):
    """zapise skalar prejet iz vnosa v
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












##================================================================##
##================================================================##
##=================PREVERIM DELOVANJE METOD=======================##
p= Matrika([[1,2,3,4], [3,4,5,6],[4,6,7,8], [2,3,4,5], [1,4,6,2]])
q = Matrika([[1,2,3,4],[2,3,4,5], [1,4,7,9], [2,3,4,5]])
z = Matrika([[1,2,3,4],[2,3,4,5], [1,4,7,9], [2,3,4,5], [1,2,3,4]])
print(p)

c = p*q
print(c) #produkt dela

d = p.kvadrat_matrike()   
print(d) #kvadrat dela

e = q.sled_matrike()
print(e) #sled dela

f = p.zmnozek_matrika_s_skalarjem(3)
print(f) #dela

l = p + z
print(l) #vsota dela

a = p - z
print(a) #razlika dela

g = p.transponiraj()
print(g) #transponiranje dela
