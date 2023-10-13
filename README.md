# Python AWS automation.
Python automation to manipulate my AWS services.
<p>A quick tutorial of how to set up an automation script to manipulate AWS services.</p>

# Follow the Steps for setup:
<ul>
  <li>Install python3</li>
  <li>Install python package Boto3</li>
  <li>Install aws-cli python package</li>
</ul>
<h3>Installing Python3</h3>
<p>Go to this url and download python3 as per your OS, <a href='https://www.python.org/downloads/'>Click here</a></p>
<h3>Installing Python Package Boto3 and Aws-cli</h3>
<div class="code-block">
  <pre><code id="my-code">
 pip install boto3
  </code></pre>
</div>
<div class="code-block">
  <pre><code id="my-code">
 pip install awscli
  </code></pre>
</div>

<h3>Set up your AWS IAM role in enviroment</h3>
<p>To know more about what is AWS IAM user role, <a href='https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html'>Click here</a></p>
<p>Run this command in CMD/PS/Terminal</p>
<div class="code-block">
  <pre><code id="my-code">
 aws configure
  </code></pre>
</div>
<p>The CMD/Terminal will ask for these details from AWS IAM user, Fill it properly as shown below</p>
<img src='https://github.com/Samit-prsl/Aws-automation/assets/118003672/1a3af5a1-e666-411c-9ff7-d9f5fba84df3' alt='...'/>
<p>Press enter to save your AWS IAM user role in AWS-cli, 
You are now ready to use Boto3 package for AWS manipulation</p>

<h3>Using Boto3 package</h3>
<p>You use the AWS SDK for Python (Boto3) to create, configure, and manage AWS services, such as Amazon Elastic Compute Cloud (Amazon EC2) and Amazon Simple Storage Service (Amazon S3). The SDK provides an object-oriented API as well as low-level access to AWS services.</p>

<a href='https://boto3.amazonaws.com/v1/documentation/api/latest/index.html'>Visit here for the Boto3 documentation</a>

<p>All the codes for starting, running, stoping and terminating an AWS EC2 instance is available in the codebase, I would always recommend to read the documentation and implement things on your own, if their is any error or bug coming up, please do cross-check your code with mine.</p>

<h3>Extra links</h3>
<p><a href='https://youtu.be/XhW17g73fvY?si=ND09uwMM7xdS6cJ3'>Click here to get an hands-on demo of how to signup for an AWS account.</a></p>
<p><a href='https://youtu.be/8TlukLu11Yo?si=xkIcXYzfaGSPFhF4'>Click here to know more about AWS EC2 instance</a></p>
