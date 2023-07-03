from dotenv import load_dotenv
load_dotenv()
from github import Github, Auth
from os import getenv, system

GIT = Github(auth=Auth.Token(getenv("TOKEN")))
REPO_NAME = "LineageOS"
MY_REPO = "Project-FelineX"

lineage = GIT.get_organization(REPO_NAME)
org = GIT.get_organization(MY_REPO)

for repo in lineage.get_repos():
    repomain = repo.full_name.replace(f"{REPO_NAME}/", "")
    if "device" not in repomain and "kernel" not in repomain:
        print(f"{REPO_NAME}/{repomain}")
        org.create_fork(repo, default_branch_only=True)
        print("Forked!")
    else:
        continue
