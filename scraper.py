class Scraper:

  def getter(self):
    import urllib.request
    user_agent = "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0"
    headers={'User-Agent':user_agent,}
    request=urllib.request.Request(self.url,None,headers)
    response = urllib.request.urlopen(request)
    return response.read()

  def cleanner(self,html):
    from bs4 import BeautifulSoup
    from nltk.tokenize import RegexpTokenizer
    
    
    soup = BeautifulSoup(html,'html.parser')
    text = soup.get_text(strip = True)
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(text)
    return tokens

  def frequency(self, tokens):
    import nltk
    from nltk.corpus import stopwords
    from collections import Counter
    sw = stopwords.words('english')
    clean_tokens = tokens[:]
    for token in tokens:
      if token in sw:
        clean_tokens.remove(token)

    return Counter(clean_tokens).most_common(15)

  def __init__(self, url, user_agent):
    import nltk
    self.url = url
    self.user_agent = user_agent