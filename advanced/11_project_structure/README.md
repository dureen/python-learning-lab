# 11 – Recommended Project Structure

```
my_project/
├── src/
│   └── my_package/
│       ├── __init__.py
│       ├── core.py
│       └── utils.py
├── tests/
│   ├── __init__.py
│   └── test_core.py
├── pyproject.toml
├── README.md
└── .gitignore
```

Tips:
- Prefer `src` layout for packages
- Use `pyproject.toml` for modern packaging
- Keep tests separate from source
- Add type hints + `mypy` / `ruff` for quality
