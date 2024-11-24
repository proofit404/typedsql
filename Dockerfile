FROM ubuntu:rolling

RUN apt update

RUN apt install -y ruby-full

RUN apt install -y gcc make libmagic-dev

RUN gem install pdd

RUN mkdir /app

WORKDIR /app

USER ubuntu

RUN mkdir -p $HOME/.cache
