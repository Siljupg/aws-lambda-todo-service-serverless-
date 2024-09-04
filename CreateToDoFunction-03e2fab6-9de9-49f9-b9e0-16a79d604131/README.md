# Simple To-Do List API

## Overview
This project is a simple serverless To-Do List API built using AWS Lambda, API Gateway, and DynamoDB.

## Setup Instructions
1. **Create DynamoDB Table**
   - Name: `ToDoTable`
   - Primary Key: `id` (string)

2. **Deploy Lambda Functions**
   - Use the AWS Console to create and deploy functions for creating, reading, updating, and deleting to-do items.

3. **Create API Gateway**
   - Set up resources and methods as described.
   - Deploy the API and get the invoke URL.

## Usage
- **Create To-Do**: `POST /todos`
- **Read To-Do**: `GET /todos/{id}`
- **Update To-Do**: `PUT /todos/{id}`
- **Delete To-Do**: `DELETE /todos/{id}`

## Example
```bash
curl -X POST -d '{"description":"Buy milk"}' https://<api-id>.execute-api.<region>.amazonaws.com/dev/todos


