# Toronto Airbnb Market Analysis & Trends Dashboard

This repository showcases a full-stack data analytics pipeline that scrapes, analyzes, and visualizes Airbnb listing data for Toronto. It uncovers actionable insights into pricing, occupancy, amenities, and host behavior—culminating in an interactive Power BI dashboard.

---

## Project Overview

I developed a proof-of-concept scraper using BeautifulSoup to simulate extraction from Airbnb listings. Due to scraping limitations and legal constraints, I validated my scraping logic using saved HTML pages.

For large-scale analysis, I used publicly available data from [Inside Airbnb](http://insideairbnb.com/get-the-data.html)—which closely mirrors what I would have extracted at scale. This allowed me to build and demonstrate the full data pipeline from extraction to insight generation.

The project answers critical market questions:

- What amenities justify a higher price?
- Which neighborhoods offer the best occupancy vs. value?
- What distinguishes Superhosts from standard hosts?
- What marketing language works best for listings?

---

## Key Features

### Web Scraping
- Simulated with saved HTML pages using BeautifulSoup and Scrapy.
- Sample HTML files provided for reproducibility.

### Data Cleaning & Preprocessing
- Handling missing values, converting prices, standardizing features.
- Amenity field parsed using `ast.literal_eval` for further processing.

### Feature Engineering
- `amenity_score`: Weighted score of key amenities.
- `occupancy_rate`: Estimated from `availability_365`.
- `host_tenure_years`: Based on `host_since` field.
- `price_per_review`, `price_per_person`, `days_since_last_review`.

### Advanced Analytics & ML
- **Descriptive Analysis**: Review scores, host behavior, property types.
- **K-Means Clustering**: Segment listings by:
  - Price vs. Occupancy Rate
  - Latitude vs. Longitude
- **Text Analysis**: Most frequent marketing keywords using word frequency & word cloud.

### Interactive Dashboard (Power BI)
- A comprehensive `.pbix` dashboard to explore:
  - Listings by neighborhood, price, property type, and superhost status.
  - Occupancy trends and pricing clusters.

---

## Dashboard & Key Insights

Key insights revealed from this project include:

- **Superhost Formula**: Superhosts tend to offer higher review scores rather than charging more. They achieve better occupancy through pricing strategies and listing quality.
- **Amenity Value**: Features like Pools and Hot Tubs correlate with premium pricing, whereas WiFi and Kitchen are baseline expectations.
- **Neighborhood Impact**: Listings near downtown and transit-heavy areas perform significantly better—frequently using keywords like “subway”, “walk”, and “downtown”.
- **Clustering Reveals Zones**: Downtown clusters exhibit high demand and density, while outer neighborhoods offer better price-to-occupancy ratios.

---

## ⚙️ Technical Workflow

1. **Scraping**: Simulated using local HTML files in `sample_airbnb_page_files/`.
2. **Parsing**: Logic developed in `airbnb_scraper/` and validated via `parse_html_simulation.py`.
3. **Analysis**: `airbnb_data_analysis.ipynb` performs:
   - Cleaning
   - Feature engineering
   - Clustering
   - Visualizations
4. **Visualization**: Final results exported and visualized in `Airbnb Scraper Dashboard.pbix`.

---

## Repository Structure

```
airbnb_scraper/                
sample_airbnb_page_files/       
sample_airbnb_page.html        
airbnb_data_analysis.ipynb     
parse_html_simulation.py       
Airbnb Scraper Dashboard.pbix  
requirements.txt               
README.md                     
.gitignore                    
scrapy.cfg               
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
Open the Power BI file in Microsoft Power BI Desktop:

```bash
Airbnb Scraper Dashboard.pbix
```

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

---

## 🛠️ Technology Stack

- **Web Scraping**: Python, BeautifulSoup, Scrapy
- **Data Processing**: pandas, numpy, ast, datetime
- **Visualization**: matplotlib, seaborn, WordCloud
- **Machine Learning**: scikit-learn (K-Means)
- **Text Analysis**: NLTK, re, Counter
- **Dashboarding**: Power BI

---

## Contribution

Contributions and improvements are welcome. Please open issues or pull requests for suggestions or bug fixes.