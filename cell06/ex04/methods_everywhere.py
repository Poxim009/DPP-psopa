
import sys

def shrink(s):
    print(s[:8])

def enlarge(s):

    print(s + 'Z' * (8 - len(s)))

if len(sys.argv) < 2:
    print("none")
else:
    for param in sys.argv[1:]:
     
        if len(param) > 8:
            shrink(param)
      
        elif len(param) < 8:
            enlarge(param)
        
        else:
            print(param)

            # python methods_everywhere.py "lol" "physically" "backpack"