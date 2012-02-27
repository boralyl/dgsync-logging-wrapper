About
=====
A small python script that can be wired up to synchronize your files with an Amazon S3 account. Provides logging functionality.

Requirements
============
dgsync - http://www.dragondisk.com/

Setup
=====
1.  Set LOG_FILE.  Specify a path for the log file.
2.  Set DGTOOLS_ACCESS_KEY.  Specify your Amazon access key.
3.  Set DGTOOLS_SECRET_KEY.  Specify your Amazon secret key.
4.  Set BUCKETS.  Specify a dictionary of buckets and local directories with the s3 url as the key and local directory as the value.
5.  Make s3sync.py executable and wire it up with the crontab.
6.  ?
7.  Profit.

Example Configuration
---------------------
> LOG_FILE = "/home/user/bin/log/syncs3.log"
> DGTOOLS_ACCESS_KEY = "Your_Amazon_Access_Key"
> DGTOOLS_SECRET_KEY = "Your_Amazon_Secret_Key"
> BUCKETS = {
>     "s3://my-bucket/Videos/": "/home/user/Videos",
>     "s3://my-bucket/Pictures/": "/home/user/Pictures",
> }

