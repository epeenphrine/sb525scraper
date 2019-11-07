import pandas as pd
import smtplib
import config


EMAIL = config.EMAIL
PASSWORD = config.PASSWORD
RECEIPENT = config.RECEIPENT

class mail:
    def __init__(self, email, password, receipent):
        self.email = email
        self.password = password
        self.receipent = receipent

csv_file = "clinical trials.csv"
csv_file2 = "clinical trials2.csv"

data = pd.read_csv(csv_file)
data2 = pd.read_csv(csv_file2)
print(data.head)
print("****************************")
print(data2.head)

status = data["Status"].tolist()
hospitals = data["hospitals"].tolist()
status2 = data2["Status"].tolist()

def comparison(a, b):
    for i in range (0, len(status)):
        if a[i] != b[i]:
            print(hospitals[i], end = "has / is ")
            print(b[i])
            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()

                smtp.login(EMAIL, PASSWORD)

                subject = "Clinical Alert"
                body = hospitals[i] + " has/is " + b[i]
                msg = f'Subject: {subject}\n\n{body}'

                smtp.sendmail(EMAIL, RECEIPENT, msg)

comparison(status, status2)


