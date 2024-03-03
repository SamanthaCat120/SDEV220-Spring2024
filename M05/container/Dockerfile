FROM python:3

WORKDIR /opt/payroll

COPY ./payroll.py .
COPY ./requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "payroll.py"]