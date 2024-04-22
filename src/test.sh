#!/bin/zsh

for i in `seq 1 $1`; do poetry run python3 crawl_url.py; done