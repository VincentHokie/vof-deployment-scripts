#!/bin/bash

set -e
set -o pipefail

create_vof_user() {
  if ! id -u vof; then
    sudo useradd -m -s /bin/bash vof
  fi
}

install_system_dependencies() {
  sudo apt-get update -y && sudo apt-get upgrade -y
  sudo apt-get install software-properties-common -y

}

install_redis(){
  if ! which redis-cli; then
    install_system_dependencies

    sudo chgrp -R vof  /usr/local # make vof the group that /usr/local belongs to
    sudo chmod -R g+rw /usr/local # give read and write permissions to the group that already owns these files

    sudo add-apt-repository ppa:chris-lea/redis-server -y
    sudo apt-get update -y
    sudo apt-get install redis-server -y
    sudo sed -i 's/127.0.0.1/0.0.0.0/g' /etc/redis/redis.conf
    sudo service redis-server restart
  fi
}

# webdis is a very simple web server providing an HTTP interface to Redis
# https://github.com/nicolasff/webdis
setup_webdis(){
  if which redis-cli; then
    sudo apt-get install make build-essential libevent-dev webdis -y # install webdis
    sudo sed -i -e "s|\"http_host\":\s\"127.0.0.1\"|\"http_host\": \"0.0.0.0\"|" /etc/webdis/webdis.json 
    sudo /etc/init.d/webdis restart
  fi
}

install_logging_agent(){
  # This installs the logging agent into the VM
  curl -sSO https://dl.google.com/cloudagents/install-logging-agent.sh
  sudo bash install-logging-agent.sh
}

main() {
  create_vof_user

  mkdir -p /tmp/workdir
  pushd /tmp/workdir #  store current dir and cd to /tmp/workdir
    install_redis
    setup_webdis
    install_logging_agent
  popd #  cd to previosuly stored  path
  rm -r /tmp/workdir

}

main "$@"
