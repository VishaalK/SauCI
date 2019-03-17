Design Document for SauCI

# Summary

SauCI is a continuous integration system built from scratch. It is intended as a learning tool to make a front-end in Django that connects to multiple different storage back-ends to compare their implementations. There are plans to add monitoring and analytics for learning purposes as well, and get some experience using Docker and Kubernetes. Along the way we might try implementing it in a server-less manner as well. Seems like a lot? That's why we're going to break it up into milestones!

SauCI is going to be bootstrapped using other CI tools, and at some point will itself run on SauCI. That would be ideal.

# Objective

SauCI is intended to give feedback about any executable command that can indicate to a computer if it succeeded or not (e.g. a bash script). 

# Architecture Options

## Compute

The system will have to retrieve source code, set up some sort of environment for that source code, and run that source code, which means we need compute. 

A virtual machine

Container service

Lambda architecture/serverless

## Storage

We want to store the results of each build. Where things failed, and what errors we had, and make this accessible to the user. In addition, we will wrap these underlying technologies in a `storage layer` or interface that makes it easy to use multiple or switch between them.

Relational database

NoSQL store (theoretically simpler for prototyping)

Column store (worth exploring for different portions)

Stream based (Kafka + Materialized views?)


# Analysis of System

## Reliability

## Scalability

What are our load parameters? Simultaneously running builds. Not all builds are made equal, some builds are much more expensive than others, and some things don't even need to be built, just run (such as node tests). We also need to protect against abuse such as fork bombs, or infinitely hanging threads.

# Decided Architecture

# Monitoring of System

# Technical Milestones

## Minimally viable product

The minimally viable product right now is a single-node (locally hosted) system that when I push to a local Git repository, it runs the tests, saves the results to a database (and logs to some file on disk), and lets me view them in a locally hosted web application.


# Encountered Challenges

1. Not letting my previous experience and familiarity with technologies bias my analysis of the options for this service. For example, my initial assumption is to build it in Docker, since it has a lot of benefits, and to use a relational database backend. This is my instinct, and it seems correct (but I haven't even written anything).
