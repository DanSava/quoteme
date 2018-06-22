import subprocess
import json

with open('factsdb/facts.json') as f:
    data = json.load(f)

nr = 4
post_no = "postNo=%d" % (nr + 3)
title = "title=%s" % data['facts'][nr]

result = subprocess.run(['node', 'node/postme.js', title, post_no], stdout=subprocess.PIPE)
print(result.stdout)
