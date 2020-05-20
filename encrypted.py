
from base64 import b64decode
import json

data = open('config.json').read()
config = json.loads(data)
code = config["secret"]
key = config["uname"]
message = list()

for i,c in enumerate(b64decode(code)):
	message.append(chr(c ^ ord(key[i%len(key)])))

print(''.join(message))
