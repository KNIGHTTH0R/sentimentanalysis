from lxml import html
import requests
from threading import Thread
import re

def test(string):
	return ("aditya"+string)

def SearchProduct(product_name):
	search_string = "http://www.amazon.in/s/?url=search-alias=aps&field-keywords="+product_name+"&Go=Go"

	#print search_string
	# _____ create header to fool the website ________

	headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
	page = requests.get(search_string,headers=headers)
	data = html.fromstring(page.content)

	# ________________  page parsing  ________________

	number = 10 # change to increase the number of scraped products
	#      extract the top 10 products

	product_name = data.xpath('//a[@class="a-link-normal s-access-detail-page  s-color-twister-title-link a-text-normal"]/h2/text()')
	product_name_list = product_name[:number]

	image_link = data.xpath('//img[@class="s-access-image cfMarker"]/@src')
	product_image_link = image_link[:number]

	price_value = data.xpath('//span[@class="a-size-base a-color-price s-price a-text-bold"]/text()') 
	price_value_list = price_value[:number]

	product_asin = data.xpath('//li[@class="s-result-item  celwidget "]/@data-asin')
	if(len(product_asin) == 0):
		product_asin = data.xpath('//li[@class="s-result-item celwidget "]/@data-asin')
	product_asin_list = product_asin[:number]

	product = data.find("a")
	string = 'a[@class="a-link-normal s-access-detail-page  a-text-normal"]/title'
	article_list = data.findall(string)
	#print product_name_list,product_image_link,price_value_list,product_asin_list
	product_features = getFeatures(product_asin_list)
	#print product_features
	product_features_list=[]
	for asin in product_asin_list:
		for pf,pa in product_features:
			if(asin == pa):
				product_features_list.append(pf)
	return product_name_list,product_image_link,price_value_list,product_asin_list,product_features_list
	
	#print article_list

	
def FetchFeatures(prod_asin):
	product_review_link = "http://www.amazon.in/dp/"+str(prod_asin)+"/"
	headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
	page = requests.get(product_review_link,headers=headers)
	data = html.fromstring(page.content)
	features_list = data.xpath('//div[@id="feature-bullets"]/ul[@class="a-unordered-list a-vertical a-spacing-none"]/li/span[@class="a-list-item"]/text()')
	#print features
	features = []
	for feature in features_list:
		features.append(re.sub('\s+',' ',feature).encode('utf-8'))
	#print '\n'
	return features,prod_asin

def getFeatures(product_asin_list):
	#p=[0,0,0,0,0,0,0,0,0,0]
	p=[0]
	i=0
	#print names
	'''
	for prod in asin:
			t = threading.Thread(target=FetchFeatures, args = (prod,))
			#t.daemon = True
			p[i] = t.start()
			#print p[i]
			#i=i+1
			#print t
	print p[0]
	'''
	import Queue
	from threading import Thread

	que = Queue.Queue()
	threads_list = list()
	for prod in product_asin_list:
		t = Thread(target=lambda q, arg1: q.put(FetchFeatures(arg1)), args=(que, prod))
		t.start()
		threads_list.append(t)

	for p in threads_list:
	    p.join()

	results_list = []
	# Check thread's return value
	while not que.empty():
	    results_list.append(que.get())
	return results_list

prod_names,prod_images,prod_price,prod_asin,prod_features = SearchProduct('mobile phone')
        #return HttpResponse(prod_names)
        #sample = ['lol','ertgf','fghytr','ghgfh','asd','asd']
product_data = zip(prod_names,prod_images,prod_price,prod_asin,prod_features)
for n,i,pr,asin,fe in product_data:
	print n,fe