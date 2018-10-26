# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class Human:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return "%s" % self.name


class Pupil(Human):
    def __init__(self, name, class_r, mother=None, father=None):
        super().__init__(name)
        self.class_r = class_r
        self.mother = mother
        self.father = father

    def set_mother(self, human):
        self.mother = human

    def set_father(self, human):
        self.father = human

    def get_parents(self):
        return "Родители ученика {}:\nотец {}\nмать {}".format(self.name, self.father, self.mother)

    def get_class_r(self):
        return self.class_r


class Teacher(Human):
    def __init__(self, name, subject, classes):
        super().__init__(name)
        self.subject = subject
        self.classes = classes

    def add_class(self, new_class):
        if not Class(new_class, self.school_n) in self.classes:
            self.classes.append(Class(new_class, self.school_n))
        else:
            print("Данный учитель уже преподаёт в указанном классе.")

    def get_classes(self):
        return self.classes

    def get_subjects(self):
        return self.subject


class School:
    def __init__(self, name, teachers, pupils):
        self.name = name
        self.teachers = teachers
        self.pupils = pupils

    def add_teacher(self, new_teacher, subject):
        if not Teacher(new_teacher, subject, []) in self.teachers:
            self.teachers.append(Teacher(new_teacher, subject, []))
        else:
            print("Этот учитель уже работает в данной школе.")

    def add_class(self, new_class):
        if not Class(new_class, self.name) in self.classes:
            self.classes.append(Class(new_class, self.name))
        else:
            print("Этот класс уже есть в данной школе.")

    def add_subject(self, new_subject):
        if not new_subject in self.subjects:
            self.subjects.append(new_subject)
        else:
            print("Этот предмет уже преподается в данной школе.")

    def get_classes_list(self):
        classes_list = set([pupil.get_class_r() for pupil in self.pupils])
        return classes_list

    def get_pupils(self, class_r):
        return [pupil.get_name() for pupil in self.pupils if class_r == pupil.get_class_r()]

    def pupil_info(self, name):
        for human in self.pupils:
            if name == human.get_name():
                teachers_ = [teacher.get_name() for teacher in self.teachers
                             if human.get_class_r() in teacher.get_classes()]
                subjects_ = [teacher.get_subjects() for teacher in self.teachers
                             if human.get_class_r() in teacher.get_classes()]
                return {
                    "name": name,
                    "class_r": human.get_class_r(),
                    "teachers": teachers_,
                    "subjects": subjects_
                }

    def pupil_parents(self, name):
        for human in self.pupils:
            if name == human.get_name():
                return human.get_parents()

    def get_teachers(self, class_r):
        teachers_ = [teacher.get_name() for teacher in self.teachers() if class_r in teacher.get_classes()]
        return teachers_


teachers = [
    Teacher("Иванов Иван Иванович", "математика", ["8А", "10Б", "9Г", "7Г", "7А"]),
    Teacher("Петров Пётр Петрович", "русский язык", ["8А", "10Б", "9Г", "7Г", "7А"]),
    Teacher("Сидоров Пантелеймон Карлович", "история", ["8А", "10Б", "9Г", "7Г", "7А"]),
    Teacher("Сидорова Клавдия Петровна", "черчение", ["10Б", "9Г"])
]

pupils = [
    Pupil("Антонов Антон Игоревич", "9Г", "Антонова Антонина Петровна", "Антонов Игорь Сидорович"),
    Pupil("Болгов Артем Игоревич", "10Б", "Болгова Регина Витальевна", "Болгов Игорь Зигмундович"),
    Pupil("Васильев Денис Филиппович", "7А", "Васильева Олимпиада Стефановна", "Васильев Альберт Энштейнович"),
    Pupil("Васильева Наталья Васильевна", "7Г", "Эпштейн Мария Витальевна", "Васильев Василий  Васильевич"),
    Pupil("Волова Анна Дмитриевна", "7А", "Волова Анна Павловна", "Волов Дмитрий Поликарпович"),
    Pupil("Глембо Алексей Сергеевич", "8А", "Глембо Маргарита Васильевна", "Глембо Исаак Ньютонович"),
    Pupil("Грачёва Анна Алексеевна", "10Б", "Грачёва Зинаида Дмитриевна", "Грачёв Алексей Семёнович"),
    Pupil("Гунькина Дарья Александровна", "7Г", "Гунькина Серафима Семёновна", "Гунькин Александр Владимирович"),
    Pupil("Докучаева Кристина Алексеевна", "9Г", "Докучаева Марина Анатольевна", "Докучаев Алексей Алексеевич"),
    Pupil("Зеленов Владимир Эдуардович", "10А", "Зеленова Роза Андреевна", "Докучаев Эдуард Антонович"),
    Pupil("Ишмухаметова Элина Ильдаровна", "10А", "Ишмухаметова Фарида Назировна", "Ишмухаметов Ильдар Резанович"),
    Pupil("Калёнова Екатерина Денисовна", "9Г", "Калёнова Леана Фархатовна", "Калёнов Денис Денисович"),
    Pupil("Коновалова Арина Александровна", "8А", "Коновалова Адель Витальевна", "Коновалов Александр Андреевич"),
    Pupil("Корбей Анастасия Сергеевна", "9Г", "Корбей Зинаида Павловна", "Корбей Сергей Сергеевич"),
    Pupil("Крицкая Екатерина Владимировна", "10А", "Крицкая Вилена Ильинична", "Крицкий Владимир Владимирович")
    ]

school = School("Гимназия №4", teachers, pupils)

print("Список классов школы: \n")
print(school.get_classes_list())

print("\nУченики 9Г класса:\n", "\n".join(school.get_pupils("9Г")), sep = "")

pupil = school.pupil_info("Коновалова Арина Александровна")
print("\nУченик {}, {} класс:\nУчителя: {}\nПредметы: {}".format(pupil["name"], pupil["class_r"], ", ".join(pupil["teachers"]), ", ".join(pupil["subjects"])))

print("\n", school.pupil_parents("Калёнова Екатерина Денисовна"), sep="")
