from tkinter import *
from tkinter import messagebox
import time
import random

tk = Tk()
# создаем всe


def u_attak():
    global AI_lost, s_x, s_y, points, points2, user_ships, turn_player
    while turn_player and user_ships <= 0:
        mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
        mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()
        ip_x = mouse_x // step_x
        ip_y = mouse_y // step_y
        # ЕСЛИ В ПОЛЕ ИИ
        if ip_x < s_x and ip_y < s_y:
            if enemy_ships[ip_y][ip_x] != 'T':
                canvas.create_rectangle(step_x * (ip_x + 1), step_y * (ip_y + 1), step_x * ip_x, step_y * ip_y,
                                        fill='blue')
                AI_lost -= 1
                time.sleep(1)
            else:
                canvas.create_rectangle(step_x * (ip_x + 1), step_y * (ip_y + 1), step_x * ip_x, step_y * ip_y,
                                        fill='yellow')
                turn_player = False
                break
        if AI_lost <= 0:
            winner = "Победа"
            winner_add = "Все корабли Противника подбиты"
            print(winner, winner_add)
            points1 = [[10 for i in range(s_x)] for i in range(s_y)]
            points2 = [[10 for i in range(s_x)] for i in range(s_y)]
            id1 = canvas.create_rectangle(step_x * 3, step_y * 5, size_map_x + step_x*3 + size_map_x - step_x * 3,
                                          size_map_y + step_y, fill="gold")
            id2 = canvas.create_rectangle(step_x * 3 + step_x // 2, step_y * 5 + step_y // 2,
                                          size_map_x + step_x*3 + size_map_x - step_x * 3 - step_x // 2,
                                          size_map_y - step_y - step_y // 2 + step_y * 3, fill="green")
            id3 = canvas.create_text(step_x * 10, step_y * 6, text=winner, font=("Arial", 50), justify=CENTER)
            id4 = canvas.create_text(step_x * 10, step_y * 8, text=winner_add, font=("Arial", 25), justify=CENTER)


def finish(x, y):
    global user_map, fin, path, user_lost, turn_player, AI_lost, s_x, s_y, points, points2, user_ships
    way = ''

    if user_map[y - 1][x] == '@':
        i = 1
        while user_map[y - i][x] == '@':
            print(x, y - i)
            time.sleep(1)
            user_map[y - i][x] = 'X'
            user_map[y - i][x + 1] = 'x'
            user_map[y - i][x - 1] = 'x'
            user_draw()
            user_lost -= 1
            tk.update()
            i += 1
        user_map[y - i][x] = 'x'
        user_map[y - i][x + 1] = 'x'
        user_map[y - i][x - 1] = 'x'
        turn_player = True
        way = 'u'

    elif user_map[y][x + 1] == '@':
        i = 1
        while user_map[y][x + i] == '@':
            print(x + i, 1)
            time.sleep(1)
            user_map[y][x + i] = 'X'
            user_map[y + 1][x + i] = 'x'
            user_map[y - 1][x + i] = 'x'
            user_lost -= 1
            user_draw()
            tk.update()
            i += 1
        user_map[y][x + i] = 'x'
        user_map[y + 1][x + i] = 'x'
        user_map[y - 1][x + i] = 'x'
        way = 'r'
        turn_player = True

    elif user_map[y][x - 1] == '@':
        i = 1
        while user_map[y][x - i] == '@':
            print(x - i, y)
            time.sleep(1)
            user_map[y][x - i] = 'X'
            user_map[y - 1][x - i] = 'x'
            user_map[y + 1][x - i] = 'x'
            user_lost -= 1
            user_draw()
            tk.update()
            i += 1
        user_map[y][x - i] = 'x'
        user_map[y - 1][x - i] = 'x'
        user_map[y + 1][x - i] = 'x'
        way = 'l'
        turn_player = True

    elif user_map[y + 1][x] == '@':
        i = 1
        while user_map[y + i][x] == '@':
            print(x, y + i)
            time.sleep(1)
            user_map[y + i][x] = 'X'
            user_map[y + i][x + 1] = 'x'
            user_map[y + i][x - 1] = 'x'
            user_lost -= 1
            user_draw()
            tk.update()
            i += 1
        user_map[y + i][x] = 'x'
        user_map[y + i][x + 1] = 'x'
        user_map[y + i][x - 1] = 'x'

        way = 'd'
        turn_player = True

    if way == 'u' or way == 'd':
        user_map[y][x + 1] = 'x'
        user_map[y][x - 1] = 'x'
    elif way == 'r' or way == 'l':
        user_map[y - 1][x] = 'x'
        user_map[y + 1][x] = 'x'

    canvas.bind_all("<Button-1>", u_attak())
    while turn_player:
        pass
    canvas.bind_all("<Button-1>", add_to_all)

    if way == 'u':
        if user_map[y - i + 3][x] == '@':

            i = 0
            while user_map[y + i][x] == '@':
                print(x, i + 1)
                time.sleep(1)
                user_map[y + i][x] = 'X'
                user_map[y + i][x + 1] = 'x'
                user_map[y + i][x - 1] = 'x'
                user_lost -= 1
                user_draw()
                tk.update()
                i += 1
            user_map[y + i][x] = 'x'
            user_map[y + i][x + 1] = 'x'
            user_map[y + i][x - 1] = 'x'
            fin = False

    if way == 'r':
        if user_map[y][x + i - 3] == '@':
            i = 0
            while user_map[y][x - i] == '@':
                print(x - i, y)
                time.sleep(1)
                user_map[y][x - i] = 'X'
                user_map[y - 1][x - i] = 'x'
                user_map[y + 1][x - i] = 'x'
                user_lost -= 1
                user_draw()
                tk.update()
                i += 1
            user_map[y][x - i] = 'x'
            user_map[y - 1][x - i] = 'x'
            user_map[y + 1][x - i] = 'x'
            fin = False

    if way == 'l':
        if user_map[y][x - i + 3] == '@':
            i = 0
            while user_map[y][x + i] == '@':
                print(x + i, y)
                time.sleep(1)
                user_map[y][x + i] = 'X'
                user_map[y - 1][x + i] = 'x'
                user_map[y + 1][x + i] = 'x'
                user_lost -= 1
                user_draw()
                tk.update()
                i += 1
            user_map[y][x + i] = 'x'
            user_map[y - 1][x + i] = 'x'
            user_map[y + 1][x + i] = 'x'
            fin = False

    if way == 'd':
        if user_map[y + i - 3][x] == '@':
            i = 0
            while user_map[y - i][x] == '@':
                print(x, y - i)
                time.sleep(1)
                user_map[y - i][x] = 'X'
                user_map[y - i][x + 1] = 'x'
                user_map[y - i][x - 1] = 'x'
                user_lost -= 1
                user_draw()
                tk.update()
                i += 1
            user_map[y - i][x] = 'x'
            user_map[y - i][x + 1] = 'x'
            user_map[y - i][x - 1] = 'x'
            fin = False

fre_points = ['.']


def check_winner_AI():
    global user_map
    win = True
    for i in range(0, 10):
        for j in range(0, 10):
            if user_map[j][i] == '@':
                win = False
    return win


list_ids = []


def AI_winner():
    global step_x, step_y, list_ids, list_ids
    winner = "Поражение"
    winner_add = "Вы потеряли все свои корабли"
    points1 = [[10 for i in range(s_x)] for i in range(s_y)]
    points2 = [[10 for i in range(s_x)] for i in range(s_y)]
    id1 = canvas.create_rectangle(step_x * 3, step_y * 3, size_map_x + step_x*3 + size_map_x - step_x * 3,
                                  size_map_y - step_y, fill="black")
    id2 = canvas.create_rectangle(step_x * 3 + step_x // 2, step_y * 3 + step_y // 2,
                                  size_map_x + step_x*3 + size_map_x - step_x * 3 - step_x // 2,
                                  size_map_y - step_y - step_y // 2, fill="red")
    id3 = canvas.create_text(step_x * 10, step_y * 5, text=winner, font=("Arial", 50), justify=CENTER)
    id4 = canvas.create_text(step_x * 10, step_y * 6, text=winner_add, font=("Arial", 25), justify=CENTER)
    list_ids.append(id1)
    list_ids.append(id2)
    list_ids.append(id3)
    list_ids.append(id4)


fin = True


def enemy_shoot():
    global user_map, enemy_was, turn_player, fin, user_lost
    if not turn_player:
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        while user_map[y][x] == 'X' or user_map[y][x] == 'x':
            x = random.randint(1, 10)
            y = random.randint(1, 10)
        if user_map[y][x] == '.':
            user_map[y][x] = 'x'
            turn_player = True
        elif user_map[y][x] == '@':
            print(x, y)
            fin = True
            if fin:
                finish(x, y)
            enemy_shoot()
            user_map[y][x] = 'X'
            user_lost -= 1

        user_draw()


pole = [['.' for i in range(15)] for i in range(15)]
def take_position(pole, ln):
    a = random.randint(3, 12)
    b = random.randint(3, 12)
    while pole[a][b] == str(ln) or pole[a][b] == '#':
        a = random.randint(3, 12)
        b = random.randint(3, 12)
    way = random.randint(1, 4)
    if way == 1:
        for i in range(0, ln):
            if pole[a - i][b] != '.':
                tf = False
                break
            else:
                tf = True
        if tf:
            for i in range(0, ln):
                pole[a - i][b] = 'T'
    if way == 2:
        for i in range(0, ln):
            if pole[a][b + i] != '.':
                tf = False
                break
            else:
                tf = True
        if tf:
            for i in range(0, ln):
                pole[a][b + i] = 'T'
    if way == 3:
        for i in range(0, ln):
            if pole[a + i][b] != '.':
                tf = False
                break
            else:
                tf = True
        if tf:
            for i in range(0, ln):
                pole[a + i][b] = 'T'
    if way == 4:
        for i in range(0, ln):
            if pole[a][b - i] != '.':
                tf = False
                break
            else:
                tf = True
        if tf:
            for i in range(0, ln):
                pole[a][b - i] = 'T'
    if tf == False:
        pole = take_position(pole, ln)
    return pole
def zapoln(m):
    global pole
    for i in range(15):
        for j in range(15):
            if m[i][j] == 'T':
                try:  # 1
                    pole[i + 1][j + 1] = '#'
                except IndexError:
                    pole[i - 1][j - 1] = '#'
                try:  # 2
                    pole[i + 1][j - 1] = '#'
                except IndexError:
                    pole[i - 1][j + 1] = '#'
                try:  # 3
                    pole[i - 1][j + 1] = '#'
                except IndexError:
                    pole[i + 1][j - 1] = '#'
                try:  # 4
                    pole[i - 1][j - 1] = '#'
                except IndexError:
                    pole[i + 1][j + 1] = '#'

                if m[i + 1][j] == 'T' and m[i - 1][j] == '.':
                    m[i - 1][j] = '#'
                if m[i - 1][j] == 'T' and m[i + 1][j] == '.':
                    m[i + 1][j] = '#'
                if m[i][j + 1] == 'T' and m[i][j - 1] == '.':
                    m[i][j - 1] = '#'
                if m[i][j - 1] == 'T' and m[i][j + 1] == '.':
                    m[i][j + 1] = '#'
    return m
def for1(pole):
    a = random.randint(3, 12)
    b = random.randint(3, 12)
    while pole[a][b] == 'T' or pole[a][b] == '#':
        a = random.randint(3, 12)
        b = random.randint(3, 12)
    pole[a][b] = 'T'
    pole[a + 1][b + 1] = '#'
    pole[a + 1][b] = '#'
    pole[a + 1][b - 1] = '#'
    pole[a][b + 1] = '#'
    pole[a][b - 1] = '#'
    pole[a - 1][b + 1] = '#'
    pole[a - 1][b] = '#'
    pole[a - 1][b - 1] = '#'
    return pole
def create(pole):
    pole = take_position(pole, 4)
    pole = zapoln(pole)
    pole = take_position(pole, 3)
    pole = zapoln(pole)
    pole = take_position(pole, 2)
    pole = zapoln(pole)
    pole = take_position(pole, 2)
    pole = zapoln(pole)
    pole = for1(pole)
    pole = zapoln(pole)
    pole = for1(pole)
    pole = zapoln(pole)
    pole = for1(pole)
    pole = zapoln(pole)
    return pole
def place():
    global pole
    respole = []
    for i in range(15):
        for j in range(15):
            if i < 3 or i > 12 or j < 3 or j > 12:
                pole[i][j] = '#'
            else:
                pole[i][j] = '.'
    pole = create(pole)
    for i in range(3, 13):
        respole.append(pole[i][3:13])
    return respole


enemy_ships = place()
'''
<- расстановка кораблей противника случайным образом, в результате получаем его карту: enemy_ships
'''
def enemy_draw():
    for i in range(10):
        for j in range(10):
            if enemy_ships[i][j] == 'X':
                canvas.create_rectangle(step_x * (j - 1), step_y * (i - 1), step_x * j, step_y * i, fill='yellow')


def enemy_die_ship():#доделать
    global enemy_ships
    for y in range(10):
        for x in range(10):
            if enemy_ships[x][y] == 'X':
                if enemy_ships[y-1][x] == 'X' or enemy_ships[y+1][x]:
                    i = 0
                    while enemy_ships[y-i][x] == 'X':# в одном напрвлении
                        i += 1
                    if enemy_ships[y-i][x] != 'T' and enemy_ships[y-i][x]!='X':
                        j = 0
                        while enemy_ships[y + j][x] == 'X':#в другом
                            j += 1
                        if enemy_ships[y + j][x] == '.':
                            for k in range(y-i, y+j):
                                enemy_ships[k][x+1] = 'X'
                                enemy_ships[k][x] = 'X'
                                enemy_ships[k][x-1] = 'X'
                elif enemy_ships[y][x-1] == 'X' or enemy_ships[y][x+1] == 'X':

                    i = 0
                    while enemy_ships[y][x-i] == 'X':  # в одном напрвлении
                        i += 1
                    if enemy_ships[y][x-i] == '.':
                        j = 0
                        while enemy_ships[y][x+j] == 'X':  # в другом
                            j += 1
                        if enemy_ships[y][x+j] != 'T' and enemy_ships[y-i][x]!='X':
                            for k in range(x - i, x + j):
                                enemy_ships[y-1][k] = 'X'
                                enemy_ships[y][k] = 'X'
                                enemy_ships[y+1][k] = 'X'
    enemy_draw()


user_map = [['.' for i in range(12)] for j in range(12)]
def user_draw():
    global user_map, step_x, step_y
    for i in range(1, len(user_map) - 1):
        for j in range(1, len(user_map[0]) - 1):
            if user_map[j][i] == '#':
                canvas.create_rectangle(step_x * (j - 1) + size_map_x + step_x * 3, step_y * (i - 1),
                                        step_x * j + size_map_x + step_x * 3, step_y * i, fill='yellow')
            elif user_map[j][i] == '.':
                canvas.create_rectangle(step_x * (j - 1) + size_map_x + step_x * 3, step_y * (i - 1),
                                        step_x * j + size_map_x + step_x * 3, step_y * i, fill='skyblue')
            elif user_map[j][i] == '@':
                canvas.create_rectangle(step_x * (j - 1) + size_map_x + step_x * 3, step_y * (i - 1),
                                        step_x * j + size_map_x + step_x * 3, step_y * i, fill='red')
            elif user_map[j][i] == 'X':  # big X
                canvas.create_rectangle(step_x * (j - 1) + size_map_x + step_x * 3, step_y * (i - 1),
                                        step_x * j + size_map_x + step_x * 3, step_y * i, fill='blue')
            elif user_map[j][i] == 'x':  # small x
                canvas.create_rectangle(step_x * (j - 1) + size_map_x + step_x * 3, step_y * (i - 1),
                                        step_x * j + size_map_x + step_x * 3, step_y * i, fill='yellow')


# размеры

size_map_x = 500
size_map_y = 500
s_x = s_y = 10
step_x = size_map_x // s_x
step_y = size_map_y // s_y
# обновление, ход иrры
app_running = True

turn_player = True


def on_closing():
    global app_running
    if messagebox.askokcancel("Выход из игры", "Хотите выйти из игры?"):
        app_running = False
        tk.destroy()


tk.protocol("WM_DELETE_WINDOW", on_closing)
tk.title("Игра Морской Бой")
tk.resizable(0, 0)
canvas = Canvas(tk, width=2 * size_map_x + step_x * 3, height=size_map_y + step_y * 3, bd=0, highlightthickness=0)
canvas.create_rectangle(0, 0, size_map_x, size_map_y, fill="skyblue")
canvas.create_rectangle(size_map_x + step_x * 3, 0, 2 * size_map_x + step_x * 3, size_map_x, fill="skyblue")

canvas.create_rectangle(size_map_x, 0, size_map_x, size_map_y, fill="lightyellow")
canvas.pack()
tk.update()  # рисуем 1 холст


def draw_table(offset_x=0):
    for i in range(0, s_x + 1):
        canvas.create_line(step_x * i + offset_x, 0, step_x * i + offset_x, size_map_y)
    for i in range(0, s_y + 1):
        canvas.create_line(offset_x, step_y * i, size_map_x + offset_x, step_y * i)
draw_table()
draw_table(size_map_x + step_x * 3)  # рисуем поле 10х10(AI)size



t3 = Label(tk, text="@@@@@@@", font=("Helvetica", 16))
t3.place(x=size_map_x + step_x*3//2 - t3.winfo_reqwidth() // 2, y= size_map_y)


def mark_igrok():
    global user_ships
    if user_ships>=0:
        t3.configure(text="Осталось расставить: " + str(user_ships) + " палуб")
        t3.place(x=size_map_x + step_x*3 // 2 - t3.winfo_reqwidth() // 2, y=size_map_y+5)

user_ships = 7
user_lost = 7

etap = 'расстановка'
def etap_ch():
    global user_ships, etap
    if user_ships > 0:
        etap = 'расстановка'
    else:
        etap = 'бой'

t4 = Label(tk, text="этап: " + etap, font=("Helvetica", 16))
t4.place(x=size_map_x + step_x * 3 // 2 - t3.winfo_reqwidth() // 2, y=size_map_y + 30)
def user_place(event):
    global user_map, user_ships, s_x, s_y, size_map_y, size_map_x, step_x
    if user_ships > 0:
        mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
        mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()
        x = (mouse_x - size_map_x - step_x*3) // step_x + 1
        y = (mouse_y - size_map_y) // step_y - 1
        # ЕСЛИ В ПОЛЕ ИИ
        if x < s_x and y < s_y and user_ships > 0:
            print('ok')
            if user_map[x][y] == '.':
                user_map[x][y] = '@'
                user_ships -= 1
            elif user_map[x][y] == '@':
                user_map[x][y] = '.'
                user_ships += 1
        etap_ch()
        t4.configure(text="этап: " + etap)
        t4.place(x=size_map_x + step_x * 3 // 2 - t3.winfo_reqwidth() // 2, y=size_map_y + 30)
        user_draw()

canvas.bind_all("<Button-1>", user_place)

t0 = Label(tk, text="Игрок №1", font=("Helvetica", 16))
t0.place(x=size_map_x // 2 - t0.winfo_reqwidth() // 2, y=size_map_y + 3)
t1 = Label(tk, text="Игрок №2", font=("Helvetica", 16))
t1.place(x=size_map_x + step_x*3 + size_map_x // 2 - t1.winfo_reqwidth() // 2, y=size_map_y + 3)

t0.configure(bg="red")
t0.configure(bg="#f0f0f0")

t3 = Label(tk, text="", font=("Helvetica", 16))
t3.place(x=size_map_x + step_x*3//2 - t3.winfo_reqwidth() // 2, y= size_map_y)


def begin_again():
    global user_map, enemy_ships, pole, enemy_ships, step_x, step_y, user_lost, user_ships, AI_lost
    for j in range(len(list_ids)):
        canvas.delete(list_ids[j])
    canvas.create_rectangle(0, 0, size_map_x, size_map_y, fill="skyblue")
    draw_table()
    pole = [['.' for i in range(15)] for i in range(15)]
    enemy_ships = place()
    user_map = [['.' for i in range(12)] for j in range(12)]
    user_ships = 7
    user_lost = 7
    AI_lost = 14
    user_draw()

    canvas.bind_all("<Button-1>", user_place)
'''
    for i in range(len(enemy_ships)):
        for j in range(len(enemy_ships[0])):
            if enemy_ships[i][j] == 'T':
                canvas.create_rectangle(step_x * (j + 1), step_y * (i + 1), step_x * j, step_y * i, fill='red')
'''


button_begin_again = Button(tk, text="Начать заново", command=begin_again)
button_begin_again.place(x=size_map_x + 20, y=170)

AI_lost = 14

def add_to_all(event):
    global AI_lost
    global s_x
    global s_y
    global points, points2, user_ships, turn_player
    mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()
    ip_x = mouse_x // step_x
    ip_y = mouse_y // step_y
    # ЕСЛИ В ПОЛЕ ИИ
    if ip_x < s_x and ip_y < s_y and turn_player and user_ships <= 0:
        if enemy_ships[ip_y][ip_x] == 'T':
            canvas.create_rectangle(step_x * (ip_x + 1), step_y * (ip_y + 1), step_x * ip_x, step_y * ip_y, fill='blue')
            AI_lost -= 1
            enemy_ships[ip_y+1][ip_x+1] = 'X'
        else:
            canvas.create_rectangle(step_x * (ip_x + 1), step_y * (ip_y + 1), step_x * ip_x, step_y * ip_y,fill='yellow')
            turn_player = False

            time.sleep(1)

        enemy_shoot()

    if AI_lost == 0:

        winner = "Победа"
        winner_add = "Все корабли Противника подбиты"
        print(winner, winner_add)
        points1 = [[10 for i in range(s_x)] for i in range(s_y)]
        points2 = [[10 for i in range(s_x)] for i in range(s_y)]
        id1 = canvas.create_rectangle(step_x * 3, step_y * 3, size_map_x + step_x*3 + size_map_x - step_x * 3,
                                      size_map_y - step_y, fill="gold")
        id2 = canvas.create_rectangle(step_x * 3 + step_x // 2, step_y * 3 + step_y // 2,
                                      size_map_x + step_x*3 + size_map_x - step_x * 3 - step_x // 2,
                                      size_map_y - step_y - step_y // 2, fill="green")
        id3 = canvas.create_text(step_x * 10, step_y * 5, text=winner, font=("Arial", 50), justify=CENTER)
        id4 = canvas.create_text(step_x * 10, step_y * 6, text=winner_add, font=("Arial", 25), justify=CENTER)
        list_ids.append(id1)
        list_ids.append(id2)
        list_ids.append(id3)
        list_ids.append(id4)
    for u in range(10):
        print(enemy_ships[u])
for i in range(10):
    print(enemy_ships[i])


while app_running:
    etap_ch()
    mark_igrok()
    if user_ships <= 0:
        canvas.bind_all("<Button-1>", add_to_all)

    if user_lost <= 0:
        AI_winner()
    if app_running:
        tk.update_idletasks()
        tk.update()
    time.sleep(0.005)