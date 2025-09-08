variable "resource_group_name" {
  description = "Name of the resource group"
  type        = string
  default     = "rg-fastapi-devops"
}

variable "location" {
  description = "Azure region for resources"
  type        = string
  default     = "East US"
}

variable "vnet_address_space" {
  description = "Address space for VNet"
  type        = list(string)
  default     = ["10.0.0.0/16"]
}

variable "subnet_address_prefixes" {
  description = "Address prefixes for subnet"
  type        = list(string)
  default     = ["10.0.1.0/24"]
}

variable "vm_size" {
  description = "Size of the virtual machine"
  type        = string
  default     = "Standard_B2s"
}

variable "admin_username" {
  description = "Admin username for the VM"
  type        = string
  default     = "azureuser"
}

variable "ssh_public_key" {
  description = "SSH public key for VM access"
  type        = string
}

variable "acr_name" {
  description = "Name of the Azure Container Registry"
  type        = string
  default     = "acrfastapidevops"
}

variable "tags" {
  description = "Tags to apply to resources"
  type        = map(string)
  default = {
    Environment = "Development"
    Project     = "FastAPI-DevOps"
    ManagedBy   = "Terraform"
  }
}
