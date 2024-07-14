config = {
    "sqlalchemy.url": "mysql+mysqlconnector://python:pass@localhost:3306/company_db"
}

# run postgres server via docker
# docker run --name some-postgres -e POSTGRES_PASSWORD=password -d postgres
# docker run --name some-postgres -p 5432:5432 -e POSTGRES_PASSWORD=password -d postgres


postgres_conf = {
    'sqlalchemy.url': 'postgresql+psycopg2://postgres:password@localhost/postgres?options=-csearch_path=company_db',
    'sqlalchemy.echo': False,
}

