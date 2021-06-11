drop table if exists usuario;
drop table if exists produto;
Create table usuario (
    cpf integer not null primary key,
	nome varchar(70) not null,
	login varchar(20) not null unique,
	senha varchar(20)
);
insert into usuario values (11122233344, 'Jonas Apolinario','Admin','@super@');
CREATE TABLE produto (
	codprod	integer NOT NULL primary key,
	dsprod	varchar(70),
	saldo	integer,
	sldmin	integer,
	prvenda	numeric(10, 2),
	prcusto	numeric(10, 2)
);

