# Customer Churn Analysis Project

This repository analyzes bank customer churn using data cleaning, exploratory analysis, visualizations, and statistical checks. Processed artifacts are stored as pickled objects for reproducible pipelines and fast loading.

## Project structure (updated)

- data/
  - raw/ : original dataset (BankChurners.csv)
  - processed/ : pickled processed datasets (e.g., cleaned_data.pkl)
- notebooks/
  - 01_data_cleaning.ipynb
  - 02_exploratory_analysis.ipynb
  - 03_statistical_analysis.ipynb
- src/
  - data_processing/ : data cleaning and transformation functions
  - visualization/ : plotting and visualization utilities
  - utils/ : helpers for loading/saving (pickle helpers, config)
- streamlit/
  - app.py : main Streamlit application
  - pages/
    - overview.py
    - detailed_analysis.py
- requirements.txt
- .gitignore
- LICENSE

Notes:

- Presentation slides and video scripts have been removed from the public repo.
- Processed datasets are saved with pickle (.pkl) under data/processed for speed and reproducibility.

## Getting started

1. Clone the repository:
   git clone <repository-url>

2. Enter the project directory:
   cd "d:\ITI\python visualization\banck churners project\bank-churn-analysis"

3. Install dependencies:
   pip install -r requirements.txt

4. Run notebooks (use Jupyter or JupyterLab) in order:

   - 01_data_cleaning.ipynb
   - 02_exploratory_analysis.ipynb
   - 03_statistical_analysis.ipynb

5. Run the Streamlit app:
   streamlit run streamlit/app.py

## Data handling

- Use the utilities in src/utils to load raw CSV and save processed DataFrame as pickle:
  - saved files: data/processed/cleaned_data.pkl
- Pickle is used for processed artifacts to preserve dtypes and speed up loading.

## License

This project is licensed under the MIT License.

```// filepath: d:\ITI\python visualization\banck churners project\bank-churn-analysis\README.md
// ...existing code...
# Customer Churn Analysis Project

This repository analyzes bank customer churn using data cleaning, exploratory analysis, visualizations, and statistical checks. Processed artifacts are stored as pickled objects for reproducible pipelines and fast loading.

## Project structure (updated)

- data/
  - raw/ : original dataset (BankChurners.csv)
  - processed/ : pickled processed datasets (e.g., cleaned_data.pkl)
- notebooks/
  - 01_data_cleaning.ipynb
  - 02_exploratory_analysis.ipynb
  - 03_statistical_analysis.ipynb
- src/
  - data_processing/ : data cleaning and transformation functions
  - visualization/ : plotting and visualization utilities
  - utils/ : helpers for loading/saving (pickle helpers, config)
- streamlit/
  - app.py : main Streamlit application
  - pages/
    - overview.py
    - detailed_analysis.py
- requirements.txt
- .gitignore
- LICENSE

Notes:
- Presentation slides and video scripts have been removed from the public repo.
- Processed datasets are saved with pickle (.pkl) under data/processed for speed and reproducibility.

## Getting started

1. Clone the repository:
   git clone <repository-url>

2. Enter the project directory:
   cd "d:\ITI\python visualization\banck churners project\bank-churn-analysis"

3. Install dependencies:
   pip install -r requirements.txt

4. Run notebooks (use Jupyter or JupyterLab) in order:
   - 01_data_cleaning.ipynb
   - 02_exploratory_analysis.ipynb
   - 03_statistical_analysis.ipynb

5. Run the Streamlit app:
   streamlit run streamlit/app.py

## Data handling

- Use the utilities in src/utils to load raw CSV and save processed DataFrame as pickle:
  - saved files: data/processed/cleaned_data.pkl
- Pickle is used for processed artifacts to preserve dtypes and speed up loading.

## License

This project is licensed under the MIT License.
```
