# Desinged By Kuromesi
# For Lab Containers
FROM pytorch/pytorch:2.0.1-cuda11.7-cudnn8-devel

ENV TZ Asia/Shanghai
RUN echo 'root:root' |chpasswd
RUN apt update && apt install -y \ 
			openssh-server \
			vim \
			&& apt clean \
			&& rm -rf /tmp/* /var/lib/apt/lists/* /var/tmp* \
			&& echo "PermitRootLogin yes" >> /etc/ssh/sshd_config \
            && mkdir /var/run/sshd		
EXPOSE 22
CMD ["/usr/sbin/sshd","-D"]