#this module is testing async_client module
#using async_client version with debug prints

import async_client_wdebug_prints
client = async_client_wdebug_prints.AsyncWebPageClient(200)

#test data

urls100 = [line.strip() for line in open("100urls.txt", 'r')]
urls2000 = [line.strip() for line in open("2000urls.txt", 'r')]
urls10000 = [line.strip() for line in open("10000urls.txt", 'r')]

#using 10, 50, 100 slices for example
data_samples = [urls100[:10], urls2000[:50], urls10000[:100]]

for sample in data_samples:
    result = client.get_pages(sample)
    if len(result) != len(sample):
        print 'Test failed with sample of ' + str(len(sample))
    else:
        print 'Test OK with sample of ' + str(len(sample))
        print result[:1]
    
