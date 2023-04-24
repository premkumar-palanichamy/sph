/* resource "aws_instance" "monitoring_app" {
  ami           = var.ami
  instance_type = "t2.micro"

  key_name = "your-ec2-key-pair"

  vpc_security_group_ids = [aws_security_group.monitoring_app.id]

  user_data = <<-EOF
              #!/bin/bash
              yum update -y
              yum install -y docker
              service docker start
              $(aws ecr get-login --no-include-email --region us-east-1)
              docker run -d -p 8080:8080 ${aws_ecr_repository.monitoring_app.repository_url}
              EOF

  tags = {
    Name = "monitoring-app-instance"
  }
} */
