#!/usr/bin/env bash

set -e

this_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
root_dir="${this_dir}/.."

cd $root_dir/docker
docker build -t example-flask:latest .
