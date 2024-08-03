terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "5.39.1"
    }
  }
}

provider "google" {
  credentials = file(var.credentials)
  project     = var.project_name
  region      = var.bucket_name
}

resource "google_storage_bucket" "auto-expire" {
  name          =  var.bucket_name
  location      = var.location
  force_destroy = true
    
  storage_class = "STANDARD"
  uniform_bucket_level_access = true

  public_access_prevention = "enforced"
}

resource "google_bigquery_dataset" "default" {
  dataset_id = var.bq_dataset_name
  location   = var.location
}