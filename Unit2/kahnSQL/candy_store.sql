CREATE TABLE candy_store (id INTEGER PRIMARY KEY, name TEXT, candy_type TEXT, quantity INTEGER, price INTEGER);

INSERT INTO candy_store VALUES (1, "Lemon Drop", "hard", 1, 5.00);
INSERT INTO candy_store VALUES (2, "LollyWhirl", "sour", 10, 50.01);
INSERT INTO candy_store VALUES (3, "Droooop", "hard", 5, 30.45);
INSERT INTO candy_store VALUES (4, "BOOM", "hard", 100, 40.10);
INSERT INTO candy_store VALUES (5, "Whatevers", "gummy", 80, 10.11);
INSERT INTO candy_store VALUES (6, "Jummy", "hard", 1, .70);
INSERT INTO candy_store VALUES (7, "Dooopsys", "gummy", 4, .50);
INSERT INTO candy_store VALUES (8, "Drops", "sour", 8, 1.50);
INSERT INTO candy_store VALUES (9, "Lemonies", "sour", 11, 2.50);
INSERT INTO candy_store VALUES (10, "Fun Stuff", "sour", 10, 5.29);
INSERT INTO candy_store VALUES (11, "Yummers", "gummy", 10, 1.01);
INSERT INTO candy_store VALUES (12, "Jungle Butt", "gummy", 11, 50.22);
INSERT INTO candy_store VALUES (13, "Funky Food", "drink", 10, 5.99);
INSERT INTO candy_store VALUES (14, "Tetete", "drink", 55, 1.99);
INSERT INTO candy_store VALUES (15, "Zaps", "sour", 10, 0.35);

SELECT price, name FROM candy_store ORDER BY price;
