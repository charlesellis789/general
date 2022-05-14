-- Postgresql
-- drop table
drop table if exists [table name];

-- allows use of guid generators
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- create index
create index [index name] on [table name]([column name]);

-- create table
create table [table name] (
	[primary key name] serial primary key,
	[column name] varchar(10)
);

-- select all table names and details
select * from information_schema.tables 
where table_schema = 'public';

-- insert into table template
insert into [table name] (
	[column name 1],
	[column name 2]
)
select
	[column name 1],
	[column name 2]
from [table name]
on conflict do nothing;

-- select all database names
select datname
from pg_database 
order by datname