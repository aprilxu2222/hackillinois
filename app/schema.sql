drop table if exists users;
create table users (
	username text primary key,
	password text not null
);

drop table if exists tasks;
create table tasks (
  id integer primary key autoincrement,
  name text not null,
  deadline date not null,
  duration text not null
);
