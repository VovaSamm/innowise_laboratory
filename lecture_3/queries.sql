-- Создание таблицы студентов
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    birth_year INTEGER
);

-- Создание таблицы оценок
CREATE TABLE grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    grade INTEGER,
    FOREIGN KEY (student_id) REFERENCES students(id)
);

-- Добавление студентов
INSERT INTO students (full_name, birth_year) VALUES ('Ivan Ivanov', 2005);
INSERT INTO students (full_name, birth_year) VALUES ('Anna Petrova', 2006);

-- Добавление оценок
INSERT INTO grades (student_id, grade) VALUES (1, 5);
INSERT INTO grades (student_id, grade) VALUES (1, 4);
INSERT INTO grades (student_id, grade) VALUES (2, 3);

-- Отчёт по студентам
SELECT students.full_name, AVG(grades.grade)
FROM students
LEFT JOIN grades ON students.id = grades.student_id
GROUP BY students.id;

-- Лучший студент
SELECT students.full_name, AVG(grades.grade) AS avg_grade
FROM students
JOIN grades ON students.id = grades.student_id
GROUP BY students.id
ORDER BY avg_grade DESC LIMIT 1;