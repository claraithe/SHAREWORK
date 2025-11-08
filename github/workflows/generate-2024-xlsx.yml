name: Generate 2024 Excel files

on:
  workflow_dispatch:
  push:
    paths:
      - 'generate_2024_xlsx.py'
      - '2024_DATA/**'

jobs:
  generate:
    name: Generate and commit 2024 Excel files
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install pandas openpyxl pdfplumber

      - name: Run generator script
        run: |
          python generate_2024_xlsx.py

      - name: Commit generated files
        uses: EndBug/add-and-commit@v9
        with:
          author_name: 'github-actions[bot]'
          author_email: '41898282+github-actions[bot]@users.noreply.github.com'
          message: 'chore: generate 2024 Excel files'
          add: '2024_OUTPUT/**'
          force: true
