# Data dictionaries for the data used in this project

## EVs Registered in WA state
[*Dictionary Source*](https://data.wa.gov/Transportation/Electric-Vehicle-Population-Data/f6w7-q2d2)

| Column Name                                       | Description                                                                                                                                                                                         |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VIN (1-10)                                        | The 1st 10 characters of each vehicle's Vehicle Identification Number (VIN).                                                                                                                        |
| County                                            | The county in which the registered owner resides.                                                                                                                                                   |
| City                                              | The city in which the registered owner resides.                                                                                                                                                     |
| State                                             | The state in which the registered owner resides.                                                                                                                                                    |
| ZIP Code                                          | The 5-digit zip code in which the registered owner resides.                                                                                                                                         |
| Model Year                                        | The model year of the vehicle, determined by decoding the Vehicle Identification Number (VIN).                                                                                                      |
| Make                                              | The manufacturer of the vehicle, determined by decoding the Vehicle Identification Number (VIN).                                                                                                    |
| Model                                             | The model of the vehicle, determined by decoding the Vehicle Identification Number (VIN).                                                                                                           |
| Electric Vehicle Type                             | This distinguishes the vehicle as all electric or a plug-in hybrid.                                                                                                                                 |
| Clean Alternative Fuel Vehicle (CAFV) Eligibility | This categorizes vehicle as Clean Alternative Fuel Vehicles (CAFVs) based on the fuel requirement and electric-only range requirement in House Bill 2042 as passed in the 2019 legislative session. |
| Electric Range                                    | Describes how far a vehicle can travel purely on its electric charge.                                                                                                                               |
| Base MSRP                                         | This is the lowest Manufacturer's Suggested Retail Price (MSRP) for any trim level of the model in question.                                                                                        |
| Legislative District                              | The specific section of Washington State that the vehicle's owner resides in, as represented in the state legislature.                                                                              |
| DOL Vehicle ID                                    | Unique number assigned to each vehicle by Department of Licensing for identification purposes.                                                                                                      |
| Vehicle Location                                  | The center of the ZIP Code for the registered vehicle.                                                                                                                                              |

## EV charging stations in WA state
[*Dictionary Source*](https://afdc.energy.gov/data_download/alt_fuel_stations_format)

| Column Name                 | Description                                                                                          |
|-----------------------------|------------------------------------------------------------------------------------------------------|
| Station Name                | The name of the station.                                                                             |
| Street Address              | The street address of the station's location.                                                        |
| Intersection Directions     | Brief additional information about how to locate the station.                                        |
| City                        | The city of the station's location.                                                                  |
| State                       | The two character code for the U.S. state or Canadian province/territory of the station's location.  |
| Zip                         | The ZIP code (postal code) of the station's location                                                 |
| Groups With Access Code     | A description of who is allowed to access the station and other station access information.          |
| Access Days Time            | Hours of operation for the station.                                                                  |
| EV Level1 EVSE Num          | The number of Level 1 EVSE (standard 110V outlet).                                                   |
| EV Level2 EVSE Num          | The number of Level 2 EVSE (J1772 connector).                                                        |
| EV DC Fast Count            | The number of DC Fast Chargers.                                                                      |
| EV Network                  | The name of the EVSE network, if applicable.                                                         |
| EV Network Web              | The EVSE network Web site, if applicable.                                                            |
| Geocode Status              | A rating indicating the approximate accuracy of the latitude and longitude for the station's address |
| Latitude                    | The latitude of the station's address.                                                               |
| Longitude                   | The longitude of the station's address.                                                              |
| Date Last Confirmed         | The date the station's details were last confirmed.                                                  |
| ID                          | A unique identifier for this specific station.                                                       |
| Updated At                  | The time the station's details were last updated (ISO 8601 format).                                  |
| Owner Type Code             | The type of organization that owns the fueling infrastructure                                        |
| Open Date                   | The date that the station began offering the service.                                                |
| EV Connector Types          | Connector types available at this station.                                                           |
| Facility Type               | The type of facility at which the station is located.                                                |
| EV Pricing                  | Information about whether and how much users must pay to use the EVSE.                               |
| EV On-Site Renewable Source | The type of renewable energy used to generate electricity on-site                                    |
