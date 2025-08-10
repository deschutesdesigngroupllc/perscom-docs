# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the PERSCOM documentation site built with Mintlify. PERSCOM is a comprehensive personnel management suite for police, fire, EMS, military, and public safety agencies. The documentation covers the product introduction, guides, integrations, and comprehensive API reference.

## Development Commands

### Code Formatting
- `npm run format` - Format JavaScript files using Prettier with the project's configuration

## Project Structure

### Documentation Organization
- `docs/` - General product documentation (introduction, getting started, pricing, etc.)
- `guides/` - Step-by-step guides for users
- `integrations/` - Documentation for API, SDKs, webhooks, and third-party integrations
- `api-reference/` - Comprehensive API documentation with all endpoints organized by resource type

### Content Architecture
- `mint.json` - Mintlify configuration file defining site navigation, theming, and structure
- `api-reference/openapi.json` - OpenAPI specification for the PERSCOM API
- All documentation files use `.mdx` format (Markdown with JSX components)

### API Documentation Structure
The API reference is extensively organized with endpoints grouped by resource:
- Core resources: Users, Groups, Units, Positions, Ranks, Awards, etc.
- Record types: Assignment, Award, Combat, Qualification, Rank, Service, Training records
- Relationship endpoints: User-specific operations for each resource type
- Each endpoint group includes standard CRUD operations plus batch operations

### Key Features
- Supports Bearer token authentication for API endpoints
- Includes Postman collection integration
- Features comprehensive navigation with icons and nested groupings
- Configured for light/dark theme support
- Includes feedback mechanisms (thumbs rating, suggest edits)

### Development Notes
- Uses Prettier for code formatting with specific configuration in `.prettierrc`
- No build process required - Mintlify handles deployment
- Content is organized following Mintlify's conventions with frontmatter metadata

## OpenAPI Specification Guidelines

### Endpoint Organization
- **CRITICAL**: All endpoints in `api-reference/openapi.json` must be sorted alphabetically by path
- When adding new endpoints, ensure they are inserted in the correct alphabetical position
- Maintain consistent alphabetical ordering to ensure predictable documentation generation
- Example correct ordering:
  ```
  /{version}/announcements
  /{version}/categories/{category}/awards
  /{version}/categories/{category}/awards/attach
  /{version}/categories/{category}/awards/batch
  /{version}/groups/{group}/units
  /{version}/groups/{group}/units/attach
  /{version}/groups/{group}/units/batch
  ```

### Automated Path Sorting
- Use `python scripts/sort_openapi_paths.py` to automatically sort all endpoint paths alphabetically
- This script preserves all endpoint definitions while reordering paths for consistency
- Run after adding new endpoints to maintain proper organization
- The script accepts an optional path argument or defaults to `api-reference/openapi.json`