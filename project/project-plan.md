# Project Plan

## Title
<!-- Give your project a short title. -->
Correlation analysis between Gender Inequality and Female Political Representation in the Americas

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
1. Is there a connection between gender inequality and female political representation across the Americas (United States, Central America or South America)?

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
Gender Inequality in political representation is an important problem, because it hinders progress toward a more inclusive and representative governance.
This projects analyzes the connection between gender inequality and female political representation across the Americas, using statistical correlation and historical analysis. 
The results can give insights into the factors that promote or hinder women's political participation.

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: Gender Inequality Index (GII)
* Metadata URL: https://hdr.undp.org/data-center/thematic-composite-indices/gender-inequality-index#/indicies/GII
* Data URL: https://hdr.undp.org/sites/default/files/2023-24_HDR/HDR23-24_Statistical_Annex_GII_Table.xlsx
* Data Type: XLSX

The Gender Inequality Index (GII) is a composite metric of gender inequality using three dimensions: reproductive health, empowerment and the labour market. It also shows the share of seats in parliament. It is available for all North- and South-America countries and you can also see the historical development.

### Datasource2: Ranking of women in national parliaments
* Metadata URL: https://data.ipu.org/women-ranking/?date_month=10&date_year=2024
* Data URL: https://data.ipu.org/export-report/women-ranking/csv?date_month=10&date_year=2024
* Data Type: CSV

This data source shows the percentage of women in national parliaments.

### Datasource3: Human development summary
* Metadata URL: https://hdr.undp.org/data-center/specific-country-data#/countries/USA
* Data URL: https://hdr.undp.org/data-center/specific-country-data#/countries/USA:~:text=DOWNLOAD-,Country%20Data%20(csv),-Metadata
* Data Type: CSV

Human development summary capturing achievements in the HDI and complementary metrics that take into account gender gaps, inequality, planetary pressures and multidimensional poverty.

### Datasource4: Share of enrolled students, new entrants and graduates by gender
* Metadata URL: https://data-explorer.oecd.org/vis?df[ds]=dsDisseminateFinalDMZ&df[id]=DSD_EAG_UOE_NON_FIN_STUD%40DF_UOE_NF_SHARE_GENDER&df[ag]=OECD.EDU.IMEP&df[vs]=1.0&dq=.ISCED11_3%2BISCED11_34%2BISCED11_35%2BISCED11_4%2BISCED11_5%2BISCED11_6%2BISCED11_7%2BISCED11_8.GRAD.....A...._T..F%2BM.&pd=2022%2C2022&to[TIME_PERIOD]=false&vw=ov&ly[cl]=EDUCATION_LEV&ly[rs]=SEX&ly[rw]=REF_AREA
* Data URL: https://sdmx.oecd.org/public/rest/data/OECD.EDU.IMEP,DSD_EAG_UOE_NON_FIN_STUD@DF_UOE_NF_SHARE_GENDER,1.0/all?dimensionAtObservation=AllDimensions&format=csvfilewithlabels
* Data Type: CSV

This dataset contains data on the share of enrolled students, new entrants and graduates by gender. Educational factors may have an impact on the female political representation.

### Datasource5: Social Institutions and Gender Index (SIGI)
* Metadata URL: https://data-explorer.oecd.org/vis?lc=en&df[ds]=dsDisseminateFinalDMZ&df[id]=DSD_SIGI%40DF_SIGI_2023&df[ag]=OECD.DEV.NPG&dq=..&lom=LASTNPERIODS&lo=5&to[TIME_PERIOD]=false&ly[cl]=MEASURE&ly[rw]=REF_AREA&vw=ov
* Data URL: https://sdmx.oecd.org/public/rest/data/OECD.DEV.NPG,DSD_SIGI@DF_SIGI_2023,/all?dimensionAtObservation=AllDimensions&format=csvfilewithlabels
* Data Type: CSV

This dataset contains data on discrimination in social institutions, which are grouped into four dimensions: discrimination in the family, restricted physical integrity, restricted access to productive and financial resources, and restricted civil liberties. The Social Institutions and Gender Index and its dimensions range from 0 to 100, with 0 indicating no discrimination and 100 indicating absolute discrimination against women.

### Datasource6: Gender, Institutions and Development Database
* Metadata URL: https://data-explorer.oecd.org/vis?lc=en&df[ds]=dsDisseminateFinalDMZ&df[id]=DSD_GID%40DF_GID_2023&df[ag]=OECD.DEV.NPG&dq=......&lom=LASTNPERIODS&lo=5&to[TIME_PERIOD]=false&vw=ov&ly[cl]=SIGI_FRAMEWORK%2CVARIABLE_CATEGORY%2CCOMBINED_MEASURE&ly[rw]=REF_AREA
* Data URL: https://sdmx.oecd.org/public/rest/data/OECD.DEV.NPG,DSD_GID@DF_GID_2023,/all?dimensionAtObservation=AllDimensions&format=csvfilewithlabels
* Data Type: CSV

This dataset contains data on gender-based discrimination in social institutions. Data help analyse women's empowerment and understand gender gaps in key areas of development.

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Search for suitable datasets [#1][i1]
2. Preprocess the datasets by cleaning unwanted columns [#2][i2]
3. Make the pipeline with the cleaned data [#3][i3]
4. Try to find the correlation between the datasets and answer the main question [#4][i4]
[i1]: https://github.com/issues
