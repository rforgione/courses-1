import os
import random
import shutil

# the pct of the training data to include in our sample
sample_pct = .25
random.seed(2)

for i in os.listdir("data/train"):
	num = random.randint(1,(1/sample_pct))
	if num == 1:
		shutil.copy("data/train/%s" % i, "data_sample/train/%s" % i)

for i in os.listdir("data/valid"):
	num = random.randint(1,(1/sample_pct))
	if num == 1:
		shutil.copy("data/valid/%s" % i, "data_sample/valid/%s" % i)

