#!/bin/bash

# navigate to /project directionary and open Git Bash there
# execute "bash pipeline.sh" in Git Bash in /project directionary
# Jayvee version 0.6.4
# Installation of cURL required

url1="https://extdataportal.worldbank.org/content/dam/sites/data/gender-data/data/data-gen/zip/indicator/learning-adjusted-years-of-school.zip"

output1="./learning-adjusted-years-of-school.zip"

curl -o "$output1" "$url1"


url2="https://extdataportal.worldbank.org/content/dam/sites/data/gender-data/data/data-gen/zip/indicator/school-enrollment-tertiary-gross.zip"

output2="./school-enrollment-tertiary-gross.zip"

curl -o "$output2" "$url2"

jv pipeline.jv