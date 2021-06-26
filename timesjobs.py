from bs4 import BeautifulSoup
import requests

print("Welcome to Python jobs")
Skills = input("Enter your skills here: ")
print("Loading...")
print(" ")
content = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

soup = BeautifulSoup(content, "lxml")
jobs = soup.find_all("li", class_= "clearfix job-bx wht-shd-bx")
for index, job in enumerate(jobs):
    published_date = job.find("span" , class_ = "sim-posted").span.text
    if "few" in published_date:
        company_name = job.find("h3", class_ = "joblist-comp-name").text.replace(" ", "")
        job_dtl = job.find("ul", class_ = "list-job-dtl clearfix").li.text
        key_skills = job.find("span", class_ = "srp-skills").text.replace(" ","")
        job_link = job.header.h2.a['href']
        if Skills in key_skills:
            with open (f'post/{index}.txt', "w") as f:
                f.write(f'''Company Name:{company_name.strip()}\n''')
                f.write(f''' {job_dtl}\n''')
                f.write(f'''Key skills:{key_skills.strip()}\n''')
                f.write(f"More info:{job_link}")
            print(f"file saved: {index}") 