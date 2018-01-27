import random, os, json

count = os.getenv("FILE COUNT") or 20
source_file = open('/usr/share/dict/words')
words = [word.strip() for word in source_file.readlines()]
source_file.close()

for identifier in range (1, count + 1):
    amount = random.uniform(1.0, 1000.0)
    content = {
        'topic': random.choice(words),
        'value': "%.2f" % amount
    }
    if identifier < 10:
        label = "0%s" %identifier
    else:
        label = identifier
    with open('./new/receipt-%s.json' %label, 'w') as f:
        json.dump(content,f)
        