variable "vpc_cidr" {
  type = string
  description = "VPC Ip range"
  default = "10.0.0.0/16"
}

variable "public_subnet" {
    type = list(string)
    description = "VPC Ip range"
    default = ["10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24"]
}