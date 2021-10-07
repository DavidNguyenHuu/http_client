import argparse
import help

def run(command):
    if command == 'get':
        print("get method")
        exit()
    else:
        print("post method")
        exit()



parser = argparse.ArgumentParser(add_help=False)
parser.add_argument("command")
parser.add_argument("-get",action="store_true")
parser.add_argument("-post",action="store_true")
args = parser.parse_args()
command=args.command


if args.get:
    help.get_help()
    exit()

elif args.post:
     help.post_help()
     exit()

elif command == 'help':
    help.general()
    exit()

run(command)

