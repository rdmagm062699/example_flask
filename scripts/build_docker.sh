#!/usr/bin/env bash

set -e

this_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
root_dir="${this_dir}/.."

rm -rf $root_dir/docker/app/temp_build
mkdir $root_dir/docker/app/temp_build

cp $root_dir/requirements.txt $root_dir/docker/app/temp_build
cp -r $root_dir/src $root_dir/docker/app/temp_build

cd $root_dir/docker/tests
docker build -t example-flask-run-tests:latest .

cd $root_dir/docker/app
docker build -t example-flask-run-app:latest .

rm -rf $root_dir/docker/app/temp_build
