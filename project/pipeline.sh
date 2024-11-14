#!/bin/bash

#navigate to pipeline.sh directionary and open Git Bash there

url1="https://extdataportal.worldbank.org/content/dam/sites/data/gender-data/data/data-gen/zip/indicator/proportion-of-seats-held-by-women-in-national-parliaments.zip"

output1="./proportion-of-seats-held-by-women-in-national-parliaments.zip"

curl -o "$output1" "$url1"

if curl -o "$output1" "$url1"; then
    echo "Download successful!"
else
    echo "Download failed!"
fi

url2="https://extdataportal.worldbank.org/content/dam/sites/data/gender-data/data/data-gen/zip/indicator/learning-adjusted-years-of-school.zip"

output2="./learning-adjusted-years-of-school.zip"

curl -o "$output2" "$url2"

if curl -o "$output2" "$url2"; then
    echo "Download successful!"
else
    echo "Download failed!"
fi

url3="https://extdataportal.worldbank.org/content/dam/sites/data/gender-data/data/data-gen/zip/indicator/school-enrollment-secondary.zip"

output3="./school-enrollment-secondary.zip"

curl -o "$output3" "$url3"

if curl -o "$output3" "$url3"; then
    echo "Download successful!"
else
    echo "Download failed!"
fi


url4="https://extdataportal.worldbank.org/content/dam/sites/data/gender-data/data/data-gen/zip/indicator/school-enrollment-tertiary-gross.zip"

output4="./school-enrollment-tertiary-gross.zip"

curl -o "$output4" "$url4"

if curl -o "$output4" "$url4"; then
    echo "Download successful!"
else
    echo "Download failed!"
fi

jv pipeline.jv