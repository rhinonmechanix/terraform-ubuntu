AWS early years

1. Started its first service with -> Amazon S3
2. Followed by -> simple queue service (SQS)
3. Same year -> EC2 was released
4. Amazon RDS -> database as a service
5. Route 53 -> DNS service
6. DynamoDB -> noSQL database
7. Code Pipeline -> DevOps orchestration tool

----------------------------------

AWS Services

1. Security and Identity - Most important service we need in aws, its helps with authentication, storing password and many more.
	a. Data Protection services
		->AWS certificate Manager
		->AWS key management service
	b. Infrastucture Protection
		->AWS Sheild
	c. Threat Detection
		-> Amazon Guard Duty
	d. Identity Management
		-> AWS IAM
		-> AWS Organizations
 
2. Compute - Refers to services which runs application.
	a. Instances
		-> Amazon EC2 - Secure and resizable VM
		-> Amazon Lightsail - Cloud platform to build applications
	b. Containers
		-> Amazon ECS - runs secure and reliable containers
		-> Amazon ECR - Store, manage, and deploy container images
		-> Amazon EKS - Fully managed Kubernetes service
	c. Edge
		-> AWS Snow family - Bring your data into AWS
		-> AWS Wavelength - Access AWS services via 5G networks
		-> VMWare Cloud on AWS - Migrate VMWare workloads

3. Storage - Refers to store data. 
	a. File Based Storage
		-> Amazon EFS - elastic and cloud native Network file system
	b. Block Storage
		-> Amazon EBS - easy to use, high performance block Storage - Used for storing all files of Amazon EC2s 
	c. Object Storage
		-> Amazon S3 - Largly used storage service to store and retrieve amount of data from anywhere in the world

4. Databases - Organised collection of data.
	a. Relational Databases
		-> Amazon Aurora
		-> amazon RDS
		-> Amazon RedShift
	b. Key-VAlue Database
		-> Amazon DynamoDB - Fast and Flexible NpSQL database for any scale.

5. Networking - Requires for connecting to internet.
	a. Cloud networks
		-> Amazon VPC - define and provision an isolated network for AWS resoures
		-> AWS Transit Gateway - Connects VPCs and On-Premises Networks
		-> Amazon Route 53 - Host our own Managed DNS
	b. Network Scaling
		-> Elastic Load Balancing
		-> AWS Global Accelerator
	c. Content Delivery
		-> Amazon CloudFront

6. Management and governance - Which helps us manage all aws and infrastructure in some cases.
	a. Account Management
		-> AWS Control Tower
		-> AWS Budgets
	b. Provisioning 
		-> AWS Service Catalog
		-> AWS Marketplace - find, test, buy and deploy software that runs on aws
	c. Operation Services
		-> Amazon CloudWatch
		-> AWS Config
		-> AWS system manager - optimize performance
		-> Amazon X-ray - analyze and debug production

7. Machine learning - services which helps us to analyze the code if correct or not and many more like image recoqnition, automatic language translation, etc.
	a. Machine Learning AI
		-> Amazon Kendra - Intelligent Search
		-> Amazon Personalize - Personalized recommendations
	b. Machine Leaarning Business Metrics
		-> Amazon Forecast - Build Accurate forecasting models
		-> Amazon Fraud Detector - Identify Potentially Fraudulent online activities
	c. Machine learning Vision
		-> Amazon Rekognition - Analyze images and videos and extract meaning
	d. Machine Learning Language Services
		-> Amazon Polly - Turns text to speech
		-> Amazon Transcribe - Turns speech to text
		-> Amazon Lex - Easily build agents like chat-bots