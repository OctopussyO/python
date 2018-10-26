# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла

import os

class Worker:
    def __init__(self, line_workers):
        line = line_workers.lstrip("\ufeff").rstrip("\n")
        self.name = line.split()[0] + " " + line.split()[1]
        self.info = {
            "name": self.name,
            "salary": line.split()[2],
            "position": line.split()[3],
            "working_hours": line.split()[4]
        }

    def get_info(self):
        return self.info

    def get_name(self):
        return self.name


class Payroll:
    def __init__(self, line_hours_of):
        line = line_hours_of.lstrip("\ufeff").rstrip("\n")
        self.name = line.split()[0] + " " + line.split()[1]
        self.salary = {
            "name": self.name,
            "worked_hours": line.split()[2],
            "cash": None
        }

    def get_info(self):
        return self.salary

    def get_name(self):
        return self.name


def formula(workers, payroll):
    for w_ in payroll:
        for w in workers:
            if w.get_name() == w_.get_name():
                time = int(w_.get_info()["worked_hours"])
                time_n = int(w.get_info()["working_hours"])
                salary = int(w.get_info()["salary"])
                if time == time_n:
                    w_.get_info().update({"cash": round(salary, 2)})
                elif time < time_n:
                    w_.get_info().update({"cash": round((salary * time / time_n), 2)})
                elif time > time_n:
                    w_.get_info().update({"cash": round((salary + (1 + (time - time_n) / time_n) * 2), 2)})


def read_file_as(file_name, class_name):
    with open(file_name, 'r', encoding="UTF-8") as f:
        return [class_name(line) for line in f][1:]


workers = read_file_as(os.path.join('data', 'workers.txt'), Worker)

payroll = read_file_as(os.path.join('data', 'hours_of.txt'), Payroll)

formula(workers, payroll)

print("Заработная плата работников составит:\n"\
      "{:<18}{:<10}{:<10}".format("Имя, фамилия", "Время, ч", "К выдаче, руб"))
for worker in payroll:
    print("{:<18}{:<10}{:<10}".format(worker.get_info()["name"], worker.get_info()["worked_hours"], worker.get_info()["cash"]))