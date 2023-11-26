provider "aws" {
    region = var.aws_region
}

# Centralizar o arquivo de cotrole de estado do terraform
terraform {
  backend "s3" {
    bucket = "terraform-state-sbi"
    key = "state/sbi/edc/mod1/terraform.tfstate"
    region = var.aws_region
    
  }
}