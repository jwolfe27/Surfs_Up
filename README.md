# Surfs Up!  Oahu, Hawaii Climate Analysis

![Oahu_Picture](https://user-images.githubusercontent.com/89044350/138095687-3a18ee4e-d091-4fce-b353-10488b852414.jpg)

## Project Overview
Analyze climate data of Oahu, Hawaii in order to make an informed decision if Oahu is the best location to open a year round Surf & Ice Cream Shop.

### Tools Used
- Jupyter Notebook with imported dependencies
- VS Code
- Flask

## Analysis
### 1. The first analysis consisted of pulling precipitation amounts in Oahu, Hawaii for a period of 1 year. 
![Hawaii_Precip_Data](https://user-images.githubusercontent.com/89044350/138100296-2c19b15e-f9b0-4c89-a1eb-78e5e457530a.PNG)
![Hawaii_Precip_Describe](https://user-images.githubusercontent.com/89044350/138100342-1783111c-5b68-4946-b806-6131c0ddaf35.PNG)

### 2. The second analysis compared the temperatures for June and December:
June:

![June_Temps](https://user-images.githubusercontent.com/89044350/138101228-b37ab459-f841-4880-a3c0-667d06eddbaa.PNG)

December:

![Dec_Temps](https://user-images.githubusercontent.com/89044350/138101348-f7aeec83-44d6-4bb4-9e1a-a4cc0f41d73d.PNG)

### 3.  Inside VSCode, we were able to utilize Python and SQLAlchemy ORM queries to reflect tables in a new model.  We then built a Flask app using the developed queries

![Routes_Build](https://user-images.githubusercontent.com/89044350/138102068-7391c39d-3a64-4710-b2b6-bd1a12d508a6.PNG)
![Define_Min_Avg_Start_End](https://user-images.githubusercontent.com/89044350/138102267-3b566383-0f32-493e-beb7-a60aa3535a75.PNG)

## Additional Analysis Performed
To add two additional analyses to the project, I compared the amount of preciptation to the temperature for the months of June and December to see if there is a trend there.

![June_Precip_Temp](https://user-images.githubusercontent.com/89044350/138109313-01385a45-68bf-4e40-a4b6-890cc08dedea.PNG)
![June_Temp_Precip_Describe](https://user-images.githubusercontent.com/89044350/138110058-200698ed-ee87-426e-9fe8-67bdcb4bac29.PNG)

![Dec_Precip_Temp](https://user-images.githubusercontent.com/89044350/138109380-049bab9b-0d74-4f47-802e-22b30d55276f.PNG)
![Dec_Temp_Precip_Describe](https://user-images.githubusercontent.com/89044350/138110130-d089cebe-82e2-465c-b5e4-3697b8392547.PNG)

## Summary
As shown above there is very little difference in terms of expected temperature between June and December. The average temperature in June is around 75, while the average temp in December is around 71.  Looking at precipitation data, June averages approximately .14 inches of rain, while December averages approximately .22" inches. There are a few outliers, but nothing concerning. The trend shows that as the temperature increases, the precipitation decreases.

If the concern for opening a year round Surf & Ice Cream Shop is getting too much precipitation,  this analysis shows that Oahu is a great destination as temperature range and precipitation amounts are minimal.  I would recommend pulling data from multiple stations before investing in additional Surf Shop locations on other islands to see if the same trends hold true.
