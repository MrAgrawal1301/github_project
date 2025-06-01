import os 
from dotenv import load_dotenv
load_dotenv()
from github import Github
token  = os.getenv("GITHUB_TOKEN")

# Public Web Github
g = Github(token)

user = g.get_user()
print(user.login)

repos = user.get_repos()
name_list = []
for repo in repos:
    print(repo.name)    
    name_list.append(repo.name)
    branches = repo.get_branches()

    for branch in branches:
        print(branch.name)
        print(branch.commit.sha)
        commit = repo.get_commit(sha=branch.commit.sha)
        print(commit.commit.author.date)



repo1 = user.get_repos()
for repo in repo1:
    print(list(repo.get_branches()))



