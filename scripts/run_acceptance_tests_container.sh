#!/usr/bin/env bash

set -e

this_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
root_dir="${this_dir}/.."

cd $root_dir

docker-compose -f docker-compose-test.yml up -d

echo "Sleeping to allow mysql to start...."
sleep 20

# Setup database
docker exec -it -w /build example-flask-mysql ./scripts/setup_database.sh

# Execute tests
docker exec -it -w /build example-flask-run-tests ./scripts/run_acceptance_tests.sh

docker-compose -f docker-compose-test.yml down
