# docker build -t chatroom -f Dockerfile.chatroom
# docker run --name chatroom -p 8080:3000 -d chatroom
FROM node:14

RUN node --version

RUN git clone https://github.com/JorleyOliveira/server-socket-io.git

WORKDIR /server-socket-io

RUN npm install

EXPOSE 4001