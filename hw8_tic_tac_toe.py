import os
import sys
import time
import random


class Field(list):

    def __init__(self, size=3):
        self.size = size
        self.empty_cell = " "
        super().__init__([[self.empty_cell for _ in range(self.size)] for __ in range(self.size)])
        # self.field = [[self.empty_cell for _ in range(self.size)] for __ in range(self.size)]

    def get_field(self):
        print("    {}".format(" | ".join([str(_) for _ in range(1, self.size + 1)])))
        for line in enumerate(self, 1):
            print("{0:-^{1}}".format("-", self.size * 4 + 3))
            print("{}|  {} ".format(line[0], " | ".join([str(_) for _ in line[1]])))

    def get_len(self):
        return self.size

    def check_cell(self, move):
        return self[move[0]][move[1]] == self.empty_cell

    def make_move(self, move, marker):
        self[move[0]][move[1]] = marker

    def check_empty_cell(self):
        for line in self:
            for cell in line:
                if cell == self.empty_cell:
                    return True
        return False


class Player:

    def __init__(self, name, marker, brain=False):
        self.name = name
        self.marker = marker
        self.brain = brain
        self._moves = []
        self.last_move = None

    def is_ii(self):
        return self.brain

    def next_move(self):
        answer = input("{}, твой ход (строка столбец): ".format(self.name))
        if answer == 'q':
            print("Спасибо за игру!")
            sys.exit(1)
        else:
            self.last_move = tuple(map(lambda x: int(x) - 1, answer.split()))
        self._moves.append(self.last_move)

    def get_moves(self):
        return self._moves


class Computer(Player):

    def __init__(self, name, marker, game_field=Field(), brain=True):
        super().__init__(name, marker, brain)
        self.game_field = game_field

    def next_move(self):
        self.last_move = self.scan_field()
        self._moves.append(self.last_move)

    def scan_field(self):
        length = self.game_field.get_len()

        empty_cells_for_left = []
        self_cells_for_left = 0
        enemy_cells_for_left = 0

        empty_cells_for_right = []
        self_cells_for_right = 0
        enemy_cells_for_right = 0

        left_i = 0
        right_i = length - 1

        empty_cells_for_line = []
        self_cells_for_line = 0
        enemy_cells_for_line = 0
        self_empty_cells_for_line = []
        self_ = 0
        enemy_empty_cells_for_line = []
        enemy_ = 0

        for x in range(length):

            if self.game_field[x][left_i] == self.game_field.empty_cell:
                empty_cells_for_left.append((x, left_i))
            elif self.game_field[x][left_i] == self.marker:
                self_cells_for_left += 1
            else:
                enemy_cells_for_left += 1
            left_i += 1

            if self.game_field[x][right_i] == self.game_field.empty_cell:
                empty_cells_for_right.append((x, right_i))
            elif self.game_field[x][right_i] == self.marker:
                self_cells_for_right += 1
            else:
                enemy_cells_for_right += 1
            right_i -= 1

            for y in range(length):
                if self.game_field[x][y] == self.game_field.empty_cell:
                    empty_cells_for_line.append((x, y))
                elif self.game_field[x][y] == self.marker:
                    self_ += 1
                else:
                    enemy_ += 1
            if length - self_ == 1 and empty_cells_for_line:
                self_cells_for_line = self_
                self_empty_cells_for_line = empty_cells_for_line
                break
            elif length - enemy_ == 1 and empty_cells_for_line:
                enemy_cells_for_line = enemy_
                enemy_empty_cells_for_line = empty_cells_for_line
                enemy_ = 0
                self_ = 0
                empty_cells_for_line = []
            else:
                enemy_ = 0
                self_ = 0
                empty_cells_for_line = []

        for y in range(length):
            for x in range(length):
                if self.game_field[x][y] == self.game_field.empty_cell:
                    empty_cells_for_line.append((x, y))
                elif self.game_field[x][y] == self.marker:
                    self_ += 1
                else:
                    enemy_ += 1
            if length - self_ == 1 and empty_cells_for_line:
                self_cells_for_line = self_
                self_empty_cells_for_line = empty_cells_for_line
                break
            elif length - enemy_ == 1 and empty_cells_for_line:
                enemy_cells_for_line = enemy_
                enemy_empty_cells_for_line = empty_cells_for_line
                enemy_ = 0
                self_ = 0
                empty_cells_for_line = []
            else:
                enemy_ = 0
                self_ = 0
                empty_cells_for_line = []

        if length - self_cells_for_left == 1 and empty_cells_for_left:
            return empty_cells_for_left[0]
        elif length - self_cells_for_right == 1 and empty_cells_for_right:
            return empty_cells_for_right[0]
        elif length - self_cells_for_line == 1 and self_empty_cells_for_line:
            return self_empty_cells_for_line[0]
        elif length - enemy_cells_for_left == 1 and empty_cells_for_left:
            return empty_cells_for_left[0]
        elif length - enemy_cells_for_right == 1 and empty_cells_for_right:
            return empty_cells_for_right[0]
        elif length - enemy_cells_for_line and enemy_empty_cells_for_line:
            return enemy_empty_cells_for_line[0]
        else:
            return random.randint(0, length-1), random.randint(0, length-1)


class Game:
    def __init__(self, players, game_field=Field(), turn=0):
        self.players = players
        self.game_field = game_field
        self.turn = turn
        self.cur_player = None

    def change_turn(self):
        self.turn = (self.turn + 1) % 2
        return self.turn

    def next_move(self):
        if not self.game_field.check_empty_cell():
            self.game_field.get_field()
            print("Удивительно! Ничья!")
            sys.exit(1)
        self.cur_player = self.players[self.change_turn()]
        if not self.cur_player.is_ii():
            self.game_field.get_field()
        return self.cur_player.next_move()

    def check_field_for_winner(self, marker):
        res_d_l = res_d_r = True
        res_l_h = res_l_v = False
        length = self.game_field.get_len()
        left_i = 0
        right_i = length - 1

        for x in range(length):
            if self.game_field[x][left_i] != marker:
                res_d_l = False
            left_i += 1

            if self.game_field[x][right_i] != marker:
                res_d_r = False
            right_i -= 1

            res_line = True
            for y in range(length):
                if self.game_field[x][y] != marker:
                    res_line = False
                    break
            res_l_h = res_l_h or res_line

        for y in range(length):
            res_line = True
            for x in range(length):
                if self.game_field[x][y] != marker:
                    res_line = False
                    break
            res_l_v = res_l_v or res_line

        return res_d_l or res_d_r or res_l_h or res_l_v


def game(player1, player2, game):
    while True:
        game.next_move()
        if game.cur_player.is_ii():
            game.game_field.get_field()
            print("Дай-ка подумать...")
            time.sleep(3)

        try:
            while True:
                if game.game_field.check_cell(game.cur_player.last_move):
                    game.game_field.make_move(game.cur_player.last_move, game.cur_player.marker)
                    break
                else:
                    game.cur_player.next_move()
        except IndexError:
            game.change_turn()
            os.system('CLS')
            print("Посмотри внимательно на поле и ходи правильно!")
            continue

        os.system('CLS')
        if game.check_field_for_winner(game.cur_player.marker):
            game.game_field.get_field()
            if not(not(player1.is_ii()) and player2.is_ii()):
                print("Поздравляю, {}! Ты выиграл!".format(game.cur_player.name))
            else:
                if game.cur_player.brain:
                    print("Ха-ха-ха! Человек, я снова победил тебя!")
                else:
                    print("Поздравляю тебя, {}! Тебе удалось обыграть меня!".format(game.cur_player.name))
            sys.exit(1)


def game_ii_via_human():
    name = input("Человек, как тебя называть? ")
    if input("Предоставлю тебе выбор, человек. Хочешь ходить первым? (y/n)").lower() == 'y':
        h_mark, c_mark = 'X', 'O'
        turn = 1
        print("Ok, даю тебе фору! Ты ходишь крестиками.")
    else:
        h_mark, c_mark = 'O', 'X'
        turn = 0
        print("Ok, крестики мои!")
    game_field = Field()
    player1 = Player(name, h_mark)
    player2 = Computer("Компьютер", c_mark, game_field)
    cur_game = Game((player1, player2), game_field, turn)

    game(player1, player2, cur_game)


def game_human_via_human():
    name1 = input("Кто будет ходить первым? ")
    name2 = input("Введите имя второго игрока: ")
    print("Ok, {} ходит крестиками, а {} - ноликами.".format(name1, name2))
    game_field = Field()
    player1 = Player(name1, "X")
    player2 = Player(name2, "O")
    cur_game = Game((player1, player2), game_field, 1)

    game(player1, player2, cur_game)


def game_ii_via_ii():
    name1 = input("Назовите компьютер, который будет играть первым: ")
    name2 = input("Назовите компьютер, который будет играть вторым: ")
    print("Ok, {} ходит крестиками, а {} - ноликами.".format(name1, name2))
    game_field = Field()
    player1 = Computer(name1, "X", game_field)
    player2 = Computer(name2, "O", game_field)
    cur_game = Game((player1, player2), game_field, 1)

    game(player1, player2, cur_game)


print("{:*^35}\nКоординаты ячейки вводятся через \n"
      "пробел в виде '№строки №столбца'.\nДля выхода введите q.\n\n"
      "Введите цифру, чтобы выбрать игру:\n1 -- Человек-Человек\n"
      "2 -- Человек-Компьютер\n3 -- Компьютер-Компьютер".format("Правила"))

while True:
    choose = input()
    if choose == "1":
        game_human_via_human()
    elif choose == "2":
        game_ii_via_human()
    elif choose == "3":
        game_ii_via_ii()
    elif choose == "q":
        print("Жаль, игра была бы такой интересной...")
        sys.exit(1)
    else:
        print("Ты что-то не то выбрал, посмотри повнимательнее.")
        continue
