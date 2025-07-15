# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### Added
- Markdown logging of assistant responses
- Memory recall using assistant.handle_request("Recall my preferences", "general")
- `.env` protection with secure `.gitignore` configuration
- Custom model selector with multiple providers (OpenRouter, Toolhouse)

### Changed
- Replaced `Toolhouse.login()` with `Toolhouse()` and `set_api_key()`, `set_provider()`
- Upgraded helper functions and logging

### Security
- Added pre-commit hook to block `.env` from being committed
