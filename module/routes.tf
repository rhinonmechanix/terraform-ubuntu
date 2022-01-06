resource "aws_route_table" "example" {
  vpc_id = aws_vpc.main.id
}

resource "aws_route_table_association" "subnet-route-associations" {
  for_each = aws_subnet.main
  subnet_id = aws_subnet.main[each.key].id
  route_table_id = aws_route_table.example.id
}