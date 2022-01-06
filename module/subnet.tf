resource "aws_subnet" "main" {
  
  vpc_id     = aws_vpc.main.id
  count = length(var.public_subnet)
  cidr_block  = var.public_subnet[count.index]

  tags = {
    Name = "Main"
  }
}