if input("Would you like to see read a random Wikipedia Article?(Y/N)")=='Y':
    import selenium
    from bs4 import BeautifulSoup
    url = "en.wikipedia.org/wiki/Special:Random" #random wikipedia page selector link

    raw_data = selenium.__loader__(url)
    html_content = raw_data.content

    soup = BeautifulSoup(html_content, 'html.parser')

    article = soup.find_all('p')
    for word in article:
        print(word.text)

else:
    exit()