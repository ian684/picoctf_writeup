#!/bin/sh
touch trash.txt
for i in {1..350};do
	curl -s http://mysterious-sea.picoctf.net:57205/ > trash.txt 
done;
