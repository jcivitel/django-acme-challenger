FROM python:3.12-alpine AS builder

RUN apk add --no-cache libgcc mariadb-connector-c pkgconf mariadb-dev \
    postgresql-dev

WORKDIR /opt/django-acme-challenger/
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /opt/django-acme-challenger/

FROM builder AS install
WORKDIR /opt/django-acme-challenger
ENV VIRTUAL_ENV=/opt/django-acme-challenger/venv

RUN python -m venv $VIRTUAL_ENV

ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install --no-cache-dir -r /opt/django-acme-challenger/requirements.txt

FROM install

EXPOSE 8000
CMD ["sh", "entry.sh"]
