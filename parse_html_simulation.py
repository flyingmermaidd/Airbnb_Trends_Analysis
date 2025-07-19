from bs4 import BeautifulSoup

# Load the saved Airbnb listing HTML file
with open("sample_airbnb_page.html", "r", encoding="utf-8") as file:
    html = file.read()

# Parse the HTML
soup = BeautifulSoup(html, "html.parser")

# Extract Listing Title
title = soup.find("h1")
print("Listing Title:", title.text.strip() if title else "Not found")

# Extract a price (e.g., $123 CAD)
price = soup.find(string=lambda text: "$" in text)
print("Sample Price:", price.strip() if price else "Not found")

# Extract all amenities that include common keywords
important_keywords = ["Wi-Fi", "Kitchen", "Parking", "Air conditioning", "Pool", "Hot tub"]
amenity_matches = []

for kw in important_keywords:
    found = soup.find_all(string=lambda t: t and kw.lower() in t.lower())
    for item in found:
        if item.strip() not in amenity_matches:
            amenity_matches.append(item.strip())

print("Amenities Found:")
for a in amenity_matches:
    print("-", a)