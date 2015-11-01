#!/usr/bin/python

#  Created on 11/1/15 by Liam Rahav

import sys
from imgurpython import ImgurClient
from keys import CLIENT_ID, CLIENT_SECRET

imgur = ImgurClient(CLIENT_ID, CLIENT_SECRET)
items = imgur.gallery()
for item in items:
    print(item.link)

