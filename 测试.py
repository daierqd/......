import sqlite3
create table contacts (
	id integer primary key autoincrement,
	name text not null ,
	phone text not null default 'unknow');

