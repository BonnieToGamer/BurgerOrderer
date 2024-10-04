FROM python:3.12.6-alpine as compiler

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

ARG SOURCE_DIR
COPY $SOURCE_DIR/requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.12.6-alpine as runner

WORKDIR /app
COPY --from=compiler /opt/venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

CMD ["python", "main.py"]