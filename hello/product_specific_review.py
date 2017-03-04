from lxml import html
import requests

def test(string):
	return ("aditya"+string)

def SearchProduct(product_name):
	search_string = "http://www.amazon.in/s/?url=search-alias=aps&field-keywords="+product_name+"&Go=Go"

	#print search_string
	# _____ create header to fool the website ________

	headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
	page = requests.get(search_string,headers=headers)
	data = html.fromstring(page.content)

	'''
	with open(r'C:\Users\Aditya\Downloads\amazon\amazonweb.html', "r") as f:
	    page = f.read()
	data = html.fromstring(page)
	'''

	# ________________  page parsing  ________________


	#      extract the top 10 products
	
	product_id_list = []
	product_name_list = []

	for i in range(10):
		product_id = '//li[@id="result_'+str(i)+'"]/@data-asin'  
		#print product_id
		p_id = data.xpath(product_id)
		product_id_list.append(str(p_id))
		
		product_name = '//li[@id="result_'+str(i)+'"]/a[@class="a-link-normal s-access-detail-page  a-text-normal"]/@title/text()'
		#print product_name
		
		
		
		p_name = data.xpath(product_name)
		product_name_list.append(p_name)
		


	names = data.xpath('//h2[@class="a-size-base a-color-null s-inline  s-access-title  color-variation-title-replacement a-text-normal"]/text()')
	product_name_list = names[:20]
	product_name = data.xpath('//a[@class="a-link-normal s-access-detail-page  a-text-normal"]/h2/text()')
	product_name_list = product_name[:20]
	image_link = data.xpath('//img[@class="s-access-image cfMarker"]/@src')
	product_image_link = image_link[:20]
	price_value = data.xpath('//span[@class="a-size-base a-color-price s-price a-text-bold"]/text()') 
	price_value_list = price_value[:20] 



	product = data.find("a")
	string = 'a[@class="a-link-normal s-access-detail-page  a-text-normal"]/title'
	article_list = data.findall(string)
	return product_name_list,product_image_link,price_value_list
	#print article_list
'''
	for i in range(10):
		print "["+str(i)+"]"+"\t"+str(product_name_list[i])+str(product_id_list[i])
		print "\n"

	print "enter the product number"
	p=raw_input()
	prod_id = product_id_list[int(p)]

	pr_id = prod_id[2:12]
	#print pr_id
	product_review_link = "http://www.amazon.in/product-reviews/"+str(pr_id)+"/"
	#print product_review_link
	headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
	page = requests.get(product_review_link,headers=headers)
	data = html.fromstring(page.content)
	reviews = data.xpath('//a[@class="a-size-base a-link-normal review-title a-color-base a-text-bold"]/text()')
	titles = data.xpath('//h1[@class="a-size-large a-text-ellipsis"]/text()')
	#print titles
	#f.write("Product : " + titles)
	i=i+1
	for review in reviews:
		try:
			print review,
		except: print ''
		print '\n'
'''