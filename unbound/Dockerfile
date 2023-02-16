FROM alpine:latest

RUN apk add --no-cache unbound

COPY unbound.conf /etc/unbound/

CMD ["unbound", "-d"]