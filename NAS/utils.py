class helper:
    def __init__(self):
        self.name = "helper"
        self.version = "1.0"
        self.description = "Help to perform tasks by getting calls from API."

    def make_dir(self, path,name):
        """
        Create a directory if it does not exist.
        """
        import os
        if(path[-1] != "/"):
            path += "/"
        # Append the name to the path
        path+= name
        # Check if the directory already exists
        if not os.path.exists(path):
            # If it doesn't exist, create it
            os.makedirs(path)
            print(f"Directory {path} created.")
        else:
            # If it does exist, print a message
            print(f"Directory {path} already exists.")