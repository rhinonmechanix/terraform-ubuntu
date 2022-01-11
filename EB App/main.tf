resource "aws_elastic_beanstalk_application" "tftest" {
  name        = var.app_name
  description = var.description
}

resource "aws_elastic_beanstalk_environment" "tfenvtest" {
  name                = var.app_name
  application         = aws_elastic_beanstalk_application.tftest.name
  solution_stack_name = var.solution_stack_name

  setting {
    namespace = "aws:ec2:vpc"
    name      = "VPCId"
    value     = var.vpc_cidr
  }

  setting {
    namespace = "aws:ec2:vpc"
    name      = "Subnets"
    value     = var.subnet_cidr
  }
}