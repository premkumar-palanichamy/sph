resource "aws_alb" "application_load_balancer" {
  name               = "monitoring-app-lb"
  load_balancer_type = "application"
  subnets = [ 
    "${aws_default_subnet.default_subnet_a.id}",
    "${aws_default_subnet.default_subnet_b.id}"
  ]
  
  security_groups = ["${aws_security_group.monitoring_app_sg.id}"]
}

resource "aws_lb_target_group" "url_monitor_target_group" {
  name     = var.target_group_name
  port     = var.container_port
  protocol = "HTTP"
  vpc_id   = data.aws_vpc.vpc
}

resource "aws_lb_listener" "url_monitor_listener" {
  load_balancer_arn = "${aws_alb.application_load_balancer.arn}"
  port              = 8080
  protocol          = "HTTP"

  default_action {
    target_group_arn = aws_lb_target_group.url_monitor_target_group.arn
    type             = "forward"
  }
}

resource "aws_lb_target_group_attachment" "url_monitor_attachment" {
  target_group_arn = aws_lb_target_group.url_monitor_target_group.arn
  target_id        = aws_ecs_service.url_monitor_service.id
  port             = var.container_port
}


