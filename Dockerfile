
WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

RUN python etl/ingest_raw_data.py

EXPOSE 8501

CMD streamlit run app.py --server.port 8080