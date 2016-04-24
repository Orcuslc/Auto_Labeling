# Dump to json
import json
import codecs

path = 'user.json'
data = {
	"user_name":"test"
}
with codecs.open(path, 'w', 'utf-8') as f:
	json.dump(data, f)