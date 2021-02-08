from flask import Flask, render_template, url_for, request
import json
import smtplib
import logging
import os

app = Flask(__name__)


@app.route('/', methods=['GET'])
def homepage():
    return render_template('index.html')

@app.route('/send_mail',methods=['POST'] )
def send_mail():
    data = json.loads(request.data)
    # send email
    triggerMail(data)
    return {message: 'Success'}


def triggerMail(data):
    name = data['name']
    email = data['email']
    query = data['message']
    
    sender = 'mohsinsajan394@gmail.com'
    receivers = ['mohsinsajan394@gmail.com']

    
    logging.info(f"User Name:{name},Email:{email},Message:{query}")
    sender_email =  os.environ.get('EMAIL')
    sender_password = os.environ.get('PASSWORD')

    try:
        smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
        smtpObj.starttls()
        smtpObj.login("sender_email_id", "sender_email_id_password")
        message = f"User Name:{name},\nEmail: {email}, \nMessage: {query}" 
        smtpObj.sendmail(sender, receivers, message)      
        print ("Successfully sent email")
        smtpObj.quit()
    except:
        print ("Error: unable to send email")




if __name__ == '__main__':
    app.run(debug=True)