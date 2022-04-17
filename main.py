import time,sys,os
from time import sleep
from datetime import datetime

try:
    import requests
except ImportError:
    print("! type: pip install requests")
try:
    import bs4
    from bs4 import BeautifulSoup as rafi
except ImportError:
    print("! type: pip install bs4")

waktu = datetime.now()
tahun = waktu.year
bulan = waktu.month
hari = waktu.day

url = "https://www.google.com/search?&q="

banner = """
Google
____ ____ ____ ____ ____ _  _ 
[__  |___ |__| |__/ |    |__| 
___] |___ |  | |  \ |___ |  | v: 0.1
Time: %s - %s - %s
                             
"""%(tahun,bulan,hari)

def ketik(_rafi_):
    for i in _rafi_+"\n":
        sys.stdout.write(i)
        sys.stdout.flush()
        sleep(00.1)

def main():
    print(banner)
    search = input("[•] Search: ")
    ketik("[•] Please Wait...")
    try:
        req = requests.get(url+search)
        soup = rafi(req.text, "html.parser")
        hasil = soup.find("div", class_="BNeawe").text
        print("[•] Result:",hasil)
    except (KeyError,IOError):
        print("[•] No Result.")
    
if __name__ == "__main__":
    os.system("git pull")
    main()
