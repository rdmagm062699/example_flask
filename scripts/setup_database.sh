#!/usr/bin/env bash

set -e

this_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
root_dir="${this_dir}/.."

mysql -u root --password=${DB_PASSWORD} -e "create database example"

create_tables=$(cat<< EOF
use example;
create table data
(
    id          INT unsigned NOT NULL AUTO_INCREMENT,
    data_value  VARCHAR(150),
    PRIMARY KEY (id)
);

create table other_stuff
(
    id          INT unsigned NOT NULL AUTO_INCREMENT,
    data_id     INT unsigned NOT NULL,
    column_one  VARCHAR(150),
    column_two  VARCHAR(150),
    PRIMARY KEY (id),
    FOREIGN KEY (data_id)
        REFERENCES data(id)
)
EOF
)

mysql -u root --password=${DB_PASSWORD} -e "${create_tables}"