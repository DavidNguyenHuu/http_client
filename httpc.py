import argparse
import help as h
import http_lib


parser = argparse.ArgumentParser(add_help=False)
subparsers = parser.add_subparsers(dest="command")

#HELP OPTIONS
help = subparsers.add_parser('help')
help.add_argument("help_option",nargs='?')
#GET OPTIONS
get_r = subparsers.add_parser('get', add_help=False)
get_r.add_argument('url')
get_r.add_argument('-v', '--verbose', action="store_true")
get_r.add_argument('-h', '--header')
get_r.add_argument('-o', '--overwrite_file')
#POST OPTIONS
post_r = subparsers.add_parser('post', add_help=False)
post_r.add_argument('url')
post_r.add_argument('-v', '--verbose', action="store_true")
post_r.add_argument('-h', '--header')
post_r.add_argument('-d', '--data')
post_r.add_argument('-f', '--file')
post_r.add_argument('-o', '--overwrite_file')


def run():
    args = parser.parse_args()

    if args.command == "help":
        if args.help_option == 'get':
            h.get_help()
        elif args.help_option == 'post':
            h.post_help()
        else:
            h.general()

    if args.command == "get":
        http_lib.get_request(args.url,args.verbose,args.header,args.overwrite_file)

    elif args.command == "post":
        http_lib.post_request(args.url,args.verbose,args.header,args.data,args.file,args.overwrite_file)

    #For testing
    #print(args)

run()

