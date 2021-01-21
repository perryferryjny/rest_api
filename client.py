import requests

if __name__ == "__main__":
    
    URL = "http://127.0.0.1:5000/"
    HEADERS = {"Content-Type": "application/xml"}
    
    req = requests.post(URL, headers=None)
    print(req.text)