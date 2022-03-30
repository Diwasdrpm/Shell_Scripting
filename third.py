from github import Github
import sys
from os.path import expanduser
import os
from git import Repo


g = Github("t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")
user = g.get_user()
print(user)
url = str(sys.argv[1]).replace("https://github.com/", "").split("/")
org = g.get_organization(url[0])
repo = org.get_repo(url[1])
my_fork = user.create_fork(repo)
local_repo = repo.clone_from("git@github.com:" + str(user.login) + "/" + str(repo.name) + ".git", os.getcwd() + "/" + str(repo.name), branch="master")
Repo.create_remote(local_repo, "upstream", "git@github.com:" + url[0] + "/" + url[1] + ".git")