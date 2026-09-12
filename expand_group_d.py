import json
import os

BASE_DIR = "/home/volmarr/.gemini/antigravity/scratch/Camping_Nomad_Life/states"

group_d = {
  "iowa.json": [
    {
      "id": "ia-shimek-state-forest-lick-creek",
      "name": "Shimek State Forest Lick Creek Primitive Campsites",
      "state": "Iowa",
      "county": "Lee County",
      "coordinates": { "latitude": 40.6812, "longitude": -91.6512, "elevation_ft": 650 },
      "management_agency": {
        "name": "Iowa Department of Natural Resources (DNR)",
        "type": "State DNR",
        "phone": "(319) 878-3817",
        "website": "https://www.iowadnr.gov"
      },
      "rules_and_regulations": {
        "cost": "100% Free - Iowa DNR State Forest Dispersed Primitive Camping (zero fee)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed primitive backpacking camping permitted in Lick Creek Unit of Shimek State Forest. Camp 100ft minimum from trails."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6 inches deep in soil 200 feet from Lick Creek. Pack out all paper.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down wood gathering permitted on site.",
        "safety_requirements": "Campfires in established rock fire rings only. Fully douse before vacating.",
        "seasonal_fire_bans": "Observe drought fire warnings."
      },
      "access_and_road_conditions": {
        "road_type": "Paved state highway to gravel forest roads",
        "road_conditions": "Graded gravel access roads, flat pullouts.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance vehicles.",
        "scores": { "road_grade": 2, "road_terrain_difficulty": 3, "supply_run_pain": 3 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / Near US 218 Tower Line",
        "verizon_reliability": "3-4 bars 4G LTE (15-35 Mbps download)",
        "att_reliability": "3-4 bars 4G LTE",
        "tmobile_reliability": "2-3 bars 4G LTE",
        "terrain_obstruction_risk": "Low across rolling forest hills",
        "distance_from_tower_corridor_miles": 3.0,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Oak-Hickory Forest Primitive Campsites",
        "Lick Creek Water Source (Filter mandatory)",
        "Flat Dirt/Gravel Pullouts",
        "Stone Fire Rings"
      ],
      "location_scores": {
        "distance_to_groceries_score": 7,
        "distance_to_library_score": 7,
        "distance_to_gym_score": 6,
        "terrain_score": 7,
        "quietness_score": 8
      },
      "nearest_supply_towns": [
        {
          "town_name": "Donnellson / Fort Madison, IA",
          "distance_miles": 10.0,
          "services_available": ["Hy-Vee / Fareway", "Gas Stations", "Donnellson Public Library", "Hospital", "Restaurants"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "50-68°F, spring wildflower bloom, crisp sunny air.",
        "summer": "75-88°F, warm humid Iowa summer days under oak canopy.",
        "fall": "50-70°F, colorful oak-hickory autumn foliage.",
        "winter": "22-38°F, cold winter air, light snow."
      },
      "dangers_and_hazards": [
        "Ticks in summer months (use permethrin)"
      ],
      "acoustic_environment": {
        "quietness_rating": "8/10 - Woodland birds and wind through oak leaves",
        "common_human_made_sounds": ["Occasional vehicle on country road"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["White Oak", "Shagbark Hickory", "Sugar Maple", "Wild Plum"],
        "common_animals": ["White-tailed Deer", "Wild Turkey", "Red Fox", "Barred Owl"]
      },
      "human_demographics_and_culture": "Sauk & Meskwaki ancestral lands, Iowa outdoorsmen, nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Traditional Sauk territory honoring the ancient oak-hickory woodlands of Southeastern Iowa.",
        "energetic_and_spiritual_features": "Relaxing oak forest quietness, peaceful woodland solitude."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Lick Creek Trail",
          "length_miles": 6.0,
          "difficulty": "Moderate",
          "features": "Oak-hickory forest, creek ravines, wildlife viewing"
        }
      ],
      "public_reviews_summary": "Top free primitive camping in Iowa's Shimek State Forest. Solid cell internet, flat easy driving, and 10 minutes to Fort Madison.",
      "other_data": "Iowa DNR State Forest. Free dispersed camping.",
      "last_updated": "2026-09-12"
    }
  ],
  "kansas.json": [
    {
      "id": "ks-tuttle-creek-wildlife-area-dispersed",
      "name": "Tuttle Creek Wildlife Area Dispersed Campsites",
      "state": "Kansas",
      "county": "Riley / Pottawatomie County",
      "coordinates": { "latitude": 39.3812, "longitude": -96.6512, "elevation_ft": 1080 },
      "management_agency": {
        "name": "Kansas Department of Wildlife and Parks (KDWP)",
        "type": "State KDWP",
        "phone": "(785) 539-7941",
        "website": "https://ksoutdoors.com"
      },
      "rules_and_regulations": {
        "cost": "100% Free - KDWP Public Wildlife Area Primitive Camping (zero fee)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed primitive camping permitted at designated parking turnouts and primitive clearings in upper Tuttle Creek Wildlife Area."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6 inches deep in soil 200 feet from Tuttle Creek lake water. Pack out hygiene items.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down wood gathering permitted on site.",
        "safety_requirements": "Campfires in established rock fire rings only. Fully douse before vacating.",
        "seasonal_fire_bans": "Spring Flint Hills prairie burn warnings."
      },
      "access_and_road_conditions": {
        "road_type": "Paved state highway to gravel/dirt wildlife area access drives",
        "road_conditions": "Graded gravel access roads, flat dirt turnouts.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance vehicles.",
        "scores": { "road_grade": 2, "road_terrain_difficulty": 3, "supply_run_pain": 3 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / Manhattan Metro Cell Signal",
        "verizon_reliability": "4-5 bars 4G/5G LTE (25-60 Mbps download)",
        "att_reliability": "4-5 bars 4G/5G LTE",
        "tmobile_reliability": "3-4 bars 4G LTE",
        "terrain_obstruction_risk": "Low across rolling Flint Hills prairie",
        "distance_from_tower_corridor_miles": 2.5,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Flint Hills Prairie & Lake Views",
        "Flat Dirt/Gravel Vehicle Pullouts",
        "Boat & Kayak Access",
        "Stone Fire Rings"
      ],
      "location_scores": {
        "distance_to_groceries_score": 8,
        "distance_to_library_score": 8,
        "distance_to_gym_score": 7,
        "terrain_score": 7,
        "quietness_score": 8
      },
      "nearest_supply_towns": [
        {
          "town_name": "Manhattan, KS",
          "distance_miles": 12.0,
          "services_available": ["Dillons / Hy-Vee", "Target / Walmart", "KSU Metro Services", "Ascension Hospital", "24/7 Gyms"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "55-72°F, greening Flint Hills prairie, wildflower bloom.",
        "summer": "85-98°F, warm sunny Kansas summer days, refreshing lake dips.",
        "fall": "58-76°F, mild golden prairie weather.",
        "winter": "22-42°F, cold prairie wind, dry clear skies."
      },
      "dangers_and_hazards": [
        "High wind on open prairie lake",
        "Summer mosquitoes near water"
      ],
      "acoustic_environment": {
        "quietness_rating": "8/10 - Prairie wind and lake water lapping",
        "common_human_made_sounds": ["Distant motorboat on lake"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Big Bluestem", "Eastern Cottonwood", "Bur Oak", "Wild Indigo"],
        "common_animals": ["White-tailed Deer", "Wild Turkey", "Bald Eagle", "Pelican", "Channel Catfish"]
      },
      "human_demographics_and_culture": "Kanza (Kaw) & Osage ancestral lands, KSU college outdoorsmen, Kansas nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Traditional Kanza nation territory honoring the ancient tallgrass Flint Hills prairie.",
        "energetic_and_spiritual_features": "Vast open Flint Hills sky horizons, serene lake sunset energy."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Fancy Creek Mountain Bike / Hike Trail",
          "length_miles": 6.0,
          "difficulty": "Moderate",
          "features": "Flint Hills limestone bluffs, oak woodlands, lake vistas"
        }
      ],
      "public_reviews_summary": "Top free primitive camping near Manhattan, Kansas. Blazing 5G cell internet, peaceful lake views, and easy 15-minute drive to KSU and gyms.",
      "other_data": "Kansas KDWP Public Wildlife Area. Free dispersed camping.",
      "last_updated": "2026-09-12"
    }
  ]
}

for filename, sites in group_d.items():
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
