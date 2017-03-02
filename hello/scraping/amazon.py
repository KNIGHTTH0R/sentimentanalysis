from lxml import html
import requests

products = ['http://www.amazon.in/Apple-MMGF2HN-13-3-inch-Integrated-Graphics/product-reviews/B01FUK9TKG/','http://www.amazon.in/Moto-Plus-4th-Gen-Black/product-reviews/B01DDP7GZK']
f= open("review.txt","w+")
i=1
for product in products:
	#print product
	page = requests.get(product)
	#print page
	data = html.fromstring(page.content)
	reviews = data.xpath('//a[@class="a-size-base a-link-normal review-title a-color-base a-text-bold"]/text()')
	titles = data.xpath('//h1[@class="a-size-large a-text-ellipsis"]/text()')
	#print titles
	#print reviews
	#f.write("Product : " + titles)
	i=i+1
	for review in reviews:
		try:
			print review + "\n"
			f.write(review + "\n")
		except: print '',
	f.write("_________________________________________________________________\n")
f.close