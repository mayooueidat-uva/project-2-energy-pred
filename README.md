# DS 4320 Project 2: [PLACEHOLDER]<br>
Executive Summary: [placeholder until finished]<br>
Name: Maya Uwaydat<br>
NetID: zvd6vz<br>
DOI: [placeholder until finished]<br>
Press Release: [placeholder]<br>
Pipeline: [placeholder]<br>
License: [MIT License](https://github.com/mayooueidat-uva/project-2-energy-pred/blob/main/LICENSE.md)
## Problem definition 
## Domain exposition 
### Terminology 
### Domain
### Further Reading
| Title | Brief description | link | 
| ------| -----------------| -------| 
| Villarosa Pollution is Killing Black Americans. This community fought back. | [placeholder] | [link](https://myuva-my.sharepoint.com/:b:/g/personal/zvd6vz_virginia_edu/IQAfai7jSp6YTo3OXZHPgXsxAYzlM6tSfUUFkkNB6sdDkWk?e=iuC9FC) | 
## Data creation
### Provenance
Data was collected from the Center for Medicare and Medicaid Services (CMS) and U.S. Energy Information Administration (EIA). For energy demand and hospital readmissions, data from 2021 to 2026 was procured; however, power plant data was unavailable for 2025-2026, so I only gathered data for 2021-2024. No API was available for CMS’s archived data, so the files were manually downloaded and unzipped from the website. When perusing the EIA’s website, I wanted to see available data on energy demand and zip codes, as I intended to refine my problem statement based on available data. Therefore, I also downloaded EIA data manually; the website’s downloads pages were easier to navigate than their API, as their API tool requires one to choose between thousands of parameters. 
	After ensuring all data was in UTF-8 format, a table or two from each dataset—hospital readmissions, energy demand, and power plants—was put into MongoDB Compass, which allowed me to view the proportion of numeric data read as strings, columns with significant NaNs, summary statistics, et cetera. All data was loaded separately and cleaned accordingly in JupyterLab, using Python. Cleaned spreadsheets were loaded into the Mongo database to be extracted in other notebooks for further processing and for analysis. 

### Code files
### Rationale
### Bias identification 
### Bias mitigation 
## Metadata
### Implicit Schema
### Database contents 
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
