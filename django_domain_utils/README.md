#Is Phish?

The exercise:

*Imagine that you run a very popular URL shortening service (similar to bit.ly, is.gd, etc.), and want to prevent malicious users from masking phishing sites with your service. One way you might do this is to check submitted URLs against the PhishTank Web site to see if it considers them to be phishes. Using the information at http://www.phishtank.com/developer_info.php, implement a web service that performs this check. Because your service is so popular, it sees over 50 new URLs per second, so keep that in mind when interacting with PhishTank.*


### Things I Did
1. Used Django to provide web service calls.
2. Used memcachier/memcached to hold previous calls in memory, increasing performance when dealing with domains/urls already checked.
3. Used indexing for speedy retrieval, and duplicate checks to make sure a URL is only stored one time.

### Service Endpoints
* **phish/generate/?url=\<url\>** - checks the given url against the list of known phishing URL's provided by PhishTank, and if it's good, returns a hash that can be used in a shortened url.
[Example return for good site](https://ancient-crag-3153.herokuapp.com/phish/generate/?url=http%3A%2F%2Fwww.opendns.com), [Example return for phishing site](https://ancient-crag-3153.herokuapp.com/phish/generate/?url=http%3A%2F%2Fvitamedika.net%2Fsecure%2FApple%2F)

* **phish/\<url_hash\>** - Pass the hash returned from the generate endpoint, and it will redirect you to the associated url. [Example shortened link](https://ancient-crag-3153.herokuapp.com/phish/f1fac614)

* **ip_check/?domain=\<domain\>** - checks to see if the given domain name has an IP address associated with it. [Example return data](https://ancient-crag-3153.herokuapp.com/ip_check/?domain=opendns.com)


###Installation
The project is running on a Heroku dyno, you may test it [here](https://ancient-crag-3153.herokuapp.com).  If you would like to run a local instance, please do the following:

1.  Make sure Python is installed on your system, and I strongly suggest using virtualenv as not to mess up any python library versions on your system.
2.  From your terminal, run this command to install the dependencies: `pip install -r reqs/dev.txt`
3. Setup the database. Run `python manage.py syncdb` and `python manage.py migrate`
4. Run `python manage.py runserver` to start the server, and point your browser to [http://localhost:8000](http://localhost:8000)