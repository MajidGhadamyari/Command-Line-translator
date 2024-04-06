import pickle
from translator import TranslationHistory
import typing
# import json


class User:
    users_list = []

    def __init__(self, name):
        self.name = name
        self.histories = []

    def edit_user(self, new_name):
        self.name = new_name

    @classmethod
    def find_user_by_name(cls, name) -> typing.Self:
        for user in User.users_list:
            if user.name == name:
                return user
        raise  # TODO

    @classmethod
    def add_user(cls, user):
        if isinstance(user, cls):
            user.users_list.append(user)

    @classmethod
    def delete_user(cls, user):
        User.users_list.remove(user)

    def add_new_history(self, history):
        if isinstance(history, TranslationHistory):
            self.histories.append(history)

    @classmethod
    def load_users_list(cls):
        with open("users_list.pickle", "rb") as db_file:
            User.users_list = pickle.load(db_file)

    @classmethod
    def save_users_list(cls):
        with open("users_list.pickle", "wb") as db_file:
            pickle.dump(cls.users_list, db_file)

    def post_data(self):
        pass

    def convert_user_to_json(self):
        data = self.__dict__
        print(data)

    # def get

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)


if __name__ == "__main__":
    # user1 = User("Arya")
    # User.add_user(user1)
    # user1 = User("Jack")
    # User.add_user(user1)
    # print(User.users_list)
    # user = User.find_user_by_name("Arya")
    # user.edit_user("Josh")
    # print("New list : ",User.users_list)
    # # print(User.users_list)
    # User.save_users_list()
    User.load_users_list()
    print(User.users_list)
    # user = User.users_list[0]
    # print(user.convert_user_to_json())
