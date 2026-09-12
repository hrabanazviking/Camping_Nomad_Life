import json
import os

BASE_DIR = "/home/volmarr/.gemini/antigravity/scratch/Camping_Nomad_Life/states"

group_j = {
  "north_dakota.json": [
    {
      "id": "nd-sheyenne-national-grassland",
      "name": "Sheyenne National Grassland Dispersed Primitive Camping",
      "state": "North Dakota",
      "county": "Ransom / Richland County",
      "coordinates": { "latitude": 46.3812, "longitude": -97.2812, "elevation_ft": 1080 },
      "management_agency": {
        "name": "US Forest Service - Dakota Prairie Grasslands (Sheyenne Ranger District)",
        "type": "USFS",
        "phone": "(701) 683-4370",
        "website": "https://www.fs.usda.gov/dpg"
      },
      "rules_and_regulations": {
        "cost": "100% Free - USFS Dispersed Primitive Camping (zero fee)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed primitive camping permitted throughout tallgrass oak savanna and oak sandhills pullouts along North Country Trail corridor."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6 inches deep in sandy soil 200 feet from Sheyenne River. Pack out hygiene products.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down oak wood gathering permitted on site.",
        "safety_requirements": "Campfires in established rock fire rings only. Fully douse with water before vacating.",
        "seasonal_fire_bans": "Spring dry grass fire warnings."
      },
      "access_and_road_conditions": {
        "road_type": "Paved state highway to gravel Forest Service roads",
        "road_conditions": "Graded gravel access roads, flat sand/dirt turnouts.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance passenger cars.",
        "scores": { "road_grade": 2, "road_terrain_difficulty": 3, "supply_run_pain": 3 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / Fargo-Lisbon Tower Line",
        "verizon_reliability": "3-4 bars 4G LTE (20-45 Mbps download)",
        "att_reliability": "3-4 bars 4G LTE",
        "tmobile_reliability": "2-3 bars 4G LTE",
        "terrain_obstruction_risk": "Low across rolling tallgrass sandhills savanna",
        "distance_from_tower_corridor_miles": 3.0,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Tallgrass Prairie & Bur Oak Savanna Campsites",
        "North Country Scenic Trailhead Access",
        "Flat Dirt/Gravel Pullouts",
        "Stone Fire Rings"
      ],
      "location_scores": {
        "distance_to_groceries_score": 7,
        "distance_to_library_score": 7,
        "distance_to_gym_score": 6,
        "terrain_score": 8,
        "quietness_score": 9
      },
      "nearest_supply_towns": [
        {
          "town_name": "Lisbon / Enderlin, ND",
          "distance_miles": 10.0,
          "services_available": ["Supermarket", "Gas Stations", "Lisbon Public Library", "Hospital", "Restaurants"]
        },
        {
          "town_name": "Fargo, ND",
          "distance_miles": 42.0,
          "services_available": ["Full Metro Services", "Costco / Target", "Sanford Medical Center", "24/7 Gyms"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "45-62°F, greening tallgrass savanna, prairie wildflower bloom.",
        "summer": "75-88°F, warm sunny tallgrass prairie days.",
        "fall": "48-68°F, golden tallgrass foliage, crisp cool nights.",
        "winter": "10-25°F, cold prairie wind, snowpack."
      },
      "dangers_and_hazards": [
        "High wind on open prairie sandhills",
        "Ticks in summer grass (use permethrin)"
      ],
      "acoustic_environment": {
        "quietness_rating": "9/10 - Prairie wind and savanna bird calls",
        "common_human_made_sounds": ["Occasional vehicle on country road"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Big Bluestem", "Bur Oak", "Western Prairie Fringed Orchid (threatened species)", "Prairie Rose"],
        "common_animals": ["Greater Prairie Chicken", "White-tailed Deer", "Wild Turkey", "Red Fox", "Regal Fritillary Butterfly"]
      },
      "human_demographics_and_culture": "Dakota & Ojibwe ancestral lands, North Dakota ranchers, North Country Trail hikers, nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Only National Grassland in the tallgrass prairie region of North America. Sacred ancestral Dakota territory.",
        "energetic_and_spiritual_features": "Profound open tallgrass prairie sky horizons, peaceful oak savanna quietness."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "North Country Trail (Sheyenne Grassland Section)",
          "length_miles": 12.0,
          "difficulty": "Easy to Moderate",
          "features": "Bur oak savanna, tallgrass prairie dunes, Sheyenne river valley"
        }
      ],
      "public_reviews_summary": "North Dakota's tallgrass prairie gem. Free primitive camping, rare bur oak savanna landscapes, fast cell internet near Lisbon, and 100% free USFS access.",
      "other_data": "Dakota Prairie Grasslands. Free dispersed primitive camping.",
      "last_updated": "2026-09-12"
    }
  ],
  "pennsylvania.json": [
    {
      "id": "pa-susquehannock-state-forest-dispersed",
      "name": "Susquehannock State Forest Dispersed Primitive Camping",
      "state": "Pennsylvania",
      "county": "Potter County",
      "coordinates": { "latitude": 41.6812, "longitude": -77.8812, "elevation_ft": 2150 },
      "management_agency": {
        "name": "Pennsylvania Department of Conservation and Natural Resources (DCNR) - Bureau of Forestry",
        "type": "State DCNR",
        "phone": "(814) 274-3600",
        "website": "https://www.dcnr.pa.gov/StateForests"
      },
      "rules_and_regulations": {
        "cost": "100% Free - Free PA DCNR State Forest Camping Permit required online/at forest district office (zero cost)",
        "stay_limit": "7 consecutive days stay limit per site",
        "guidelines": "Dispersed primitive roadside camping permitted at designated motorized sites throughout Susquehannock State Forest."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6-8 inches deep in organic soil 200 feet from streams. Pack out hygiene products.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down wood gathering permitted on forest lands.",
        "safety_requirements": "Campfires in established rock fire rings only. Fully douse with water before vacating.",
        "seasonal_fire_bans": "Spring/autumn dry leaf weather fire warnings."
      },
      "access_and_road_conditions": {
        "road_type": "Paved state route to gravel Forest Service roads (Denton Hill Road)",
        "road_conditions": "Graded gravel access roads, flat pullout turnouts.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance passenger cars.",
        "scores": { "road_grade": 3, "road_terrain_difficulty": 3, "supply_run_pain": 3 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / Route 6 & Coudersport Tower Line",
        "verizon_reliability": "3-4 bars 4G LTE near Coudersport / Route 6 corridor",
        "att_reliability": "3-4 bars 4G LTE",
        "tmobile_reliability": "2-3 bars 4G LTE",
        "terrain_obstruction_risk": "Low to Moderate across high Allegheny plateau crests",
        "distance_from_tower_corridor_miles": 4.0,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "High Allegheny Plateau Cherry & Maple Forest Campsites",
        "Cherry Springs International Dark Sky Park Access",
        "Flat Dirt/Gravel Pullouts",
        "Stone Fire Rings"
      ],
      "location_scores": {
        "distance_to_groceries_score": 6,
        "distance_to_library_score": 6,
        "distance_to_gym_score": 5,
        "terrain_score": 10,
        "quietness_score": 10
      },
      "nearest_supply_towns": [
        {
          "town_name": "Coudersport, PA",
          "distance_miles": 12.0,
          "services_available": ["Shop 'n Save Supermarket", "Gas Stations", "Coudersport Public Library", "UPMC Cole Hospital", "Restaurants"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "42-58°F, spring forest leaf-out, crisp mountain air.",
        "summer": "68-80°F, cool high-elevation escape from Pennsylvania summer heat.",
        "fall": "45-65°F, world-class black cherry and maple autumn foliage.",
        "winter": "18-32°F, heavy snowfall, snowmobile and winter woods trail hiking."
      },
      "dangers_and_hazards": [
        "Black bears in Potter County (store food securely)"
      ],
      "acoustic_environment": {
        "quietness_rating": "10/10 - High plateau forest wind and absolute night silence",
        "common_human_made_sounds": ["Occasional forest road vehicle"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Black Cherry", "Sugar Maple", "Eastern Hemlock", "American Beech"],
        "common_animals": ["Elk", "Black Bear", "White-tailed Deer", "Porcupine", "Ruffed Grouse"]
      },
      "human_demographics_and_culture": "Seneca (Iroquois) ancestral lands, Pennsylvania Wilds lumber culture, stargazers, nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Heart of the Pennsylvania Wilds. World-famous Bortle Class 2 dark sky stargazing near Cherry Springs State Park.",
        "energetic_and_spiritual_features": "Profound high plateau silence, world-class Milky Way night skies."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Susquehannock Trail System (STS)",
          "length_miles": 10.0,
          "difficulty": "Moderate",
          "features": "Allegheny plateau ridges, black cherry forests, remote stream valleys"
        }
      ],
      "public_reviews_summary": "Pennsylvania's dark sky primitive camping capital. Free state forest sites near Cherry Springs, fast cell internet near Coudersport, and world-class stargazing.",
      "other_data": "PA DCNR Bureau of Forestry. Free permit required.",
      "last_updated": "2026-09-12"
    }
  ]
}

for filename, sites in group_j.items():
    filepath = os.path.join(BASE_DIR, filename)
    if os.path.exists(filepath):
        data = json.load(open(filepath))
        existing_ids = {s["id"] for s in data}
        added = 0
        for s in sites:
            if s["id"] not in existing_ids:
                data.append(s)
                added += 1
        with open(filepath, "w") as f:
            json.dump(data, f, indent=2)
        print(f"Updated {filename}: added {added} new sites (total: {len(data)})")
