from dotenv import load_dotenv
load_dotenv()
from github import Github, Auth
from os import getenv, system

GIT = Github(auth=Auth.auth(getenv("TOKEN")))
REPO_NAME = "LineageOS"
MY_REPO = "Project-FelineX"

user = GIT.get_user(REPO_NAME)

for repo in user.get_repos():
    repo = repo.full_name.replace(f"{REPO_NAME}/", "")
    if "device" not in repo and "kernel" not in repo:
        print(repo)
    else:
        continue
