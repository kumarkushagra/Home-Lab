from .env import cloudStorage
from subServices import helper

if __name__ == "__main__":
    # Create an instance of the helper class
    my_helper = helper()
    user = "Kushagra"

    # Use the make_dir method to create a directory
    my_helper.make_dir(cloudStorage, user)