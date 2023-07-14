from dotenv import load_dotenv
load_dotenv()
from sys import argv
from time import sleep
from github import Github, Auth
from os import getenv, system, remove
MY_ORG = str(getenv("MY_REPO"))
TARGET_ORG = str(getenv("TARGET_REPO"))
try:
    remove("logs.txt")
except:
    pass
logFile = open("logs.txt", "a")

GIT = Github(auth=Auth.Token(getenv("TOKEN")))
my_org = GIT.get_organization(MY_ORG)
target_org = GIT.get_organization(TARGET_ORG)
MY_REPOS = my_org.get_repos()
TARGET_REPOS = target_org.get_repos()

for repo_num, repo in enumerate(MY_REPOS):
    print(repo_num, repo)
    repo_name = str(repo.full_name).replace(f"{MY_ORG}/", "")
    print(repo_name)
    if (repo_name in TARGET_REPOS):
        print("Meow")
        print(target_org.forks())
        print(target_org.forks_url())
logFile.close()
