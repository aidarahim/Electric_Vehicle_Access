# Electric Vehicles: Equitable Access

## Executive Summary

On April 16, 2021, The Washington state legislature [passed](https://www.autoweek.com/news/green-cars/a36146281/washington-to-ban-gas-cars/#:~:text=The%20Washington%20state%20legislature%20has,the%20exception%20of%20emergency%20vehicles.) the Clean Cars 2030 bill, which will require that by 2030, all new light-duty vehicles sold or registered in the state be electric, with the exception of emergency vehicles. The bill outlines a transition period and calls for a number of impact studies to be completed before 2030, including an analysis centered on "equity, especially including disadvantaged and low-income communities, communities of color, and rural communities, and strategies for maximizing equity in implementation of the 2030 requirement," among other research.

In this work, we initiate a study that explores 3 areas:
1. The relationship between electric vehicle ownership and economic means
2. Access to charging facilities and the concept of 'garage orphan'
3. Networking of charging stations and 'range anxiety'

We find that 73% of electric vehicles (EVs) in WA state are owned in zipcodes with median income higher than the state median income. Growth in EV ownership the higher income zipcodes occurs at a faster rate as well. Over the last 10 years, 72% of housing permits in Seattle have been for non-single-family-housing, which is great for home ownership but underscores the need for equitable access to charging facilities across economic means. Large swathes of the state lack a well-connected charging station network, feeding into owners' range anxiety.

<p style="text-align: center"><img src="./images/Seattle_stations.png" alt="Data Trends" style="width: 1000px;"/></p>

<p style="text-align: center"><em>Charging stations in downtown Seattle, clustered by population and median income.</em></p>

## Introduction
EV sales make up XX % of national vehicle EV_sales. EVs are attractive because...
Chargers / charging station levels



#### Problem statement
How does electric vehicle ownership relate to markers of economic means?

Sources:
1. [Clean Cars 2030 passed by WA legislature](https://www.autoweek.com/news/green-cars/a36146281/washington-to-ban-gas-cars/#:~:text=The%20Washington%20state%20legislature%20has,the%20exception%20of%20emergency%20vehicles.)
2. [Clean Cars 2030](https://www.autoweek.com/news/green-cars/a35616508/washington-state-bill-ev-only-sales-by-2030/)
3. [Removing Barriers to Electric Vehicle
Adoption by Increasing Access to
Charging Infrastructure](http://www.seattle.gov/Documents/Departments/OSE/FINAL%20REPORT_Removing%20Barriers%20to%20EV%20Adoption_TO%20POST.pdf)
4. [Seattle city household and family survey](https://www.census.gov/acs/www/data/data-tables-and-tools/narrative-profiles/2018/report.php?geotype=place&state=53&place=63000)
5. [Update on electric vehicle costs in the US through 2030](https://theicct.org/sites/default/files/publications/EV_cost_2020_2030_20190401.pdf)

## Data analysis
The following observations were gathered from analysis of data on EV ownership, charging cycles, geographical charging station distribution, housing permits, and WA state population and income:
* EV registrations have been increasing over the last 10 years, though registrations for 2020 dropped down, presumably due to Covid-19
* The rate of increase in battery electric vehicle (BEV) sales outpaces that of plugin-hybrid electric vehicle (PHEV) sales. In fact, the drop in overall EV sales in the past couple of years is due to a drop in PHEV EV_sales
* The EV median price of \\$35,000 is ~1.5X the average price of a gas vehicle (\$21,000) [[source]](https://theicct.org/sites/default/files/publications/EV_cost_2020_2030_20190401.pdf)
* 72.8% of EV registrations in WA state were carried out in zip codes with median income above the state median income
* For both above- and below-median income groups, BEV ownership constitutes a higher percentage of total EV ownership
* With each resale, the EV goes from higher to lower median income zipcodes, and from higher to lower sale price. This bodes well for increased accessibility (price-wise), because EVs generally have lower maintenance costs due to much fewer moving parts, though battery longevity issues will start to arise
* Ownership growth is faster among owners in above-median zipcodes compared to below-median zipcodes, though ownership continues to grow there too. This is a promising trend
* From 3 datasets on charging cycles:
  * Charging at home occurs in the evening
  * Charging at work peaks in the morning only on weekdays
  * Usage of publicly accessible charging stations peak in the morning, at lunchtime, and at dinnertime, for both weekdays and weekends
* Housing lot sizes DO NOT follow Benford's law
* Since 2010, more non-single-family type homes (70%) are being constructed compared to single family homes, as these tend to be cheaper. But these homes also typically do not have easy access to power for the parked EV. Thought and effort need to be given to expanded and equitable access to vehicle charging across economic demographics
* Charging station network distribution lags behind EV-advanced countries such as Norway and China

## Modeling
Time series models were used to forecast EV sales 15 years into the future, as well as charging times for workplace-based charging stations. The models implemented were ARIMA, SARIMA and Facebook's Prophet.

K-Means clustering was applied to household charging data as well as population and income data, as relates to EV charging station distribution. Clustering was also carried out using objective numerical measures of distance.

## Conclusions

## Recommendations

## APPENDIX

### 1. Repository Contents

### 1.1. Jupyter notebooks

### 1.2. Data folder

### 2. Data Description

### 3. Software Requirements

Electric vehicles are the future. Consumers are interested in the greatly reduced fueling costs, minimal parts and maintenance, reduced carbon emissions, and exhilirating acceleration and power. The US big 3 automakers are chasing Tesla's dominance in the EV space:

Best of all, rebates and incentives save you money when you purchase or lease a new EV, helping make your transaction more affordable.
* On Jan 20, 2021, General Motors announced that they aim to sell only zero-emission cars and trucks by [2035](https://www.nytimes.com/2021/01/29/business/general-motors-electric-cars.html)
* Ford announced a \$29 billion investment in EVs and autonomous vehicles through 2025, with a statement that in the future, the majority of Ford vehicles will be electric, while traditional gasoline powertrains will be augmented with hybrid and plug-in hybrid [powertrains](https://www.caranddriver.com/news/a35432253/ford-ev-commitment-announced/)
* Stellantis – the product of a $52 billion merger between automakers Fiat Chrysler and Groupe PSA – plans to offer an array of all-electric or hybrid vehicles through [2025](https://www.cnbc.com/2021/01/19/from-jeep-to-maserati-stellantis-to-rollout-10-new-ev-models-in-2021.html)
* A record number of almost 100 pure electric EV models is set to debut by the end of [2024](https://www.consumerreports.org/hybrids-evs/why-electric-cars-may-soon-flood-the-us-market/)


<img src="./Checkin 02/images/EV_sales.png" style="float: center">

*Source*: [SeekingAlpha](https://seekingalpha.com/article/4410640-ev-company-news-for-month-of-february-2021)

However, one of the most commonly cited barriers is the uncertainty associated with needing access to charging facilities for PEV drivers to plug in their vehicles (range anxiety). EV charging companies, towns and municipalities, individual businesses, local and federal government, are all interested in providing servies and capitalizing on this projected need. But how many and what kind of charging stations are needed? Where and how often do PEV drivers charge? The charging model for EVs is very dissimilar to that for fossil fuel vehicles, with charging time dependent on charger type and battery capacity. Therefore it's not as simple as adding EV charging stations to gas stations. The user's charging behavior will vary depending on where they live, where they work, and their travel patterns. Other than at home or at the workplace (primary and secondary charging locations), charging also occurs at individual charging stations at different parking lots. There are lots of logistical questions to answer, but what is clear is that publicly accessible EV charging infrastructure will need to be expanded.

**In this project, I will develop a proposal for EV charging station distribution in WA state over time until 2030, based on historical and projected EV sales in WA and the current EV charging station distribution in WA.**
