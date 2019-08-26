# LOGS ANALYSIS PROJECT - Udacity FSDN

The project requires to create a reporting tool that would fetch results from a large database of a "NEWS" website and prints out
reports(in plain text) based on the data in the given database.

The Python script uses the psycopg2 library to query the database and produce a report that answers the following three questions:

What are the most popular three articles of all time?
Who are the most popular article authors of all time?
On which days did more than 1% of requests lead to errors?


### Prerequisites

* [Python3](https://www.python.org) - The code uses ver 3.6.4

* [Vagrant](https://www.vagrantup.com) - A virtual environment builder and manager  

* [VirtualBox](https://www.virtualbox.org) - An open source virtualiztion product
 
* [Udacity Preconfigured VM](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip) Alternately, you can use Github to fork and clone [this](https://github.com/udacity/fullstack-nanodegree-vm) repository.

* Udacity [“news”](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) Database File.



### Installing

* Download and install Python.
* Download and install Vagrant and VirtualBox.
* Download this Udacity folder with preconfigured vagrant settings.
* Download data provided by Udacity 	
* Unzip file to extract newsdata.sql.This file should be inside the Vagrant folder.
* Open a terminal windows and navigate to your VM folder Vagrant.
* Use Commands 'vagrant up' to start the VM and'vagrant ssh' to connect to it. 
* cd to /vagrant shared folder.
* Load the database using 'psql -d news -f newsdata.sql'
* connect to the database using 'psql -d news'. 
* Create Views given below then exite psql with ctrl+D.

CREATE THE FOLLOWING VIEWS
	

	CREATE VIEW logstar AS
	SELECT count(*) as stat, 
	status, cast(time as date) as day
	FROM log WHERE status like '%404%'
	GROUP BY status, day
	ORDER BY stat desc limit 3;


	CREATE VIEW totalvisitors AS
	SELECT count(*) as visitors,
	cast(time as date) as errortime
	FROM log
	GROUP BY errortime;


	CREATE VIEW errorcount AS
	SELECT * from logstar join totalvisitors
	ON logstar.day = totalvisitors.errortime;	


## Running the tool

* Open a terminal windows and navigate to your VM folder Vagrant.
* Use Commands 'vagrant up' to start the VM and 'vagrant ssh' to connect to 	it.
* cd to /vagrant folder.
* execute the Python file using 'python report-results.py'.
	











ENVIRONMENT CONFIGURATIONS




	
RUNNING THE PROGRAM


	