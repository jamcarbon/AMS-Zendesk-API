#!/bin/bash

aws cloudformation describe-stacks

aws cloudformation validate-template --template-body file://C:\Users\jamca\OneDrive\Documents\Github\Repositories\AMS-Zendesk-API\infrastructure\stack.yaml

aws cloudformation create-stack --stack-name Zendesk-AMS-integration-test --template-body file://C:\Users\jamca\OneDrive\Documents\Github\Repositories\AMS-Zendesk-API\infrastructure\stack.yaml --capabilities CAPABILITY_NAMED_IAM

aws cloudformation delete-stack --stack-name Zendesk-AMS-integration-test





aws cloudformation create-stack --stack-name minimal-example --template-body file://C:\Users\jamca\OneDrive\Documents\Github\Repositories\AMS-Zendesk-API\infrastructure\stack.yaml --capabilities CAPABILITY_NAMED_IAM

aws cloudformation create-stack \
  --stack-name minimal-example \
  --capabilities CAPABILITY_NAMED_IAM \
  --template-body file://minimal-example.yml


aws cloudformation create-stack --stack-name Consegna-AMS-Zendesk-Integration-s1 --template-body file://infrastructure\step1_stack.yaml --capabilities CAPABILITY_NAMED_IAM

aws cloudformation describe-stack-events --stack-name minimal-example

aws cloudformation delete-stack --stack-name minimal-example

aws cloudformation update-stack --stack-name minimal-example --template-body file://C:\Users\jamca\OneDrive\Documents\Github\Repositories\AMS-Zendesk-API\infrastructure\stack.yaml --capabilities CAPABILITY_NAMED_IAM

aws cloudformation update-stack --stack-name minimal-example --template-body file://G:\Github\Repos\AMS-Zendesk-API\infrastructure\stack.yaml --capabilities CAPABILITY_NAMED_IAM

aws cloudformation validate-template --template-body file://G:\Github\Repos\AMS-Zendesk-API\infrastructure\stack.yaml



#step2

aws cloudformation validate-template --template-body file://C:\Users\jamca\OneDrive\Documents\Github\Repositories\AMS-Zendesk-API\infrastructure\step2_stack.yaml

aws cloudformation create-stack --stack-name step2stack --template-body file://infrastructure\step2_stack.yaml --capabilities CAPABILITY_NAMED_IAM --parameters ParameterKey=ZendeskAPIKey,ParameterValue=

aws cloudformation update-stack --stack-name step2stack --template-body file://G:\Github\Repos\AMS-Zendesk-API\infrastructure\step2_stack.yaml --capabilities CAPABILITY_NAMED_IAM --parameters ParameterKey=ZendeskAPIKey,ParameterValue=SampleZendeskAPI123456789

aws cloudformation describe-stack-events --stack-name step2stack

aws cloudformation delete-stack --stack-name step2stack



#Deployed in MfE account#275312195412
#step1
aws cloudformation create-stack --stack-name Consegna-AMS-Zendesk-Integration-s1 --template-body file://infrastructure\step1_stack.yaml --capabilities CAPABILITY_NAMED_IAM
#step2
aws cloudformation update-stack --stack-name Consegna-AMS-Zendesk-Integration-s2 --template-body file://infrastructure\step2_stack.yaml --capabilities CAPABILITY_NAMED_IAM --parameters ParameterKey=ZendeskAPIKey,ParameterValue=5b5GYZD5DrDr3PljmTWt3W3NVtRzqznUgNsCbtp6 ParameterKey=RequesterEmail,ParameterValue=mfesupport@consegna.cloud


mfesupport@consegna.cloud

