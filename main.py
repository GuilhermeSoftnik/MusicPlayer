from ursina import *
from ursina import curve
# from ursina.prefabs.radial_menu import RadialMenu, RadialMenuButton
app=Ursina()
window . color                 = color.black
window . borderless            = False
window . fps_counter . visible = False
window . exit_button . enabled = False
bg=Entity(model='quad',collider=None,color=color.white50,parent=camera.ui,texture='Fundo.jpg')

musicas = os.listdir(__file__+'/../Musicas')
tocando = musicas.index(random.choice(musicas))
musica  = Audio(musicas[tocando])

titulo_da_faixa=Text(musicas[tocando],parent=camera.ui,scale=3,x=-.6,y=.4)


playB     = Button('Play/Pause',scale=.23,y=-.25,x=0.00,model='circle')
voltarB   = Button('Voltar <|' ,scale=.23,y=-.25,x=-.25,model='circle')
avancarB  = Button('Avançar |>',scale=.23,y=-.25,x=0.25,model='circle')
# skipB     = Draggable(model='circle',scale=.1,x=-.25,max_value=musica.length)
aleatoriaB= Button('Aleatoria' ,scale=.23,y=-.4,x=0.00,model='diamond')
aleatoriaB.fit_to_text()

def play():
    global musica
    if musica.playing==True:
        print('A musica pausada')
        musica.pause()
    else:
        print('A musica tocando')
        musica.resume()

def avancar():
    global musica
    global tocando
    global musicas

    try:
        destroy(musica)
        print(tocando)
        tocando+=1
        musica  = Audio(musicas[tocando])
    except IndexError:
        destroy(musica)
        print(tocando)
        tocando = 1
        musica  = Audio(musicas[tocando])

def voltar():
    global musica
    global tocando
    global musicas
    
    destroy(musica)
    print(tocando)
    tocando-=1
    musica  = Audio(musicas[tocando])

def aleatoria():
    global tocando, musicas, musica
    destroy(musica)
    tocando = musicas.index(random.choice(musicas))
    musica  = Audio(musicas[tocando])

playB     .on_click = play
voltarB   .on_click = voltar
avancarB  .on_click = avancar
aleatoriaB.on_click=aleatoria


def update():
    global musicas
    global tocando
    global musica
    titulo_da_faixa.text=musicas[tocando]

    try:
        if musica.time == musica.length:
            print('Essa musica acabou... Proxima!')
            avancar()
    except:
        print('Erro, passando para a proxima musica...')
        avancar()

app.run()