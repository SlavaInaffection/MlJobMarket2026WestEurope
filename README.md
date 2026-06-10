# MlJobMarket2026WestEurope
Research about West Europe Job market on DS/ML/AI engineer position, made by Viacheslav Volkov(https://www.linkedin.com/in/oftendaydream/)

# ML Engineer Job Market Research — Europe 🇪🇺

A data research project analyzing Machine Learning Engineer job postings
across 10 European countries to understand market demand, required skills,
and salary trends.

## What it does

- Fetches real job postings from 10 European countries via the Adzuna API
- Cleans and structures the raw data
- Extracts in-demand skills from job descriptions
- Analyzes trends across countries

## Countries covered

Austria, Belgium, Germany, Spain, France, Italy, Netherlands, Poland, UK, Switzerland

## Project structure

ResearchJobMarket/
├── fetchData.py       # fetches job postings from Adzuna API
├── clearData.py       # cleans raw data, extracts skills
├── analyze.py         # analysis and visualizations
└── README.md

## How to run

1. Clone the repo
2. Install dependencies
pip install requests pandas matplotlib seaborn

3. Add your Adzuna API credentials to fetchData.py
4. Run in order:
python fetchData.py
python clearData.py
python analyze.py

## Tech stack

- Python
- Pandas
- Requests
- Matplotlib / Seaborn
- Adzuna Jobs API

## Limitations

- Adzuna free tier returns truncated job descriptions
  which limits skill extraction accuracy
- Salary data is sparse across most countries
- Dataset represents a snapshot in time (June 2026)

## Author

Viacheslav Volkov
LinkedIn/X: @oftendaydream