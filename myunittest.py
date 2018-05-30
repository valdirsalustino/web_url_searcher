import unittest
import requests

from urlscraping import getUrls, remove_unreachable_urls, send_document_to_cloudant, MyParser


# models for cloudant queries
from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey






class MyGetURLs(unittest.TestCase):
    def test_getURL(self):
    	url = 'https://www.wikipedia.org'
    	f = requests.get(url)
    	p = MyParser()
    	p.feed(f.text)
    	list_of_urls = p.output_list
    	list_of_urls = [url for url in list_of_urls if url is not None]
    	for url in list_of_urls:
            	if 'http' not in url: list_of_urls.remove(url)

    	self.assertEqual( getUrls('https://www.wikipedia.org'), list_of_urls )

    def test_removal(self):
    	url = 'https://www.google.com'
    	f = requests.get(url)
    	p = MyParser()
    	p.feed(f.text)
    	list_of_urls = p.output_list
    	list_of_urls = [url for url in list_of_urls if url is not None]

    	good_urls = []
    	for url in list_of_urls:
    		if 'http' not in url: continue
    		f = requests.get(url)
    		if f.status_code == 200 :
    			good_urls.append(url)

    	self.assertEqual(remove_unreachable_urls(list_of_urls), good_urls)

    def test_sendtocloudant(self):
    	###########################################################
    	############## my credentials #############################
    	###########################################################
    	serviceUsername = "68019c5d-fdfa-44f5-abee-707e5488207b-bluemix"
    	servicePassword = "364551f0c73f520a889da3a69af1cc597c8c64a8504132bf2be2a0f8fc73951a"
    	serviceURL = "https://68019c5d-fdfa-44f5-abee-707e5488207b-bluemix.cloudant.com"
    	###########################################################

    	parent_url = 'https://www.ibm.com'
    	list_of_urls = ['https://www.google.com', 'https://www.google.com']
    	jsonList = {"parent_url" : parent_url,"list_of_urls" : list_of_urls}
    	databaseName = 'valid_urls'
    	client = Cloudant(serviceUsername, servicePassword, url=serviceURL)
    	client.connect()
    	database = client.create_database(databaseName)
    	newDocument = database.create_document(jsonList)

    	self.assertEqual( database[newDocument['_id']]['list_of_urls'], list_of_urls )


if __name__ == '__main__':
    unittest.main()