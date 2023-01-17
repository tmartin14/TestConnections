# Test API connections for DataSet
import datetime
import requests
import base64

# Variables
timeout=3
use_proxy=False
proxyurl='http://username:password@proxy.zzzz.com:8080'
dataset_url='https://app.scalyr.com/api/query'
dataset_api_key='YOUR-READ-TOKEN-HERE'


def test_connection(url,headers,message):
    print('\n')
    print(message)
    print('       Start Time: ' + str(datetime.datetime.now()))
    if use_proxy:
        response = requests.get(url, headers=headers, proxies=proxies, timeout=timeout)
    else:
        response = requests.get(url, headers=headers, timeout=timeout)
    if headers != "":
         print('            Headers = ' + str(headers))
    print_results(response.status_code)


def print_results(status):
    if status == 200:
        print('            SUCCESS!  Response Status Code: ' + str(status))
    else:
            print('            Connection FAILED.  Response Status Code: ' + str(status))
    print('       End Time: ' + str(datetime.datetime.now()))
    print('\n')


test_connection("http://www.google.com","","Trying Google to see if we can reach the outside world...")

headers = {"Authorization": "Bearer {}".format(dataset_api_key)}
test_connection(dataset_url,headers,"Trying DataSet API @ " + dataset_url)
