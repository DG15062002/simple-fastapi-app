terraform {
  required_version = ">= 1.0"
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
    random = {
      source  = "hashicorp/random"
      version = "~> 3.1"
    }
  }
}

provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "main" {
  name     = var.resource_group_name
  location = var.location

  tags = var.tags
}

module "network" {
  source = "./modules/network"

  resource_group_name     = azurerm_resource_group.main.name
  location               = azurerm_resource_group.main.location
  vnet_address_space     = var.vnet_address_space
  subnet_address_prefixes = var.subnet_address_prefixes
  
  tags = var.tags
}

module "vm" {
  source = "./modules/vm"

  resource_group_name = azurerm_resource_group.main.name
  location           = azurerm_resource_group.main.location
  subnet_id          = module.network.subnet_id
  public_ip_id       = module.network.public_ip_id
  vm_size           = var.vm_size
  admin_username    = var.admin_username
  ssh_public_key    = var.ssh_public_key
  
  tags = var.tags
}

resource "azurerm_container_registry" "acr" {
  name                = var.acr_name
  resource_group_name = azurerm_resource_group.main.name
  location           = azurerm_resource_group.main.location
  sku                = "Basic"
  admin_enabled      = true

  tags = var.tags
}
