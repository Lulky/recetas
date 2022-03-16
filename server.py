from flask_app import app

#importar mis controladores
from flask_app.controllers import recipes_controller, users_controller

if __name__=="__main__":
    app.run(debug=True)