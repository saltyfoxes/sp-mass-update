from tokens import SYSTEM_ID
from helpers import get_response

#grab members
members = get_response("GET", f"https://api.apparyllis.com/v1/members/{SYSTEM_ID}")
data = members.json()

#filtering members by empty custom fields
filtered = [] 
for entry in data:
    try:
        if entry['content']['info'][':group id']!="":
            filtered.append(entry['id'])
    except: 
        pass

#grab group and update with members
groups = get_response("GET", f"https://api.apparyllis.com/v1/groups/{SYSTEM_ID}")

for entry in groups.json():
    if entry['content']['name']==":group name":
        del entry['content']['uid']
        del entry['content']['buckets']
        del entry['content']['lastOperationTime']

        entry['content']['members'] = filtered
        group_id = entry['id']
        get_response("PATCH", f"https://api.apparyllis.com/v1/group/{group_id}", entry['content'])
