#!/bin/bash
for f in *.pdf
do
  echo "Processing $f file..."
  pdftotext -enc UTF-8 $f
done
