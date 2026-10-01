import os
from time import sleep


RED = '\u001b[41m'      
GREEN = '\u001b[42m'    
BLUE = '\u001b[44m'     
WHITE = '\u001b[47m'    
BLACK = '\u001b[40m'   
RESET = '\u001b[0m'     

# строчка чтобы ескейп-символы заработали
os.system('')


# ф-я, которая очищает консоль
# в ос вин команда cls
# os.name == 'nt' значит, что у меня вин
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


# флаг бангладеща
# зеленый прямоугольник и красный круг внутри
def draw_flag():
    height = 18         
    length = 60         
    center_x = 27       
    center_y = 9        
    radius = 6         

    # иду по каждой строке сверху вниз
    for y in range(height):
        line = ''       # сюда буду собирать строку из цветных пробелов
        for x in range(length):
            dx = (x - center_x) / 2
            dy = y - center_y
            if dx * dx + dy * dy <= radius * radius:
                line = line + RED + ' '      # красный пробел
            else:
                line = line + GREEN + ' '    # зелёный пробел

        # reset в конце строки, чтобы цвет не вытека дальше
        print(line + RESET)


# повторяющийся узор 
# "#" - xthyfz gkbnrf "." - ,tkfz gkbnrf
TILE = [
    '#####.',
    '#...#.',
    '#.###.',
    '#.#...',
    '#.####',
    '......',
]


def draw_pattern():
    # повторяю плитку 3 раза вниз
    for _ in range(3):
        for row in TILE:
            line = ''
            for _ in range(8):
                for ch in row:
                    if ch == '#':
                        line = line + BLACK + '  '   # чёрная клетка 
                    else:
                        line = line + WHITE + '  '   # белая клетка
            print(line + RESET)



def animation():
    for _ in range(4):
        # 4 кадра
        for frame in range(4):
            clear()                       
            print('Кадр', frame + 1)      
            shift = frame * 10

            for _ in range(3):
                print(f'\u001b[{shift}C' + RED + ' ' * 6 + RESET)

            sleep(0.5)      # пауза 
    clear()




def diagram():
   
    folder = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(folder, 'sequence.txt')

  
    with open(path) as f:
        numbers = [float(x) for x in f.read().replace(',', ' ').split()]

   
    first = sum(abs(n) for n in numbers[:125])
    second = sum(abs(n) for n in numbers[125:250])

    # сколько процентов составляет первая сумма от общей
    percent1 = first / (first + second) * 100
    
    percent2 = 100 - percent1

    # рисую полоску длиной 50 символов
    width = 50
    len1 = round(percent1 / 100 * width)    
    len2 = width - len1                     

    print(BLUE + ' ' * len1 + RED + ' ' * len2 + RESET)
    print(BLUE + '  ' + RESET, f'первые 125:  {first:.2f}  ({percent1:.1f}%)')
    print(RED + '  ' + RESET, f'вторые 125:  {second:.2f}  ({percent2:.1f}%)')



draw_flag()
print()
draw_pattern()
input('Enter - анимация...')
animation()
diagram()