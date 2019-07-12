import time
from datetime import datetime as dt
hosts_temp= r"C:\Users\abruz\Documents\WebSite Blocker\hosts"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "https://mail.google.com/mail/u/0/#inbox", "https://twitter.com/home"]

while True:
    if dt(dt.now().year, dt.now().month, dt. now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt. now().day, 21 ):
        print("Working hours...")
        with open(hosts_path, 'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+ " " +website+"\n")
    else:
        print("Fun hours")
        with open(hosts_path, 'r+') as file:
            content=file.readlines() #Lê cada linha, agora content possui uma lista de linhas
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
    time.sleep(5)
