from model import Matrika, razumevanje_matrike, razumevanje_skalarja
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
    rezultat = razumevanje_matrike(mat1) + razumevanje_matrike(mat2)
    return bottle.template("rezultat.tpl", rezultat = rezultat)



@bottle.get('/odstej/')
def odstej():
    return bottle.template('odštevanje.tpl')

@bottle.post('/odstevanje/')
def odstevaj():
    mat1 = bottle.request.forms['matrika1']
    mat2 =  bottle.request.forms['matrika2']
    rezultat = razumevanje_matrike(mat1) - razumevanje_matrike(mat2)
    return bottle.template("rezultat.tpl", rezultat = rezultat)

@bottle.get('/zmnozi_matriki/')
def zmnozi_matriki():
    return bottle.template("mnozenje_matrik.tpl")

@bottle.post('/mnozenje_matrik/')
def mnozi():
    mat1 = bottle.request.forms['matrika1']
    mat2 =  bottle.request.forms['matrika2']
    rezultat = razumevanje_matrike(mat1) * razumevanje_matrike(mat2)
    return bottle.template("rezultat.tpl",rezultat = rezultat)



@bottle.get('/zmnozi_skalarjem/')
def zmnozi_s_skalarjem():
    return bottle.template("mnozenje_skalar.tpl")

@bottle.post('/mnozenje_s_skalarjem/')
def zmnozi():
    mat1 = bottle.request.forms['matrika1']
    skalar = bottle.request.forms['skalar']
    rezultat = razumevanje_matrike(mat1).zmnozek_matrika_s_skalarjem(razumevanje_skalarja(skalar))
    return bottle.template("rezultat.tpl", rezultat = rezultat)





@bottle.get('/kvadriraj/')
def kvadrat():
    return bottle.template("kvadriranje_matrike.tpl")

@bottle.post('/kvadriranje/')
def kvadriraj():
    mat1 = bottle.request.forms['matrika1']
    rezultat = razumevanje_matrike(mat1).kvadrat_matrike()
    return bottle.template("rezultat.tpl", rezultat = rezultat)




@bottle.get('/transponiraj/')
def transponiranka():
    return bottle.template("transponiranje.tpl")

@bottle.post('/transponiranje/')
def transponiraj():
    mat1 = bottle.request.forms['matrika1']
    rezultat = razumevanje_matrike(mat1).transponiraj()
    return bottle.template("rezultat.tpl", rezultat = rezultat)


@bottle.get('/izracunaj_sled/')
def sled():
    return bottle.template("izracunaj_sled.tpl")

@bottle.post('/racunanje_sledi/')
def racunaj_sled():
    mat1 = bottle.request.forms['matrika1']
    rezultat = razumevanje_matrike(mat1).sled_matrike()
    return bottle.template("rezultat_sled.tpl", rezultat = rezultat)


   

bottle.run(debug= True, reloader= True)





