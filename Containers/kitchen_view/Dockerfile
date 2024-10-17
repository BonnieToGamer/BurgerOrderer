FROM python:3.12.6-alpine AS compiler

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Set the current working dir
WORKDIR /app

# Setup python virtual env
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy the pip requirements.txt to the app
# And install them
COPY Containers/kitchen_view/requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.12.6-alpine AS runner

# Move to current working dir
WORKDIR /app

# Copy the compiler steps virtual env
COPY --from=compiler /opt/venv /opt/venv

# Add virtual env to PATH
ENV PATH="/opt/venv/bin:$PATH"

# run the application
CMD ["python", "-u", "main.py"]