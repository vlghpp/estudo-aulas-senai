create table pedido (
	cod numeric(7) not null, 
	valor varchar(80) not null,
	cpf numeric(11) not null,
	
	PRIMARY KEY(cod)
	FOREIGN KEY(cpf), REFERENCES cliente(cpf)
)


create table cliente(
	cpf numeric(11) not null unique,
	nome varchar(100) not null,
	fone numeric(11) not null 
)

create table itens(
	cod_carro numeric(7) not null unique,
	cod_pedido numeric(7) not null unique,
	
	FOREIGN KEY (cod_pedido) REFERENCES pedido (cod),
	FOREIGN KEY (cod_carro) REFERENCES carro (cod)
)


create table carro(
	cod numeric(7) not null,
	modelo varchar(80) not null unique,
	valor float(8) not null,
	PRIMARY KEY (cod)
)
