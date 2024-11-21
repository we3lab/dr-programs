# dr-programs
Data Records
------------
Data in this repository consists of metadata (2 CSV files) and program data (2 CSV files):
Metadata
- program_parameters.csv
- simulation_parameters.csv
Program Data
- us_program_parameters.csv
- us_simulation_parameters.csv

Metadata
--------
Metadata is stored in two CSV files, one with program parameters and one with simulation parameters. Each parameter takes up one row. 
- **Minimum number of event days (min_days):** The minimum number of days the program event is called for a customer per month
- **Maximum number of event days (max_days):** The maximum number of days the program event is called for a customer per month
- **Minimum duration of event (min_dur):** The event should last for more than the minimum duration specified by the program
- **Maximum duration of event (max_dur):** The event should not last longer than the maximum duration specified by the program
- **Program start time (start_time):** The program can be either 24 hours or last for a specified period of time and the start time is generally provided if it is not a 24-hour period
- **Program end time (end_time):** The program can be either 24 hours or last for a specified period of time and the end time is generally provided if it is not a 24-hour period
- **Maximum Events (max_events):** Maximum number of events that can be called in a season 
- **Maximum event hours (max_hours):** Maximum total hours of all events called in a year 
- **Events per day (events_daily):** The maximum event that a customer can provide on a single day.
- **Maximum consecutive event days (max_consec):** The maximum consecutive days the customer can be called in a particular month
- **Notification type	(notif_type):**	The event is generally notified the day before or the day of and is captures by this parameter
- **Notification time (notif_time):**	If the event is notified the day before or the day of the program generally specifies the time. Note: This can also be historic event related
- **Notification time delta (notif_delt):** The number of hours between the notifcation time and the beginning of an event 
- **Baseline calculation method (base_method):** The method used by each program to calculate the baseline energy usage
- **Presence of historic data	(hist_pres):** Programs may or may not have historic data present 
- **Payment function (pay_function):** Form of compensation for shifts in energy load (or being available to shift energy loads) when called upon 
- **Region (region):** The United States Department of Energy separates the states into the West Region, The Southeast and Midwest Region, and the Northeast Region
- **Days of the Week (dow):**	Which days of the week can events fall on? 
- **Season (season):** Some programs run during the summer, winter, or both
- **Eligibility (elig):**	Eligibility to particpate in the program (minimum bids, minimum peak demand, etc.)
- **Company (comp):**	Which company or companies offer this program
- **Start month (sm):** Month during which the DR event season starts
- **End month	(em):**	Month during which the DR event season ends 
- **State	(state):** State in which the program is eligible
- **Utility (util):**	Eligible utilities 
- **Trigger (trigger):** Event trigger type
- **Eligible load type (load):** What type of load is eligible for particpation in the program 
- **Program or rate (program_rate):**	Classification as a program or a rate by the Department of Energy 
- **Payment  Function (function_pay):** Function for calculating payment after an event
- **Baseline Function	(function_base):** Function for calculating baseline 
- **Delivered Ratio (delivered ratio):** = amount reduced/nomination of delivery 
- **Amount reduced:** baseline - consumption
- **Inclusion of weekends	(weekends):**	Does the baseline calculation include weekends or not? 
- **Inclusion of holidays	(holidays):** Does the baseline calculation include holidays or not?
- **Inclusion of previous events (prev_events):**	Does the baseline calculation include previous events or not?
- **Baseline hours (base_hours):** Time of day during which load measurements can be taken for baseline calculation 
- **Range Value (range_val):** Number of load measurements taken at a certain frequency for baseline calculation
- **Range Resolution (range_res):** Frequency of load measurement for baseline calculation 
- **Date Range (base_dates):** Dates during which load measurements are taken for baseline calculation 
- **Function (function):** Function applied to load measurement for baseline calculation 
- **Firm Level Demand	(firm_level):**	Load level that companies are expected to reduce their load to (alternative to baseline) 

 Methods
 -------
To create this dataset, the U.S. DOE Federal Energy Management Program's Demand Response and Time-Variable Pricing website, which listed and described energy management programs across the united States, was referenced. 

First, program parameters were defined. These parameters characterize each program by their distinct features. These parameters can be found in program_parameters.csv in the metadata file. 

Next, programs were populated in the dataset along with their parameters (if available) and a url link to the program source/website. 

The dataset, after being populated, was cross-checked with the U.S. DOE Federal Energy Management Program's...

 Simulation Parameters
 ---------------------
 Simulation parameters can be used to characterized simulated demand response events using the demand response simulator. These parameters can be found in... 

 Attribution & Acknowledgements
 ------------------------------




 