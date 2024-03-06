from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
from collections import Counter
from xlsxwriter import Workbook

num_pages = 4
df = pd.DataFrame(columns=['Job Title', 'Company', 'Salary','Skills','Link'])
var_list = np.empty((0,))
base_url = 'https://nofluffjobs.com'


for i in range(num_pages):
    page = requests.get(f'https://nofluffjobs.com/pl/Python?page={i+1}')
    soup = BeautifulSoup(page.text, 'html.parser')

    job_titles = soup.find_all('h3', class_='posting-title__position')
    companies = soup.find_all('h4', class_='company-name')
    salaries = soup.find_all('span', class_='salary')
    skills = soup.find_all('div', class_ = 'tiles-container')
    links = soup.find_all('a', class_='posting-list-item')

    for job_title,company,salary,skill,link in zip(job_titles,companies,salaries,skills,links):
        data = {
            'Job Title': job_title.text,
            'Company': company.text,
            'Salary': salary.text,
            'Skills': skill.text,
            'Link': base_url+link['href']
        }
        skills_array = np.array([var.strip() for var in skill.text.split("•")])
        var_list = np.append(var_list, skills_array)
        df = df._append(data,ignore_index = True)


skill_counts = Counter(var_list)
# Convert Counter object to dictionary
skill_dict = dict(skill_counts)

data_list = list(skill_dict.items())
df_sheet2 = pd.DataFrame(data_list, columns=['Skill', 'Count'])
df_sheet2 = df_sheet2.sort_values(by='Count',ascending=False)



file_path = 'jobs_scrapping.xlsx'


with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
    # Write the first DataFrame (df) to the first sheet
    df.to_excel(writer, sheet_name='Jobs', index=False)

    # Write the second DataFrame (df_sheet2) to the second sheet
    df_sheet2.to_excel(writer, sheet_name='Skills', index=False)


