import pygame


class Ceil:
    # конструктор
    def __init__(self, Place, Number, SpcBtwn):
        self.__SpcBtwn = SpcBtwn
        self.__place = Place
        self.__number = Number
        self.find_coord()

    # метод вычисления координат по местоположению в списке
    def find_coord(self):
        column = self.__place[0]
        line = self.__place[1]
        x = 30 * column + self.__SpcBtwn * (column+1)
        y = 30 * line + self.__SpcBtwn * (line + 1)
        self.__coord = (x, y)
    # метод изменения координаты из-за смещения

    def find_coord_y(self, Shift):
        line = self.__place[1]
        x = self.__coord[0]
        y = 30 * line + self.__SpcBtwn * (line + 1) - Shift
        self.__coord = (x, y)

    # все сеттэры и геттэры для класса
    # @property позволяет вызывать геттер простым запросом к атрибуту
    # MyCeil.get_coord() ==> MyCeil.coord
    # @имя атрибута.setter позволяет выполнять присвоение, вместо вызова метода
    @property
    def coord(self):
        return self.__coord
    # сеттера для координат нет, так мы их вычисляем, а не сами придумываем

    @property
    def place(self):
        return self.__place

    @place.setter
    def place(self, IS):
        self.__place = (IS[0] % 9, IS[0] // 9)
        self.find_coord_y(IS[1])

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, Number):
        self.__number = Number

    # переопределяем вывод строкового представления об объекте
    def __str__(self):
        info = "Number: {} \t Coordinates of Ceil: {} \t Place in ndarray: {}"
        return info.format(self.__number, self.__coord, self.__place)

    # рисование ячейки с цифрой
    def Draw(self, MainSurface, Font, selectedIndex):
        selectedPlace = (selectedIndex % 9, selectedIndex // 9)
        color = (255, 0, 0) if selectedPlace == self.place else (255, 255, 255)
        # сначала рисуем ячейку
        surface = pygame.Surface((30, 30))
        pygame.draw.rect(surface, color, (0, 0, 30, 30), 2)

        # теперь рисуем цифру
        # text это внучатая поверхность
        if self.number != 0:
            text = Font.render(str(self.number), 1, color)
            surface.blit(text, text.get_rect(center=(15, 15)))
        MainSurface.blit(surface, self.coord)
