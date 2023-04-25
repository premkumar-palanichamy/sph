resource "aws_security_group" "monitoring_app_sg" {
  name_prefix = "monitoring-app-sg-"

  ingress {
    from_port = 0
    to_port   = 80
    protocol  = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port = var.container_port
    to_port   = var.container_port
    protocol  = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
        from_port   = 0
        to_port     = 0
        protocol    = "-1"
        cidr_blocks = ["0.0.0.0/0"]
    }
}
