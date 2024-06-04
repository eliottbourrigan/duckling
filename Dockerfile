
FROM python:3.9-slim

# Working directory
WORKDIR /app
COPY . /app

# Install requirements
RUN pip install -U duckduckgo_search
RUN pip install -r requirements.txt

# Expose the port
EXPOSE 80

# Run the app
CMD ["fastapi", "run", "api.py", "--port", "80"]
