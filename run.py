from app import start_app
from app.database import db

app = start_app()

if __name__ == "__main__" :
    app.run(debug=True)
