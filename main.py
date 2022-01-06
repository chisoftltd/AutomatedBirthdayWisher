import random
import smtplib
import datetime as dt
import pandas

#   -------------------------------- CONSTANTS --------------------------------------
now = dt.datetime.now()
weekday = now.weekday()
month = now.month
my_email = 'python.chinwe@gmail.com'
pwd = 'pyt@#chinwe'

#   -------------------------------- READ CSV FILE --------------------------------------
try:
    data = pandas.read_csv("family/birthdays.csv")
except FileNotFoundError:
    print("File not found!")
else:
    names = data.to_dict(orient="records")

#   -------------------------------- Automated Birthday Wisher ----------------------------------
for name in names:
    if name["month"] == month and name["day"] == weekday:
        index = random.randint(1, 3)
        with open("letter_templates/letter_" + str(index) + ".txt") as fletter:
            letter = fletter.read()
            bd_name = name["name"].title()
            birthday_letter = letter.replace('[NAME]', f"{bd_name}")
            with smtplib.SMTP("smtp.gmail.com", 587, timeout=30) as connection:
                connection.starttls()
                connection.login(my_email, pwd)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=name["email"],
                    msg=f"Subject:Happy Birthday - {bd_name.title()}"
                        f"\n\n{birthday_letter}"
                )
