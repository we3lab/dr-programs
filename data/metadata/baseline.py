#Baseline Determining Functions 
#Date Range: dates from which baseline days are selected 

#Weekends?: Yes or no (Can measurements be taken on weekdends?)
weekends: True/False 
#Holidays? Yes or no (can measurements be taken on holidays?)
holidays: True/False 
#Previous events? 
prev_events: True/False 
#Time range: time of day during which load can be measured 
base_hours: 0-24 
#Load measurement frequency - minutes vs. hourly vs. monthly: how often load is measured 
range_resolution: "month", "days", "hours", "minutes" 
range_value: #
#Load measurement function - avg vs. max: function applied to load measurements in a given time range and date range
function: mean(), max(), min(), median()

#Alternative: Firm Level Demand value is baseline; Firm level demand is a baseline value that the company has to meet in order to receive payment
#Add another variable called firm level demand that will be used in the payment function instead of baseline. (payment function
#will either use baseline or firm level demand)F