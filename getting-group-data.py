from tokens import SYSTEM_ID
from helpers import get_response, write_to_file

groups = get_response("GET", f"https://api.apparyllis.com/v1/groups/{SYSTEM_ID}")

write_to_file("allgroups.json", groups.content)