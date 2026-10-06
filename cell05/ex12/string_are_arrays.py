import sys

if len(sys.argv)!=2:
    print("None")
else:
    text = sys.argv[1]

    count = text.count("z")

    if count == 0:
        print(none)
    else:
        print(count*"z")