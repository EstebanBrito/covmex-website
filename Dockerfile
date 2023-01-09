FROM python:3.10-slim
WORKDIR /website
COPY ./requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
CMD streamlit run app.py --server.address 0.0.0.0 --server.port $PORT