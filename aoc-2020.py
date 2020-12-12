import os

for i in range(1, 13):
    if i > 1:
        print()
    directory = str(i).zfill(2)
    print('___ Day', directory, "___")
    os.chdir(directory)
    filename = os.getcwd() + '/aoc-2020-' + directory + '.py'
    exec(open(filename).read())
    os.chdir('..')