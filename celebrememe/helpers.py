import re
def get_meme_text_from_tweet(tweet):
	# create a list of the words so we can split the sentence approriately.
	# ['Hi', 'there.', 'This', 'is', 'a', 'tweet']
	words_list = tweet.split()
	break_point = len(words_list)//2
	# if a period or comma is present Split the top and bottom text on that as it will 
	# be more comedic. Period takes precedence over comma, which takes precedence over len//2
	for index, word in enumerate(words_list):
		if word[-1] == ",":
			if index != len(words_list)-1:
				break_point = index+1
				break

	for index, word in enumerate(words_list):
		if word[-1] == ".":
			if index != len(words_list)-1:
				break_point = index+1
				break

	# grab the first half of the words
	# ['Hi', 'there.']
	top_text = words_list[:break_point]
	# grab the second half of the words
	# ['This', is', 'a', 'tweet']
	bottom_text = words_list[break_point:]
	# Join the words in the list and replace hashtags with url-friendly percent encoding
	top_text = " ".join(top_text)
	top_text = top_text.replace("#", "%23")

	bottom_text = " ".join(bottom_text)
	bottom_text = bottom_text.replace("#", "%23")

	top_text, bottom_text = remove_emoticons(top_text,bottom_text)
	
	# return a tuple of the top_text and bottom text
	return (top_text, bottom_text)

def remove_emoticons(top_text, bottom_text):
	try:
	    # UCS-4
	    highpoints = re.compile(u'[\U00010000-\U0010ffff]')
	except re.error:
	    # UCS-2
	    highpoints = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
	# replace emoticons with empty spaces
	top_text = highpoints.sub(u'', unicode(top_text))
	bottom_text = highpoints.sub(u'\u25FD', unicode(bottom_text))
	# convert from unicode strings back to ascii strings
	top_text = top_text.encode('ascii','ignore')
	bottom_text = bottom_text.encode('ascii','ignore')
	# return tuple of top and bottom text
	return top_text, bottom_text