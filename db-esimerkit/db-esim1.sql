-- Huom: Käyttäjät ja uudet tietokannat luodaan
-- pääkäyttäjänä, eli 'root'-tunnuksella

-- Uuden käyttäjän luonti, ÄLÄ käytä henkilökohtaista salasanaa
CREATE USER dbharkat@localhost IDENTIFIED BY 'salakala';
-- Annetaan uudelle käyttäjälle rajatut oikeudet tietokantaan
-- "ankkalinna", joka luodaan pari riviä alempana
GRANT SELECT, INSERT, UPDATE ON ankkalinna.* TO dbharkat@localhost;

-- Poistetaan tietokanta ennen uuden luontia, jos se on jo olemassa
DROP DATABASE IF EXISTS ankkalinna;

-- Luodaan ankkalinnatietokanta
CREATE DATABASE ankkalinna;
USE ankkalinna;

CREATE TABLE ankkalinnalainen(
    ID int not null auto_increment,
    etunimi varchar(40),
    sukunimi varchar(40),
    primary key (id)
);

create table lemmikki(
ID int not null auto_increment,
nimi varchar(40),
primary key (id)
);

create table omistaa(
lemmikki_ID int,
ankkalinnalainen_ID int,
primary key (lemmikki_ID,ankkalinnalainen_ID),
foreign key (lemmikki_ID) references lemmikki(ID),
foreign key (ankkalinnalainen_ID) references ankkalinnalainen(ID)
);

insert into ankkalinnalainen(etunimi, sukunimi)
values("Aku", "Ankka"),("Roope", "Ankka"),
("Tupu", "Ankka"), ("Milla", "Magia"), ("Mikki", "Hiiri");

insert into lemmikki(nimi)
values ("Pulivari"), ("Pluto"), ("Korri");

insert into omistaa(lemmikki_ID, ankkalinnalainen_ID)
values(1,1),(1,3),(2,5),(3,4);

-- Annetaan käyttäjälle luku- ja päivitysoikeudet tietokantaan ankkalinna
GRANT SELECT, INSERT, UPDATE ON ankkalinna.* TO python@localhost;
-- Kirjautuminen käyttäjällä (terminaali): mysql -u python -psalakala

-- Hae lemmikki-taulun kaikki sisältö
SELECT * FROM lemmikki;
