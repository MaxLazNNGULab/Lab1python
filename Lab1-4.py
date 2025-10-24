List_students_prev = ["Иванов", "Петров", "Зайцева", "Галкина", "Смирнова"]

list_students_result_session = ["Иванов", "Медведев", "Зайцева", "Ворошилова", "Смирнова"]

list_result_session = [
    {"информатика":4, "высшая алгебра":5,"философия":3,"история":4},
    {"физика":4, "высшая алгебра":5,"философия":4,"история":4},
    {"информатика":4, "мат анализ":3,"философия":3,"история":4},
    {"информатика":4, "высшая алгебра":5,"английский":4,"история":4},
    {"информатика":4, "высшая алгебра":5,"философия":4,"история":4}
]

students_grades = {}
for i, student in enumerate(list_students_result_session):
    students_grades[student] = list_result_session[i]

result = []

for student in List_students_prev:
    if student in students_grades:
        grades = students_grades[student].values()
        if all(grade > 3 for grade in grades):
            result.append(student)

for student in result:
    print(student)