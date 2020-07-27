import smtplib

#set up smtp connecton
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("pypy3blogspot@gmail.com", "Madhan@20")

def greet(name):
    return ("hiii" +  " " + "Madhan" + " good morning pypy3.blogspot.com")
def send(email,message):
    s.sendmail("pypy3blogspot@gmail.com", email , message)

for i in range(1,2):
    name = "madhan"
    email = "madhansubramani20022000@gmail.com"
    print(email,greet(name))
    send(email,greet(name))

