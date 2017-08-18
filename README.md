# prod-api

Productivity tools REST API built as serverless microframework deployed on [AWS][] using [Chalice][]

Following AWS services are used:

* AWS API Gateway
* AWS Lambda
* AWS EC2
* AWS S3

Run following commands to deploy

	$ set AWS_DEFAULT_PROFILE=profile1
	$ chalice deploy

To get URL

	$ chalice url
	
[aws]: http://aws.amazon.com
[chalice]: https://github.com/aws/chalice