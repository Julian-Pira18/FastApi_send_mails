-- Elimina la base de datos si existe
-- DROP DATABASE IF EXISTS emails_db;

-- Crea la base de datos 
-- CREATE database emails_db;


-- Inserción de datos en la tabla 'users'
INSERT INTO users (id, name, lastname, email, password, photo_url, role_id)
VALUES
(1, 'Jose', 'Pira', 'pirajulian568@gmail.com', 'password123', 'https://example.com/john.jpg', 1),
(2, 'Jane', 'Smith', 'jane.smith@example.com', 'password456', 'https://example.com/jane.jpg', 2);

-- Inserción de datos en la tabla 'course'
INSERT INTO course (id, name, description, photo_url, is_public, rquirements, max_amount_students, author_id, professor_id)
VALUES
(1, 'Course 1', 'Introduction to Python', 'https://example.com/course1.jpg', TRUE, 'Basic programming knowledge', 1, 1, 2),
(2, 'Course 2', 'Advanced Machine Learning', 'https://example.com/course2.jpg', TRUE, 'Basic Python and ML knowledge', 20, 1, 1),
(3, 'Course 3', 'Database Management', 'https://example.com/course3.jpg', FALSE, 'SQL knowledge required', 1, 2, 2);

-- Inserción de datos en la tabla 'event'
INSERT INTO event (name, date, course_id, event_link)
VALUES
('Event 1', NOW(), 1, 'https://example.com/event1'),
('Event 2', NOW(), 1, 'https://example.com/event2'),
('Event 4', NOW(), 2, 'https://example.com/event2'),
('Event 5', NOW(), 2, 'https://example.com/event2'),
('Event 6', NOW(), 3, 'https://example.com/event2'),
('Event 3', NOW(), 3, 'https://example.com/event3');

-- Inserción de datos en la tabla 'user_course'
INSERT INTO user_course (user_id, course_id)
VALUES
(1, 1),
(1, 2),
(1, 3),
(2, 2);