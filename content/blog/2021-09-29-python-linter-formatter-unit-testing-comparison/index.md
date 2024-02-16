---
Title: Python Linters, Formatters, and Unit Testing Comparison
Date: 2021-09-29T16:20:00
# Categories: Python
Tags: [python, comparison]
Slug: 2021-09-29-python-linter-formatter-unit-testing-comparison
Summary: Python linters, formatters, and unit testing comparison
---

## Linters

|                    | Flake8             | Pylint             |
| ------------------ | ------------------ | ------------------ |
| Installation       | pip install flake8 | pip install pylint |
| Speed              | Fast               | Slow               |
| Strictness         | Not so strict      | Strict             |
| Configurable       | Little             | Highly             |
| Recommend Scenario | Side-project       | CI                 |

<!-- Note: pycodestyle = pep8, pydocstyle = pep257 -->

## Formatters

|              | autopep8             | black             | yapf             |
| ------------ | -------------------- | ----------------- | ---------------- |
| Installation | pip install autopep8 | pip install black | pip install yapf |
| Configurable | Little               | Almost none       | Highly           |
| Note         | Follow PEP8          | Superset of PEP8  | -                |

## Unit Testing

|                   | pytest             | unittest |
| ----------------- | ------------------ | -------- |
| Installation      | pip install pytest | Built-in |
| Barriers to entry | Low                | High     |
| Plugins           | Lots               | -        |
| Compatible        | unittest           | -        |

## Reference

- https://www.kevinpeters.net/auto-formatters-for-python
- https://realpython.com/pytest-python-testing/
