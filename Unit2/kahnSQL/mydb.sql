/** Grocery list:
Bananas (4)
Peanut Butter (1)
Dark Chocolate Bars (2)
**/

CREATE TABLE groceries (id INTEGER PRIMARY KEY, name TEXT, quantity INTEGER );

INSERT INTO groceries VALUES (1, "Bananas", 4);
INSERT INTO groceries VALUES (2, "Peanut Butter", 1);
INSERT INTO groceries VALUES (3, "Dark chocolate bars", 2);


-- sql queries use select.
SELECT name FROM groceries;

SELECT * FROM groceries WHERE aisle > 5 ORDER BY aisle;

-- SQL engine first does grouping of the rows based on aisle. So first group by, THEN sums up the quantity in each of those groups, then finally it selects teh first aisle value that it saw in each group. You can get innacurate data if you use something different, for example, SELECT name ... GROUP BY aisle. They should be the same to accurately display the data in this case 
SELECT aisle, SUM(quantity) FROM groceries GROUP BY aisle;

-- Aggregate function-> useful for things like getting the max/min, sum, average of values in our database
