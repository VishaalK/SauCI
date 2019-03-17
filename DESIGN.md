Design Document for SauCI

# Summary

SauCI is a continuous integration system built from scratch. It is intended as a learning tool to make a front-end in Django that connects to multiple different storage back-ends to compare their implementations. There are plans to add monitoring and analytics for learning purposes as well, and get some experience using Docker and Kubernetes. Along the way we might try implementing it in a server-less manner as well.

SauCI is going to be bootstrapped using other CI tools, and then will itself run on SauCI.

# Objective

SauCI is intended to give feedback about any executable command that can indicate to a computer if it succeeded or not (e.g. a bash script). 

# Architecture


