variable "resource_group_name" {
  description = "Name of the resource group"
  type        = string
}

variable "location" {
  description = "Azure region for resources"
  type        = string
}

variable "vnet_address_space" {
  description = "Address space for VNet"
  type        = list(string)
}

variable "subnet_address_prefixes" {
  description = "Address prefixes for subnet"
  type        = list(string)
}

variable "tags" {
  description = "Tags to apply to resources"
  type        = map(string)
  default     = {}
}
