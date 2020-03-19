# Pull base image
FROM python:3.6-slim

RUN \
	echo "weasyprint dependencies" \
	&& apt-get update \
	&& apt-get install -y --no-install-recommends \
		libcairo2 \
		libpango1.0-0 \
		libpangocairo-1.0.0 \
		libgdk-pixbuf2.0-0 \
		shared-mime-info

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system

# Copy project
COPY . /code/
