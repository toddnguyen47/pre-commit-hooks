# pre-commit-hooks

Pre-commit hooks to use with https://pre-commit.com/

## Usage

```yaml
---
fail_fast: false
repos:
  - repo: https://github.com/toddnguyen47/pre-commit-hooks
    rev: v1.1.0
    hooks:
      - id: convert-beginning-tabs
        args: ["--whitespaces-count", "2"] # defaults to 4 with no args
      - id: convert-text-to-html
        args: ["--textfiles", "file1.txt, file2.txt"] # comma-separated list of text files
      - id: minify-json
```
