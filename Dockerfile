FROM python:3.10-buster

WORKDIR /data_source

COPY ./local_data.py   .

COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "local_data.py"] 