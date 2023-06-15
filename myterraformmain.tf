provider "google" {
  credentials = "D:\\Papa\\MyPrograms\\my-key.json"
  project     = "learned-vault-387908"
  region      = "us-central1"
  zone        = "us-central1-a"
}

resource "google_container_cluster" "my-web-cluster" {
  name               = "my-web-cluster"
  location           = "us-central1"
  initial_node_count = 1
}

resource "google_container_node_pool" "my-web-nodepool" {
  name    = "my-web-nodepool"
  cluster = google_container_cluster.my-web-cluster.id
  node_config {
    machine_type = "e2-standard-1"
    oauth_scopes = ["https://www.googleapis.com/auth/logging.write"]
  }

  provisioner "local-exec" {
    command = "kubectl apply -f deployment.yaml"
  }
}