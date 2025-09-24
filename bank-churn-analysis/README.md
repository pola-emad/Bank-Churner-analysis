# Customer Churn Analysis Project

This project aims to analyze customer churn for a bank using various data analysis techniques. The analysis includes data cleaning, exploratory data analysis (EDA), and statistical analysis to derive insights and recommendations for improving customer retention.

## Project Structure

- **data/**: Contains raw and processed data files.
  - **raw/**: Contains the original dataset (`BankChurners.csv`).
  - **processed/**: Contains the cleaned dataset (`cleaned_data.csv`).

- **notebooks/**: Jupyter notebooks for different stages of analysis.
  - `01_data_cleaning.ipynb`: Data cleaning process, including handling missing values and data type transformations.
  - `02_exploratory_analysis.ipynb`: Exploratory data analysis with visualizations and insights.
  - `03_statistical_analysis.ipynb`: Statistical analysis including hypothesis testing.

- **src/**: Source code for data processing and visualization.
  - **data_processing/**: Functions for cleaning and processing data.
  - **visualization/**: Functions for creating visualizations.
  - **utils/**: Utility functions for data loading and saving.

- **streamlit/**: Streamlit web application files.
  - `app.py`: Main application file.
  - **pages/**: Contains different pages for the Streamlit app.
    - `overview.py`: Overview page with key performance indicators.
    - `detailed_analysis.py`: Detailed analysis page for in-depth exploration.

- **docs/**: Documentation files.
  - `presentation.pptx`: Slide deck for presenting findings.
  - `video_script.md`: Outline for a video summarizing the project.

- **requirements.txt**: List of dependencies required to run the project.

- **.gitignore**: Specifies files and directories to be ignored by version control.

## Getting Started

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```
   cd bank-churn-analysis
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Open Jupyter Notebook and run the analysis notebooks in order.

5. To run the Streamlit app, execute:
   ```
   streamlit run streamlit/app.py
   ```

## License

This project is licensed under the MIT License.