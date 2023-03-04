import urllib.request as urllib

def url_checker(url):
    
    print("cheking connectivity")

    response = urllib.urlopen(url)
    print(f"Connected to {url} succesfully")
    print(f"The response code was: {response.getcode()}")



print("This url site checker program")
url_input = input("Enter your url to check the connectivity: ")

url_checker(url_input)
