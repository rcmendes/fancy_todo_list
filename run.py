import os
from fancy_todo_list.configuration import app

env = os.environ.get("APP_ENV", "dev")
port = os.environ.get("APP_PORT", 5000)

debug = True if env == "dev" else False


app.run("0.0.0.0", port=port, debug=debug)
