<p align="center"><img src="../art/header.png" alt="Logo"></p>

<div align="center">

# The Official PERSCOM Documentation

A Mintlify website used for displaying the official PERSCOM documentation.

[Documentation](https://docs.perscom.io) • [API Reference](https://docs.perscom.io/api-reference) • [Live Demo](https://demo.perscom.io)

</div>

## About PERSCOM

PERSCOM is a comprehensive personnel management suite designed for police, fire, EMS, military, and public safety agencies. This repository contains the official documentation covering product features, integration guides, and complete API reference.

## Repository Structure

```
├── docs/                    # General product documentation
├── guides/                  # Step-by-step user guides  
├── integrations/           # API, SDK, and third-party integration docs
├── api-reference/          # Complete API documentation
│   ├── endpoints/          # Organized by resource type
│   └── openapi.json       # OpenAPI specification
├── art/                   # Images and assets
└── mint.json             # Mintlify configuration
```

## Development

### Prerequisites
- Node.js (for formatting tools)
- npm

### Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-org/perscom-docs.git
   cd perscom-docs
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Format code**
   ```bash
   npm run format
   ```

### Documentation Format

- All documentation files use `.mdx` format (Markdown with JSX components)
- Configuration is managed through `mint.json`
- API documentation is auto-generated from the OpenAPI specification

### Key Features

- **Comprehensive API Reference**: 100+ endpoints organized by resource type
- **Interactive Examples**: Code samples in PHP, JavaScript, and Python
- **Postman Integration**: Official collection for API testing
- **Multi-format Support**: CRUD operations plus batch processing
- **Authentication**: Bearer token-based API authentication

### Content Organization

The API reference includes comprehensive coverage of:
- **Core Resources**: Users, Groups, Units, Positions, Ranks, Awards
- **Record Management**: Assignment, Award, Combat, Qualification, Service, Training records
- **Relationship Operations**: User-specific endpoints for all resources
- **Batch Operations**: Efficient bulk data processing

### Contributing

When editing documentation:
- Follow the existing MDX format and structure
- Run `npm run format` before committing
- Ensure all links and references are accurate
- Test any code examples provided

### Developer Scripts

- **OpenAPI Path Sorting**: `python scripts/sort_openapi_paths.py`
  - Automatically sorts all endpoint paths in the OpenAPI specification alphabetically
  - Maintains consistent organization for better documentation navigation
  - Run after adding new API endpoints to ensure proper ordering

### Deployment

This documentation is deployed automatically via Mintlify. No manual build process is required.