# documentdb_tutorial
This repository provides a short description on using DocumentDB for storing real time data and steps to create a Document DB cluster.


To install the mongo shell on Amazon Linux, complete the following steps.

Create the repository file. At the command line of your EC2 instance, execute the follow command:

```
echo -e "[mongodb-org-3.6] \nname=MongoDB Repository\nbaseurl=https://repo.mongodb.org/yum/amazon/2013.03/mongodb-org/3.6/x86_64/\ngpgcheck=1 \nenabled=1 \ngpgkey=https://www.mongodb.org/static/pgp/server-3.6.asc" | sudo tee /etc/yum.repos.d/mongodb-org-3.6.repo 
```

When it is complete, install the mongo shell by executing the following command:

```
sudo yum install -y mongodb-org-shell
```
