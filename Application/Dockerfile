



FROM ubuntu:14.04


ENV DEBIAN_FRONTEND noninteractive



RUN apt-get update
RUN apt-get -qq update
RUN apt-get install -y nodejs npm 
RUN apt-get install -y python python-dev python-pip python-virtualenv && \
  rm -rf /var/lib/apt/lists/*

RUN easy_install pip 
RUN pip install requests

# TODO could uninstall some build dependencies


# fucking debian installs `node` as `nodejs`
RUN update-alternatives --install /usr/bin/node node /usr/bin/nodejs 10



RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

# Install app dependencies
COPY package.json /usr/src/app/
RUN npm install 

# Bundle app source

COPY . /usr/src/app



EXPOSE 8080



CMD ["npm", "start"]