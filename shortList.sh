#!/bin/bash
for f in *.pdf
do
  pdftotext -enc UTF-8 $f
done

python findScores.py
echo "Please visit the shortlisted directory for your result"