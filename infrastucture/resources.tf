
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
