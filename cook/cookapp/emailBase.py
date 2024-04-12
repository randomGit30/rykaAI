from django.core.mail import send_mail

def send_ai_response_email(user_email, ai_response):
    subject = 'Your AI-Generated Mental Wellbeing recipes'
    from_email = 'shikshakcook@gmail.com' 
    recipient_list = [user_email]
    
    message = ai_response
    
    # Send the email
    send_mail(subject, message, from_email, recipient_list)

# def send_custom_email():
#     subject = "Your Custom Email Subject"
#     message = "This is a fallback message for email clients that don't support HTML."
#     html_message = """
#     <html>
#         <body>
#             <h1>This is a Heading</h1>
#             <p>This is a paragraph in the email body.</p>
#         </body>
#     </html>
#     """
#     sender = "shikshakcook@gmail.com"
#     recipient = ["arreyanhamid@icloud.com"]

#     send_mail(
#         subject,
#         message,
#         sender,
#         recipient,
#         html_message=html_message
#     )