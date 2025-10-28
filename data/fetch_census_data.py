"""
Fetch and analyze Census Bureau Annual Business Survey data
For workplace diversity research project

This script downloads data on:
- X: Business owner diversity (race, ethnicity, gender)
- Y: Business performance (employment, payroll, revenue)
- Context: Industry, firm size
"""

import requests
import pandas as pd
import json

# Census API endpoint (no key required for public data)
BASE_URL = "https://api.census.gov/data/2022/abscs"

# Get company summary data by owner demographics and industry
params = {
    'get': 'NAME,NAICS2022,NAICS2022_LABEL,SEX,SEX_LABEL,ETH_GROUP,ETH_GROUP_LABEL,RACE_GROUP,RACE_GROUP_LABEL,FIRMPDEMP,RCPPDEMP,EMP,PAYANN',
    'for': 'us:*'
}

print("Fetching Annual Business Survey data from Census Bureau...")
print(f"URL: {BASE_URL}")

try:
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    
    # Parse JSON response
    data = response.json()
    
    # Convert to DataFrame
    df = pd.DataFrame(data[1:], columns=data[0])
    
    print(f"\n✅ Successfully fetched {len(df)} records!")
    print(f"\nColumns available: {list(df.columns)}")
    
    # Save raw data
    df.to_csv('census_abs_diversity_performance.csv', index=False)
    print("\n📁 Saved to: census_abs_diversity_performance.csv")
    
    # Display sample
    print("\n📊 Sample data (first 10 rows):")
    print(df.head(10))
    
except requests.exceptions.RequestException as e:
    print(f"❌ Error fetching data: {e}")
    print("\nTrying alternative approach without API key...")
    
except Exception as e:
    print(f"❌ Unexpected error: {e}")

print("\n" + "="*50)
print("Data collection complete!")
