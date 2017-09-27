from routes.front import front
from routes.back import back
from app import app
app.register_blueprint(front)
app.register_blueprint(back)