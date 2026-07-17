# 1. Use an official, stable Python runtime as a parent image
FROM python:3.10-slim

# 2. Set environment variables to optimize Python performance inside Docker
# Prevents Python from writing pyc files to disc; Prevents buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# 3. Set the working directory
WORKDIR /usr/src/app

# 4. Install essential system dependencies (for building some Python wheels if needed)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# 5. Copy requirements first to leverage Docker layer caching
COPY requirements.txt ./

# 6. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 7. Copy the rest of your application code
COPY . .

# 8. Expose port 8000 (standard for Django development servers)
EXPOSE 8000

# 9. Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
