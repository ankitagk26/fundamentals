CREATE TABLE department (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50) NOT NULL,
    location VARCHAR(50)
);

CREATE TABLE student (
    roll_no INT PRIMARY KEY,
    name VARCHAR(60) NOT NULL,
    dept_id INT,
    marks INT,
    city VARCHAR(40),
    FOREIGN KEY (dept_id) REFERENCES department(dept_id)
);

INSERT INTO department (dept_id, dept_name, location) VALUES
(1, 'Computer Science', 'Block A'),
(2, 'mechanics', 'Block B'),
(3, 'Economics', 'Block C');

INSERT INTO student (roll_no, name, dept_id, marks, city) VALUES
(1011, 'Aarav', 1, 92, 'Bengaluru'),
(1012, 'Meera', 1, 88, 'Mysuru'),
(1013, 'Verma', 2, 76, 'Bengaluru'),
(1014, 'Ananya', 1, 95, 'Mangaluru'),
(1015, 'Kabir', 3, 68, 'Bengaluru'),
(1016, 'Diya', NULL, 84, 'Bengaluru');

UPDATE student
SET marks = 90
WHERE roll_no = 1012;

DELETE FROM student
WHERE roll_no = 1015;

SELECT roll_no, name, marks
FROM student
WHERE marks >= 85
ORDER BY marks DESC;

SELECT name, city
FROM student
WHERE name LIKE 'A%';

SELECT d.dept_name,
       COUNT(s.roll_no) AS total_students,
       AVG(s.marks) AS avg_marks,
       MAX(s.marks) AS highest_marks
FROM department d
LEFT JOIN student s ON d.dept_id = s.dept_id
GROUP BY d.dept_name
HAVING COUNT(s.roll_no) >= 1;

SELECT s.roll_no, s.name, d.dept_name, s.marks
FROM student s
INNER JOIN department d ON s.dept_id = d.dept_id
ORDER BY s.roll_no;

SELECT s.roll_no, s.name, d.dept_name, s.marks
FROM student s
LEFT JOIN department d ON s.dept_id = d.dept_id
ORDER BY s.roll_no;
