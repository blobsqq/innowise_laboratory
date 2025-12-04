-- SQL Queries

-- 1. Create tables
-- Table with students
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTO_INCREMENT, -- Primary key
    full_name TEXT NOT NULL, -- Full name of the student
    birth_year INTEGER NOT NULL -- Year of birth
);

-- Table with student grades
CREATE TABLE IF NOT EXISTS grades (
    id INTEGER PRIMARY KEY AUTO_INCREMENT, -- Primary key
    student_id INTEGER NOT NULL, -- Student id
    subject TEXT NOT NULL, -- Name of the subject
    grade INTEGER NOT NULL CHECK(grade > 0 AND grade < 101), -- Grade between 1 and 100
    FOREIGN KEY (student_id) REFERENCES students (id) -- Foreign key for student_id
);


-- Create indexes to optimize queries.
-- Index for 'JOIN grades ON grades.student_id = students.id'
CREATE INDEX IF NOT EXISTS idx_grades_student_id ON grades(student_id);


-- 2. Insert data
-- Add data to 'students' table
INSERT INTO students (full_name, birth_year)
VALUES  ('Alice Johnson', 2005),
        ('Brian Smith', 2004),
        ('Carla Reyes', 2006),
        ('Daniel Kim', 2005),
        ('Eva Thompson', 2003),
        ('Felix Nguyen', 2007),
        ('Grace Patel', 2005),
        ('Henry Lopez', 2004),
        ('Isabella Martinez', 2006);

--  Add data to 'grades' table
INSERT INTO grades (student_id, subject, grade)
VALUES  (1, 'Math', 88),
        (1, 'English', 92),
        (1, 'Science', 85),
        (2, 'Math', 75),
        (2, 'History', 83),
        (2, 'English', 79),
        (3, 'Science', 95),
        (3, 'Math', 91),
        (3, 'Art', 89),
        (4, 'Math', 84),
        (4, 'Science', 88),
        (4, 'Physical Education', 93),
        (5, 'English', 90),
        (5, 'History', 85),
        (5, 'Math', 88),
        (6, 'Science', 72),
        (6, 'Math', 78),
        (6, 'English', 81),
        (7, 'Art', 94),
        (7, 'Science', 87),
        (7, 'Math', 90),
        (8, 'History', 77),
        (8, 'Math', 83),
        (8, 'Science', 80),
        (9, 'English', 96),
        (9, 'Math', 89),
        (9, 'Art', 92);


-- 3. Find all grades for a specific student (Alice Johnson).
SELECT students.full_name, grades.subject, grades.grade
FROM grades
JOIN students ON grades.student_id = students.id
WHERE students.full_name = 'Alice Johnson';

-- 4. Calculate the average grade per student.
SELECT students.full_name,
		AVG(grades.grade) AS average_grade
FROM students
JOIN grades ON grades.student_id = students.id
GROUP BY students.id, students.full_name;

-- 5. List all students born after 2004.
SELECT *
FROM students
WHERE students.birth_year > 2004;

-- 6. Create a query that lists all subjects and their average grades.
SELECT subject, AVG(grade) as average_grade
FROM grades
GROUP BY subject;

-- 7. Find the top 3 students with the highest average grades.
SELECT students.full_name as full_name,
		AVG(grades.grade) as average_grade
FROM students
JOIN grades ON grades.student_id = students.id
GROUP BY students.full_name
ORDER BY average_grade DESC
LIMIT 3;

-- 8. Show all students who have scored below 80 in any subject.
SELECT DISTINCT students.full_name
FROM students
JOIN grades ON grades.student_id = students.id
WHERE grades.grade < 80;