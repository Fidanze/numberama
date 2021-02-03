# здесь подключаются модули
import pkg_resources.py2_warn
import pygame
import functions as fc
import copy

# здесь определяются константы, классы и функции
FPS = 60
Width = 800
Height = 600
BLACK = (0, 0, 0)
Interval = 33
FCOP = -1
selCeil = 0
# сдвиг поверхности
Shift = 0
Result = False

# массив Nx9
table = []
table = fc.Restart(table, Interval)
OldTable = copy.deepcopy(table)

# здесь происходит инициация, создание объектов и др.
pygame.init()
sc = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("My game")
clock = pygame.time.Clock()
NumberFont = pygame.font.SysFont('arial', 28)
sc = fc.DrawButtons(sc, NumberFont)

# если надо до цикла отобразить объекты на экране


# главный цикл
while not Result:

    # задержка
    clock.tick(FPS)

    # цикл обработки событий
    for i in pygame.event.get():

        # событие выхода
        if i.type == pygame.QUIT:
            exit()

        # события мыши
        if i.type == pygame.MOUSEBUTTONDOWN:
            # нажатие ЛКМ
            if i.button == 1:
                index = fc.MouseClick(i.pos, Interval, table, Shift)
                # КО в табле и номер в списке
                # нажатие на ячейку и проверка на
                # существование данной ячейки в table
                if index is not None and index < len(table):
                    Ceil = table[index].number
                    # проверка ячейки на пустоту
                    if Ceil != 0:
                        if FCOP == -1:
                            FCOP = index
                            selCeil = Ceil
                        elif FCOP != index:
                            # проверка на условие стирания
                            if Ceil == selCeil or Ceil + selCeil == 10:
                                if fc.CheckPair(FCOP, index, table):
                                    OldTable = copy.deepcopy(table)
                                    table[FCOP].number = 0
                                    table[index].number = 0
                            FCOP = -1
                else:
                    FCOP = -1
                    for id in range(0, 3):
                        if i.pos[0] >= 625 and i.pos[0] <= 775:
                            if i.pos[1] >= 93 * id + 33:
                                if i.pos[1] <= 93 * (id + 1):
                                    if id == 0:
                                        table = copy.deepcopy(OldTable)
                                        break
                                    elif id == 1:
                                        OldTable = copy.deepcopy(table)
                                        table = fc.AddNumbers(table, Interval)
                                        break
                                    else:
                                        Shift = 0
                                        table = fc.Restart(table, Interval)
                                        OldTable = copy.deepcopy(table)
                                        sc.fill(BLACK)
                                        break

            # прокрутка мыши вниз
            if i.button == 5:
                lenTable = len(table)//9
                if 600 + Shift <= (30 + Interval) * (lenTable+1) + Interval:
                    Shift += 20
                    fc.update(table, Shift)

            # прокрутка мыщи вверх
            if i.button == 4 and Shift > 0:
                Shift -= 20
                fc.update(table, Shift)

    # изменение поверхности
    table = fc.DeleteEmptyLines(table)
    fc.update(table, Shift)
    sc.fill(BLACK)
    for i in table:
        if i.coord[1] - 30 <= 600 and i.coord[1] + 30 > 0:
            i.Draw(sc, NumberFont, FCOP)
    sc = fc.DrawButtons(sc, NumberFont)

    # условие победы
    if len(table) // 9 == 0:
        sum = 0
        for i in table:
            if i.number == 0:
                sum += 1
        if sum == len(table):
            Result = True
            break

    # обновление экрана
    pygame.display.update()
exit()
