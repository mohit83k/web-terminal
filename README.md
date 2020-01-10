# Web Terminal

## Summary

It is browser based shell / terminal. It runs python to host the website , which takes the command and execute on
the same machine where website is hosted.

## Technology Stack
	+ Python  3.7.3
	+ Flask
	+ Html , Css , JavaScript

## Key Points

1. Configurable

  	Database is abtracted to use a python module as a plugin. Plugin have to implement the abstract class
  	`DbFramework`. Database and it's required properties can be configured in config.json.
  	Simple file system DB is already implemented. Such DB have very low speed and high memory consumption.
	

## Future Road Map

1. Implement ssh client so that server can act as an interface between ssh and http. Using this, webserver needed to be installed only at one server. It can then connect to other servers using ssh and act as kind of a relay. 

