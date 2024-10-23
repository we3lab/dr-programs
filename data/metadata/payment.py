#Structure
#Domain: delivered ratio (how much is shed vs how much is bid to shed, kind of a percentage of expected load shed) 
#Slope: how much payment changes as delivered ratio changes 
#Intercept: payment ratio (how much is paid; this value is multiplied by the capacity price * load shed) 

#Variables
#Capactiy payment in $ per KW (negative if there is a penalty) 

#Some capacity payments are determined using the average of the two consecutive hours with the highest load reduction 
#So we would include time/date stamps where load reduction is evaluated and what function to apply to the load reduction values at those times/dates

#Some capacity payments are different depending on the day of the week or the month 

#Some payment structures include a flat participation incentive 

#Note- Some programs only have energy payments, some only have capacity payments, some have both. I have not included energy payments