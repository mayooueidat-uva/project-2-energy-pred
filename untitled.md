# Your Quality of Health is Electrifying  
## Can monthly electricity demand and generator type be used to predict something as importat as hospital readmissions? The power of prediction can be electrifying sometimes, but sometimes...it isn't. 
## problem statement 
Energy generation, especially by fossil-fuel sources, can have negative health implications for communities surrounding the plants. It is crucial to determine what features of power plants contribute to negative health outcomes, so we must see whether energy demand in certain months, or types of generator, contribute to excess readmissions.
## Solution description 
Data from the Energy Information Administration (EIA) and the Centre for Medicare and Medicaid Services (CMS) was gathered. While the EIA data was used to investigate monthly energy demand and generator type; meanwhile, the CMS data was used to view excess readmission rates, which gives a sense of the proportion of readmissions a hospital receives compared to what is "normal." Electricity used to generate energy in British thermal units was used as a proxy for demand.<br>
The excess readmission ratio corresponding to each power plant was the average excess readmission rate for the ZIP code it was located in. 
The most important features contributing to excess readmissions rates were identified using a machine-learning tool called 'SHAP'. No one feature contributed exceedingly more than others, though monthly demand seemed to contribute more than generator type. 
## Chart