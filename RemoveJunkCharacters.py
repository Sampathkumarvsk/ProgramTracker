import re
str = "afbvnici@$%&&((()446"
clean_string = re.sub(r'[^0-9]','',str)
print(clean_string)
