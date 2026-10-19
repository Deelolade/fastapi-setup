<!--==commands==-->

<!--1. To create a database migration ==> uv run alembic revision --autogenerate -m "initial schema"-->

<!--2. To drop  database and schemas ==> psql -U bloguser -d blog -c 'DROP SCHEMA public cascade; CREATE SCHEMA public;'-->

<!--3. To run the migration created ==> uv run alembic upgrade head -->

<!--4. To roll back on migrations ==> uv run alembic downgrade -1 ; to move back one migration -->

<!--5. To check what migrations you are on  ==> uv run alembic current -->

<!--6. To check migrations history   ==> uv run alembic history -->

<!--7. to work on postgresql in the CLI ==> export PATH="$PATH:/c/Program Files/PostgreSQL/18/bin"-->

<!--8. Boto3 is the official AWS SDK for Python maintained by Amazon Web Services that allows developers to create, configure, and manage AWS services using Python code -->

<!--9. add --dev when installing packages, so the packages are not used in production, E.G test dependencies  -->

<!--10.  -->