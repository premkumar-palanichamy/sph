resource "aws_ecs_cluster" "url_monitor_cluster" {
  name = var.cluster_name
}

resource "aws_ecs_service" "url_monitor_service" {
  name            = var.service_name
  cluster         = aws_ecs_cluster.url_monitor_cluster.id
  task_definition = aws_ecs_task_definition.url_monitor_task.arn
  desired_count   = var.desired_count

  network_configuration {
    subnets         = var.subnet_ids
    security_groups = ["${aws_security_group.monitoring_app_sg.id}"]
    assign_public_ip = true
  }

  load_balancer {
    target_group_arn = aws_lb_target_group.url_monitor_target_group.arn
    container_name   = var.container_name
    container_port   = var.container_port
  }

  depends_on = [aws_lb_target_group_attachment.url_monitor_attachment]
}
