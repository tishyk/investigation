import re
import time
time.clock()

""" Parse text with simple lines for answer status(200,404,304,etc) from "access.log.1":
127.0.0.1 - - [27/Sep/2015:06:30:55 +0300] "GET /server-status HTTP/1.1" 200 7217 "-" "Python-urllib/2.7"
127.0.0.1 - - [27/Sep/2015:06:30:55 +0300] "POST /server-status HTTP/1.1" --- "-" "Python-urllib/2.7"
106.125.52.69 - - [27/Sep/2015:06:30:58 +0300] "GET /ua.archive.ubuntu.com/12_04/dists/precise/Release.gpg HTTP/1.1" 304 187 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.16)"
"""

result={}
# create template for search in every log line, use re.search.
# (\d{3}) - create one group.
# Ex.("[GET|POST]).*?(HTTP.*?)"\s{1,5}(\d{3})? - will find 3 groups ("GET or "POST),(HTTP/1.1),(200)
# result.setdefault(key,0) -> use help(result.setdefault) 
template = re.compile('"[GET|POST].*?HTTP.*?"\s{1,5}(\d{3})?')

with open("access.log.1") as f:
    for line in f.readlines()[-3:]:
        key = template.search(line).groups()[0]
        if key:
            result[key]=result.setdefault(key,0)+1
        
print result,' result time: %.3f sec.'%time.clock()
