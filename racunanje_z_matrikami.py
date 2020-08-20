from model import Matrika, razumevanje_matrike, razumevanje_skalarja, ali_je_skalar_podan, pravilnost_vnosa_skalarja, ali_so_vrstice_enako_dolge
import model
import bottle

@bottle.get('/')
def osnovna_stran():
    return bottle.template('osnovna_stran.tpl')

@bottle.get('/sestej/')
def sestej():
    return bottle.template('seštevanje.tpl')
    
@bottle.post('/sestevanje/')
def sestevaj():
    mat1 = bottle.request.forms['matrika1']
    mat2 =  bottle.request.forms['matrika2']
    mat11 = razumevanje_matrike(mat1)
    mat22 = razumevanje_matrike(mat2)
    if mat11.ali_je_matrika_podana() == False or mat22.ali_je_matrika_podana() == False:
        return bottle.template("neustrezen.tpl")
    elif mat11.vrstice != mat22.vrstice:
        return bottle.template("neustrezen.tpl")
    elif sum(mat11.dolzine_vrstic()) != sum(mat22.dolzine_vrstic()):
        return bottle.template("neustrezen.tpl")
    else:
        rezultat = mat11 + mat22
        return bottle.template("rezultat.tpl", rezultat = rezultat)

@bottle.get('/odstej/')
def odstej():
    return bottle.template('odštevanje.tpl')

@bottle.post('/odstevanje/')
def odstevaj():
    mat1 = bottle.request.forms['matrika1']
    mat2 =  bottle.request.forms['matrika2']
    mat11 = razumevanje_matrike(mat1)
    mat22 = razumevanje_matrike(mat2)
    if mat11.ali_je_matrika_podana() == False or mat22.ali_je_matrika_podana() == False:
        return bottle.template("neustrezen.tpl")
    elif mat11.vrstice != mat22.vrstice:
        return bottle.template("neustrezen.tpl")
    elif sum(mat11.dolzine_vrstic()) != sum(mat22.dolzine_vrstic()):
        return bottle.template("neustrezen.tpl")
    else:
        rezultat = mat11 - mat22
        return bottle.template("rezultat.tpl", rezultat = rezultat)

@bottle.get('/zmnozi_matriki/')
def zmnozi_matriki():
    return bottle.template("mnozenje_matrik.tpl")

@bottle.post('/mnozenje_matrik/')
def mnozi():
    mat1 = bottle.request.forms['matrika1']
    mat2 =  bottle.request.forms['matrika2']
    mat11 = razumevanje_matrike(mat1)
    mat22 = razumevanje_matrike(mat2)
    if mat11.ali_je_matrika_podana() == False or mat22.ali_je_matrika_podana() == False:
        return bottle.template("neustrezen.tpl")
    elif ali_so_vrstice_enako_dolge(mat11.dolzine_vrstic()) == False or ali_so_vrstice_enako_dolge(mat22.dolzine_vrstic()) == False:
        return bottle.template("neustrezen.tpl")
    elif mat11.stolpci != mat22.vrstice:
        return bottle.template("neustrezen.tpl")
    else:
        rezultat = mat11 * mat22
        return bottle.template("rezultat.tpl", rezultat = rezultat)

@bottle.get('/zmnozi_skalarjem/')
def zmnozi_s_skalarjem():
    return bottle.template("mnozenje_skalar.tpl")

@bottle.post('/mnozenje_s_skalarjem/')
def zmnozi():
    mat1 = bottle.request.forms['matrika1']
    skalar = bottle.request.forms['skalar']
    mat11 = razumevanje_matrike(mat1)
    skalar11 = pravilnost_vnosa_skalarja(skalar)
    if mat11.ali_je_matrika_podana() == False or ali_je_skalar_podan(skalar11) == False:
        return bottle.template("neustrezen.tpl")
    if ali_so_vrstice_enako_dolge(mat11.dolzine_vrstic()) == False:
        return bottle.template("neustrezen.tpl")
    else:
        rezultat = mat11.zmnozek_matrika_s_skalarjem(razumevanje_skalarja(skalar))
        return bottle.template("rezultat.tpl", rezultat = rezultat)

@bottle.get('/kvadriraj/')
def kvadrat():
    return bottle.template("kvadriranje_matrike.tpl")

@bottle.post('/kvadriranje/')
def kvadriraj():
    mat1 = bottle.request.forms['matrika1']
    mat11 = razumevanje_matrike(mat1)
    if mat11.ali_je_matrika_podana() == False:
        return bottle.template("neustrezen.tpl")
    elif ali_so_vrstice_enako_dolge(mat11.dolzine_vrstic()) == False:
        return bottle.template("neustrezen.tpl")
    elif mat11.ali_je_matrika_kvadratna() == False:
        return bottle.template("neustrezen.tpl")
    else:
        rezultat = mat11.kvadrat_matrike()
        return bottle.template("rezultat.tpl", rezultat = rezultat)

@bottle.get('/transponiraj/')
def transponiranka():
    return bottle.template("transponiranje.tpl")

@bottle.post('/transponiranje/')
def transponiraj():
    mat1 = bottle.request.forms['matrika1']
    mat11 = razumevanje_matrike(mat1)
    if mat11.ali_je_matrika_podana() == False:
        return bottle.template("neustrezen.tpl")
    elif ali_so_vrstice_enako_dolge(mat11.dolzine_vrstic()) == False:
        return bottle.template("neustrezen.tpl")
    else:
        rezultat = mat11.transponiraj()
        return bottle.template("rezultat.tpl", rezultat = rezultat)

@bottle.get('/izracunaj_sled/')
def sled():
    return bottle.template("izracunaj_sled.tpl")

@bottle.post('/racunanje_sledi/')
def racunaj_sled():
    mat1 = bottle.request.forms['matrika1']
    mat11 = razumevanje_matrike(mat1)
    rezultat = mat11.sled_matrike()
    if mat11.ali_je_matrika_podana() == False:
        return bottle.template("neustrezen.tpl")
    elif ali_so_vrstice_enako_dolge(mat11.dolzine_vrstic()) == False:
        return bottle.template("neustrezen.tpl")
    elif mat11.ali_je_matrika_kvadratna() == False:
        return bottle.template("neustrezen.tpl")    
    else:
        return bottle.template("rezultat_sled.tpl", rezultat = rezultat)


bottle.run(debug= True, reloader= True)





