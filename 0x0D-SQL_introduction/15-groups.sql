-- a script that lists the number of records with the same score in the table
select score, count(*) as number from second_table
group by score
order by number desc;
