create table pessoa (
	cpf numeric(11) not null,
	nome varchar(100) not null,
	sexo varchar(1) not null,
	telefone numeric(11) not null
)


drop table pessoa
Alter Table computador
Add cpf numeric(11) not null

select * from pessoa


alter table computador
drop telefone

alter table pessoa
add constraint pk_pessoa primary key (cpf)

alter table pessoa
alter column telefone
type varchar(14)

create table computador(
	codigo numeric(4) not null,
	marca varchar(50) not null,
	modelo varchar(50) not null
)

select * from computador

insert into pessoa (cpf, nome, sexo, telefone) values (12312312311, 'Vitão','F', '(48)9985-45906')
insert into pessoa (cpf, nome, sexo, telefone) values (12312312312, 'Alisso','M', '(48)9999-99990')


insert into computador (codigo, marca, modelo, cpf) values (1224, 'porsche','panameira', 12312312310)
delete from computador where telefone

alter table computador
add constraint pk_computador primary key (codigo)

alter table computador add constraint FK_computador_pessoa foreign key (cpf) references pessoa(cpf)