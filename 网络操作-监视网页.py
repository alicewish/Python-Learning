# Import requests (to download the page)
import requests

# Import BeautifulSoup (to parse what we download)
from bs4 import BeautifulSoup

# Import Time (to add a delay between the times the scape runs)
import time

# Import smtplib (to allow us to email)
import smtplib

start_time = time.time()  # 初始时间戳

# This is a pretty simple script. The script downloads the homepage of VentureBeat, and if it finds some text, emails me.
# If it does not find some text, it waits 60 seconds and downloads the homepage again.

# while this is true (it is true by default),
while True:
    # set the url as VentureBeat,
    url = "http://Google.com/"
    # set the headers like we are a browser,
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    # download the homepage
    response = requests.get(url, headers=headers)
    # parse the downloaded homepage and grab all text, then,
    soup = BeautifulSoup(response.text, "lxml")

    # if the number of times the word "Google" occurs on the page is less than 1,
    if str(soup).find("Google") == -1:
        # wait 60 seconds,
        time.sleep(60)
        # continue with the script,
        continue

    # but if the word "Google" occurs any other number of times,
    else:
        # create an email message with just a subject line,
        msg = 'Subject: This is Chris\'s script talking, CHECK GOOGLE!'
        # set the 'from' address,
        fromaddr = 'YOUR_EMAIL_ADDRESS'
        # set the 'to' addresses,
        toaddrs  = ['AN_EMAIL_ADDRESS','A_SECOND_EMAIL_ADDRESS', 'A_THIRD_EMAIL_ADDRESS']

        # setup the email server,
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        # add my account login name and password,
        server.login("YOUR_EMAIL_ADDRESS", "YOUR_PASSWORD")

        # Print the email's contents
        print('From: ' + fromaddr)
        print('To: ' + str(toaddrs))
        print('Message: ' + msg)

        # send the email
        server.sendmail(fromaddr, toaddrs, msg)
        # disconnect from the server
        server.quit()

        break

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 秒(两位小数)
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分+秒(取整)
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
