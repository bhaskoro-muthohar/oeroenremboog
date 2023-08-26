[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

# [Oeroenremboog](https://oeroenremboog-yrln4wnriq-et.a.run.app/)

Oeroenremboog is a data visualization and analysis project created for a hackathon event. It aims to provide insights through visualization, correlation analysis, and regression prediction.

## Project Structure

- `main.py`: Main script that connects to the database and fetches data
- `app.py`: Streamlit application file containing the data visualization dashboard
- `database_config.py`: Configuration file for the DuckDB database
- `etl/`: Directory containing ETL scripts
- `core/`: Directory containing additional utility scripts
- `raw_data/`: Directory containing raw data files
- `requirements.txt`: File containing the list of required packages and dependencies
## How to run the application

### Locally

1. Install the required packages:

   ```
   pip install -r requirements.txt
   ```

2. Run the main script to fetch data from the database:

   ```
   python main.py
   ```

3. Run the Streamlit app:

   ```
   streamlit run app.py
   ```

### With Docker

1. Build the Docker image:

   ```
   docker build -t oeroenremboog .
   ```

2. Run the Docker container:

   ```
   docker run -p 8501:8501 oeroenremboog
   ```

3. Open your browser and visit `http://localhost:8501` to view the application.