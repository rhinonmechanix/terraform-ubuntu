terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "3.70.0"
    }
  }
}

provider "aws" {
  #access_key = "ACCESS_KEY"
  #secret_key = "SECRET_KEY"
  region = "us-east-2"
}