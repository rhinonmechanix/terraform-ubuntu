variable "vpc_cidr" {
  type = string
  description = "VPC Ip range"
  default = "10.0.0.0/16"
}

variable "public_subnet" {
    type = map(number)
    description = "VPC Ip range"
  default = {
    us-east-1      = 1
    us-west-1      = 2
    us-west-2      = 3
    eu-central-1   = 4
    ap-northeast-1 = 5
  }
}