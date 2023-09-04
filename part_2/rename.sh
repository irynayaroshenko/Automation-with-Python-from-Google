#!/usr/bin/env bash
# in video #!/bin/bash

for file in *.HTM; do
  name=$(basename "$file" .HTM)
  mv "$file" "$name.html"
  # echo mv "$file" "$name.html" - use it to test if script works before changing file system files
done
