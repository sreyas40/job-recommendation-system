
FROM mysql:latest

ENV MYSQL_ROOT_PASSWORD=root_password
ENV AUTH_DATABASE=authDB
ENV USER_DATABASE=usersDB
ENV AUTHAPI_HOST=authapi
ENV USERAPI_HOST=userapi

COPY 01-init.sql /docker-entrypoint-initdb.d/01-init.sql
COPY 02-UtilsDB-4.sql /docker-entrypoint-initdb.d/02-UtilsDB.sql
COPY 03-Data-28072024.sql /docker-entrypoint-initdb.d/03-Data.sql

EXPOSE 3306
