FROM python:3.8-alpine
RUN apk update && apk add bash
RUN adduser -D myuser
RUN apk update && apk add python3-dev gcc g++ libc-dev musl-dev linux-headers
USER myuser
WORKDIR /home/myuser
ENV PATH="/home/myuser/.local/bin:${PATH}"
COPY --chown=myuser:myuser . .
RUN pip install -r requirements.txt
