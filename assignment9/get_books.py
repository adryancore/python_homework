# Task 4: Write out the Data

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
import pandas as pd
import json

# Initialize the Firefox WebDriver
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

try:
    # Load the target web page
    url = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"
    driver.get(url)

    # Wait until at least one search result item is present (up to 10 seconds)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "li.row.cp-search-result-item"))
    )

    # Find all <li> elements with the class 'row cp-search-result-item'
    li_elements = driver.find_elements(By.CSS_SELECTOR, "li.row.cp-search-result-item")

    results = []

    for li in li_elements:
        # Extract the title
        try:
            title_element = li.find_element(By.CSS_SELECTOR, "h2.cp-title span.title-content")
            title = title_element.text.strip()
        except:
            title = ""

        # Extract the author(s)
        try:
            author_elements = li.find_elements(By.CSS_SELECTOR, "span.cp-author-link a")
            authors = [author.text.strip() for author in author_elements]
            author = "; ".join(authors)
        except:
            author = ""

        # Extract the format and year
        try:
            format_year_element = li.find_element(By.CSS_SELECTOR, "div.cp-format-info span.display-info-primary")
            format_year = format_year_element.text.strip()
        except:
            format_year = ""

        # Append the extracted data to the results list
        results.append({
            "Title": title,
            "Author": author,
            "Format-Year": format_year
        })

    # Create a DataFrame from the results list
    df = pd.DataFrame(results)

    # Write the DataFrame to a CSV file
    df.to_csv('assignment9/get_books.csv', index=False)

    # Write the results list to a JSON file
    with open('assignment9/get_books.json', 'w') as json_file:
        json.dump(results, json_file, indent=4)

    # Print the DataFrame
    print(df)

finally:
    # Close the browser
    driver.quit()
