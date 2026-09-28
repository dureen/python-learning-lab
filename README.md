# Python Learning Lab

Hands-on Python tutorial repository divided into **Beginner**, **Intermediate**, and **Advanced** levels.

Each lesson contains:
- Clear explanation
- Runnable example code
- Practice exercises
- Corresponding unit tests (in `/tests`)

## Structure

```
python-learning-lab/
├── beginner/          # Fundamentals
├── intermediate/      # Intermediate concepts
├── advanced/          # Advanced topics
├── tests/             # Unit tests for each level
└── examples/          # Small complete projects
```

## How to use

1. Clone the repository
2. (Recommended) Create a virtual environment
3. Go into any lesson folder and run the Python files
4. Run tests with `pytest`

```bash
git clone https://github.com/dureen/python-learning-lab.git
cd python-learning-lab
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest
```

## Requirements

- Python 3.10+
- pytest (for running tests)

## License

MIT License – see [LICENSE](LICENSE)
