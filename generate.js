var moment = require('moment'),
	fs = require('fs'),
	timemapRaw,
	lines;

console.log('#!/bin/bash');

timemapRaw = fs.readFileSync(__dirname + '/data/timemap.txt', {encoding: 'utf8'});

lines = timemapRaw.split("\n");

lines.forEach(function(line) {

	var matches, url, timestamp;

	if (line.match(/rel="(first |last )?memento"/)) {

		matches = line.match(/<(http:\/\/web.archive.org\/web\/[0-9]*\/(.*))>/);
		url = matches[1];

		matches = line.match(/datetime="(.*)"/);
		timestamp = moment.utc(matches[1]).unix();

		console.log('if [ ! -s data/snapshots/' + timestamp + '.html ]');
		console.log('	then');
		console.log('		curl "' + url + '" > data/snapshots/' + timestamp + '.html');
		console.log('fi');

	}

});