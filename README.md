# documentdb_tutorial
This repository provides a short description on using DocumentDB for storing real time data and steps to create a Document DB cluster.

# Create Security Groups

We will setup 2 security groups, the first security group (demoEC2) allows you to SSH into your EC2 instance from your local machine (client). The second security group (demoDB) enables you to connect to your Amazon DocumentDB cluster on port 27017 (the default port for Amazon DocumentDB) from your EC2 instance. 

# Create EC2 Instance

The next step is to create an EC2 instance in the same Region and VPC that you use to provision your Amazon DocumentDB cluster.

# Create DocumentDB cluster

The next step is to create the Document DB cluster using the demoDB security group we created to get the required access to the cluster. 


# Install MongoShell in an EC2 instance

To install the mongo shell on Amazon Linux, complete the following steps.

Create the repository file. At the command line of your EC2 instance, execute the follow command:

```
echo -e "[mongodb-org-3.6] \nname=MongoDB Repository\nbaseurl=https://repo.mongodb.org/yum/amazon/2013.03/mongodb-org/3.6/x86_64/\ngpgcheck=1 \nenabled=1 \ngpgkey=https://www.mongodb.org/static/pgp/server-3.6.asc" | sudo tee /etc/yum.repos.d/mongodb-org-3.6.repo 
```

When it is complete, install the mongo shell by executing the following command:

```
sudo yum install -y mongodb-org-shell
```

To encrypt data in transit, download the CA certificate for Amazon DocumentDB. See the following code:

```
wget https://s3.amazonaws.com/rds-downloads/rds-combined-ca-bundle.pem
```
