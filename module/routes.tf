resource "aws_route_table" "example" {
  vpc_id = aws_vpc.main.id
}

resource "aws_route_table_association" "subnet-route-associations" {
  count = length(var.public_subnet)
  subnet_id = aws_subnet.main[count.index].id
  route_table_id = aws_route_table.example.id
}