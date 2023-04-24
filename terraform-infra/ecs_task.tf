resource "aws_ecs_task_definition" "url_monitor_task" {
  family                   = "url-monitor-task"
  execution_role_arn       = aws_iam_role.ecs_task_execution_role.arn
  container_definitions    = file("${path.module}/ecs/container-definition.json")
  requires_compatibilities = ["FARGATE"]
  network_mode             = "awsvpc"
  cpu                      = 256
  memory                   = 512
}