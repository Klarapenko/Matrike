
class Matrika:

    def __init__(self, matrika):
        self.vrstice = len(matrika)
        self.stolpci = len(matrika[0])
        self.matrika = matrika


    def __repr__(self):
        return f' Matrika({self.matrika})'

    

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
                for j in range(self.stolpci):
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

    
    def kvadrat_matrike(self): #tuki ne rabim prevert če se stolpci in vrstice ujemajo
        transponirana = self.transponiraj()
        matrika = []
        for i in range(self.vrstice):
            vrstica_v_produktu = []
            for j in range(self.stolpci):
                vsota_produktov = 0
                for clen in zip(self.matrika[i], transponirana.matrika[j]):
                    produkt = clen[0] * clen[1]
                    vsota_produktov += produkt
                    produkt = 0
                vrstica_v_produktu.append(vsota_produktov)
            matrika.append(vrstica_v_produktu)
        return Matrika(matrika)

    def ali_je_matrika_kvadratna(self):
        return self.vrstice == self.stolpci

    def sled_matrike(self):
        if self.ali_je_matrika_kvadratna() == True:
            sled = 0
            A = self.matrika
            for i in range(self.vrstice):
                sled += A[i][i]
        return sled

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



##================================================================##
##================================================================##
p= Matrika([[1,2,3,4], [3,4,5,6],[4,6,7,8], [2,3,4,5], [1,4,6,2]])
q = Matrika([[1,2,3,4],[2,3,4,5], [1,4,7,9], [2,3,4,5]])
print(p)
c = p*q
print(c)

d = p.kvadrat_matrike()   
print(d)

e = q.sled_matrike()
print(e)

f = p.zmnozek_matrika_s_skalarjem(3)
print(f)
