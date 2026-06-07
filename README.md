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
| Measure ID | Identifies what types of patients are represented in the readmissions ratios columns of a particular row in the data sheet. 
- READM-30-AMI-HRRP: Heart attack patients 
- READM-30-COPD-HRRP: Pulmonary disease patients 
- READM-30-CABG-HRRP: Coronary artery bypass graft patients 
- READM-30-HF-HRRP: Heart failure patients 
- READM-30-HIP-KNEE-HRRP: Hip/knee replacement patients 
- READM-30-PN-HRRP: Pneumonia patients
| String | See "Brief description" column. | 

### Quantification of uncertainty
## Link to press release 
## Link to data 
