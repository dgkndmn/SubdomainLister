import requests

with open("subdomainlist.txt", "w") as dosya:
    pass


request_adress = input("Type the adress like http://xxx): ")

size_of_array = int(input("Enter the count of the words you will add to the list: "))

def add_to_list():
    keywords_list = []
    x = 0
    while x < size_of_array:
        word = input("Enter the keyword:")
        keywords_list.append(word)
        x = x+1

    for word in keywords_list:
        with open("subdomainlist.txt","a") as subdomain_list:
            subdomain_list.write(f"{word}\n")

add_to_list()

with open("subdomainlist.txt","r") as subdomain_list:
    for word in subdomain_list:
        word = word.strip().rstrip()
        url = "http://" + word + "." + request_adress
        try:
            response = requests.get(url)
            print(f"{url} --> OK")
        except:
            print(f"{url} --> ERROR")

