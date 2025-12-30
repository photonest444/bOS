# tag: fourteam-bos-utilits-update-ubuild
import os
import requests
import zipfile
import argparse
from threading import Thread
import time
os.system('cls' if os.name == 'nt' else 'clear')

parser = argparse.ArgumentParser(description="ubuild for bOS")
parser.add_argument("--code", default="", help="ubuild code")
args = parser.parse_args()

if args.code == "fourteam-bos-utilits-update-ubuild-code": # i know this isn't secure but it for miss clicks
    cwd = os.getcwd()

    print("Downloading...")

    def clone_repo(url,branch):
        repo_name = url.split('/')[-1]
        zip_url = f'{url}/archive/refs/heads/{branch}.zip'
        zip_filename = f'{repo_name}.zip'
        response = requests.get(zip_url, stream=True)
        response.raise_for_status()
        with open("installation.zip", 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        with zipfile.ZipFile("installation.zip", 'r') as zip_ref:
            zip_ref.extractall('.')

    clone_repo("https://github.com/photonest444/bOS", "main")

    #response = requests.get("http://fourteam4t.temp.swtest.ru/ubuildfile")
    response = requests.get("http://bosstageserver.com.swtest.ru/ubuildfile")
    files = response.text.split(",")

    print("Downloaded successful")
    print("Installing...")

    y = 0
    for i in files:
        print(f"Installing {files[y]}...")
        f = open(cwd+"/bOS-main/"+files[y],"r",encoding="utf-8")
        text = f.read()
        f = open(cwd+"/"+files[y],"a")
        f.close()
        f = open(cwd+"/"+files[y], "w",encoding="utf-8")
        f.write(text)
        f.close()
        print(f"Installed {files[y]}")
        y = y+1

    print("Installation successful")
    print("Finishing...")
    os.remove("installation.zip")
    open("back","w",encoding="utf-8").write("")

    print("New build succesfully installed!")

    def f1():
        exit()
    def f2():
        os.system(f'python {cwd}/bOS.py --print "Updated with ubuild"')

    time.sleep(2)

    Thread(target=f1).start()
    Thread(target=f2).start()

else:
    pass