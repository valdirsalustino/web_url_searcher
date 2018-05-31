# class to retrieve the urls from the requests.text elements 
# find in it a nice approach
# from: https://stackoverflow.com/questions/6883049/regex-to-find-urls-in-string-in-python
from html.parser import HTMLParser
import requests

class MyParser(HTMLParser):
    """
    Class served as the passer from which I can 
    retrieve the list of URLs inside the
    we content.

    Usage: 
    p = MyParser()
    p.feed(f.text)
    list_of_urls = p.output_list
    """
    def __init__(self, output_list=None):
        HTMLParser.__init__(self)
        if output_list is None:
            self.output_list = []
        else:
            self.output_list = output_list
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            self.output_list.append(dict(attrs).get('href'))
            
            
# function to get all urls within an url content:
def getUrls(url):    
    """
    This function retrieve the internal urls inside given initial url.
    Usage: 
    list_of_urls = getUrls('https://www.google.com')

    The function return a list of strings containing the internal urls.
    """
    f = requests.get(url)
    p = MyParser()
    p.feed(f.text)
    list_of_urls = p.output_list
    #deal with possible strange None values
    list_of_urls = [url for url in list_of_urls if url is not None]
    for url in list_of_urls:
            if 'http' not in url: list_of_urls.remove(url)
    return list_of_urls
            
    
# verify the we can reach the url:
def remove_unreachable_urls(list_of_urls):
    """
    This function try to connect to every urls within the list_of_urls given.
    The function in try to connect to the link: in case os success it keeps the url;
    in case of failure it shall remove the urls from the list.

    Usage: 
    reachable_urls = remove_unreachable_urls(list_of_urls)

    The function returns a list of strings containing the urls where the connection could be stablished. 
    Note: Depending on your connection and the size of the list_of_urls given the function may take several time. Please, be patient. 
    """
    list_of_reachable_url = []
    for url in list_of_urls:
        try:
            f = requests.get(url)
            print('\t',url, 'status_code:', f.status_code)
            list_of_reachable_url.append(url)
        except:
            print('\t',url, 'not reachable -- > removed')

    return list_of_reachable_url


def send_document_to_cloudant(parent_url, list_of_urls, database, list_of_json_ids):
    """
    This function try to send the list_of_urls to the Cloudant database.
    In case of sucess the function return one object of the class 'cloudant.document.Document':
    In case of a connection failure or lack of privilege to write the object into Cloudant, the function return
    an Exception error. 

    The list_of_urls is stored as a JSON object with two members:
      -- parent_url: which are the owner of the list_of_urls given.
      -- list_of_urls: the proper url list.

    Usage: 
    reachable_urls = remove_unreachable_urls(list_of_urls)

    The function returns a list of strings containing the urls where the connection could be stablished. 
    Note: Depending on your connection and the size of the list_of_urls given the function may take several time. Please, be patient. 

    """

    # first, one need to convert to JSON format:     
    jsonList = {
        "parent_url" : parent_url,
        "list_of_urls" : list_of_urls
    }
    
    try:
        newDocument = database.create_document(jsonList)
        if newDocument.exists():
            print ("Document created sucessfully with _id: '{}' ".format(newDocument['_id']))
            list_of_json_ids.append(newDocument['_id'])
            return newDocument
    except Exception as e:
        print("\nDocument could not be created:", e)  
        return e
