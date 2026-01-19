import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Configuration
SWIGGY_FILE = 'swiggy_file.csv'
CREDENTIALS_FILE = 'credentials.json'
SHEET_ID = '1lSobLES_B61sjYOl3Ko32ig_nktMtocmg7Ksvgl-dL4'

def prepare_swiggy_data():
    """Clean and filter Swiggy dataset"""
    print("📊 Loading Swiggy dataset...")
    
    # Load CSV
    df = pd.read_csv(SWIGGY_FILE)
    print(f"✅ Loaded {len(df)} total restaurants")
    
    # Define target cities
    top_cities = [
        'Bangalore', 'Bengaluru', 'Mumbai', 'Delhi', 'New Delhi',
        'Pune', 'Hyderabad', 'Chennai', 'Kolkata', 'Ahmedabad',
        'Jaipur', 'Indore', 'Chandigarh', 'Kochi', 'Lucknow',
        'Bhubaneswar', 'Coimbatore', 'Surat', 'Nagpur', 'Gurgaon'
    ]
    
    # Filter for target cities (case-insensitive)
    # Try different possible column names for city
    city_column = None
    for col in ['city', 'location', 'City', 'Location', 'area', 'Area']:
        if col in df.columns:
            city_column = col
            break
    
    if city_column is None:
        print("Available columns:", df.columns.tolist())
        print("❌ Could not find city column. Please check the CSV structure.")
        return None
    
    print(f"📍 Using '{city_column}' column for city filtering")
    
    # Filter cities
    df_filtered = df[df[city_column].str.contains('|'.join(top_cities), case=False, na=False)]
    print(f"✅ Filtered to {len(df_filtered)} restaurants in target cities")
    
    if len(df_filtered) == 0:
        print("⚠️ No data found for target cities. Using all data instead.")
        df_filtered = df.head(200)  # Take first 200 if no city match
    
    # Try to get top-rated restaurants per city
    try:
        # Look for rating column
        rating_col = None
        for col in ['rating', 'Rating', 'avg_rating', 'restaurant_rating']:
            if col in df.columns:
                rating_col = col
                break
        
        if rating_col:
            # Convert rating to numeric
            df_filtered[rating_col] = pd.to_numeric(df_filtered[rating_col], errors='coerce')
            
            # Get top 10-12 per city
            df_final = df_filtered.groupby(city_column).apply(
                lambda x: x.nlargest(min(12, len(x)), rating_col)
            ).reset_index(drop=True)
        else:
            # No rating column, just take first 150
            df_final = df_filtered.head(150)
    except Exception as e:
        print(f"⚠️ Could not sort by rating: {e}")
        df_final = df_filtered.head(150)
    
    print(f"✅ Selected {len(df_final)} restaurants for upload")
    
    # Create standardized dataframe for Google Sheets
    # Map columns flexibly
    result_data = {
        'City': [],
        'Name': [],
        'Category': [],
        'Area': [],
        'Description': [],
        'Rating': [],
        'Phone': [],
        'Price': [],
        'Google_Maps_Link': []
    }
    
    for _, row in df_final.iterrows():
        # City
        city = row.get(city_column, 'Unknown')
        result_data['City'].append(str(city))
        
        # Name
        name = row.get('restaurant_name', row.get('name', row.get('Name', 'Restaurant')))
        result_data['Name'].append(str(name))
        
        # Category (cuisine)
        cuisine = row.get('cuisine', row.get('Cuisine', row.get('food_type', 'Multi-cuisine')))
        if pd.notna(cuisine):
            # Take first cuisine if multiple
            category = str(cuisine).split(',')[0].strip()
        else:
            category = 'Restaurant'
        result_data['Category'].append(category)
        
        # Area
        area = row.get('area', row.get('Area', row.get('locality', 'City Center')))
        result_data['Area'].append(str(area))
        
        # Description
        desc = f"Popular restaurant serving {category} cuisine"
        rating_val = row.get(rating_col if rating_col else 'rating', '')
        if pd.notna(rating_val) and rating_val != '':
            desc += f". Rated {rating_val}/5"
        result_data['Description'].append(desc)
        
        # Rating
        rating = row.get(rating_col if rating_col else 'rating', 4.0)
        if pd.isna(rating):
            rating = 4.0
        result_data['Rating'].append(float(rating))
        
        # Phone
        phone = row.get('phone', row.get('contact', 'Available on Swiggy'))
        result_data['Phone'].append(str(phone))
        
        # Price
        price = row.get('average_price', row.get('price_for_two', row.get('cost', '')))
        if pd.notna(price):
            try:
                price_num = float(str(price).replace('₹', '').replace(',', ''))
                if price_num < 300:
                    price_range = '₹₹'
                elif price_num < 800:
                    price_range = '₹₹₹'
                else:
                    price_range = '₹₹₹₹'
            except:
                price_range = '₹₹'
        else:
            price_range = '₹₹'
        result_data['Price'].append(price_range)
        
        # Google Maps Link (empty for now)
        result_data['Google_Maps_Link'].append('')
    
    result_df = pd.DataFrame(result_data)
    
    print(f"\n📊 Data Summary:")
    print(f"   Total entries: {len(result_df)}")
    print(f"   Cities covered: {result_df['City'].nunique()}")
    print(f"   Categories: {result_df['Category'].nunique()}")
    
    return result_df

def upload_to_google_sheets(df):
    """Upload data to Google Sheets"""
    print("\n☁️ Uploading to Google Sheets...")
    
    # Setup credentials
    scope = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive'
    ]
    
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        CREDENTIALS_FILE, 
        scope
    )
    
    client = gspread.authorize(creds)
    
    # Open sheet
    try:
        sheet = client.open_by_key(SHEET_ID).sheet1
        print("✅ Connected to Google Sheet")
    except Exception as e:
        print(f"❌ Error connecting to sheet: {e}")
        return False
    
    # Clear existing data
    sheet.clear()
    print("✅ Cleared existing data")
    
    # Prepare data for upload
    upload_data = [df.columns.values.tolist()] + df.values.tolist()
    
    # Upload
    try:
        sheet.update('A1', upload_data)
        print(f"✅ Uploaded {len(df)} rows to Google Sheets!")
        print(f"\n🎉 SUCCESS! Check your sheet at:")
        print(f"   https://docs.google.com/spreadsheets/d/{SHEET_ID}")
        return True
    except Exception as e:
        print(f"❌ Error uploading: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Starting data preparation...\n")
    
    # Prepare data
    df = prepare_swiggy_data()
    
    if df is not None and len(df) > 0:
        # Upload to Google Sheets
        success = upload_to_google_sheets(df)
        
        if success:
            print("\n✅ Data preparation complete!")
            print("\nNext steps:")
            print("1. Check your Google Sheet to verify data")
            print("2. Ready to build the RAG chatbot!")
        else:
            print("\n❌ Upload failed. Please check your credentials and Sheet ID.")
    else:
        print("\n❌ Data preparation failed. Please check the CSV file structure.")