 def get_data(position,location):
 
    records = []  # creating the record list
    url = get_url(position, location)  # create the url while passing in the position and location.
    
    while True:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        cards = soup.find_all('div', 'jobsearch-SerpJobCard')  

        for card in cards:
            record = get_record(card)
            records.append(record)

        try:
            url = 'https://www.indeed.com' + soup.find('a', {'aria-label': 'Next'}).get('href')
            delay = randint(1, 10)
            sleep(delay)
        except AttributeError:
  
            break
    return pd.DataFrame(records) 
          