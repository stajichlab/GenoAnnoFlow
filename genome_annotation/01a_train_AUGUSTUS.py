import sys
import os.path.isfile
from datetime import datetime
import random

#Open file given in arguments and split it randomly into test and training sets
filename = sys.argv[1]
if not os.path.isfile(filename):
    sys.exit("%s doesn't exist in current directory!" % filename)

records = []
with open(filename) as inputFASTA:
    for line in inputFASTA:
        if line.startswith('>'):
            records.append(line)
        else:
            records[-1] += line

random.seed(str(datetime.now()))
test_set = []
for i in range(0,math.ceil(len(records) / 2)):
    test_set.append(records.pop(random.randint(0,len(records) - 1)))
train_set = records

if len(train_set) < 200:
    print('Warning: Training set less than 200 transcripts, good performance will be more difficult to achieve')

test_filename = "%s.test.fa:%s" % (filename, len(test_set))
train_filename = "%s.train.fa:%s" % (filename, len(train_set))

with open(test_filename, 'w') as testOutput:
    for record in test_set:
        testOutput.write(record)

with open(train_filename, 'w') as trainOutput:
    for record in train_set:
        trainOutput.write(record)


