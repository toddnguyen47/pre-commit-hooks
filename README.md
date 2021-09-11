# pre-commit-hooks

Pre-commit hooks to use with https://pre-commit.com/

## Usage

```yaml
- repo: https://github.com/toddnguyen47/pre-commit-hooks
  rev: v0.0.6
  hooks:
    - id: convert-beginning-tabs
      args: ["--whitespaces-count", "2"] # defaults to 4 with no args
```
