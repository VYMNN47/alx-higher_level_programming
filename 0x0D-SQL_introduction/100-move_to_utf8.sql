-- a script that converts hbtn_0c_0 database to UTF8
use hbtn_0c_0
alter table first_table
convert to character set tf8mb4 collate utf8mb4_unicode_ci;
