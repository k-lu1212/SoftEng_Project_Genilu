#!/usr/bin/python
import requests
import json
import sys
import csv
import sys

print(sys.argv[1])
GITHUB_OWNER_REPO = sys.argv[1]
GITHUB_OWNER_REPO_API = "https://api.github.com/repos/"+GITHUB_OWNER_REPO
access_token = "e6b1dd419d910ec0e8e57af7c5b3594751fadd73"



#Request : https://api.github.com/repos/spring-projects/spring-amqp/commits
#Doc : https://developer.github.com/v3/repos/commits/
def commits():
    allCommits = []
    i = 1
    while True:
        # Params and access token
        payload = "page="+str(i)+"&per_page=100"
        if(access_token != None):
            payload += "&access_token="+access_token

        # Request and load
        r = requests.get(GITHUB_OWNER_REPO_API+"/commits", params=payload)
        commits = json.loads(r.content)
        print "remaining-rate:"+str(r.headers['X-RateLimit-Remaining']) + \
            " reset:"+str(r.headers['X-RateLimit-Reset']) + \
            " page:"+str(i) + \
            " len:"+str(len(commits))

        # Check rate limit
        if(int(r.headers['X-RateLimit-Remaining']) == 0):
            print "No more rate.... generate other access_token..."
            exit()

        # While not end, continue
        if(len(commits)==0):
            break
        else:
            allCommits+=commits
            i+=1
    return allCommits

def create_dic(commits_list):

    with open('commits.csv', 'wb') as csvfile:
		spamwriter = csv.writer(csvfile,delimiter=',', quoting=csv.QUOTE_MINIMAL)
								
		spamwriter.writerow(['idCommit','name', 'date', 'message', 'nfiles', 'changes'])
		all_commits = []
		idCommit = 0
		for c in commits_list :
			idCommit+=1
			comm = {}
			sha = c['sha']
			payload = "&access_token="+access_token
			r = requests.get(GITHUB_OWNER_REPO_API+"/commits/"+sha, params=payload)
			
			commit = json.loads(r.content)
			nb_file = len(commit['files'])
			for f in range(0,nb_file) :
				if commit['commit']['committer']['name'] != 'GitHub':
					data = []
					data.append(idCommit)
					data.append(commit['commit']['committer']['name'].replace('\n', '').encode("utf-8"))
					data.append(commit['commit']['committer']['date'].replace('\n', '').encode("utf-8"))
					data.append(commit['commit']['message'].replace('\n', '').encode("utf-8"))
					data.append(commit['files'][f]['filename'].replace('\n', '').encode("utf-8")) 
					data.append(commit['files'][f]['changes']) 
					spamwriter.writerow(data)
				
            
commits = commits()
print("Writting commits.csv ...")
commit = create_dic(commits)
print("Done")