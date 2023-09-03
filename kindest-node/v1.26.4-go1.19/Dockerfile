# template of other dockerfiles
ARG IMAGE_NAME=kindest/node:v1.26.4

FROM ${IMAGE_NAME}

ENV TZ Asia/Shanghai
RUN apt update && apt install build-essential vim -y \
    && apt clean \
	&& rm -rf /tmp/* /var/lib/apt/lists/* /var/tmp*
RUN curl https://dl.google.com/go/go1.19.linux-amd64.tar.gz -o /tmp/go.tar.gz \
    && tar -C /usr/local -xzf /tmp/go.tar.gz \
    && rm /tmp/go.tar.gz && echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.bashrc

ENTRYPOINT [ "/usr/local/bin/entrypoint", "/sbin/init" ]