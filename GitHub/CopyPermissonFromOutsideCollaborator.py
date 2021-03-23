pip3 install github3.py

import pycurl
import github3
############# Configuration Area #########################
# Put your GitHub token here
githubToken = ""
# GitHub ID that you want to copy from
copyFromId = ""
# GitHub ID that you want to copy to
copyToId = ""
# GitHub Organization
orgName = ""
##########################################################

gh = github3.login(token=githubToken)
org = gh.organization(orgName)
teams = list(org.teams())
members = list(org.members())
repos = list(org.repositories(type="all"))

cnt = 0
stop = 0
url = ""
permission = ""

for repo in repos:
    cnt = cnt + 1
    if repo.archived == False:
    # if repo.archived == False and repo.name == "itops-ValidationRules":
        # print("Repo ", cnt, ": ", repo.name)
        collaborators = list(repo.collaborators(affiliation='outside'))
        for collaborator in collaborators:
            if collaborator.as_dict()["login"] == copyFromId:
                permission = collaborator.permissions
                print(collaborator.as_dict()["login"], ":", copyFromId, "Found", repo.name)
                permission = collaborator.permissions
                url = "https://api.github.com/repos/{}/{}/collaborators/{}".format(orgName, repo.name, copyToId)
                pycurl_connect = pycurl.Curl()
                pycurl_connect.setopt(pycurl.URL, url)
                pycurl_connect.setopt(pycurl.HTTPHEADER, ['Content-Type: application/json', 'Accept: application/json', 'Authorization: token ' + githubToken])
                pycurl_connect.setopt(pycurl.CUSTOMREQUEST, "PUT")
                if permission["admin"] == True:
                    pycurl_connect.setopt(pycurl.POSTFIELDS,'{"permission":"admin"}') # push: write, pull: read, admin: admin
                elif permission["push"] == True:
                    pycurl_connect.setopt(pycurl.POSTFIELDS,'{"permission":"push"}') # push: write, pull: read, admin: admin
                elif permission["pull"] == True:
                    pycurl_connect.setopt(pycurl.POSTFIELDS,'{"permission":"pull"}') # push: write, pull: read, admin: admin
                pycurl_connect.perform()
                pycurl_connect.close()
                print("Added ", copyToId ," to repo", repo.name)


