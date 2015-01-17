# Route53-DynDns
Simple script that can update a Route53 hostname with current IP address.

This requires some setup on aws to run. You should create a new IAM user with the following policy:

    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Action": [
            "route53:ChangeResourceRecordSets",
            "route53:ListHostedZones",
            "route53:ListResourceRecordSets"
          ],
          "Resource": [
            "*"
          ]
        }
      ]
    }

You also need to install boto on the machine that this will be running on

On RHEL Systems:

    sudo yum install python-setuptools
    sudo easy_install pip
    sudo pip install boto

On Debian Systems:

    sudo apt-get install python-setuptools
    sudo easy_install pip
    sudo pip install boto

Generate console credentails for your IAM user. You will need to provide these credentials as environment variables to whatever user runs this script. You could place the following lines in the user's ~/.bash_profile

    export AWS_ACCESS_KEY_ID=accesskeyhere
    export AWS_SECRET_ACCESS_KEY=yoursecretaccesskeyhere
    
Once this is set up you can create a cron job to run the script at a defined interval. I run this script via jenkins, providing the credentials as parameters.
