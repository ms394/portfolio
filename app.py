from flask import Flask, render_template, url_for, request
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging
import os


app = Flask(__name__)

print(os.getenv('PASSWORD'))

@app.route('/', methods=['GET'])
def homepage():
    return render_template('index.html')

@app.route('/send_mail',methods=['POST'] )
def send_mail():
    data = json.loads(request.data)
    # send email
    triggerMail(data)
    return {'message': 'Success'}


def triggerMail(data):
    name = data['name']
    email = data['email']
    query = data['message']
    print(os.getenv('PASSWORD'))
    sender = os.getenv('EMAIL')
    receiver = os.getenv('EMAIL')

    msg = MIMEMultipart()

    message_body = f'User - {name}, User Email - {email}, Message - {query}'

    msg['From']=sender
    msg['To']=receiver
    msg['Subject']='This is TEST'

    msg.attach(MIMEText(message_body, 'plain'))


    smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(sender, os.getenv('PASSWORD'))


    text = msg.as_string()
    smtpObj.sendmail(sender, receiver , text)
    smtpObj.quit()




if __name__ == '__main__':
    app.run(debug=True)