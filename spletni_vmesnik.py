from model import Matrika
import bottle

#def sprejem_matrike(mat):
    ### še nevem kako se bo vpisovalo v streznik##
    #dopolnim kasnej


@bootle.get('/')
def osnovna_stran():
    bottle.template('osnovna_stran.tpl')


@bottle.get('/izbirna_stran/')
    def naslednja_stran():
        bottle.template('naslednja_stran.tpl')


@bottle.get('/sestej/')
def sestej():
    pass

@bottle.post('/sestevanje/')





@bottle.get('/odstej/')
def odstej():
    pass

@bottle.post('/odstevanje/')



@bottle.get('/transponiraj/')
def transponiraj():
    pass

@bottle.post('/transponiranje/')



@bottle.get('/zmnozi_matriki/')
def zmnozi_matriki():
    pass

@bottle.post('/mnozenje_matrik/')




@bottle.get('/kvadriraj/')
def kvadriraj():
    pass

@bottle.post('/kvadriranje/')



@bottle.get('/izracunaj_sled/')
def sled():
    pass

@bottle.post('/racunanje_sledi/')



@bottle.get('/zmnozi_skalarjem/')
def zmnozi_s_skalarjem():
    pass

@bottle.post('/mnozenje_s_skalarjem/')
   





