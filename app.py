from flask import Flask
from flask_mail import Mail , Message
from dotenv import load_dotenv, dotenv_values

## INICIALIZAMOS LA APLICACION DE FLASK
app = Flask(__name__)

load_dotenv()
config = dotenv_values(".env")
print(config['MAIL_USERNAME'])
app.config['MAIL_SERVER']=config['MAIL_SERVER']
app.config['MAIL_PORT'] = int(config['MAIL_PORT'])
app.config['MAIL_USERNAME'] = config['MAIL_USERNAME']
app.config['MAIL_PASSWORD'] = config['MAIL_PASSWORD']
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

## INICIALIZAMOS FLASK MAIL
mail = Mail(app)





@app.route('/')
def send_mail():
    ##SE ENVIA UN PIXEL DE TRACKEO PARA REVISAR SI EL CORREO FUE VISUALIZADO
        msg = Message('Hello from the other side!', sender =   'peter@mailtrap.io', recipients = ['snahuelpan@gmail.com'])
        msg.body = "Hey Paul, sending you this email from my Flask app, lmk if it works"
        msg.html = '<img src="http://127.0.0.1:5000/static/pixel_tracker.png" style="width:500px;height:228px;">'
        mail.send(msg)
        return "Message sent!"


if __name__ == '__main__':
    app.run()