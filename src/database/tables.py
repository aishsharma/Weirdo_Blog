__author__ = "Aishwarya Sharma"


# This class represents the "posts" table in the blog database.
class Post:
    def __init__(self, post_id=None, title=None, content=None, create_date=None, edit_date=None):
        self.post_id = post_id
        self.title = title
        self.content = content
        self.create_date = create_date
        self.edit_date = edit_date

    def __str__(self):
        result = ("Post ID: " + str(self.post_id) +
                  "\nTitle: " + str(self.title) +
                  "\nContent:\n" + str(self.content) +
                  "\nCreated On: " + str(self.create_date) +
                  "\nEdited On: " + str(self.edit_date)
                  )
        return result

    def dictionary_mapper(self, dictionary):
        self.post_id = dictionary["post_id"]
        self.title = dictionary["title"]
        self.content = dictionary["title"]
        self.create_date = dictionary["create_date"]
        self.edit_date = dictionary["edit_date"]
        return self

    def to_dict(self):
        result = {
            "post_id": self.post_id,
            "title": self.title,
            "content": self.content,
            "create_date": self.create_date.__str__(),
            "edit_data": self.edit_date.__str__()
        }
        return result
