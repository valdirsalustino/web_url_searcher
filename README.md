# Web URL searcher

This application was suggested by the by IBM recruting team in order to avaliate the developer skills of candidates for software analytics. 
The strategy:
The chosen languange is python because it have several powerfull libraries for web scraping.

The unit tester is ..... 


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


Just clone the the project with: git clone `https://github.com/valdirsalustino/web_url_searcher.git` 

Change the root directory to the created `web_url_searcher`: cd `web_url_searcher`


### Prerequisites

This application was tested in my local machine with python 3.6.4

After download the source code you need to install the <a href="https://console.bluemix.net/docs/cli/reference/bluemix_cli/get_started.html#getting-started">IBM Cloud CLI </a> and the <a href="https://docs.docker.com/engine/installation/">Docker CLI</a>.

```
Example:

python urlSearcher.py 
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
