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
    return controller.get_posts()


# Get a specific post
@get('/api/getPost/<post_id>')
def get_post(post_id):
    return controller.get_posts(post_id)


# New Post. Returns True or False depending on success or failure
@post('/api/addPost/<title>/<content>')
def add_post(title, content):
    return controller.add_post(title, content)


# Edit Post. Returns True or False depending on success or failure
@post('/api/editPost/<post_id>/<title>/<content>')
def edit_post(title, content):
    return controller.edit_post(title, content)
