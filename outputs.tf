output "instance_id" {
  description = "ID of the EC2 instance"
  value       = aws_instance.ec2_aws.id
}

output "loops" {
  value = aws_iam_user.example
}