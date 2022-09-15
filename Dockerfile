FROM python:3.9-slim


COPY requirements.txt app/requirements.txt
RUN pip install --no-cache-dir -r app/requirements.txt

EXPOSE 8000

COPY . app

WORKDIR app

# Use the ping endpoint as a healthcheck,
# so Docker knows if the API is still running ok or needs to be restarted
HEALTHCHECK --interval=21s --timeout=3s --start-period=10s CMD curl --fail http://localhost:8000/ || exit 1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]