variable "vpc_cidr" {
    type = string
    default = "10.0.0.0/16"
}

variable "subnet_cidr" {
    type = string
    default = "10.0.101.0/24"
}

variable "solution_stack_name" {
    type = string
    default = "64bit Amazon Linux 2015.03 v2.0.3 running Go 1.4"
}

variable "app_name" {
    type = string
    default = "MyFirstApp"
}

variable "description" {
    type = string
    description = "EB application"
}