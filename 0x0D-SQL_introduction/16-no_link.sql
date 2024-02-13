-- a script that lists all records of the table
select score, name from second_table
where name is not NULL
order by score desc;
