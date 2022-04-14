import os
import json
import sys

stream = ""

if len(sys.argv) > 1:
    stream = os.popen('gh api orgs/FishtechCSOC/repos --paginate --jq \'.[] | select(.full_name | contains("' + sys.argv[1] + '")) | {full_name,description,html_url}\'')
else:
    stream = os.popen('gh api orgs/FishtechCSOC/repos --paginate --jq \'.[] | {full_name,description,html_url}\'')

rawJson = stream.read()

rawJson = '[' + rawJson.replace('}\n', '},')
rawJson = rawJson.rstrip(rawJson[-1]) + ']'

print(rawJson)

# repos = json.loads(rawJson)

# for repo in repos:
#    print(repo["name"])
