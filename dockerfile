FROM python:3.10-slim
ENV TOKEN='7142098510:AAFbVJUPs9nDIA5mZbXzWFDpQKgB_OdllkU'
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "MID_FIO_bot.py" ]