import smtplib

server = smtplib.SMTP_SSL("smtp.office365.com", 992)
server.login('email', 'senha')
server.sendmail('annezdz@hotmail.com', 'annezdz@hotmail.com', 'Oi Anne')
server.quit()
