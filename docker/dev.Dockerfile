FROM python:3.11

WORKDIR /usr/src

RUN apt-get update && apt-get install -y \
    libasound2-dev \
    libssl-dev \
    libffi-dev \
    libnacl-dev \
    python3-dev

RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV DISCORD_BOT_TOKEN=${DISCORD_BOT_TOKEN}
ENV DJANGO_API_URL=${DJANGO_API_URL}

CMD ["python", "main.py"]