# Jobs Scrapping Program

This Python program scrapes job listings from the NoFluffJobs website and generates an Excel file containing two sheets: one with job details `Jobs` and another with the count of skills mentioned in the job listings `Skills`.

You can find the output Excel file in the same directory as the script.

## Files

`Param_and_rec.py` returns offers with given paramters and extra jobs recommended by the website based on them.

`Param_only.py` returns offers only with given parameters.

All is based on Polish version of the website, so given criteria [skills, seniority, localisation] have to be in this language as well.

## Description

- The program scrapes job listings from the NoFluffJobs website. It fetches details such as job title, company, salary, skills required, and the link to the job listing.

- It counts the occurrences of each skill mentioned in the job listings and creates a histogram of skills on the `Skills` sheet.

- The program utilizes BeautifulSoup for web scraping, Requests for making HTTP requests, Pandas for data manipulation, NumPy for handling arrays, and XlsxWriter for writing Excel files.

