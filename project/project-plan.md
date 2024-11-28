# Project Plan

## Title
<!-- Give your project a short title. -->
Correlation analysis between Female School Education and Female Political Representation in America (Canada, United States, Guatemala, Honduras)

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
1. Is there a correlation between a woman's school education and female political representation across the Americas (Canada, United States, Guatemala, Honduras)?

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
Gender Inequality in political representation is an important problem, because it hinders progress toward a more inclusive and representative governance.
This project analyzes if there is a correlation between female school education and female political representation across the Americas (Canada, United States, Guatemala, Honduras), using statistical correlation. 
The results can give insights into the factors that promote or hinder women's political participation.

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: Share of women in parliament
* Metadata URL: https://ourworldindata.org/grapher/share-of-women-in-parliament-ipu
* Data URL: https://ourworldindata.org/grapher/share-of-women-in-parliament-ipu.csv?v=1&csvType=full&useColumnShortNames=trueproportion-of-seats-held-by-women-in-national-parliaments.zip
* Data Type: CSV

This data source shows the percentage of shares of women in parliaments.

### Datasource2: Learning-Adjusted Years of School
* Metadata URL: https://genderdata.worldbank.org/en/indicator/hd-hci-lays
* Data URL: https://extdataportal.worldbank.org/content/dam/sites/data/gender-data/data/data-gen/zip/indicator/learning-adjusted-years-of-school.zip
* Data Type: CSV

This data source shows the Learning-adjusted years of school. It shows the expected years, that a pupil will stay in school, by gender and countries.
Learning-adjusted years of school are calculated by multiplying the estimates of expected years of school by the ratio of most recent harmonized test scores to 625.

### Datasource3: School enrollment, secondary (%)
* Metadata URL: https://genderdata.worldbank.org/en/indicator/se-sec-enrr
* Data URL: https://extdataportal.worldbank.org/content/dam/sites/data/gender-data/data/data-gen/zip/indicator/school-enrollment-secondary.zip
* Data Type: CSV

This data source shows the percentage of secondary school enrollment, by gender and countries.

### Datasource4: School enrollment, tertiary (% gross)
* Metadata URL: https://genderdata.worldbank.org/en/indicator/se-ter-enrr
* Data URL: https://extdataportal.worldbank.org/content/dam/sites/data/gender-data/data/data-gen/zip/indicator/school-enrollment-tertiary-gross.zip
* Data Type: CSV

This data source shows the percentage of tertiary school enrollment, by gender and countries.
Gross enrollment ratio is the ratio of total enrollment, regardless of age, to the population of the age group that officially corresponds to the level of tertiary school.

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Search for suitable datasets 
2. Create Project plan and keep up to date
3. Filter out datasets and select the most important ones 
4. Preprocess the selected datasets by cleaning unwanted columns and unwanted data
5. Build an automated pipeline with the cleaned data (Project Work 3 - Data Pipeline)
6. Write the data report (Project Work 4 - Data Report)
7. Test the pipeline (Project Work 5 - Automated Testing)
8. Try to find the correlation between the datasets and answer the main question
9. Make and write the final report (Project Work 7 - Final Report)
10. Prepare a presentation (Project Work 8 - Presentation)