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
<<<<<<< HEAD
  time text not null
);
=======
  duration text not null
);
/*
drop table if exists daily;
create table daily (
  day date primary key,
  task_name text not null,
  task_time text not null,
);*/
>>>>>>> f15279dbf6ec98bed8c179a035fbfb303af1c6a4
