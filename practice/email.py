# # Sending emails without attachments using Python.
# # importing the required library.
# import smtplib
#
# # creates SMTP session
# email = smtplib.SMTP('email-smtp.us-west-2.amazonaws.com', 587)
#
# # TLS for security
# email.starttls()
#
# # authentication
# # compiler gives an error for wrong credential.
# email.login("AKIA5HG6FCJZTNZ7SUUN","BNkX4/viP6NOXG/7LKH2qvfJlZRFS2Xvtr2bfRIXLnoZ")
#
# # message to be sent
# message = "message_to_be_send"
#
# # sending the mail
# email.sendmail("premaseem.webmaster@gmail.com", "premaseem.webmaster@gmail.com", message)
#
# # terminating the session
# email.quit()