from database import dal

__author__ = "Aishwarya Sharma"


# Returns a single post or a list of posts if post_id is nothing
def get_posts(post_id=None):
    posts = dal.get_posts(post_id)
    return posts


# Returns True if post is successfully added to database. Otherwise return False
def add_post(title, content):
    return dal.add_post(title, content)


# Returns True if edited post is successfully added to database. Otherwise return False
def edit_post(post_id, title, content):
    return dal.edit_post(post_id, title, content)
