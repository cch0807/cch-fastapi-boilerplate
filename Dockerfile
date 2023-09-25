FROM python:3.11.5

ENV PYTHONUNBUFFERED 1

EXPOSE 8000
WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends netcat-traditional

COPY poetry.lock pyproject.toml ./
RUN pip install poetry==1.6.1 && \
    poetry config virtualenvs.in-project true && \
    poetry install --no-dev

COPY . ./

# CMD poetry run alembic upgrade head && \
#     poetry run uvicorn --host=0.0.0.0 app.main:app