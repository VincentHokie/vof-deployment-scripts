provider "google" {
  credentials = "${file("${var.credential_file}")}"
  project = "${var.project_id}"
  region = "${var.region}"
}

terraform {
  backend "gcs" {
    bucket = "vof-tfstate-daniel"
    project = "vof-testbed-2"
    credentials = "service-account.json"
  }
}

data "terraform_remote_state" "vof" {
  backend = "gcs"
  config {
    bucket = "vof-tstate-daniel"
    path = "${var.state_path}"
    project = "vof-testbed-2"
    credentials = "service-account.json"
  }
}
