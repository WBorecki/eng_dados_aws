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
  default = "subnet-0c4a20c0deeac1cea"
}

variable "vpc_id" {
  default = "vpc-07aad847cd0f6a1b5"  
}