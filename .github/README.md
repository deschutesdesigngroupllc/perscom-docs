<p align="center"><img src="../art/header.png" alt="PERSCOM Documentation"></p>

<div align="center">

# PERSCOM Documentation

The official documentation for PERSCOM, built with [Mintlify](https://mintlify.com).

[![Documentation](https://img.shields.io/badge/docs-perscom.io-blue)](https://docs.perscom.io)
[![License](https://img.shields.io/badge/license-MIT-green)](../LICENSE)

</div>

## About PERSCOM

[PERSCOM](https://perscom.io) is a powerful personnel management platform built for military simulation units, emergency services, and public safety organizations. It provides tools for managing personnel records, assignments, awards, qualifications, and more.

## Documentation Structure

| Directory | Description |
|-----------|-------------|
| `docs/` | General product documentation |
| `guides/` | Step-by-step user guides |
| `integrations/` | API, SDKs, webhooks, and third-party integrations |
| `api-reference/` | Complete API endpoint documentation |

## Local Development

### Prerequisites

- [Node.js](https://nodejs.org/) (v18 or higher)
- npm or yarn

### Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/DeschutesDesignGroupLLC/perscom-docs.git
    cd perscom-docs
    ```

2. Install the Mintlify CLI:
    ```bash
    npm i -g mintlify
    ```

3. Install dependencies:
    ```bash
    npm install
    ```

4. Start the development server:
    ```bash
    mintlify dev
    ```

5. Open [http://localhost:3000](http://localhost:3000) in your browser.

### Formatting

Run Prettier to format files before committing:

```bash
npm run format
```

## Contributing

We welcome contributions to improve the documentation. Please see [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

### Quick Contribution Guide

1. Fork the repository
2. Create a feature branch (`git checkout -b improve-docs`)
3. Make your changes
4. Run `npm run format` to format your changes
5. Commit your changes (`git commit -m "Improve X documentation"`)
6. Push to the branch (`git push origin improve-docs`)
7. Open a Pull Request

## Resources

- [PERSCOM Website](https://perscom.io)
- [Live Documentation](https://docs.perscom.io)
- [API Reference](https://docs.perscom.io/api-reference/introduction)
- [Community Slack](https://perscom.io/slack)

## License

This documentation is open source and available under the [MIT License](../LICENSE).