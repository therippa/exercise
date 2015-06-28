#Domain Tagging, Jr.

The exercise:

*Create an application that hundreds of thousands of Internet users will use to track Web site domain names and accompanying descriptions.*

*Your application should provide two Web pages:*

1. *One that allows users to submit one domain and description at a time.*
2. *One that displays all valid domains along with their descriptions and the submission date, ordered from newest to oldest.*

*For our purposes, a valid domain is one that has one or more IP addresses in the DNS.*

*Your application should include a table called "domain" that stores (at a minimum):*

1. *the domain name, whether or not it is valid*
2. *the description*
3. *the date and time of submission.*

*Keep in mind that users might attempt to submit any sort of text-like data as a domain, e.g., "http://www.opendns.com/about/", "notareal.comdomain", or pretty much anything else.*

*Also, domains should be stored in the database without any "www" prefix and without any other URL components. For example, "http://www.opendns.com/about/" should be stored as "opendns.com".*

### Things I Did
1. Used Angular/Express to create a one-page app providing the user interface (I deviated from the two-pages instruction to make things more interesting and demonstrate binding)
2. Created a web service using Django to check if the domain name has an IP address associated with it.  The web service is hosted on Heroku, so installing the **django\_domain\_utils** project is not necessary for testing.
3. Used mongoose/mongodb for persistent database storage
4. Used bower for package dependency management
5. Another slight deviation from the instructions that I thought would be an improvement - invalid domains are listed in the table, but the row his highlighted to show the error

###Installation
The project is running on a Heroku dyno, you may test it [here](http://blooming-retreat-9088.herokuapp.com/#/home).  If you would like to run a local instance, please do the following:

1.  Make sure NodeJS is installed on your system
2.  From your terminal, run this command to install the dependencies: `npm install && bower install`
3. Run `npm start` to start the server, and point your browser to [http://localhost:3000](http://localhost:3000)