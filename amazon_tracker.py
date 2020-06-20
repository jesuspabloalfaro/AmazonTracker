import requests
from bs4 import BeautifulSoup
import time
import config
import smtplib

links = []

headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
start_time = time.time()
def remove(string):
    return " ".join(string.split())

class initial:
    def userChoice(self):
        while True:
            userInput = int(input("0) Break \n1) Add \n2) Remove \nChoice: "))
            if(userInput == 0):
                break
            elif(userInput == 1):
                link = input("Insert Link To Item: ")
                links.append(link)
            elif(userInput == 2):
                f = open("links.txt", "r+")
                for x in f:
                    print(x.rstrip('\n'))
                choice = str(input("Input Link To Be Removed: "))
                with open("links.txt", "r") as f:
                    lines = f.readlines()
                with open("links.txt", "w") as f:
                    for line in lines:
                        if line.strip("\n") != choice:
                            f.write(line)
    
    def getLinks(self):
        for link in links:
            f = open("links.txt", "a")
            r = requests.get(link, headers=headers)
            soup = BeautifulSoup(r.text, "html5lib")

            title = soup.find("span", id="productTitle")

            f.write(link + " " + remove(str(title.text)) + '\n')
            f.close()
    
    def send_email(self, subject, msg):
        try:
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login(config.EMAIL_ADDRESS, config.PASSWORD)
            message = 'Subject: {}\n\n{}'.format(subject, msg)
            server.sendmail(config.EMAIL_ADDRESS, config.EMAIL_ADDRESS, message)
            server.quit()
            print("Success: Email sent!")
        except:
            print("Message Failed.")

    def looper(self):
        while True:
            f = open("links.txt", "r")
            for x in f:
                r = requests.get(x, headers=headers)
                soup = BeautifulSoup(r.text, "html5lib")

                price = soup.find("span", id="priceblock_ourprice")
                title = soup.find("span", id="productTitle")
                priceNew = str(price.text)

                subject = "THERE WAS A PRICE CHANGE"
                msg = remove(str(title.text)) + " IS NOW: " + priceNew

                if(priceNew < str(price.text)):
                    test.send_email(subject, msg)

                print(remove(str(title.text + " " + price.text)))
            f.close()
            time.sleep(05.0 - ((time.time() - start_time) % 05.0))

test = initial()
test.userChoice()
test.getLinks()
test.looper()