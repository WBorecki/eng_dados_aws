variable "base_bucket_name" {
  default = "datalake-igti-tf"
}

variable "ambiente" {
  default = "producao"
}

variable "numero_conta" {
  default = "674055950479"
}

variable "aws_region" {
  default = "us-east-2"
}

variable "key_pair_name" {
  default = "sbi_chave_de_acesso"
}

variable "airflow_subnet_id" {
  default = "subnet-0623ec4aede470cc0"
}

variable "vpc_id" {
  default = "vpc-01c81daaa1d70a519"  
}