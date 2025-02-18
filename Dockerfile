FROM python:3.9

WORKDIR /app

COPY requirments.txt /app

RUN pip install --no-cache-dir -r requirements.txt

COPY pyton.py /app/ 

EXPOSE 5000

CMD ["python", "app.py"]