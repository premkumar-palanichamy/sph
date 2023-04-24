output "url_monitor_url" {
  value = aws_ecs_service.url_monitor_service.load_balancers[0].dns_name
}