#Instructions

###Activate Virtual Environment & Install Dependencies
```
source venv/bin/activate
pip install -r requirements.txt
```

###Log in to AWS Console
Log in to the console and go the instances list so that
you can view the instances that are spun up and terminated.

###Run to launch an Instance
```
python launchtest.py
```
This will spin up an EC2 instance called 'class-libcloud',
wait 30 seconds for you to see that it is running in the AWS
console, and then shutdown.
