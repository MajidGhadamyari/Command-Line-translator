import argparse
import cli_funcs
from user import User

global_parser = argparse.ArgumentParser()
sub_parser = global_parser.add_subparsers()

parser_add_user = sub_parser.add_parser("add_user", help="Add user")
parser_add_user.add_argument("-n", "--name", help="Enter your name")
parser_add_user.set_defaults(func=cli_funcs.add_user)
parser_edit_user = sub_parser.add_parser("edit_user", help="edit user")
parser_edit_user.add_argument("-n", "--new-name", help="New name")
parser_edit_user.add_argument("-o", "--old-name", help="Old name")
parser_edit_user.set_defaults(func=cli_funcs.edit_user)

parser_delete_user = sub_parser.add_parser("delete_user", help="delete user")
parser_delete_user.add_argument("-n", "--name", help="user's name")
parser_delete_user.set_defaults(func=cli_funcs.delete_user)

parser_history_user = sub_parser.add_parser("user_history", help="user history")
parser_history_user.add_argument("-n", "--name", help="user's name")
parser_history_user.set_defaults(func=cli_funcs.display_history)

translate_parser = sub_parser.add_parser("translate", help="translate a text from a language to another language")
translate_parser.add_argument("-u", "--user", help="user's name")
translate_parser.add_argument("--translator", help="Give your bing")
translate_parser.add_argument("--src_text", help="Give your text")
translate_parser.add_argument("--trg_lang", help="Give your target language")
translate_parser.add_argument("--src_lang", default="auto", help="Give your source language")
translate_parser.set_defaults(func=cli_funcs.translate)

args = global_parser.parse_args()
print(args)
User.load_users_list()
print(User.users_list)
args.func(args)
User.save_users_list()
print(User.users_list)
