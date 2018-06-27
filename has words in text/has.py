#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

text_file = io.open("text.txt", mode="r", encoding="utf-8")
text_string = text_file.read().lower()

books_file = io.open("books.txt", mode="r", encoding="utf-8")

has = []
for line in books_file:
	if line.strip().lower() in text_string:
		has.append(line)
for i in has:
	print(i)
print(len(has))
