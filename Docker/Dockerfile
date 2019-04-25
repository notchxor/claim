FROM ubuntu:18.04
RUN apt-get update
RUN apt install -y wget
VOLUME /mnt/dev/data
RUN cd /mnt/dev/data


RUN wget https://github.com/EOSIO/eos/releases/download/v1.7.2/eosio_1.7.2-1-ubuntu-18.04_amd64.deb
RUN git clone https://github.com/notchxor/claim.git


