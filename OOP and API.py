class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def rating(self):
        sum_rating = 0
        len_rating = 0
        for course in self.grades.values():
            sum_rating += sum(course)
            len_rating += len(course)
        rating = round(sum_rating / len_rating, 3)
        return rating

    def rating_course(self, course):
        sum_rating = 0
        len_rating = 0
        for lesson in self.grades.keys():
            if lesson == course:
                sum_rating += sum(self.grades[course])
                len_rating += len(self.grades[course])
        rating = round(sum_rating / len_rating, 3)
        return rating

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}\n" \
              f"Средняя оценка за домашние задания: {self.rating()}\n" \
              f"Курсы в процессе изучения: {','.join(self.courses_in_progress)}\n" \
              f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Сравнивать преподователей и студентов нельзя!")
            return
        return self.rating() < other.rating()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def rating(self):
        sum_rating = 0
        len_rating = 0
        for course in self.grades.values():
            sum_rating += sum(course)
            len_rating += len(course)
        rating = round(sum_rating/len_rating, 2)
        return rating

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.rating()}"
        return res

    def rating_course(self, course):
        sum_rating = 0
        len_rating = 0
        for lesson in self.grades.keys():
            if lesson == course:
                sum_rating += sum(self.grades[course])
                len_rating += len(self.grades[course])
        rating = round(sum_rating / len_rating, 2)
        return rating

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Сравнивать преподователей и студентов нельзя!")
            return
        return self.rating() < other.rating()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f"Имя: {self.name} \nФамилия: {self.surname}"
        return res


student_1 = Student('Roy', 'John', 'man')
student_1.courses_in_progress += ['Python', 'git']
student_1.finished_courses += ['Введение в програмирования']

student_2 = Student('Eman', 'Smith', 'man')
student_2.courses_in_progress += ['Python']
student_2.finished_courses += ['git', 'Ввудение в програмирование']

student_3 = Student('Emma', 'Ross', 'women')
student_3.courses_in_progress += ['git']
student_3.finished_courses += ['Python']

reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['git']


lecturer_1 = Lecturer('Tom', 'John')
lecturer_1.courses_attached += ['Python']
lecturer_2 = Lecturer('Clark', 'Kent')
lecturer_2.courses_attached += ['git']


student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_1.rate_lecturer(lecturer_1, 'Python', 8)
student_1.rate_lecturer(lecturer_1, 'Python', 9)
student_1.rate_lecturer(lecturer_2, 'git', 8)
student_1.rate_lecturer(lecturer_2, 'git', 9)
student_1.rate_lecturer(lecturer_2, 'git', 9)

student_2.rate_lecturer(lecturer_1, 'Python', 10)
student_2.rate_lecturer(lecturer_1, 'Python', 9)
student_2.rate_lecturer(lecturer_1, 'Python', 10)
student_2.rate_lecturer(lecturer_2, 'git', 10)
student_2.rate_lecturer(lecturer_2, 'git', 7)
student_2.rate_lecturer(lecturer_2, 'git', 7)

student_3.rate_lecturer(lecturer_1, 'Python', 9)
student_3.rate_lecturer(lecturer_1, 'Python', 10)
student_3.rate_lecturer(lecturer_1, 'Python', 10)
student_3.rate_lecturer(lecturer_2, 'git', 10)
student_3.rate_lecturer(lecturer_2, 'git', 10)
student_3.rate_lecturer(lecturer_2, 'git', 10)

reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Git', 10)
reviewer_1.rate_hw(student_1, 'Git', 10)

reviewer_1.rate_hw(student_2, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Python', 9)
reviewer_1.rate_hw(student_2, 'Git', 8)
reviewer_1.rate_hw(student_2, 'Git', 8)

reviewer_1.rate_hw(student_3, 'Python', 10)
reviewer_1.rate_hw(student_3, 'Python', 10)
reviewer_1.rate_hw(student_3, 'Python', 10)
reviewer_1.rate_hw(student_3, 'Git', 10)
reviewer_1.rate_hw(student_3, 'Git', 10)

student_list = [student_1, student_2, student_3]
reviewer_list = [reviewer_1]
lecturer_list = [lecturer_1, lecturer_2]


def rating_courses(courses, student_list):
    sum_rating = 0
    quantity_rating = 0
    for stud in student_list:
        for course in stud.grades:
            stud_rating = stud.rating_course(course)
            sum_rating += stud_rating
            quantity_rating += 1
    rating = round(sum_rating / quantity_rating, 2)
    return rating


print(reviewer_1)
print(lecturer_1)
print(lecturer_2)
print(student_1)
print(student_2)
print(rating_courses('Python', student_list))
print(rating_courses('Python', lecturer_list))
print(rating_courses('git', student_list))
print(rating_courses('git', lecturer_list))
