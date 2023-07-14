from dotenv import load_dotenv
load_dotenv()
from sys import argv
from time import sleep
from github import Github, Auth
from os import getenv, system, remove
MY_REPO = str(getenv("MY_REPO"))
try:
    remove("logs.txt")
except:
    pass
logFile = open("logs.txt", "a")

GIT = Github(auth=Auth.Token(getenv("TOKEN")))
org = GIT.get_organization(MY_REPO)

for repo_num, repo in enumerate(org.get_repos()):
    print(f"Deleting {repo.full_name}")
    try:
        repo.delete()
        logFile.write(f"{repo_num} - [DELETED] - {repo.full_name}")
        print(f"{repo_num} - [DELETED] - {repo.full_name}")
    except:
        logFile.write(f"{repo_num} - [ERROR] - {repo.full_name}")
        print(f"{repo_num} - [ERROR] - {repo.full_name}")
logFile.close()
