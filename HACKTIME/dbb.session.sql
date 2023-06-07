
-- CREATE TABLE programmers(
--     id SERIAL PRIMARY KEY,
--     first_name VARCHAR(20),
--     last_name VARCHAR(30),
--     login VARCHAR(40),
--     email VARCHAR(40),
--     country VARCHAR(50),
--     salary FLOAT ,
--     programmer_level VARCHAR(60)
-- );

-- SELECT * FROM programmers;

-- INSERT INTO programmers(
--     first_name,
--     last_name,
--     login,
--     email,
--     country,
--     salary,
--     programmer_level
-- )

-- VALUES(
--     'Zinaddin',
--     'Zidan',
--     'zidi',
--     'ziddna@gmail.com',
--     'France',
--     990000,
--     'senior'
-- );


-- Отсортируйте всех пользователей по логину

-- SELECT * FROM programmers
-- ORDER BY login;

-- Отсортируйте всех пользователей по стране
-- SELECT * FROM programmers
-- ORDER BY country;


-- Отсортируйте всех пользователей по emaily
-- SELECT * FROM programmers
-- ORDER BY email;

-- SELECT * FROM programmers
-- ORDER BY login;

-- SELECT id, first_name FROM programmers;

-- Запрос гле логин содержит  as , и т.д

-- SELECT * FROM programmers
-- WHERE email LIKE '%zi%' OR email LIKE '%am%'
-- OR email LIKE '%si%'
-- OR email LIKE '%am%' OR email LIKE '%qwe%' OR email LIKE '%er%'
-- OR email LIKE '%ka%' OR email LIKE '%Z%'; 

-- Запрос где логин заканчивается на lol , kan , ck, ie, ig

-- SELECT * FROM programmers
-- WHERE login like '%ma%' OR login LIKE '%m%';


-- SELECT max(salary) FROM programmers
-- WHERE country='France' AND programmer_level='Senior';
