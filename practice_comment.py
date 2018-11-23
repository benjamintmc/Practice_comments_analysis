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

total_len = 0
for review in data:
	len(review)
	total_len += len(review)


print('Average review length is', total_len/len(data), 'characters')