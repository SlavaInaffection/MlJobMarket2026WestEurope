import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os # to check folders
os.makedirs("charts", exist_ok=True)

def load_data():
    return pd.read_csv('ml_jobs_europe_clean.csv')

def skill_plotbar(df):
    skills = []
    for skill in df['skills']:
        if pd.isna(skill) : # check if the row is NaN
            continue
        for s in skill.split(','): # split words in a row
            skills.append(s.strip()) # add words and delete spaces
    counted_skill = pd.Series(skills).value_counts() # count every unique skill
    
    # Making a plotbar
    plt.figure(figsize=(12, 5))
    sns.barplot(x=counted_skill.index, y=counted_skill.values )
    plt.title('Common skills in ML job vacancies')
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    # first graph 
    plt.savefig(f'charts/most_common_skills.png')



def country_plotbar(df):
    countries = []
    for country in df['country']:
        if pd.isna(country):
            continue
        countries.append(country)

    counted_country = pd.Series(countries).value_counts()
    print(counted_country)
    
    plt.figure(figsize=(12, 5))
    sns.barplot(x=counted_country.index, y=counted_country.values )
    plt.title('Most common countries for ML job')
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    # second graph 
    plt.savefig(f'charts/vacanies_per_country.png')


def skills_by_country(df,input_country):
    country_df = df[df["country"] == input_country]
    skills_country = []
    for skill_country in country_df["skills"]:
        if pd.isna(skill_country) : # check if the row is NaN
            continue
        for s in skill_country.split(','): # split words in a row
            skills_country.append(s.strip()) # add words and delete spaces
    counted_skill_country = pd.Series(skills_country).value_counts() # count every unique skill
    
    plt.figure(figsize=(12, 5))
    sns.barplot(x=counted_skill_country.index, y=counted_skill_country.values )
    plt.title(f'Most common skills in {input_country}  for ML job')
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    # third one graph 
    #plt.savefig(f'charts/skills_{country}.png')


def polular_title_function(df):
    # dont need a loop cuz we need just whole column
    counted_titles = df["title"].value_counts()
    top_titles = counted_titles.head(15)


    plt.figure(figsize=(12, 5))
    sns.barplot(x=top_titles.index, y=top_titles.values )
    plt.title(f'Most common titles')
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    #plt.savefig('charts/common_titles.png')




# run functions
if __name__ == "__main__":
    df = load_data()
    # polular_title_function(df)
    
    # Delete '#' to use function by urself


    #skill_plotbar(df)
    #country_plotbar(df)
    #for country in df["country"].unique():
        #skills_by_country(df, country)
