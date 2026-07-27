# 1. Use a lightweight Python version as the base
FROM python:3.9-slim

# 2. Set the directory inside the container where our code will live
WORKDIR /app

# 3. Copy the requirements file first 
# (This is a DevOps trick: it makes builds faster by caching the install step)
COPY requirements.txt .

# 4. Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of the application code (app.py, templates, etc.)
COPY . .

# 6. Tell Docker which port the app runs on
EXPOSE 5000

# 7. The command to run the application when the container starts
CMD ["python", "app.py"]