import random

similes = []
theologians = []
files = [
        'similes-stable-01.txt',
        'theologians-01.txt',
        ]
for file in files:
    file_open = open(file, "r")
    file_line = file_open.readline()
    while file_line:
        if file == 'similes-stable-01.txt':
            if len(file_line) > 1:
                similes.append(file_line[:-1])
        else:
            if len(file_line) > 1:
                theologians.append(file_line[:-1])
        file_line = file_open.readline()
    file_open.close()
print("%s-%s"%(random.choice(similes), random.choice(theologians)))

