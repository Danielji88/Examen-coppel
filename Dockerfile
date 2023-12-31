FROM python:3.8

WORKDIR /Main

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "Main.py"]