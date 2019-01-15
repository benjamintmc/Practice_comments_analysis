# comment/review analytic
import time
import progressbar

reviews = []
count = 0
bar = progressbar.ProgressBar(max_value=1000000)
with open('reviews.txt', 'r', encoding='utf-8-sig') as f:
	for line in f:
		reviews.append(line)
		count += 1
		bar.update(count)
print('\n', count, 'reviews in total.')

# # word count function
# wc = {} # word count
# start_time = time.time()
# for review in reviews:
# 	words = review.strip().split()
# 	for word in words:
# 		if word in wc:
# 			wc[word] += 1
# 		else:
# 			wc[word] = 1
# # for key in wc:
# # 	if wc[key] >= 100:
# # 		print(key, wc[key])
# end_time = time.time()
# print(end_time - start_time)

# # searching function
# while True:
# 	search = input('\nHow many times have your word appers in the reviews? ')
# 	if search in wc:
# 		print(search, 'have appeared', wc[search], 'times.')
# 	elif search == '_DONE':
# 		break
# 	else:
# 		print('This word has never shown in the reviews...')
# 	print('Thank you for using this function!')

# # calculat the average length of reviews
# total_len = 0
# for review in data:
#     len(review)
#     total_len += len(review)
# print('Average review length is', total_len/len(data), 'characters')

# # filter review with at least 100 characters
# filter1 = []
# filter2 = []
# for review in data:
#     if len(review) > 100:
#         filter1.append(len(review))
#     elif len(review) <= 100:
#         filter2.append(len(review))
# print(len(filter1), 'reviews have more than 100 characters')
# print(len(filter2), 'reviews have up to 100 characters')

# # filter review wiht "good"
# filter_good = []
# for review in data:
#     if 'is good' in review:
#         filter_good.append(review)
# print(len(filter_good), 'reviews with "is good" in it')