# sb525scraper
saves enrollment status for sb525 clinical trial as CSV.

i left alot of the print statements to show how each problem is broken down 

use chrontab or scheduler to schedule the sb525 scripts at two different intervals

CSV comparison checks for difference in the CSV files. So if any of the rows in the CSV file changes it will send an email it will send an email

put email and password that you want to send from and the receipent in the config.py
