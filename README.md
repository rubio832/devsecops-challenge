# DevSecOps Challenge (Cost-Optimized Version)

This project implements a simple serverless web application with a CI/CD pipeline that includes DevSecOps practices, optimized for cost.

## Architecture

[Include an architecture diagram here]

## How to run

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Install Serverless Framework: `npm install -g serverless`
4. Deploy: `serverless deploy`

## CI/CD Pipeline

The pipeline includes the following stages:
- SAST with Bandit
- SCA with OWASP Dependency-Check
- Deployment to AWS Lambda
- Sending findings to AWS Security Hub

## ASPM Platform

We use AWS Security Hub as our ASPM platform. Security findings from our pipeline are sent directly to Security Hub for centralized management and analysis.

## Vulnerability Prioritization Strategy

We prioritize vulnerabilities based on:
1. CVSS Score
2. Exposure of the affected component
3. Criticality of the affected data

## Cost Optimization

This implementation uses serverless technologies to minimize costs:
- AWS Lambda for compute
- API Gateway for HTTP routing
- DynamoDB for database (if needed)
- AWS Security Hub for vulnerability management

There are no constantly running servers, which significantly reduces costs. You only pay for actual usage.