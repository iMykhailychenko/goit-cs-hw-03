--Get all tasks of a specific user. Use SELECT to retrieve tasks by user_id.
SELECT title, description, status_id
FROM tasks
WHERE user_id = 5;

--Select tasks with a specific status. Use a JOIN to select tasks with a specific status, for example, 'new'.
SELECT title
FROM tasks t
JOIN status s ON t.status_id = s.id
WHERE s.name = 'new';

--Update the status of a specific task. Change the status of a specific task to 'in progress' or another status.
UPDATE tasks
SET status_id = (
	SELECT id
	FROM status
	WHERE name = 'in progress'
)
WHERE id = 72;

--Get a list of users who have no tasks at all. Use combination of SELECT, WHERE NOT EXISTS, and a subquery to get a list of users without tasks.
SELECT *
FROM users u
WHERE NOT EXISTS (
	SELECT 1
	FROM tasks t
	WHERE t.user_id = u.id
);

--Add a new task for a specific user. Use INSERT to add a new task.
INSERT INTO tasks (title, description, status_id, user_id)
VALUES ('Custom task', 'It is manually added task for user #4', 1, 4);

--Get all tasks that are not yet completed. Select tasks where the status is not 'completed'.
SELECT *
FROM tasks
WHERE status_id != (
	SELECT id
	FROM status
	WHERE name = 'completed'
);

--Delete a specific task. Use DELETE to delete a task by its id.
DELETE FROM tasks
WHERE id = 32;

--Find users with a specific email. Use SELECT with a LIKE condition to filter users by email.
SELECT fullname
FROM users
WHERE email LIKE '%.com';

--Update a user's name. Change a user's name using UPDATE.
UPDATE users
SET fullname = 'TestName'
WHERE id = 48;

--Get the number of tasks for each status. Use SELECT, COUNT, GROUP BY to group tasks by statuses.
SELECT s.name AS status_name, COUNT(*) AS task_count
FROM tasks t
JOIN status s ON t.status_id = s.id
GROUP BY s.name;

--Get tasks assigned to users with a specific email domain. Use SELECT with a LIKE condition in combination with JOIN to select tasks assigned to users whose email contains a specific domain (for example, '%@example.com').
SELECT u.fullname, u.email, t.title, t.status_id
FROM tasks t
JOIN users u ON t.user_id = u.id
WHERE u.email LIKE '%@example.com';

--Get a list of tasks without a description. Select tasks where the description is missing.
SELECT *
FROM tasks
WHERE description IS NULL;

--Get users and their tasks that are in progress. Use INNER JOIN to get a list of users and their tasks with a specific status.
SELECT u.fullname, t.title, t.status_id
FROM users u
JOIN tasks t ON t.user_id = u.id
JOIN status s ON t.status_id = s.id
WHERE s.name = 'in progress';

--Get users and the number of their tasks. Use LEFT JOIN and GROUP BY to get a list of users and the number of their tasks.
SELECT u.fullname, COUNT(t.user_id) AS task_count
FROM users u
LEFT JOIN tasks t ON u.id = t.user_id
GROUP BY u.fullname;
