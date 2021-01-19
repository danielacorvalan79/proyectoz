#Postgres y SQL

Realizar un `dump` desde la base de datos:
`pg_dump -U usuario_db nombre_db > nombre_archivo.sql`

Realizar un `restore` hacia la base de datos:
`psql -U usuario_db nombre_db < nombre_archivo.sql`
