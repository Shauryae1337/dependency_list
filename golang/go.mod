# Module declaration
module example.com/mymodule

# Go version requirement
go 1.21

# Direct dependencies with mixed versions
require (
    # Latest stable version of a major dependency
    github.com/prometheus/client_golang v0.14.0
    
    # Older version of a dependency for compatibility
    github.com/hashicorp/hcl v1.0.0
    
    # Newer version of a dependency with breaking changes
    golang.org/x/crypto v0.10.0
    
    # Development version from main branch
    github.com/grpc/grpc-go v1.59.0-rc1
)

# Replace directive for a forked dependency
replace (
    github.com/hashicorp/hcl => github.com/mycompany/hcl v1.0.0-custom
)

# Exclude problematic versions
exclude (
    golang.org/x/crypto v0.8.0  # Known security vulnerability
    github.com/prometheus/client_golang v0.13.0  # Broken API
)
