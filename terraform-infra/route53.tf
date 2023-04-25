resource "tls_private_key" "self_signed_key" {
  algorithm   = "RSA"
  rsa_bits    = 2048
}

resource "tls_self_signed_cert" "self_signed_cert" {
  key_algorithm   = "RSA"
  private_key_pem = tls_private_key.self_signed_key.private_key_pem

  subject {
    common_name  = "ladvik.com"
    organization = "My Org"
    country      = "US"
  }

  validity_period_hours = 8760 # 1 year
}

resource "aws_lb_listener" "url_monitor_listener_https" {
  load_balancer_arn = aws_alb.application_load_balancer.arn
  port              = 443
  protocol          = "HTTPS"
  ssl_policy        = "ELBSecurityPolicy-2016-08"

  certificate_arn = tls_self_signed_cert.self_signed_cert.cert_pem

  default_action {
    target_group_arn = aws_lb_target_group.url_monitor_target_group.arn
    type             = "forward"
  }
}

resource "aws_route53_zone" "monitor_route" {
  name = "ladvik.com."
}

resource "aws_route53_record" "monitor_cname" {
  zone_id = aws_route53_zone.monitor_route.zone_id
  name    = "app.ladvik.com."
  type    = "CNAME"
  ttl     = "300"
  records = ["${aws_alb.application_load_balancer.dns_name}"]
}
