.mode table

CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;

select * from parents;
select * from dogs;
-- select * from sizes;

CREATE TABLE size_of_dogs AS
SELECT
  dogs.name,
  sizes.size
FROM
  dogs
JOIN
  sizes
ON
  dogs.height > sizes.min
  AND dogs.height <= sizes.max;


SELECT * from size_of_dogs;

CREATE TABLE by_parent_height AS SELECT  child
FROM parents JOIN dogs on parents.parent==dogs.name ORDER BY height DESC;
  


CREATE TABLE sentences AS  SELECT
  s1.child || ' and ' || s2.child || ' are ' || sd1.size || ' siblings.' AS sentence
FROM
  parents s1
JOIN
  parents s2
    ON s1.parent = s2.parent AND s1.child < s2.child
JOIN
  size_of_dogs sd1 ON s1.child = sd1.name
JOIN
  size_of_dogs sd2 ON s2.child = sd2.name
WHERE
  sd1.size = sd2.size
ORDER BY
  s1.child;

SELECT * FROM sentences
