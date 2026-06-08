# DS 4320 Project 2: [PLACEHOLDER]<br>
Executive Summary: [placeholder until finished]<br>
Name: Maya Uwaydat<br>
NetID: zvd6vz<br>
DOI: [placeholder until finished]<br>
Press Release: [placeholder]<br>
Pipeline: [placeholder]<br>
License: [MIT License](https://github.com/mayooueidat-uva/project-2-energy-pred/blob/main/LICENSE.md)
## Problem definition 
### Problem statement
**Initial general problem:** The generation of energy leads to waste that is unhealthy to be around, so we must find out how energy demand and hospital readmissions are linked. 
**Refined problem statement:** ______ Therefore, it is crucial to determine what ____ contribute to _____, and use a feature-selecting model that 
### Motivation 
### Rationale 
The project was refined over the course of research and data cleaning and was largely shaped by the available data. At first, I started asking myself questions about hospital readmissions; then, I recalled some coursework about power plants placed in disadvantaged areas negatively contributing to residents' health. I wanted to investigate the degree to which a *number* of features might have contributed to hospital readmissions, and I chose both the means of generating electricity and energy demand based on my background reading and the data on the Energy Information Administration (EIA) website. I also wanted to look at how readmissions may be affected compared to the "normal" level, which is why I went with the excess readmission ratio. 
## Domain exposition 
### Terminology 
| ---- | 
| ----- | 
### Domain
### Further Reading
| Title | Brief description | link | 
| ------| -----------------| -------| 
| Villarosa Pollution is Killing Black Americans. This community fought back. | This article from the New York Times served as the inspiration for the project. Power plants are often placed in the neighbourhoods of disadvantaged populations, and their waste has serious health implications, making them a contributor to systemic discrimination. | [link](https://myuva-my.sharepoint.com/:b:/g/personal/zvd6vz_virginia_edu/IQAfai7jSp6YTo3OXZHPgXsxAYzlM6tSfUUFkkNB6sdDkWk?e=iuC9FC)|
| What should every data scientist know when working with ZIP Codes? | Middle Tennessee State University provides a reader on the limitations of working with ZIP codes, which is useful for me, as I planned to look at the health effects of energy generation at a ZIP-code level. | [link](https://myuva-my.sharepoint.com/:u:/g/personal/zvd6vz_virginia_edu/IQD3cxCpeKPuTqy_wc8fj3ikATeszpSQcOaFRpLX7ttT7fY?e=Edsykz) | 
| PEACH: Defining & Measuring SES | This article is a short reader on proxy data for socioeconomic status. Benefits and limitations of using addresses, unmet needs surveys, ZIP codes, and census data were discussed. | [link](https://myuva-my.sharepoint.com/my?id=%2Fpersonal%2Fzvd6vz%5Fvirginia%5Fedu%2FDocuments%2FDS%204320%20Project%202%2FPEACH%20%2D%20Defining%20%26%20Measuring%20SES%2Ehtml&parent=%2Fpersonal%2Fzvd6vz%5Fvirginia%5Fedu%2FDocuments%2FDS%204320%20Project%202&ga=1) | 
| On the Use of ZIP Codes and ZIP Code Tabulation Areas (ZCTAs) for the Spatial Analysis of Epidemiological Data | I planned to assess energy demand vs. readmissions at the ZIP code level, as that was the location data most accessible to me; however, the article says that the ZIP code is a “particularly problematic” unit of geographical analysis because tend to be attributed to facilities used for distributing mail (like post offices) and not necessarily space. Though I am not using ZIP codes to make predictions, it is still useful for me to understand their limitations as proxy data in public health contexts. | [link](https://myuva-my.sharepoint.com/my?id=%2Fpersonal%2Fzvd6vz%5Fvirginia%5Fedu%2FDocuments%2FDS%204320%20Project%202%2Fon%20the%20use%20of%20zip%20codes%2Epdf&parent=%2Fpersonal%2Fzvd6vz%5Fvirginia%5Fedu%2FDocuments%2FDS%204320%20Project%202&ga=1) | 
| Human Health Impacts of Energy Transitions across the United States among Sociodemographic Subpopulations for the Year 2050| Not all the power plants used in the data set are coal or natural gas; therefore, potential adverse health effects by the plants might vary. This paper demonstrates that using less-pollutant energy generation methods can benefit public health. | [link](https://myuva-my.sharepoint.com/:b:/g/personal/zvd6vz_virginia_edu/IQA-UZRJaoHjRYjmiyY4gqZWAXayuW9n18jfctBVzw2U1uk?e=qhi4Wh) | 
## Data creation
### Provenance
Data was collected from the Center for Medicare and Medicaid Services (CMS) and U.S. Energy Information Administration (EIA). For energy demand and hospital readmissions, data from 2021 to 2026 was procured; however, power plant data was unavailable for 2025-2026, so I only gathered data for 2021-2024. No API was available for CMS’s archived data, so the files were manually downloaded and unzipped from the website. When perusing the EIA’s website, I wanted to see available data on energy demand and zip codes, as I intended to refine my problem statement based on available data. Therefore, I also downloaded EIA data manually; the website’s downloads pages were easier to navigate than their API, as their API tool requires one to choose between thousands of parameters.<br>
After ensuring all data was in UTF-8 format, a table or two from each dataset—hospital readmissions, energy demand, and power plants—was put into MongoDB Compass, which allowed me to view the proportion of numeric data read as strings, columns with significant NaNs, summary statistics, et cetera. All data was loaded separately and cleaned accordingly in JupyterLab, using Python. Cleaned spreadsheets were loaded into the Mongo database to be extracted in other notebooks for further processing and for analysis. 

### Code files
| Title | Description | link | 
| ----- | ------------| ----- | 
| clean.py | part of pipeline that cleans raw data after it has been appropriately put into csv format. | [file](https://github.com/mayooueidat-uva/project-2-energy-pred/blob/main/code_files/clean.py) | 
| pre_analysis.py | the part of the pipeline that creates a new data table (from cleaned data) that can be used in our model. | [file](https://github.com/mayooueidat-uva/project-2-energy-pred/blob/main/code_files/pre_analysis.py) | 
| the_ml_part.py | part of the pipeline where model selection is done for HistGradientBoostingRegressor, and then the model is used to assess what features are most important for predicting excess readmission rate. | [file](https://github.com/mayooueidat-uva/project-2-energy-pred/blob/main/code_files/the_ml_part.py) | 
### Rationale
### Bias identification 
ZIP codes for hospitals will not always be the same as ZIP codes for affected patients. Having worked in a hospital before, I know that people will often travel to hospitals; for example, I was at a clinic in Little Rock (central Arkansas) and we had patients coming from Bella Vista (on the border of Missouri and Arkansas). Additionally, the demand data was replete with NaN values; and while pd.DataFrame.interpolate was used to accommodate for them, I lacked the time to deliberate how to impute values. 
### Bias mitigation 
## Metadata
### Implicit Schema
```
Collection: unplanned_data

{
    _id: objectid,
    City: string, 
    Facility ID: string,
    Facility Name: string,
    Start Date: date,
    Measure ID: string,
    ZIP: numeric
}

Collection: readm_data

{
    _id: objectid,
    Facility ID: string,
    Facility Name: string,
    Start Date: date,
    Excess Readmission Ratio: double,
    Measure ID: string
}

Collection: plants_data
{
    _id: objectid,
    Plant Name: string,
    County: string,
    State: string,
    ZIP: double
}

CollectioN: generators_data

{
    _id: objectid,
    Plant Name: string,
    County: string,
    State: string,
    Technology: string
}

Collection: demand_data

{
    _id: objectid, 
    Plant Name: string, 
    Elec_MMBtu January: double, 
    Elec_MMBtu February: double,
    Elec_MMBtu March: double,
    Elec_MMBtu April: double, 
    Elec_MMBtu May: double, 
    Elec_MMBtu June: double, 
    Elec_MMBtu July: double, 
    Elec_MMBtu August: double, 
    Elec_MMBtu September: double, 
    Elec_MMBtu October: double, 
    Elec_MMBtu November: double, 
    Elec_MMBtu December: double, 
    YEAR: double
}
```
### Database contents 
| Name | brief description | 
| ----- | ---------------- | 
| unplanned_data | Original files acquired from CMS for each year for years 2024-2026 (data collection start dates for the files are from 2019-2021, and end dates are from 2022-2024). A cleaned set of JSON documents consisted of hospital identificatory information, start and end date of unplanned hospital visits, hospital ZIP code, and causes of readmission. |
| readm_data | Original files acquired from CMS for each year for years 2024-2026. A cleaned set of JSON documents consisted of hospital identificatory information, start and end date of patient readmissions, readmission type, as well as excess readmission rate. | 
| plants_data | Original files acquired from the EIA for each year. A cleaned set of JSON documents consisting of plant identificatory and location information, including ZIP code, for years 2021-2024. | 
| generators_data | Original files acquired from the EIA for each year. A cleaned set of JSON documents consisted of utility/plant identificatory and location information for years 2021-2024. Additionally, they included the type of technology used for each generator (hydroelectric, steam coal, etc). | 
| demand_data | Original files acquired from the EIA for each year. A cleaned JSON file comprised of the demand data from years 2021-2026 and includes plant identificatory information and the quantity of energy in MMBtu (million British thermal units) used for electricity generation each month, which is used as a proxy for energy demand. |
### Data dictionary 
| Name | Brief description | Data Type | Example |
| ------| -----------------| -------| -------|
| Facility ID |An ID assigned to providers and suppliers paid under Medicare Part A. First two letters of the ID represent where the facility is located; second four digits represent the type of facility. This is not relevant to this project; here, it’s merely used as identificatory information. |String|010001|
| City | City/town the facility is present in (energy facility or hospital facility; this is present in both energy data files and hospital data files). | String | DOTHAN | 
| Facility Name | A hospital facility’s name. | String | SOUTHEAST HEALTH MEDICAL CENTER | 
| ZIP | The ZIP code of the facility (energy facility or hospital facility; this is present in both energy data files and hospital data files). NOTE: this is categorical data, but it is stored in numerical data format for ease of use. | float64 | 36301 | 
| Measure ID | Identifies what types of patients are represented in the readmissions ratios columns of a particular row in the data sheet. READM-30-AMI-HRRP: Heart attack patients; READM-30-COPD-HRRP: Pulmonary disease patients; READM-30-CABG-HRRP: Coronary artery bypass graft patients; READM-30-HF-HRRP: Heart failure patients; READM-30-HIP-KNEE-HRRP: Hip/knee replacement patients; READM-30-PN-HRRP: Pneumonia patients | String | See "Brief description" column. | 
| Start Date | Represents the start date for collecting data for our calculations in a given row. Our data is refreshed annually, so there is no time window between start and end dates smaller than a year. | Timestamp | 2016-07-01 | 
| End Date | Represents the end date for collecting data for our calculations in a given row. Our data is refreshed annually, so there is no time window between start and end dates smaller than a year. | Timestamp | 2019-06-30 | 
| Excess Readmission Ratio | Description: Calculated by dividing a hospital’s predicted readmissions ratio (based on the hospital’s own data) by its expected readmissions ratio (which is averaged from data from other hospitals with similar patients) | float64 | Example: 0.9875 | 
| County | The county where the power utility/plant/generator is located. | String | Aleutians East| 
| State | The state where the power plant/generator is located. | String | AK | 
| Technology | The type of technology a given generator uses to generate energy. | String | Petroleum Liquids | 
| Plant Name | The name of a given power plant. | String | Mitchell Dam | 
|  Elec_MMBtu {Month} | The energy (in British thermal units) consumed for generating electricity in a given month for a given plant. | float64| 31,943.0| 
| Year | The year that energy data was collected. | float64 | 2024|



### Quantification of uncertainty
## Link to press release 
## Link to data 
