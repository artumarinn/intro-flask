
use prueba;

create table Usuario(id int, email varchar(255), username varchar(50)); 

alter table Usuario add edad int;

alter table Usuario modify column email varchar(50);

insert into Usuario (email, username, edad)
values ('lala@correo.com', 'marin', 30);

delete from Usuario where email = 'arturo@correo.com' limit 1;

alter table Usuario add primary key (id);

alter table Usuario modify column id int auto_increment;

select* from Usuario where edad < 30;

select * from usuario;

update Usuario set edad = 32  where id = "2";

delete from Usuario where id = "2";






