FROM ubuntu:focal

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update -y && apt install -y python3-pip default-lib mysqlclient-dev vim curl gnupg
RUN pip install mysql

RUN curl -s https://packages.wazuh.com/key/GPG-KEY-WAZUH | gpg --no-default-keyring --keyring gnupg-ring:/usr/share/keyrings/wazuh.gpg --import && chmod 644 /usr/share/keyrings/wazuh.gpg && \
    echo "deb [signed-by=/usr/share/keyrings/wazuh.gpg] https://packages.wazuh.com/4.x/apt/ stable main" | tee -a /etc/apt/sources.list.d/wazuh.list
    
RUN apt update -y && apt install -y wazuh-manager wazuh-indexer mysql-server openssh-server
COPY wazuh /wazuh
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
EXPOSE 1514/tcp 1515/tcp 514/udp 1516/tcp 3306/tcp 22/tcp

ENTRYPOINT [ "/entrypoint.sh" ]