import csv
import smtplib
from email.mime.text import MIMEText

YOUR_EMAIL = "wenhaolu2027@gmail.com"
YOUR_PASSWORD = "skpd bjfj bxpa wgfm" # make an app password for gmail (turn on 2 step verification first), should be 16 letter
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

with open("message.txt", "r") as file: # change message.txt up a lil bit
    base_message = file.read()

with open("updated.csv", newline='') as csvfile: # use colleges.csv, i used updated bc my gmail crashed in the middle
    reader = csv.DictReader(csvfile)
    for row in reader:
        college = row["College"]
        email = row["Email"]
        personalized_message = base_message.replace("[School Name]", college)

        msg = MIMEText(personalized_message)
        msg["Subject"] = f"Prospective Student Inquiry"
        msg["From"] = YOUR_EMAIL
        msg["To"] = email

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(YOUR_EMAIL, YOUR_PASSWORD)
            server.sendmail(YOUR_EMAIL, email, msg.as_string())

print("sent emailiggas")
