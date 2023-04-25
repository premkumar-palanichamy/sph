data "aws_vpc" "vpc" {
  tags {
    Name = "${var.vpc_name}"
  }
}

/* data "aws_subnet_ids" "subnet" {
  vpc_id = "${data.aws_vpc.selected.id}"
  tags {
    Tier = "public"
  }
} */