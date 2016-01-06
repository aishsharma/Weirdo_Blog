from bottle import get, post, route, static_file, error
import controller


# Route to serve static files
@route('/')
def index():
    return static_file("index.html", root="Web")


@route('/:filename#.*#')
def static(filename):
    return static_file(filename, root="Web")


@error
def error():
    return static_file("404.html", root="Web")


# Routes for API

# Get all posts
@get('/api/getPosts')
def get_posts():
    data = []
    posts = controller.get_posts()

    # Converting list of Post objects to list of dictionary objects
    for entry in posts:
        data.append(entry.to_dict())
    results = {"data": data}

    return results


# Get a specific post
@get('/api/getPost/<post_id>')
def get_post(post_id):
    data = []
    posts = controller.get_posts(post_id)

    # Converting list of Post objects to list of dictionary objects
    for entry in posts:
        data.append(entry.__dict__)
    results = {"data": data}

    return results


# New Post. Returns True or False depending on success or failure
@post('/api/addPost')
def add_post(title, content):
    results = {"data": controller.add_post(title, content)}
    return results


# Edit Post. Returns True or False depending on success or failure
@post('/api/editPost')
def edit_post(title, content):
    results = {"data": controller.edit_post(title, content)}
    return results
