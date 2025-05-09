# Task 6: Scraping Structured Data

from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import os

# Ensure we're in the right directory
print("Current working directory:", os.getcwd())

# Set up the Firefox driver (make sure you have geckodriver installed)
driver = webdriver.Firefox()

# Open the OWASP Top 10 page
driver.get("https://owasp.org/www-project-top-ten/")

# Use the XPath to find all the vulnerabilities
vulnerabilities = driver.find_elements(By.XPATH, "//a[@href]/strong")

# List to store extracted data
vulnerability_data = []

# Loop through the found elements and extract the title and href link
for vuln in vulnerabilities:
    title = vuln.text
    link = vuln.find_element(By.XPATH, "..").get_attribute("href")
    vulnerability_data.append({"title": title, "link": link})

# Print extracted data
if vulnerability_data:
    print("Extracted Data:")
    for vuln in vulnerability_data:
        print(vuln)
else:
    print("No vulnerabilities found on the page.")

# Define the file path
csv_path = '/Users/adryancorcione/python_class/python_hw/assignment9/owasp_top_10.csv'

# Debug: Check if the CSV path exists before writing
print("Checking if CSV path exists:", os.path.exists(os.path.dirname(csv_path)))

# Write the extracted data to a CSV file
try:
    with open(csv_path, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["title", "link"])
        writer.writeheader()
        writer.writerows(vulnerability_data)

    print("Data written to owasp_top_10.csv.")
except Exception as e:
    print("Error writing to CSV:", e)

# Close the browser
driver.quit()

# Print the final working directory for confirmation
print("Final working directory:", os.getcwd())
