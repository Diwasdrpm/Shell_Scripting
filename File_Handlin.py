from github import Github

g= Github('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')

repo_name= input("Enter the reop path(username/repository_name): ")
repo = g.get_repo(repo_name)
pulls = repo.get_pulls(state='open', sort='created', base='master')
count = 0
print("Pull requests which are still opened:")
for numbers in pulls:
    print(""+str(numbers.number))
    count+=1
    print("")
    # print(numbers.assignees)

print("Total Pull requests in this repo are: ")
print(count)

