### code made by Viacheslav Volkov linkedIn/X.com - @oftendaydream


import pandas as pd

df = pd.read_csv("ml_jobs_europe_raw.csv")

df = df.drop_duplicates(subset=["title", "company"])

COUNTRY_MAP = {
    "at": "Austria",
    "be": "Belgium",
    "de": "Germany",
    "es": "Spain",
    "fr": "France",
    "it": "Italy",
    "nl": "Netherlands",
    "pl": "Poland",
    "gb": "UK",
    "ch": "Switzerland"
}
df["country"] = df["country"].map(COUNTRY_MAP)
print(df["country"].head)
print(df.shape)
#function to make skills
def skill_function(description):
    skills = [
    # languages
    "python", "sql", "java", "scala", "julia", "c++", "r programming","rstudio","tidyverse", "ggplot"
    
    # ml / dl frameworks
    "pytorch", "tensorflow", "keras", "jax", "scikit-learn",
    "xgboost", "lightgbm", "catboost",
    
    # nlp
    "nlp", "bert", "gpt", "llm", "transformers", "huggingface",
    "spacy", "nltk", "langchain", "rag", "llamaindex",
    "text classification", "named entity recognition", "ner",
    "sentiment analysis", "text generation",
    
    # computer vision
    "computer vision", "opencv", "yolo", "cnn",
    "image classification", "object detection", "segmentation",
    "stable diffusion", "gan", "diffusion",
    
    # mlops / infra
    "mlops", "docker", "kubernetes", "airflow", "mlflow",
    "kubeflow", "wandb", "dvc", "fastapi", "flask",
    "aws", "azure", "gcp", "spark", "kafka", "hadoop",
    
    # data
    "pandas", "numpy", "matplotlib", "seaborn", "plotly",
    "tableau", "powerbi", "dbt", "postgresql",
    "mysql", "mongodb", "redis", "elasticsearch",
    
    # tools
    "git", "linux", "matlab", "streamlit", "jupyter",
    ]
    found = []
    for skill in skills:
        if skill in description.lower():
            found.append(skill)
    return ", ".join(found)
            
df["skills"] = df["description"].apply(skill_function)
print(df["skills"][10])
print(df["description"][0][-100:])
print(df[df["skills"] != ""].shape)
#df.to_csv("ml_jobs_europe_clean.csv", index = False)
