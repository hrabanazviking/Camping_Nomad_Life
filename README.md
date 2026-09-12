# Camping Nomad Life - 100% Free Primitive Camping Database (USA)

Welcome to **Camping Nomad Life**, the definitive, open-source dataset of 100% free primitive camping locations across the United States. Designed specifically for digital nomads, off-grid vanlifers, boondockers, overland travellers, and wilderness campers.

## 🌲 Core Principles

1. **100% Free - Zero Hidden Fees**: Every location listed in this database is strictly free to camp with zero cost, zero hidden fees, and no mandatory paid permits.
2. **Real & Accurate Data**: Comprehensive, field-verified information covering road access, cell connectivity, local hazards, supply accessibility, wildlife, acoustics, and local folklore.
3. **Consistent Schema**: Standardized JSON format across all 50 US states (500 verified campsites; 10 sites per state) for seamless API consumption and data analysis.

---

## 📂 File Structure

```
Camping_Nomad_Life/
├── README.md
├── schema.json
├── validate_dataset.py
└── states/
    ├── alabama.json
    ├── alaska.json
    ├── arizona.json
    ├── arkansas.json
    ├── california.json
    └── ... (alphabetical order by state)
```

---

## 📶 Nomad Connectivity Rating

Each campsite includes a dedicated connectivity section:
- **Verizon / AT&T / T-Mobile Reliability**: Specific signal strength, bandwidth capabilities, and band expectations.
- **Terrain Obstruction Risk**: Assessment of canyon walls, dense canopy, or land formations blocking cellular line-of-sight.
- **Distance from Tower/Town Corridor**: Distance in miles to the nearest major cellular tower array.
- **Cellular Internet Dependability**: Boolean and qualitative rating for remote work (video calls, SSH, streaming).

---

## 📊 Scoring Metrics (Scale 1-10)

- **Road Grade Score** (1 = flat/gentle, 10 = extreme incline/steep switchbacks)
- **Road Terrain Difficulty Score** (1 = smooth paved/well-maintained gravel, 10 = extreme 4x4 crawling/boulders/deep ruts)
- **Supply Run Pain Score** (1 = quick painless drive, 10 = exhausting multi-hour off-road trip)
- **Distance to Groceries Score** (10 = under 5 miles, 1 = >50 miles away)
- **Distance to Library Score** (10 = under 5 miles, 1 = >50 miles away)
- **Distance to Gym Score** (10 = under 5 miles, 1 = >50 miles away)
- **Terrain Score** (1 = flat parking spot, 10 = spectacular dramatic natural landscape)
- **Quietness Score** (1 = loud highway/industrial noise, 10 = near complete natural silence)

---

## 🛠️ Data Validation

Run the built-in validator to verify schema compliance:
```bash
python3 validate_dataset.py
```
