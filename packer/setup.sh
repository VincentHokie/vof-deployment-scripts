#!/bin/bash

set -e
set -o pipefail

create_vof_user() {
  if ! id -u vof; then
    sudo useradd -m -s /bin/bash vof
  fi
}

setup_vof_code() {
  sudo chown -R vof:vof /home/vof 
  cd /home/vof/app

  # ensure only the required gems are installed on production and staging
  if [[ "$RAILS_ENV" == "production" || "$RAILS_ENV" == "staging" ]]; then
    bundle install --without development test sandbox
  else
    bundle install  
  fi
}

start_supervisor_service() {
  sudo service supervisor start
}

main() {
  create_vof_user

  setup_vof_code
  start_supervisor_service
}

main "$@"
