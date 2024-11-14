#!/bin/bash

# navigate to /project directionary and open Git Bash there
# bash pipeline.sh in Git Bash ausführen

url1="https://extdataportal.worldbank.org/content/dam/sites/data/gender-data/data/data-gen/zip/indicator/learning-adjusted-years-of-school.zip"

output1="./learning-adjusted-years-of-school.zip"

curl -o "$output1" "$url1"

if curl -o "$output1" "$url1"; then
    echo "Download successful!"
else
    echo "Download failed!"
fi

url2="https://extdataportal.worldbank.org/content/dam/sites/data/gender-data/data/data-gen/zip/indicator/school-enrollment-secondary.zip"

output2="./school-enrollment-secondary.zip"

curl -o "$output2" "$url2"

if curl -o "$output2" "$url2"; then
    echo "Download successful!"
else
    echo "Download failed!"
fi


url3="https://extdataportal.worldbank.org/content/dam/sites/data/gender-data/data/data-gen/zip/indicator/school-enrollment-tertiary-gross.zip"

output3="./school-enrollment-tertiary-gross.zip"

curl -o "$output3" "$url3"

if curl -o "$output3" "$url3"; then
    echo "Download successful!"
else
    echo "Download failed!"
fi

jv pipeline.jv