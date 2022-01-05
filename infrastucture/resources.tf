# vpc
resource "aws_vpc" "main" {
  cidr_block = var.cidr_block_vpc
  tags = {
    name = var.tags
  }
}

# subnet
resource "aws_subnet" "main" {
  vpc_id     = aws_vpc.main.id
  cidr_block = var.cidr_block

  tags = {
    Name = var.tags
  }
}

# route table
resource "aws_route_table" "example" {
  vpc_id = aws_vpc.main.id

  route {
    cidr_block = var.cidr_block
  }

  tags = {
    Name = var.tags
  }
}

resource "aws_route_table_association" "a" {
  subnet_id      = aws_subnet.main.id
  route_table_id = aws_route_table.example.id
}

# Aws instance
resource "aws_instance" "ec2_aws" {
  ami           = "${data.aws_ami.ubuntu.id}"
  instance_type = var.instance_type
  key_name      = var.key_name

  tags = {
    Name = "Terraform ec2"
  }
}

resource "aws_iam_user" "example" {
  for_each = var.userNames
  name     = each.value
}

data "aws_ami" "ubuntu" {
  most_recent = var.most_recent

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  owners = ["099720109477"] # Canonical
}
