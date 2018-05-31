# Web URL searcher

This application was suggested by the by IBM recruting team in order to avaliate the developer skills of candidates for software analyst. 
The strategy:
The chosen languange is python because it have several powerfull libraries for web scraping and connection to Cloudant database.

The challenge includes:
<ul> 
<li> The app needs to receive an URL; </li> 
<li> The app needs to find all links inside this given URL; </li>
<li> The app needs to save this links found in database (SQL or No-SQL) </li>
<li> The app needs listing this links saved in the database. </li>
<li> After collecting all links from the initial URL. Collect from the newly found links. I mean, the system gets the first link saved, and start the process (get all links and keep on the database). Follow does it to the second, third and successively until the last link saved and tracked. </li>
</ul>
 

<p> Please, as an extra effort, include in your solution the following: </p>
<ul>
<li> Your code needs to be integrated with git on your GitHub personal profile; </li>
<li> Your code needs to contain unit testing; </li>
<li> Your code needs to be served on the IBM Cloud; </li>
<li> Your code needs to run with containers, with in IBM Cloud; </li>
</ul>

## Getting Started


Just clone the the project at github: `git clone https://github.com/valdirsalustino/web_url_searcher.git` 

Change the folder created `cd web_url_searcher`

Run the code `python urlSearcher.py`

As default the program scrape the url: www.google.com
Please edit the variable `initial_url = "www.google.com"` to whateve url you want to scrape.
There is an option which allows the user to past the url into the iterative command line. 
However it fails to be iterative within a container in the IBM cloud, to my best knowledge.

The package includes an unit test for every function used by the urlSearcher.py

just run `python myunittest.py`

In the package there are the following files:
<ul> 
    <li> `Dockerfile`: contain the instruction to build the docker image. It uses the `requirements.txt` file; </li>
    <li> `README.md`: the file you are reading now;</li>
    <li> `myunittest.py`: the unit test build on top of the `unittest` package, more info <a href="https://docs.python.org/2/library/unittest.html">here</a>;</li>
    <li> `requirements.txt`: the requirements file which docker uses to build their image. It just contain cloudant library requirement;</li>
    <li> `urlSearcher.py`:  the file you use to run the scraper;</li>
    <li> `urlscraping.py`:  the python module with functions used by the `urlSearcher.py`.</li>
</ul>

### Prerequisites

This application is tested with python 3.6.4.

After download the source code you need to install the <a href="https://console.bluemix.net/docs/cli/reference/bluemix_cli/get_started.html#getting-started">IBM Cloud CLI </a> and the <a href="https://docs.docker.com/engine/installation/">Docker CLI</a>, in order to run the image on the container.

```
Example to run in the container image:


```
The software will ask you for an url which you have to proved. For example: 
Please past an url: '<https://your_url>'

### Installing

It is an installation free software. You just need to have python and the requered libraries.

## Running the tests
An example with a given url:

`python urlSearcher.py `

Please past an url: `https://en.wikipedia.org/wiki/Cloudant`

and the output shall show you the following steps relating to store the result into the Cloudant No SQL database, restore its result and find more urls within the initial stored urls.


### Break down into end to end tests

#### Unit test
As suggested, I perform the unit test using the <a href="https://docs.python.org/2/library/unittest.html">unittest — Unit testing frameworkh</a>

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Cloudant](https://www.ibm.com/cloud/cloudant) - The No SQL highly scalable database
* [Container](https://www.ibm.com/cloud/container-service) - The IBM cloud repository service. 
* [Python 3.6.4](https://www.python.org/downloads/release/python-364/) - Python language

## Contributing

You are welcome to give suggestion about this application.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Valdir Salustino Guimarães** - 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

The IBM recruting team for release this challenge.
