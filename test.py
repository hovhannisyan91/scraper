from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set up the Selenium WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open the Wikipedia page
url = "https://simple.wikipedia.org/wiki/List_of_countries"
driver.get(url)

# Find the section with class "mf-section-1"
sections = driver.find_elements(By.CLASS_NAME, "mf-section-1")

# Initialize an empty list to store the split values
split_values = []

# Extract and split the text from each section
for section in sections:
    text = section.text.strip()  # Get text and remove extra spaces
    if text:  # Ensure the text is not empty
        split_values.extend(text.split(" - "))  # Split by " - " and add to list

# Print the split values
print(split_values)

print("Done")