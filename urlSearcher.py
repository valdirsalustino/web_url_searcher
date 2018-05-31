#make queries on the urls to retrieve its contents
import requests


# models for cloudant queries
from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey

from urlscraping import getUrls, remove_unreachable_urls, send_document_to_cloudant

###########################################################
############## my credentials #############################
###########################################################
serviceUsername = "68019c5d-fdfa-44f5-abee-707e5488207b-bluemix"
servicePassword = "364551f0c73f520a889da3a69af1cc597c8c64a8504132bf2be2a0f8fc73951a"
serviceURL = "https://68019c5d-fdfa-44f5-abee-707e5488207b-bluemix.cloudant.com"
###########################################################

#initial_url = input('Please, past an url: ')

initial_url = "www.google.com"
#print("\n\t ---- initial url: ", initial_url) 

print ("=======================================================================")
print ("==               Thank you for use the URL searcher                  ==")
print ("==             Author: Valdir Salustino Guimaraes.                   ==")
print ("==             You are welcome to make suggestions:                  ==")
print ("==    github: https://github.com/valdirsalustino/web_url_searcher    ==")
print ("==   I will scrape the urls inside:", initial_url)
print ("=======================================================================")

if 'http' not in initial_url: 
    print("No 'http:' I will assume the url as ", 'https://'+initial_url)

initial_url = 'https://'+initial_url 

#get list of url within given url
list_of_urls = getUrls(initial_url)

print ("There were found", len(list_of_urls), " internal urls within the initial url")
print ("\n Removing unreachable urls:")
#remove unreachable urls
list_of_reachable_url = remove_unreachable_urls(list_of_urls)

print ("\n\t--> Out of the ", len(list_of_urls), " initial urls, ", len(list_of_reachable_url), " is reachable.")
#print (list_of_reachable_url)

 
#store the urls to Cloudant No SQL
#================================== 
#create the client:
client = Cloudant(serviceUsername, servicePassword, url=serviceURL)
try:
    client.connect()
except Exception as e:
    print ("Fail to connect with the Cloudant:", e)

#data base name
databaseName = 'valid_urls'

#create the database
try:
    myDatabase = client.create_database(databaseName)
    print("\nDatabase '{}' created successfully".format(databaseName))
except Exception as e:
    print("\nDatabase", databaseName, "could not be created:", e)    


# write urls Cloudant
print ('\nWrite url list to Cloundant NoSQL database:')
print ('_'*50)

list_of_json_ids = []            
newDocument = send_document_to_cloudant(initial_url, list_of_reachable_url, myDatabase, list_of_json_ids)

# Query the list of stored urls: 
print ('\nTry to query the stored URLs from Cloudant database:')
print ('_'*50)
print ('\tTry to retrieve the object _id',newDocument['_id'])

try:
    list_of_retrieved_urls = myDatabase[newDocument['_id']]
    print('\t--Sucessfully retrieve the list of urls as json object.')
except Exception as e:
    print('Could not get the data:',e)

print(list_of_retrieved_urls['list_of_urls'])

print ('\nIterave over the list of retrieved urls:')


for url in list_of_retrieved_urls['list_of_urls']:
    print (url)
    print ('_'*30)
    list_of_urls = getUrls(url)
    #remove_unreachable_urls(list_of_urls)
    print(url,'.'*20,len(list_of_urls), 'url inside')
    print ('Writing the urls to Cloudant database: ')
    send_document_to_cloudant(parent_url=url, list_of_urls=list_of_urls, database=myDatabase,list_of_json_ids=list_of_json_ids )
    


print ('All ok.')
print ('_'*50)

print ('\n In summary the list below shows the _id of the JSON documents at Cloudant')
print (list_of_json_ids)
