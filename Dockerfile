FROM python:3.10.12-bullseye

WORKDIR /app

RUN apt-get update && \
    apt-get install -y git-lfs && \
    git lfs install

COPY . /app

RUN pip install -r requirements.txt

RUN git lfs pull 

RUN python etl/ingest_raw_data.py

EXPOSE 8501

CMD streamlit run app.py --server.port 8080