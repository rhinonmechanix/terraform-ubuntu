resource "aws_subnet" "main" {
  
  for_each = var.public_subnet
  
  vpc_id     = aws_vpc.main.id

  cidr_block        = cidrsubnet(aws_vpc.main.cidr_block, 4, each.value)

  tags = {
    Name = "Main"
  }
}