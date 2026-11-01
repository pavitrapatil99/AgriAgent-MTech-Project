# utils/karnataka_locations.py

# Current Karnataka district list
KARNATAKA_DISTRICTS = [
    "Bagalkote",
    "Ballari",
    "Belagavi",
    "Bengaluru Rural",
    "Bengaluru South",
    "Bengaluru Urban",
    "Bidar",
    "Chamarajanagar",
    "Chikkaballapur",
    "Chikkamagaluru",
    "Chitradurga",
    "Dakshina Kannada",
    "Davanagere",
    "Dharwad",
    "Gadag",
    "Hassan",
    "Haveri",
    "Kalaburagi",
    "Kodagu",
    "Kolar",
    "Koppal",
    "Mandya",
    "Mysuru",
    "Raichur",
    "Shivamogga",
    "Tumakuru",
    "Udupi",
    "Uttara Kannada",
    "Vijayanagara",
    "Vijayapura",
    "Yadgir"
]

# Karnataka's 10 agro-climatic zones
AGRO_CLIMATIC_ZONES = [
    "North Eastern Transition Zone (Zone 1)",
    "North Eastern Dry Zone (Zone 2)",
    "Northern Dry Zone (Zone 3)",
    "Central Dry Zone (Zone 4)",
    "Eastern Dry Zone (Zone 5)",
    "Southern Dry Zone (Zone 6)",
    "Southern Transition Zone (Zone 7)",
    "Northern Transition Zone (Zone 8)",
    "Hilly Zone (Zone 9)",
    "Coastal Zone (Zone 10)"
]

# Taluk-to-zone mapping
# Based on the KSNDMC 2017 agro-climatic zone classification.
# Some newer administrative changes are reflected in this mapping.

DISTRICT_TALUK_ZONES = {

    "Bagalkote": {
        "Badami": "Northern Dry Zone (Zone 3)",
        "Bagalkote": "Northern Dry Zone (Zone 3)",
        "Hungund": "Northern Dry Zone (Zone 3)",
        "Jamakhandi": "Northern Dry Zone (Zone 3)",
        "Mudhol": "Northern Dry Zone (Zone 3)",
        "Bilgi": "Northern Dry Zone (Zone 3)"
    },

    "Ballari": {
        "Ballari": "Northern Dry Zone (Zone 3)",
        "Sandur": "Northern Dry Zone (Zone 3)",
        "Siruguppa": "Northern Dry Zone (Zone 3)",
        "Kurugodu": "Northern Dry Zone (Zone 3)",
        "Kampli": "Northern Dry Zone (Zone 3)"
    },

    "Belagavi": {
        "Ramdurg": "Northern Dry Zone (Zone 3)",
        "Gokak": "Northern Dry Zone (Zone 3)",
        "Raibag": "Northern Dry Zone (Zone 3)",
        "Soundatti": "Northern Dry Zone (Zone 3)",
        "Athani": "Northern Dry Zone (Zone 3)",
        "Hukkeri": "Northern Transition Zone (Zone 8)",
        "Chikkodi": "Northern Transition Zone (Zone 8)",
        "Bailhongal": "Northern Transition Zone (Zone 8)",
        "Belagavi": "Northern Transition Zone (Zone 8)",
        "Khanapur": "Hilly Zone (Zone 9)"
    },

    "Bengaluru Rural": {
        "Devanahalli": "Eastern Dry Zone (Zone 5)",
        "Doddaballapura": "Eastern Dry Zone (Zone 5)",
        "Hoskote": "Eastern Dry Zone (Zone 5)",
        "Nelamangala": "Eastern Dry Zone (Zone 5)"
    },

    "Bengaluru South": {
        "Channapatna": "Eastern Dry Zone (Zone 5)",
        "Kanakapura": "Eastern Dry Zone (Zone 5)",
        "Magadi": "Eastern Dry Zone (Zone 5)",
        "Ramanagara": "Eastern Dry Zone (Zone 5)",
        "Harohalli": "Eastern Dry Zone (Zone 5)"
    },

    "Bengaluru Urban": {
        "Anekal": "Eastern Dry Zone (Zone 5)",
        "Bengaluru North": "Eastern Dry Zone (Zone 5)",
        "Bengaluru South": "Eastern Dry Zone (Zone 5)",
        "Bengaluru East": "Eastern Dry Zone (Zone 5)"
    },

    "Bidar": {
        "Bhalki": "North Eastern Transition Zone (Zone 1)",
        "Basavakalyan": "North Eastern Transition Zone (Zone 1)",
        "Bidar": "North Eastern Transition Zone (Zone 1)",
        "Humnabad": "North Eastern Transition Zone (Zone 1)",
        "Aurad": "North Eastern Transition Zone (Zone 1)"
    },

    "Chamarajanagar": {
        "Kollegal": "Southern Dry Zone (Zone 6)",
        "Chamarajanagar": "Southern Dry Zone (Zone 6)",
        "Yelandur": "Southern Dry Zone (Zone 6)",
        "Gundlupet": "Southern Dry Zone (Zone 6)"
    },

    "Chikkaballapur": {
        "Bagepalli": "Eastern Dry Zone (Zone 5)",
        "Chikkaballapur": "Eastern Dry Zone (Zone 5)",
        "Chintamani": "Eastern Dry Zone (Zone 5)",
        "Gudibanda": "Eastern Dry Zone (Zone 5)",
        "Gouribidanur": "Eastern Dry Zone (Zone 5)",
        "Sidlaghatta": "Eastern Dry Zone (Zone 5)"
    },

    "Chikkamagaluru": {
        "Kadur": "Central Dry Zone (Zone 4)",
        "Tarikere": "Southern Transition Zone (Zone 7)",
        "Koppa": "Hilly Zone (Zone 9)",
        "Sringeri": "Hilly Zone (Zone 9)",
        "Mudigere": "Hilly Zone (Zone 9)",
        "Narasimharajapura": "Hilly Zone (Zone 9)",
        "Chikkamagaluru": "Hilly Zone (Zone 9)"
    },

    "Chitradurga": {
        "Chitradurga": "Central Dry Zone (Zone 4)",
        "Hiriyur": "Central Dry Zone (Zone 4)",
        "Hosadurga": "Central Dry Zone (Zone 4)",
        "Holalkere": "Central Dry Zone (Zone 4)",
        "Molakalmuru": "Central Dry Zone (Zone 4)",
        "Challakere": "Central Dry Zone (Zone 4)"
    },

    "Dakshina Kannada": {
        "Bantwal": "Coastal Zone (Zone 10)",
        "Belthangadi": "Coastal Zone (Zone 10)",
        "Mangaluru": "Coastal Zone (Zone 10)",
        "Puttur": "Coastal Zone (Zone 10)",
        "Sulya": "Coastal Zone (Zone 10)"
    },

    "Davanagere": {
        "Harapanahalli": "Northern Dry Zone (Zone 3)",
        "Davanagere": "Central Dry Zone (Zone 4)",
        "Harihara": "Central Dry Zone (Zone 4)",
        "Jagalur": "Central Dry Zone (Zone 4)",
        "Honnali": "Southern Transition Zone (Zone 7)",
        "Channagiri": "Southern Transition Zone (Zone 7)"
    },

    "Dharwad": {
        "Navalgund": "Northern Dry Zone (Zone 3)",
        "Kundgol": "Northern Transition Zone (Zone 8)",
        "Hubli": "Northern Transition Zone (Zone 8)",
        "Dharwad": "Northern Transition Zone (Zone 8)",
        "Kalghatgi": "Hilly Zone (Zone 9)"
    },

    "Gadag": {
        "Ron": "Northern Dry Zone (Zone 3)",
        "Naragund": "Northern Dry Zone (Zone 3)",
        "Gadag": "Northern Dry Zone (Zone 3)",
        "Mundargi": "Northern Dry Zone (Zone 3)",
        "Shirahatti": "Northern Transition Zone (Zone 8)"
    },

    "Hassan": {
        "Arasikere": "Central Dry Zone (Zone 4)",
        "Channarayapatna": "Southern Dry Zone (Zone 6)",
        "Hassan": "Southern Dry Zone (Zone 6)",
        "Holenarasipura": "Southern Transition Zone (Zone 7)",
        "Alur": "Southern Transition Zone (Zone 7)",
        "Arkalgud": "Southern Transition Zone (Zone 7)",
        "Belur": "Southern Transition Zone (Zone 7)",
        "Sakleshpur": "Hilly Zone (Zone 9)"
    },

    "Haveri": {
        "Haveri": "Northern Transition Zone (Zone 8)",
        "Shiggaon": "Northern Transition Zone (Zone 8)",
        "Savanur": "Northern Transition Zone (Zone 8)",
        "Byadgi": "Northern Transition Zone (Zone 8)",
        "Hirekerur": "Northern Transition Zone (Zone 8)",
        "Ranebennur": "Northern Transition Zone (Zone 8)",
        "Hangal": "Hilly Zone (Zone 9)"
    },

    "Kalaburagi": {
        "Aland": "North Eastern Transition Zone (Zone 1)",
        "Chincholi": "North Eastern Transition Zone (Zone 1)",
        "Afzalpur": "North Eastern Dry Zone (Zone 2)",
        "Chitapur": "North Eastern Dry Zone (Zone 2)",
        "Kalaburagi": "North Eastern Dry Zone (Zone 2)",
        "Jewargi": "North Eastern Dry Zone (Zone 2)",
        "Sedam": "North Eastern Dry Zone (Zone 2)"
    },

    "Kodagu": {
        "Virajpet": "Hilly Zone (Zone 9)",
        "Somwarpet": "Hilly Zone (Zone 9)",
        "Madikeri": "Hilly Zone (Zone 9)"
    },

    "Kolar": {
        "Bangarapet": "Eastern Dry Zone (Zone 5)",
        "Kolar": "Eastern Dry Zone (Zone 5)",
        "Malur": "Eastern Dry Zone (Zone 5)",
        "Mulbagal": "Eastern Dry Zone (Zone 5)",
        "Srinivasapura": "Eastern Dry Zone (Zone 5)"
    },

    "Koppal": {
        "Gangavathi": "Northern Dry Zone (Zone 3)",
        "Koppal": "Northern Dry Zone (Zone 3)",
        "Kushtagi": "Northern Dry Zone (Zone 3)",
        "Yelbarga": "Northern Dry Zone (Zone 3)"
    },

    "Mandya": {
        "Nagamangala": "Southern Dry Zone (Zone 6)",
        "Srirangapatna": "Southern Dry Zone (Zone 6)",
        "Malavalli": "Southern Dry Zone (Zone 6)",
        "Maddur": "Southern Dry Zone (Zone 6)",
        "Mandya": "Southern Dry Zone (Zone 6)",
        "Pandavapura": "Southern Dry Zone (Zone 6)",
        "Krishnarajpet": "Southern Dry Zone (Zone 6)"
    },

    "Mysuru": {
        "Krishnarajanagara": "Southern Dry Zone (Zone 6)",
        "T. Narasipura": "Southern Dry Zone (Zone 6)",
        "Mysuru": "Southern Dry Zone (Zone 6)",
        "Nanjangud": "Southern Dry Zone (Zone 6)",
        "H.D. Kote": "Southern Transition Zone (Zone 7)",
        "Hunsur": "Southern Transition Zone (Zone 7)",
        "Periyapatna": "Southern Transition Zone (Zone 7)"
    },

    "Raichur": {
        "Raichur": "North Eastern Dry Zone (Zone 2)",
        "Deodurga": "North Eastern Dry Zone (Zone 2)",
        "Manvi": "North Eastern Dry Zone (Zone 2)",
        "Lingsugur": "Northern Dry Zone (Zone 3)",
        "Sindhnur": "Northern Dry Zone (Zone 3)"
    },

    "Shivamogga": {
        "Bhadravathi": "Southern Transition Zone (Zone 7)",
        "Shivamogga": "Southern Transition Zone (Zone 7)",
        "Shikaripur": "Southern Transition Zone (Zone 7)",
        "Sorab": "Hilly Zone (Zone 9)",
        "Tirthahalli": "Hilly Zone (Zone 9)",
        "Sagar": "Hilly Zone (Zone 9)",
        "Hosanagar": "Hilly Zone (Zone 9)"
    },

    "Tumakuru": {
        "Madhugiri": "Central Dry Zone (Zone 4)",
        "Pavagada": "Central Dry Zone (Zone 4)",
        "Koratagere": "Central Dry Zone (Zone 4)",
        "Chikkanayakanahalli": "Central Dry Zone (Zone 4)",
        "Sira": "Central Dry Zone (Zone 4)",
        "Tiptur": "Central Dry Zone (Zone 4)",
        "Gubbi": "Eastern Dry Zone (Zone 5)",
        "Tumakuru": "Eastern Dry Zone (Zone 5)",
        "Turuvekere": "Southern Dry Zone (Zone 6)",
        "Kunigal": "Southern Dry Zone (Zone 6)"
    },

    "Udupi": {
        "Udupi": "Coastal Zone (Zone 10)",
        "Karkala": "Coastal Zone (Zone 10)",
        "Kundapura": "Coastal Zone (Zone 10)"
    },

    "Uttara Kannada": {
        "Sirsi": "Hilly Zone (Zone 9)",
        "Siddapur": "Hilly Zone (Zone 9)",
        "Yellapur": "Hilly Zone (Zone 9)",
        "Supa": "Hilly Zone (Zone 9)",
        "Haliyal": "Hilly Zone (Zone 9)",
        "Mundgod": "Hilly Zone (Zone 9)",
        "Karwar": "Coastal Zone (Zone 10)",
        "Kumta": "Coastal Zone (Zone 10)",
        "Honnavar": "Coastal Zone (Zone 10)",
        "Bhatkal": "Coastal Zone (Zone 10)",
        "Ankola": "Coastal Zone (Zone 10)"
    },

    "Vijayanagara": {
        "Hosapete": "Northern Dry Zone (Zone 3)",
        "Kudligi": "Northern Dry Zone (Zone 3)",
        "Hagaribommanahalli": "Northern Dry Zone (Zone 3)",
        "Kotturu": "Northern Dry Zone (Zone 3)",
        "Hoovina Hadagali": "Northern Dry Zone (Zone 3)",
        "Harapanahalli": "Northern Dry Zone (Zone 3)"
    },

    "Vijayapura": {
        "Basavana Bagewadi": "Northern Dry Zone (Zone 3)",
        "Vijayapura": "Northern Dry Zone (Zone 3)",
        "Indi": "Northern Dry Zone (Zone 3)",
        "Muddebhihal": "Northern Dry Zone (Zone 3)",
        "Sindagi": "Northern Dry Zone (Zone 3)"
    },

    "Yadgir": {
        "Shorapur": "North Eastern Dry Zone (Zone 2)",
        "Shahapur": "North Eastern Dry Zone (Zone 2)",
        "Yadgir": "North Eastern Dry Zone (Zone 2)"
    }
}