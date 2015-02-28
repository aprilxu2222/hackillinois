drop table if exists users;
create table users (
	username text primary key,
	passsword text not null
)

drop table if exists tasks;
create table tasks (
  id integer primary key autoincrement,
  name text not null,
  deadline date not null,
  time text not null
);

drop table if exists subtasks;
create table subtasks (
  subtasks_id integer primary key autoincrement,
  tasks_id integer not null,
  name text not null,
  time text not null
);

drop table if exists daily;
create table daily (
  day date primary key,
  task_name text not null,
  task_time text not null,
);