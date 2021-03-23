import pycurl
############# Configuration Area #########################
# Put your GitHub token here
githubToken = ""
# GitHub ID that you want to give permission
copyToId = ""
# Repository and Permissions
reposAndPermissions = {
}
###### The below is the sample
####reposAndPermissions = {
####    "RepoName1":"admin",
####    "RepoName2":"push", 
####    "RepoName3":"pull" 
####}
# GitHub Organization
orgName = ""
##########################################################

for repo in reposAndPermissions:
    print(repo, reposAndPermissions[repo])
    url = "https://api.github.com/repos/{}/{}/collaborators/{}".format(orgName,repo, copyToId)
    url
    pycurl_connect = pycurl.Curl()
    pycurl_connect.setopt(pycurl.URL, url)
    header = "['Content-Type: application/json', 'Accept: application/json', 'Authorization: token " + githubToken + "']"
    pycurl_connect.setopt(pycurl.HTTPHEADER, ['Content-Type: application/json', 'Accept: application/json', 'Authorization: token ' + githubToken])
    pycurl_connect.setopt(pycurl.CUSTOMREQUEST, "PUT") 
    pycurl_connect.setopt(pycurl.POSTFIELDS,'{"permission":"'+reposAndPermissions[repo]+'"}') # push: write, pull: read, admin: admin
    pycurl_connect.perform()
    pycurl_connect.close()
    print("Added", copyToId ,"to repo", repo, "with permisson", reposAndPermissions[repo])


