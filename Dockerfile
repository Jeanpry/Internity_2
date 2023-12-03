FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

ADD requirements.txt .

RUN pip install -r requirements.txt
RUN python -m spacy download en_core_web_sm

COPY ./app /app/app