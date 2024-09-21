from colorama import init, Fore, Back, Style
import sys, time, math, os

init()


class Screen:
    def __init__(self, height, width):
        self.screen = []
        for x in range(height):
            temp = []
            for y in range(width):
                temp.append(0)
            self.screen.append(temp)

    def clear(self):
        for y in range(len(self.screen)):
            for x in range(len(self.screen[y])):
                self.screen[y][x] = 0

    def draw(self):
        for x in self.screen:
            for y in x:
                # time.sleep(0.5)
                if y == 1:
                    sys.stdout.write(Fore.WHITE + Back.WHITE + "[]")
                else:
                    sys.stdout.write(Fore.BLACK + Back.BLACK + "[]")
            sys.stdout.write(Style.RESET_ALL + "\n")

    def line(self, m, b):
        lineList = []
        for x in range(len(self.screen[0])):
            lineList.append([x, m * x + b])
        for x in lineList:
            try:
                self.screen[round(x[1])][round(x[0])] = 1
            except:
                pass

    def sin(self, pos, height, offset=0):
        lineList = []
        for x in range(len(self.screen[0])):
            lineList.append([(x + offset) % len(self.screen[0]), math.sin(x) * height + pos])
        for x in lineList:
            try:
                self.screen[round(x[1])][round(x[0])] = 1
            except:
                pass


scr = Screen(50, 50)

a = 0
os.system("cls")
wait = input("")
while True:
    scr.sin(30, math.sin(a/10)*4, a%100)
    os.system("cls")
    scr.draw()
    scr.clear()

