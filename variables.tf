variable "userNames" {
  description = "names"
  type = set(string)
  default = ["Todd", "James", "Alice", "Dottie"]
}

variable "cidr_block_vpc" {
  description = "cidr block"
  type = string
  default = "10.0.0.0/16"
}

variable "cidr_block" {
  description = "cidr block"
  type = string
  default = "10.0.0.0/24"
}

variable "tags" {
  description = "tag names"
  type = string
  default = "example"
}

variable "instance_type" {
  description = "type of instance"
  type = string
  default = "t2.micro"
}

variable "key_name" {
  description = "SSH key pair"
  type = string
  default = "MyKeyPair"
}

variable "most_recent" {
  description = "Finding the latest os"
  type = bool
  default = true
}