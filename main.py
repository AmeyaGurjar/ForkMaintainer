from dotenv import load_dotenv
load_dotenv()
from github import Github, Auth
from os import getenv, system

GIT = Github(auth=Auth.Token(getenv("TOKEN")))
REPO_NAME = "LineageOS"
MY_REPO = "Project-FelineX"

lineage = GIT.get_user(REPO_NAME)
user = GIT.get_organization(MY_REPO)

for repo in lineage.get_repos():
    repo = repo.full_name.replace(f"{REPO_NAME}/", "")
    if "device" not in repo and "kernel" not in repo:
        print(f"{REPO_NAME}/{repo}")
        try:
            user.create_fork(f"{REPO_NAME}/{repo}")
            print("Forked!")
        except Exception as e:
            print(e)
    else:
        continue
