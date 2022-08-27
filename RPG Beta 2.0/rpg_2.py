import pygame as pg

from madeira import Madeira
from items import Menu
from items import Craft
from items import mochila
from items import Enchada
from items import Picareta
from utilitarios import exit1
from Banana import Banana
from ferro import ferro

pg.init()

janela = pg.display.set_mode([1280, 840])
pg.display.set_caption('Rpg')

drawgroup_world1 = pg.sprite.Group()
drawgroup_mochila = pg.sprite.Group()
drawgroup_craft = pg.sprite.Group()
font = pg.font.Font('freesansbold.ttf', 32)

picareta_sprite = pg.image.load('data/Picareta.png')
enchada_sprite = pg.image.load('data/enchada.png')
machado_sprite = pg.image.load('data/Machado.png')
loadingp = pg.transform.scale(picareta_sprite, [30, 30])

loadinge = pg.transform.scale(enchada_sprite, [33, 33])

loadingm = pg.transform.scale(machado_sprite, [30, 30])


# background
bg = pg.image.load('data/bg2.png')
bg_ = pg.transform.scale(bg, ([1280, 840]))

#menu
menu = Menu(drawgroup_world1)

# inventario
mochila = mochila(drawgroup_world1)
back = exit1(drawgroup_mochila, drawgroup_craft)

# craft
craft = Craft(drawgroup_world1)
enchada = Enchada(drawgroup_craft)
picareta = Picareta(drawgroup_craft)
# mineração
ferro = ferro(drawgroup_world1)
ferros_value = 0
picareta_num = 0
ym = 650


tempo = 0
def minerar():

    x = 605
    janela.blit(loadingp, (x, ym))
    pg.display.update()
    pg.time.wait(tempo)
    x = 640
    janela.blit(loadingp, (x, ym))
    pg.display.update()
    pg.time.wait(tempo)
    x = 675
    janela.blit(loadingp, (x, ym))


xpM = 0
# Fazenda
yf = 630
def farmar():

    x = 960
    janela.blit(loadinge, (x, yf))
    pg.display.update()
    pg.time.wait(tempo)
    x = 995
    janela.blit(loadinge, (x, yf))
    pg.display.update()
    pg.time.wait(tempo)
    x = 1030
    janela.blit(loadinge, (x, yf))
enchada_num = 0
banana = Banana(drawgroup_world1)
bananas_value = 0

xpF = 0
# madeira
xpMa = 0
madeira_value = 0
def madeirar():

    x = 200
    janela.blit(loadingm, (x, ym))
    pg.display.update()
    pg.time.wait(tempo)
    x = 235
    janela.blit(loadingm,(x, ym))
    pg.display.update()
    pg.time.wait(tempo)
    x = 270
    janela.blit(loadingm, (x, ym))



madeira = Madeira(drawgroup_world1)
# Main
handled = False
gameLoop = True

if __name__ == "__main__":
    while gameLoop:
        pg.time.wait(50)

        # Textos
        show_ferro = font.render('Ferros:' + str(ferros_value), True, [0, 0, 0])
        show_bananas = font.render('Bananas:' + str(bananas_value), True, [0, 0, 0])
        show_enchadas = font.render('Enchadas:' + str(enchada_num),True, [0,0,0])
        show_picaretas = font.render('picaretas:' + str(picareta_num), True, [0, 0, 0])
        show_madeiras = font.render('madeiras:' + str(madeira_value), True, [0, 0, 0])


        not_enchada = font.render('Voce não possui uma enchada', True, [0, 0, 0])

        #   Jogoo
        for event in pg.event.get():
            if event.type == pg.QUIT:
                gameLoop = False
            if event.type == pg.MOUSEBUTTONDOWN and ferro.rect.collidepoint(pg.mouse.get_pos()) and not handled:
                pg.time.wait(50)

                if xpM >= 2000:
                    tempo = 430
                    tempo -= picareta_num * 25
                    if tempo < 50:
                        tempo = 50
                    minerar()

                    ferros_value += 3
                    xpM += 100
                    lv4 = font.render('+4 Ferros ' + str(xpM) + '/xxx', True, [0, 0, 0])

                    janela.blit(lv4, (10, 40))
                    pg.display.update()
                    pg.time.wait(430)
                    print(tempo)
                elif xpM >= 400:
                    tempo = 800
                    tempo -= picareta_num * 25
                    if tempo < 0:
                        tempo = 50
                    minerar()

                    ferros_value += 3
                    xpM += 100
                    lv3 = font.render('+3 Ferros ' + str(xpM) + '/2000', True, [0, 0, 0])

                    janela.blit(lv3, (10, 40))
                    pg.display.update()
                    pg.time.wait(800)


                elif xpM >= 100:
                    tempo = 1000
                    tempo -= picareta_num * 25
                    minerar()

                    xpM += 70
                    ferros_value += 2
                    lv2 = font.render('+2 Ferros ' + str(xpM) + '/400', True, [0, 0, 0])

                    janela.blit(lv2, (10, 40))
                    pg.display.update()
                    pg.time.wait(1000)


                else:
                    tempo = 1300
                    tempo -= picareta_num * 25
                    minerar()

                    ferros_value += 1
                    xpM += 50
                    lv1 = font.render('+1 Ferro ' + str(xpM) + '/100', True, [0, 0, 0])
                    janela.blit(lv1, (10, 40))
                    pg.display.update()
                    pg.time.wait(1300)


                pg.event.clear()

            elif event.type == pg.MOUSEBUTTONDOWN and banana.rect.collidepoint(
                    pg.mouse.get_pos()) and enchada_num >= 1 and not handled:

                if xpF >= 2000:
                    tempo = 400
                    farmar()

                    bananas_value += 4
                    xpF += 100
                    lv4 = font.render('+4 Bananas ' + str(xpF) + '/xxx', True, [0, 0, 0])

                    janela.blit(lv4, (10, 40))
                    pg.display.update()
                    pg.time.wait(530)

                elif xpF >= 400:
                    tempo = 800
                    farmar()

                    bananas_value += 3
                    xpF += 100
                    lv3 = font.render('+3 Bananas ' + str(xpF) + '/2000', True, [0, 0, 0])

                    janela.blit(lv3, (10, 40))
                    pg.display.update()
                    pg.time.wait(800)

                elif xpF >= 100:
                    tempo = 1000
                    farmar()

                    xpF += 70
                    bananas_value += 2
                    lv2 = font.render('+2 Bananas ' + str(xpF) + '/400', True, [0, 0, 0])

                    janela.blit(lv2, (10, 40))
                    pg.display.update()
                    pg.time.wait(1000)

                else:
                    tempo = 1300
                    farmar()

                    bananas_value += 1
                    xpF += 50
                    lv1 = font.render('+1 Bananas ' + str(xpF) + '/100', True, [0, 0, 0])
                    janela.blit(lv1, (10, 40))
                    pg.display.update()
                    pg.time.wait(1300)

                pg.event.clear()

            elif event.type == pg.MOUSEBUTTONDOWN and banana.rect.collidepoint(
                    pg.mouse.get_pos()) and enchada_num < 1 and not handled:
                janela.blit(not_enchada, (10, 40))
                pg.display.update()
                pg.time.wait(1000)

            elif event.type == pg.MOUSEBUTTONDOWN and madeira.rect.collidepoint(pg.mouse.get_pos()):
                if xpMa >= 2000:
                    tempo = 400
                    madeirar()
                    xpMa += 100
                    madeira_value += 4

                    lv4 = font.render('+4 madeiras ' + str(xpMa) + '/xxx', True, [0, 0, 0])

                    janela.blit(lv4, (10, 40))
                    pg.display.update()
                    pg.time.wait(530)
                elif xpMa >= 400:
                    tempo = 800
                    madeirar()
                    xpMa += 100
                    madeira_value += 3

                    lv3 = font.render('+3 madeiras ' + str(xpMa) + '/2000', True, [0, 0, 0])

                    janela.blit(lv3, (10, 40))
                    pg.display.update()
                    pg.time.wait(800)

                elif xpMa >= 100:
                    tempo = 1000
                    madeirar()

                    xpMa += 70
                    madeira_value += 2
                    lv2 = font.render('+2 madeiras ' + str(xpMa) + '/400', True, [0, 0, 0])

                    janela.blit(lv2, (10, 40))
                    pg.display.update()
                    pg.time.wait(1000)

                else:
                    tempo = 1300
                    madeirar()

                    madeira_value += 1
                    xpMa += 50
                    lv1 = font.render('+1 Madeira ' + str(xpMa) + '/100', True, [0, 0, 0])
                    janela.blit(lv1, (10, 40))
                    pg.display.update()
                    pg.time.wait(1300)

                pg.event.clear()


            elif event.type == pg.MOUSEBUTTONDOWN and mochila.rect.collidepoint(pg.mouse.get_pos()) and not handled:
                mochila_open = True
                while mochila_open:
                    for event in pg.event.get():
                        if event.type == pg.QUIT:
                            mochila_open = False
                            gameLoop = False
                        if event.type == pg.MOUSEBUTTONDOWN and back.rect.collidepoint(
                                pg.mouse.get_pos()) and not handled:
                            mochila_open = False
                    janela.fill([255, 255, 255])
                    janela.blit(show_ferro, (60, 80))
                    janela.blit(show_bananas, (60, 120))
                    janela.blit(show_madeiras, (60, 160))
                    janela.blit(show_enchadas, (60, 200))
                    janela.blit(show_picaretas, (60, 240))

                    drawgroup_mochila.draw(janela)

                    pg.display.update()
            elif event.type == pg.MOUSEBUTTONDOWN and craft.rect.collidepoint(pg.mouse.get_pos()) and not handled:
                craft_open = True
                while craft_open:
                    lore_enchada = font.render(str(ferros_value) + ' /10', True, [0, 0, 0])
                    lore_picareta = font.render(str(ferros_value) + ' /10', True, [0, 0, 0])
                    for event in pg.event.get():
                        if event.type == pg.QUIT:
                            craft_open = False
                            gameLoop = False
                        if event.type == pg.MOUSEBUTTONDOWN and back.rect.collidepoint(
                                pg.mouse.get_pos()) and not handled:
                            craft_open = False
                        if event.type == pg.MOUSEBUTTONDOWN and enchada.rect.collidepoint(
                                pg.mouse.get_pos()) and not handled:
                            if ferros_value >= 10:
                                enchada_num += 1
                                ferros_value -= 10

                                pg.display.update()
                            else:
                                print('sem ferros suficientes')
                        if event.type == pg.MOUSEBUTTONDOWN and picareta.rect.collidepoint(
                                pg.mouse.get_pos()) and not handled:
                            if ferros_value >= 10:
                                picareta_num += 1
                                ferros_value -= 10

                                pg.display.update()
                            else:
                                print('sem ferros suficientes')

                        janela.fill([255, 255, 255])
                        janela.blit(lore_enchada, (60, 190))
                        janela.blit(lore_picareta, (260, 190))
                        drawgroup_craft.draw(janela)

                        pg.display.update()

        janela.blit(bg_, (0, 0))
        drawgroup_world1.draw(janela)
        pg.display.update()
