FROM python:3.7-slim
# Change back to root user to install dependencies
USER root
RUN apt-get update -qq \
 && apt-get install -y --no-install-recommends \
    # required by psycopg2 at build and runtime
    libpq-dev \
     # required for health check
    curl \
 && apt-get autoremove -y
RUN apt-get update -qq && \
  apt-get install -y --no-install-recommends \
  build-essential \
  wget \
  openssh-client \
  graphviz-dev \
  pkg-config \
  git-core \
  openssl \
  libssl-dev \
  libffi6 \
  libffi-dev \
  libpng-dev
ENV PATH "/usr/local/bin:${PATH}" \
    PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=UTF-8 \
    LC_ALL=en_US.UTF-8 \
    LANG=en_US.UTF-8
RUN pip install --no-cache-dir rasa==1.10.3 \
	&& pip install --no-cache-dir wincertstore==0.2 \
	&& pip install --no-cache-dir spacy==2.3.0 \
	&& pip install --no-cache-dir msgpack==0.5.6 \
	&& pip install --no-cache-dir elasticsearch==6.4.0 \
	&& pip install --no-cache-dir nltk==3.3 \
	&& python3.7 -m spacy download en_core_web_lg \
	&& python3.7 -m spacy link en_core_web_lg en \
	&& python3.7 -m spacy download pt_core_news_lg \
	&& python3.7 -m spacy link pt_core_news_lg pt \
	&& python3.7 -m spacy validate \
	&& pip install --no-cache-dir nltk==3.3
RUN [ "python3.7", "-c", "import nltk; nltk.download('stopwords')" ]