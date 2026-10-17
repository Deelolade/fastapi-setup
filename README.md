<!--==commands==-->

<!--1. To create a database migration ==> uv run alembic revision --autogenerate -m "initial schema"-->

<!--2. To drop  database and schemas ==> psql -U bloguser -d blog -c 'DROP SCHEMA public cascade; CREATE SCHEMA public;'-->

<!--3. To run the migration created ==> uv run alembic upgrade head -->

<!--4. To roll back on migrations ==> uv run alembic downgrade -1 ; to move back one migration -->

<!--5. To check what migrations you are on  ==> uv run alembic current -->

<!--6. To check migrations history   ==> uv run alembic history -->

<!--7. to work on postgresql in the CLI ==> export PATH="$PATH:/c/Program Files/PostgreSQL/18/bin"-->