# pre-commit-hooks

Pre-commit hooks to use with https://pre-commit.com/

## Usage

```yaml
---
fail_fast: false
repos:
  - repo: https://github.com/toddnguyen47/pre-commit-hooks
    rev: v1.5.0
    hooks:
      - id: convert-beginning-tabs
        args: ["--tab-size", "2"] # defaults to 4 with no args
      - id: convert-beginning-spaces
        # --tab-size defaults to 4 with no args
        # --comment-char is empty string ("") by default
        args: ["--tab-size", "2", "--comment-char", "*"]
      - id: convert-text-to-html
        args: [
            "--textfiles",
            "file1.txt, file2.txt", # comma-separated list of text files
            "--margin",
            "10" # OPTIONAL: float value to use as margin ems. Defaults to 10.
        ]
      - id: minify-json
      - id: prettify-json
        args: ["--indent", "2"] # defaults to indenting with 2 spaces
```

## Note when Adding More Hooks

Change these files:
1. `.pre-commit-hooks.yaml`
2. `setup.cfg`
3. `README.md`
