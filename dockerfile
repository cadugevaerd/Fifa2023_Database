FROM python:3-slim

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY datasets/ ./datasets/
COPY pages/ ./pages/
COPY *.py ./

#CMD [ "python", "-m","streamlit","run","./1_🏠️_Home.py","--server.port=8501", "--server.address=0.0.0.0" ]
CMD [ "python", "-m","streamlit","run","./1_🏠️_Home.py","--server.port=8501"]