FROM python:3.6

COPY . /var/question-identifier
WORKDIR /var/question-identifier

RUN \
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google.list

RUN \
    apt-get update && \
    apt-get install -y google-chrome-stable unzip && \
    rm -rf /var/lib/apt/lists/*

RUN pip install -r requirements.txt

ARG CHROMEDRIVER_VERSION=2.36
RUN \
    curl -sL https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip -o /tmp/chromedriver.zip && \
    unzip /tmp/chromedriver.zip -d /usr/local/bin && \
    rm /tmp/chromedriver.zip

RUN python -m nltk.downloader -d /usr/share/nltk_data all

