# Jobs Scrapping Program

This Python program scrapes Python-related job listings from the NoFluffJobs website and generates an Excel file containing two sheets: one with job details `Jobs` and another with the count of skills mentioned in the job listings `Skills`.

You can find the output Excel file in the same directory as the script.

## Description

- The program scrapes job listings from the NoFluffJobs website for Python-related positions. It fetches details such as job title, company, salary, skills required, and the link to the job listing.

- It counts the occurrences of each skill mentioned in the job listings and creates a histogram of skills on the `Skills` sheet.

- The program utilizes BeautifulSoup for web scraping, Requests for making HTTP requests, Pandas for data manipulation, NumPy for handling arrays, and XlsxWriter for writing Excel files.

