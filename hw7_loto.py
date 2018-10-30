import random
import sys
import os


class CardGenerator:
    def make_card(self):
        nums = set()
        while len(nums) < self._n * self._lines:
            nums.add(random.randint(1, self._N))
        self.card = [list(nums)[i:i + self._n] for i in range(0, self._n * self._lines, self._n)]
        random.shuffle(self.card)

        for line in self.card:
            empty = self._empty
            while empty > 0:
                n_empty = random.randint(0, len(line) - 1)
                if line[n_empty] != " ":
                    line[n_empty] = " "
                    empty -= 1

        return self.card

    def __init__(self, title="Карта", N=90, lines=3, n=9, empty=4):
        self.title = title
        self._N = N
        self._lines = lines
        self._n = n
        self._empty = empty
        self.card = self.make_card()
        self.score = 0

    def __str__(self):
        return "{:-^27}\n{}\n{:-^27}\n".format(self.title, \
                "\n".join(' '.join(str(x) if len(str(x)) == 2 else " " + str(x) \
                                   for x in line) for line in self.card), "-")

    def search(self, num):
        for line in self.card:
            if num in line:
                line[line.index(num)] = "X"
                self.score += 1
                if self.score == 15:
                    print("Победила {}!".format(self.title))
                    sys.exit(1)
                return True
        else:
            return False


class Barrel:
    def __init__(self, N=90):
        self._quantity = N
        self._bag = [x for x in range(1, self._quantity + 1)]
        random.shuffle(self._bag)
        self.current_barrel = 0

    def get_barrel(self):
        self.current_barrel = self._bag.pop()
        print("Новый бочонок: {} (осталось {})\n".format(self.current_barrel, len(self._bag)))


def game():
    comp = CardGenerator("Карта Компьютера")
    comp.make_card()
    chel = CardGenerator("Карта Человека")
    chel.make_card()
    bag = Barrel()

    while True:
        bag.get_barrel()
        print(comp)
        print(chel)
        user_answer = input('Зачеркнуть цифру? (y/n) ')
        if user_answer.lower() == "y":
            if chel.search(bag.current_barrel):
                print("Ход выполнен, игра продолжается.")
                comp.search(bag.current_barrel)
                continue
            elif not chel.search(bag.current_barrel):
                print("Человек, на твоей карточке нет такой цифры. Game over!")
                sys.exit(1)
        elif user_answer.lower() == "n":
            if chel.search(bag.current_barrel):
                print("Человек, ты пропустил цифру на своей карте. Game over!")
                sys.exit(1)
            elif not chel.search(bag.current_barrel):
                comp.search(bag.current_barrel)
                continue


with open(os.path.join('data', 'loto.txt'), 'r', encoding='UTF-8') as rules:
    for line in rules:
        print(line.rstrip('\n'))

user_ans = input("\nВы хотите сыграть? (y/n) ")
if user_ans.lower() == "y":
    game()
else:
    sys.exit(1)
