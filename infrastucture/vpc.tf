# vpc
resource "aws_vpc" "main" {
  cidr_block = var.cidr_block_vpc
  tags = {
    name = var.tags
  }
}