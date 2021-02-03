import math
import pygame
from Classes import Ceil

# нажатие на ячейку


def MouseClick(position, SpcBtwn, table, Shift):
    column = -1
    line = -1
    # определяем столбец
    for i in range(9):
        x = 30*i + SpcBtwn*(i+1)
        if (position[0] >= x and position[0] <= x+30):
            column = i
            break
    # определяем строку
    for j in range(math.ceil(len(table) / 9)):
        y = 30*j + SpcBtwn*(j+1) - Shift
        if (position[1] >= y and position[1] <= y+30):
            line = j
            break
    if column != -1 and line != -1:
        return column + line * 9

# проверка пары на условие зачёркивания


def CheckPair(fi, si, table):
    if HorCheck(fi, si, table):
        return True
    if fi % 9 == si % 9 and VertCheck(fi, si, table):
        return True
    return False

# проверка вертикального доступа


def VertCheck(fi, si, table):
    CanYouDoIt = True
    begin = min(fi, si) + 9
    stop = max(fi, si)
    while begin < stop:
        if table[begin].number != 0:
            CanYouDoIt = False
            break
        begin += 9
    return CanYouDoIt

# проверка горизонтального доступа


def HorCheck(fi, si, table):
    CanYouDoIt = True
    begin = min(fi, si) + 1
    stop = max(fi, si)
    while begin < stop:
        if table[begin].number != 0:
            CanYouDoIt = False
            break
        begin += 1
    return CanYouDoIt

# обновление данных объектов


def update(table, Shift):
    for id, item in enumerate(table):
        item.place = (id, Shift)

# добавление чисел


def AddNumbers(table, SpcBtwn):
    TWOZ = []
    # ищем в массиве ненулевые значения
    i = 0
    for id, item in enumerate(table):
        if item.number != 0:
            place = i + len(table)
            place = (place % 9, place // 9)
            TWOZ.append(Ceil(place, item.number, SpcBtwn))
            i += 1
    table.extend(TWOZ)
    return(table)

# удаление пустых чисел


def DeleteEmptyLines(table):
    emptyLines = []
    # определяем пустые строки
    for i in range(len(table)//9):
        condition = True
        for j in range(9):
            if table[i*9+j].number != 0:
                condition = False
                break
        if condition:
            emptyLines.append(i)
    for i in emptyLines:
        for j in range(i*9, (i+1)*9):
            table[j] = -1
    for i in range(len(emptyLines)*9):
        table.remove(-1)
    return table

# рестарт


def Restart(tb, SpcBtwn):
    startNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9,
                    1, 1, 1, 2, 1, 3, 1, 4, 1,
                    5, 1, 6, 1, 7, 1, 8, 1, 9
                    ]
    tb = []
    for i in range(3):
        for j in range(9):
            tb.append(Ceil((j, i), startNumbers[i * 9 + j], SpcBtwn))
    return tb

# рисование кнопок


def DrawButtons(MainSurface, Font):
    # сначала рисуем ячейку
    buttons = ("Отменить", "Добавить", "Рестарт")
    white = (255, 255, 255)
    bs = pygame.Surface((200, 600))
    pygame.draw.rect(bs, white, (0, 0, 200, 600), 2)
    MainSurface.blit(bs, (600, 0))

    # теперь рисуем текст
    # text это внучатая поверхность
    for id, item in enumerate(buttons):
        surface = pygame.Surface((150, 60))
        pygame.draw.rect(surface, white, (0, 0, 150, 60), 2)
        text = Font.render(item, 1, white)
        surface.blit(text, text.get_rect(center=(75, 30)))
        MainSurface.blit(surface, (625, 93 * id + 33))
    return MainSurface
