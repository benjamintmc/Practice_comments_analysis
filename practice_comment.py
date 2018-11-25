# comment/review analytic

data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 == 0:
			print(len(data))
print('Loading finished,', len(data), 'results in total')

# calculat the average length of reviews
total_len = 0
for review in data:
	len(review)
	total_len += len(review)
print('Average review length is', total_len/len(data), 'characters')

# filter review with at least 100 characters
filter1 = []
filter2 = []
for review in data:
	if len(review) > 100:
		filter1.append(len(review))
	elif len(review) <= 100:
		filter2.append(len(review))
print(len(filter1), 'reviews have more than 100 characters')
print(len(filter2), 'reviews have up to 100 characters')