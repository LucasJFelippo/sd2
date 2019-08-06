CREATE DATABASE "project";

CREATE TABLE "usuario"(
    "cod" SERIAL,
    "nome" VARCHAR(100),
    "login" VARCHAR(32),
    "altura" FLOAT,
    "idade" INT,
    "email" VARCHAR(200),
    "senha" VARCHAR(92),
    CONSTRAINT "usuariopk" PRIMARY KEY ("cod")
)

INSERT INTO "usuario" ("nome", "login", "altura", "idade", "email", "senha") VALUES ('Lucas', 'lucas', 1.8, 18, 'lucas@gmail.com', '12345');

SELECT * FROM "usuario";