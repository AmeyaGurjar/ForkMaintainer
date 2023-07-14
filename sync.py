from dotenv import load_dotenv
load_dotenv()
from sys import argv
from time import sleep
from github import Github, Auth
from os import getenv, system, remove
MY_ORG = str(getenv("MY_REPO"))
TARGET_ORG = str(getenv("TARGET_REPO"))
TARGET_ALL_REPOS = []
try:
    remove("sync-logs.txt")
except:
    pass
logFile = open("sync-logs.txt", "a")

GIT = Github(auth=Auth.Token(getenv("TOKEN")))
my_org = GIT.get_organization(MY_ORG)
target_org = GIT.get_organization(TARGET_ORG)
MY_REPOS = my_org.get_repos()
TARGET_REPOS = target_org.get_repos()

for tar_num, tar_repo in enumerate(TARGET_REPOS):
    TARGET_ALL_REPOS.append(str(tar_repo.full_name))
    print(f"[{tar_num}] - FETCHED")
    
for repo_num, repo in enumerate(MY_REPOS):
    repo_name_tar = str(repo.full_name).replace(f"{MY_ORG}/", f"{TARGET_ORG}/")
    repo_name = str(repo.full_name).replace(f"{MY_ORG}/", "")
    if (repo_name_tar in TARGET_ALL_REPOS):
        final_repo = target_org.get_repo(repo_name)
        print(final_repo.forks_url)
        final_repo.merge(commit_message="Synced")
        
logFile.close()
