# -*- coding: utf-8 -*-

import sys
import math

unicode_number_array   = [u"၀", u"၁", u"၂", u"၃", u"၄", u"၅", u"၆", u"၇", u"၈", u"၉"]
unicode_counting_num   = [u"သုည", u"တစ်", u"နှစ်", u"သုံး", u"လေး", u"ငါး", u"ခြောက်", u"ခုနစ်", u"ရှစ်", u"ကိုး"]
unicode_counting_array = [u"ဆယ်", u"ရာ", u"ထောင်", u"သောင်း", u"သိန်း"]
unicode_creaky_tone    = u"့"

def get_utf8_from_array(array, index):
	before = array[index]

	return before.encode("utf-8")

def convert_mm_num_to_english_num(value):					# convert myanmar numerals to english numerals
	converted = ""
	for char in list(value.decode("utf-8")):
		for i, j in enumerate(unicode_number_array):
			if j == char:
				converted = converted + str(i)

	return converted

def convert_english_num_to_mm_num(value):					# convert english numerals to myanmar numerals
	number = int(value)
	number_string = str(number)

	converted = ""
	for char in number_string:
		char_num = int(char)
		converted = converted + unicode_number_array[char_num]

	return converted

def convert_num_to_words(value):				# convert english numerals to myanmar words
	number = int(value)
	count = 5

	collectedString = ""

	while number >= 10:
		if number >= math.pow(10, count):
			prefix = int(number/math.pow(10, count))
			number -= int(math.pow(10, count) * prefix)

			suffix = ""
			if number > 0 and count > 0 and count < 4:
				suffix = unicode_creaky_tone.encode("utf-8")

			if prefix > 9:
				collectedString += convert_num_to_words(prefix)
			else:
 				collectedString += get_utf8_from_array(unicode_counting_num, prefix)

			collectedString += get_utf8_from_array(unicode_counting_array, count - 1) + suffix

		count -= 1

	if number > 0:
		collectedString += get_utf8_from_array(unicode_counting_num, number)

	return collectedString

def convert_words_to_num(words):							# convert myanmar words to english number
	total = 0
	cached_words = words.replace(unicode_creaky_tone.encode("utf-8"), "")
	cached_words = words.replace(" ", "")

	for index, val in reversed(list(enumerate(unicode_counting_array))):
		val = val.encode("utf-8")
		parts = cached_words.split(val)

		if len(parts) > 1:
			for i, j in enumerate(unicode_counting_num):
				if parts[0] == j.encode("utf-8"):
					total += i * math.pow(10, index + 1)

		if len(parts) > 1:
			cached_words = parts[1]

	if len(cached_words) != 0:
		for i, j in enumerate(unicode_counting_num):
			if parts[0] == j.encode("utf-8"):
				total += i

	return int(total)

if __name__ == "__main__":
	print convert_english_num_to_mm_num(123456789)
	print convert_mm_num_to_english_num("၁၂၃၄၅၆၇၈၉")
	print convert_num_to_words(10000)
	print convert_words_to_num("နှစ်ဆယ့်သုံးသိန်းနှစ်သောင်းသုံးထောင့်နှစ်ရာ့သုံးဆယ့်နှစ်")
