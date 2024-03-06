FROM python:3.10-buster

WORKDIR /data_source

COPY ./area_data_source.py   .

COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "area_data_source.py"] 