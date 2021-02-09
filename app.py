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
    response = triggerMail(data)
    if response =='success':
        message = 'Success'
    else:
        message = 'Error'
    return {'message': message} 
    


def triggerMail(data):
    name = data['name']
    email = data['email']
    query = data['message']
    senderEmail = os.getenv('EMAIL')
    senderPassword = os.getenv('PASSWORD')
    sender = senderEmail
    receiver = senderEmail

    msg = MIMEMultipart()

    message_body = name+' left the following message \\n'+query+'\\nYou can reach out to him at '+email
    message_html = '''
                        <html>
                            <body>
                                <p>{name} left you the following message</p>
                                <p style="font-style:italic">" {query} "<p>
                                <p>You can reach out to him at - {email}</p>
                            </body>
                        </html>
                   '''.format(name=name, query=query, email=email)
    msg['From']=sender
    msg['To']=receiver
    msg['Subject']=f'{name} sent you a message.'

    msg.attach(MIMEText(message_html, 'html'))

    try:
        smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login(sender, senderPassword)


        text = msg.as_string()
        smtpObj.sendmail(sender, receiver , text)
        smtpObj.quit()
        return 'success'
    except:
        return 'error'




if __name__ == '__main__':
    app.run(debug=True)