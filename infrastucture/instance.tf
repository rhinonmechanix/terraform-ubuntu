resource "aws_instance" "ec2_aws" {
  ami           = "${data.aws_ami.ubuntu.id}"
  instance_type = var.instance_type
  key_name      = var.key_name

  tags = {
    Name = "Terraform ec2"
  }
}