import re
def getCommit(commit):
    return re.sub('[^A-Za-z]','',commit)

commit='0??+0+!!someCommIdhsSt'

print(getCommit(commit))
