FROM ubuntu:18.04
RUN apt-get update
RUN apt install -y wget libicu60 libusb-1.0-0 libcurl3-gnutls python3.6 python3-dev python3-pip  locales
RUN wget https://github.com/EOSIO/eos/releases/download/v1.7.4/eosio_1.7.4-1-ubuntu-18.04_amd64.deb
RUN dpkg -i eosio_1.7.4-1-ubuntu-18.04_amd64.deb

ADD claim.py  /root/
ADD config.ini /root/
WORKDIR /root
RUN cleos -u https://api.eosargentina.io  wallet create -n claim --to-console | tail -n1 | cut -d "\""  -f2 > /root/wallet.txt &&  echo "wallet_pass: $( cat /root/wallet.txt)" >> /root/config.ini && sleep 5
CMD ./usr/bin/cleos -u https://api.eosargentina.io wallet unlock -n claim --password $(cat /root/wallet.txt)  
ENTRYPOINT  python3 claim.py
