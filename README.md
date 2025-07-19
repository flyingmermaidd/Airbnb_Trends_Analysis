# Airbnb Trends Analysis

## Overview

This project provides a comprehensive analysis of Airbnb listings using web scraping, data cleaning, exploratory data analysis (EDA), feature engineering, clustering, and visualization techniques. The goal is to uncover pricing trends, occupancy patterns, host effectiveness, and neighborhood insights for Airbnb rentals.

The project includes:

- A **proof-of-concept scraper** to gather Airbnb listing data using Scrapy.
- **Data cleaning and preprocessing** pipelines to prepare the data for analysis.
- Extensive **feature engineering** including amenity scoring, occupancy rate, and host tenure.
- **Exploratory Data Analysis (EDA)** with correlations, price analysis, neighborhood insights, and host comparisons.
- **Clustering analysis** by price, occupancy, geographic location, and additional listing features.
- **Text analysis** on listing descriptions to identify common themes.
- A **Power BI dashboard** (`Airbnb Scraper Dashboard.pbix`) to interactively explore the data and insights.

## Repository Structure

```
airbnb_scraper/                # Scrapy project folder for web scraping
sample_airbnb_page_files/      # Sample downloaded Airbnb page resources
sample_airbnb_page.html        # Sample Airbnb page HTML file for scraper testing
airbnb_data_analysis.ipynb     # Jupyter notebook with data cleaning, analysis, clustering, and visualization
parse_html_simulation.py       # Script simulating HTML parsing logic
Airbnb Scraper Dashboard.pbix  # Power BI dashboard file visualizing cleaned and feature-engineered data
requirements.txt               # Python dependencies for data processing and analysis
README.md                     # Project documentation (this file)
.gitignore                    # Git ignore rules
scrapy.cfg                   # Scrapy configuration file
```

## Setup & Installation

1. **Clone the repository:**

```bash
git clone https://github.com/flyingmermaidd/Airbnb_Trends_Analysis.git
cd Airbnb_Trends_Analysis
```

2. **Create a Python virtual environment and activate it:**

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Run the Jupyter notebook:**

```bash
jupyter notebook airbnb_data_analysis.ipynb
```

The notebook walks through all data preparation, feature engineering, exploratory analysis, clustering, and text analysis steps.

## Using the Power BI Dashboard

The file `Airbnb Scraper Dashboard.pbix` is designed for interactive exploration of the Airbnb listing data.

- Open the `.pbix` file with Power BI Desktop.
- Load or refresh the data using the exported CSV: `airbnb_cleaned_for_powerbi.csv`.
- Explore the following dashboard pages:
  - Superhost pricing and occupancy comparisons
  - Amenities effect on price distributions
  - Neighborhood occupancy and price trends
  - Listing clustering by price, occupancy, and location

## Key Features and Insights

- **Superhost Analysis:** Examines if superhosts charge premium prices and maintain higher occupancy rates.
- **Amenities Impact:** Visualizes how the presence of key amenities influences listing prices.
- **Neighborhood Trends:** Identifies neighborhoods with highest occupancy and best price-to-occupancy ratios.
- **Host Effectiveness:** Compares host tenure, review scores, and listing performance.
- **Clustering:** Groups listings and neighborhoods by pricing and occupancy metrics, including geospatial clusters.
- **Text Analytics:** Extracts common descriptive terms used in Airbnb listings to understand guest appeal.

## Contribution

Contributions and improvements are welcome. Please open issues or pull requests for suggestions or bug fixes.

## License

This project is licensed under the MIT License.

---

*Developed by Rimi Mondal*