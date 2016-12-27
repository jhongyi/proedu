FROM nginx:latest
ADD nginx.conf /etc/nginx/nginx.conf

# 建立log資料夾
ENV DOCKYARD_LOGHOME /home/docker/log
RUN mkdir -p ${DOCKYARD_LOGHOME}/info
RUN mkdir -p ${DOCKYARD_LOGHOME}/error
