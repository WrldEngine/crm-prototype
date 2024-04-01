# CRM Prototype on FastAPI
![Watchers](https://img.shields.io/github/watchers/WrldEngine/crm-prototype?)
![Forks](https://img.shields.io/github/forks/WrldEngine/crm-prototype)
![Stars](https://img.shields.io/github/stars/WrldEngine/crm-prototype)

<div>
  <img src="https://img.shields.io/badge/fastapi-black?style=for-the-badge&logo=fastapi"/>
  <img src="https://img.shields.io/badge/redis-black?style=for-the-badge&logo=redis"/>
  <img src="https://img.shields.io/badge/celery-black?style=for-the-badge&logo=celery">
  <img src="https://img.shields.io/badge/postgresql-black?style=for-the-badge&logo=postgresql"/>
  <img src="https://img.shields.io/badge/openapi-yellow?style=for-the-badge&logo=openapi"/>
  <img src="https://img.shields.io/badge/sqlalchemy-black?style=for-the-badge&logo=sqlalchemy"/>
  <img src="https://img.shields.io/badge/pytest-black?style=for-the-badge&logo=pytest"/>
</div>

## Deployment Linux
1. Setup [poetry](https://pypi.org/project/poetry/) and install requirements (`poetry install`)
2. Rename `.env.dist` to `.env` and configure it
3. Run virtual env with `poetry shell` command
4. Run database migrations with `make migrate` command
5. Run `make createsuperuser` to create superuser
5. Run server `uvicorn main:app --host 0.0.0.0 --port 80`

## Deployment via Docker
- Run `docker-compose up --build`

## Migrations
**Make migration script:**

    make migration message=YOUR_MIGRATION_MESSAGE_HERE

**Run migrations:**

    make migrate

## Running Tests

To run tests, run the following command

```bash
pytest tests
```

## Used Technologies

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://docs.sqlalchemy.org/en/20/orm/quickstart.html)
- [Pydantic](https://docs.pydantic.dev/latest/)
- [PostgreSQL](https://www.postgresql.org/)
- [Redis](https://redis.io/)
- [Celery](https://docs.celeryq.dev/en/stable/)
- [PyTest](https://docs.pytest.org/en/8.0.x/)

## Demo

![demo](demo/image.png)
![demo](demo/scheme.png)


## Authors

- [Kamran Pulatov(WrldEngine)](https://www.github.com/WrldEngine)