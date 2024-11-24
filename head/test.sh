#!/bin/bash

dest="/backups"

echo "$dest"

printf "%s/b" "$dest"

echo "Value ${"%s/bbb" "${dest}"}"

u=${1:-root}
read
