# Security Policy

## Reporting a vulnerability

Please report security issues in this SDK or the PropRaven API privately to
**support@propraven.com** with the subject "Security". Do not open a public issue. We will
acknowledge your report and keep you updated while we investigate.

## Handling API keys

PropRaven API keys (`pz_...`) and webhook secrets (`whsec_...`) are secrets. Use this SDK only on
servers you control. Never embed keys in browser bundles, mobile apps or public repositories.
