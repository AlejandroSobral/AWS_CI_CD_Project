## AWS CI CD Learning project

This project has one an simple objective: Learn.
The stuff is just about building a very-simple Python application; and show it as a web-site.

The web-site itself will show a list of Argentinian football teams, and user will be able to choose one, then the title record will prompt. 

As per the application, that's all.

However, the focus will be set upon how its infrastructure is designed & deployed.

The setps will be set on a GitHub CI/CD pipeline. Using Python, Terraform and AWS.

## Information collecting process

The informations is scrapped from Web, mainly from promiedos.com.ar. Therefore, a JSON file is created, based on the collected information.
This will represent a step.


## DB creation

The DB will be located at AWS. Particularly, DynamoDB. Based on the previous JSON file. Not sure it this can be performed using Terraform or Python; maybe both?


## EC2 instance deploy

The EC2 instance will be deployed using Terraform. It should include the required steps to be able to host the web.

