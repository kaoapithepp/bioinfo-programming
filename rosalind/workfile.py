file_txt = open("workfile.txt", "r")

tmp = file_txt.readlines()

def readEvenLine(lines):
    for line in range(0, len(lines)):
        if line%2 != 0:
            print(lines[line])
        else:
            pass

readEvenLine(tmp)

file_txt.close()