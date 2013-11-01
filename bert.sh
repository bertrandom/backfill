#!/bin/bash
if [ -s data/snapshots/1150179475.html ]
	then
		curl "http://web.archive.org/web/20060613061755/http://flickr.com/about/" > data/snapshots/1150179475.html
fi
