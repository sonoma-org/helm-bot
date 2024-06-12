FROM python:3.12.2-bookworm
COPY . /app
COPY /bot /app
RUN pip install -r /app/requirements.txt
ENTRYPOINT ["/app/entrypoint.sh"]
