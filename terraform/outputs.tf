output "resource_group_name" {
  description = "Name of the resource group"
  value       = azurerm_resource_group.main.name
}

output "vm_public_ip" {
  description = "Public IP address of the VM"
  value       = module.network.public_ip_address
}

output "vm_ssh_connection" {
  description = "SSH connection string for the VM"
  value       = "ssh ${var.admin_username}@${module.network.public_ip_address}"
}

output "acr_login_server" {
  description = "Login server URL for ACR"
  value       = azurerm_container_registry.acr.login_server
}

output "kubernetes_access_urls" {
  description = "Access URLs for deployed services"
  value = {
    ingress_http    = "http://${module.network.public_ip_address}:30080"
    ingress_https   = "https://${module.network.public_ip_address}:30443"
    prometheus      = "http://${module.network.public_ip_address}:30090"
    grafana         = "http://${module.network.public_ip_address}:30091"
    alertmanager    = "http://${module.network.public_ip_address}:30092"
  }
}
