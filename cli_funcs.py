from translation_history import TranslationHistory
from translator import Translator
from user import User


def translate(args):
    tr_history = TranslationHistory(src_text=args.src_text, translator=args.translator, trg_lang=args.trg_lang,
                                    src_lang=args.src_lang)
    Translator.translate_text(tr_history)
    print(tr_history.trg_text)
    user = User.find_user_by_name(args.name)
    user.histories.append(tr_history)


def add_user(args):
    User.add_user(User(args.name))


def delete_user(args):
    user = User.find_user_by_name(args.name)
    User.delete_user(user)


def edit_user(args):
    user = User.find_user_by_name(args.old_name)
    user.edit_user(args.new_name)


def display_history(args):
    user = User.find_user_by_name(args.name)
    for i, history in enumerate(user.histories, 1):
        print(f"\033[94m{'-' * 40}( {i} ){'-' * 40}\033[0m")
        print(history)


