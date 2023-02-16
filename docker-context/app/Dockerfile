FROM python:3.10-buster

COPY ./requirements.txt /tmp/requirements.txt
COPY ./run.sh /run.sh

WORKDIR /app
EXPOSE 8000

ARG USER=buster

RUN python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    apt-get -y update && \
    apt-get -y install netcat-openbsd && \
    /venv/bin/pip install -r /tmp/requirements.txt && \
    rm -rf /tmp

RUN adduser \
        --disabled-password \
        --no-create-home \
        ${USER}

RUN chown -R ${USER}:${USER} /run.sh &&\
    chmod +x /run.sh &&\
    chown -R ${USER}:${USER} /app

ENV PATH="/:/venv/bin:$PATH"

USER ${USER}

CMD [ "/run.sh" ]