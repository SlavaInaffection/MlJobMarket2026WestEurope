### code made by Viacheslav Volkov linkedIn/X.com - @oftendaydream

import requests
import pandas as pd
API_KEY = ''
API_ID = ''
# dir(all commands), status code to check status code 
# countries from api documentation
countries = ["at", "be", "de", "es", "fr", "it", "nl", "pl", "gb", "ch"]
keywords = ["machine learning", "data scientist", "ML engineer", "deep learning", "AI engineer"]


page = 1
jobs = []
# for each country make a list of each job, loop for using multiple keywords 
for country in countries:
    url = f'https://api.adzuna.com/v1/api/jobs/{country}/search/{page}'
    Params = {
    "app_id" : API_ID,
    "app_key": API_KEY,
    "results_per_page": 50,
    
    }
    for keyword in keywords:
        Params['what'] = keyword
        response = requests.get(url,params=Params)
        if response.status_code == 200:
            data = response.json()
        else:
            print(f'Failed, {response.status_code}')
            print(response.text)

        for job in data["results"]:
            jobs.append({
                'title': job['title'],
                'company': job['company'].get('display_name', 'Unknown'),
                'country': country,
                'description': job['description'],
                'url': job['redirect_url']
            
    })
    
df = pd.DataFrame(jobs)
df.to_csv("ml_jobs_europe_raw.csv", index=False)
print(f'Saved {len(df)} jobs')










