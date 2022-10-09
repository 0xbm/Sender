Sender is application for send @mail and/or text messages(SMS).

To open application please exec only main.py

EMAIL:
You can send text or text with attachment.
To send emails using Gmail, you'll need to set up an app password. This is pretty simple:
First: go to 'myaccount.google.com/security'
Second: turn on 2fa
Third: generate password to your application (it's not your default password) 

SMS:
You must register on site www.twilio.com and register your phone number to get:
* account_sid 
* auth_token 
* service_sid

*Requirements*
pip install -r requirements.txt
