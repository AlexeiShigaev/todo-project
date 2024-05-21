FROM python

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN pip install --upgrade pip poetry
RUN poetry config virtualenvs.create false --local
RUN ls -al
COPY pyproject.toml poetry.lock ./
RUN poetry install

COPY todo_app/. ./

#CMD ["gunicorn", "todo_app.wsgi:application", "--bind", "0.0.0.0:8000"]
