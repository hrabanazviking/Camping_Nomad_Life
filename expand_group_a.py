import json
import os

BASE_DIR = "/home/volmarr/.gemini/antigravity/scratch/Camping_Nomad_Life/states"

group_a = {
  "connecticut.json": [
    {
      "id": "ct-pachaug-state-forest-mount-misery",
      "name": "Pachaug State Forest Mount Misery Primitive Backpack Shelter",
      "state": "Connecticut",
      "county": "New London County",
      "coordinates": { "latitude": 41.5812, "longitude": -71.8612, "elevation_ft": 440 },
      "management_agency": {
        "name": "Connecticut Department of Energy and Environmental Protection (DEEP)",
        "type": "State DEEP",
        "phone": "(860) 424-3000",
        "website": "https://portal.ct.gov/DEEP"
      },
      "rules_and_regulations": {
        "cost": "100% Free - Free CT DEEP Backpacking Permit required online (zero cost)",
        "stay_limit": "1 night stay limit per shelter area",
        "guidelines": "Primitive backpacking camping permitted at designated Mount Misery shelter site along Pachaug Trail. Carry in / carry out."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Use wooden pit privy at shelter site or dig cat-hole 6 inches deep in soil 200 feet from streams. Pack out all paper.",
        "trash_policy": "Strict Carry-In / Carry-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down wood gathering permitted on site.",
        "safety_requirements": "Campfires in established stone fire pit only. Fully douse with water before departing.",
        "seasonal_fire_bans": "Spring dry weather forest fire restrictions."
      },
      "access_and_road_conditions": {
        "road_type": "Paved state road to gravel forest parking lot",
        "road_conditions": "Graded gravel access parking lot, 1.2 mile hike-in on trail.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance passenger cars.",
        "scores": { "road_grade": 2, "road_terrain_difficulty": 2, "supply_run_pain": 3 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / Near I-395 Corridor",
        "verizon_reliability": "4-5 bars 4G/5G LTE (25-55 Mbps download)",
        "att_reliability": "4-5 bars 4G/5G LTE",
        "tmobile_reliability": "3-4 bars 4G LTE",
        "terrain_obstruction_risk": "Low (Gentle rolling piney woods topography)",
        "distance_from_tower_corridor_miles": 2.5,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Wooden Shelter Lean-To",
        "Pit Privy Toilet",
        "Mount Misery Brook Water Source (Filter mandatory)",
        "Stone Fire Ring"
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
          "town_name": "Griswold / Jewett City, CT",
          "distance_miles": 6.0,
          "services_available": ["Better Valu Supermarket", "Gas Stations", "Slater Library", "Restaurants"]
        },
        {
          "town_name": "Norwich, CT",
          "distance_miles": 14.0,
          "services_available": ["Full Metro City Services", "Stop & Shop", "Backus Hospital", "24/7 Gyms"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "48-65°F, blooming wild azaleas, pleasant spring breezes.",
        "summer": "72-84°F, warm Connecticut forest summer weather.",
        "fall": "50-68°F, vibrant colorful hardwood foliage.",
        "winter": "25-40°F, crisp winter weather, light snow."
      },
      "dangers_and_hazards": [
        "Ticks in summer months (use permethrin)"
      ],
      "acoustic_environment": {
        "quietness_rating": "8/10 - Brook water flow and woodland songbirds",
        "common_human_made_sounds": ["Occasional distant vehicle on country road"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["White Pine", "Red Oak", "Mountain Laurel", "Rhododendron"],
        "common_animals": ["White-tailed Deer", "Wild Turkey", "Red Fox", "Barred Owl"]
      },
      "human_demographics_and_culture": "Mohegan and Pequot ancestral lands, Connecticut backpackers, digital nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Traditional Mohegan territory honoring the ancient white pine groves and sacred brook waters of New London County.",
        "energetic_and_spiritual_features": "Relaxing pine forest quietness, peaceful brook cascades."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Pachaug Trail (Mount Misery Section)",
          "length_miles": 5.5,
          "difficulty": "Easy to Moderate",
          "features": "Mount Misery summit view, rhododendron sanctuaries, pine groves"
        }
      ],
      "public_reviews_summary": "Connecticut's top free primitive shelter camping. Blazing 5G cell internet, clean wooden lean-to, and easy 10-minute drive to Jewett City.",
      "other_data": "CT DEEP State Forest. Free backpacking permit required.",
      "last_updated": "2026-09-12"
    }
  ],
  "delaware.json": [
    {
      "id": "de-blackbird-state-forest-primitive",
      "name": "Blackbird State Forest Primitive Campsite",
      "state": "Delaware",
      "county": "New Castle County",
      "coordinates": { "latitude": 39.3612, "longitude": -75.6612, "elevation_ft": 60 },
      "management_agency": {
        "name": "Delaware Department of Agriculture - Forest Service",
        "type": "State Forest Service",
        "phone": "(302) 653-6505",
        "website": "https://agriculture.delaware.gov/forestry"
      },
      "rules_and_regulations": {
        "cost": "100% Free - Free Delaware Forest Service Camping Permit required online (zero cost)",
        "stay_limit": "3 consecutive nights stay limit",
        "guidelines": "Primitive camping at designated sites in Blackbird State Forest Tybout Tract. Carry in / carry out."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Use portable toilet or dig cat-hole 6 inches deep in soil 200 feet from water drainages. Pack out all paper.",
        "trash_policy": "Strict Carry-In / Carry-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down wood gathering permitted on site.",
        "safety_requirements": "Campfires in established metal fire rings only. Fully douse with water before vacating.",
        "seasonal_fire_bans": "Dry weather forest fire warnings."
      },
      "access_and_road_conditions": {
        "road_type": "Paved county road to gravel forest entrance road",
        "road_conditions": "Smooth gravel driveway, flat parking turnouts.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance vehicles.",
        "scores": { "road_grade": 1, "road_terrain_difficulty": 2, "supply_run_pain": 2 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / Near US 13 & I-95 Tower Lines",
        "verizon_reliability": "4-5 bars 4G/5G LTE (35-75 Mbps download)",
        "att_reliability": "4-5 bars 4G/5G LTE",
        "tmobile_reliability": "4-5 bars 4G LTE",
        "terrain_obstruction_risk": "Low (Flat coastal plain forest)",
        "distance_from_tower_corridor_miles": 1.5,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Oak & Pine Shade Campsites",
        "Covered Picnic Tables",
        "Flat Dirt/Gravel Vehicle Pullouts",
        "Metal Fire Rings"
      ],
      "location_scores": {
        "distance_to_groceries_score": 8,
        "distance_to_library_score": 8,
        "distance_to_gym_score": 7,
        "terrain_score": 6,
        "quietness_score": 8
      },
      "nearest_supply_towns": [
        {
          "town_name": "Smyrna / Townsend, DE",
          "distance_miles": 5.0,
          "services_available": ["Food Lion / Acme Markets", "Gas Stations", "Smyrna Public Library", "Restaurants"]
        },
        {
          "town_name": "Dover, DE",
          "distance_miles": 16.0,
          "services_available": ["Full State Capital Metro", "Target / Walmart", "Bayhealth Hospital", "24/7 Gyms"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "55-70°F, blooming wild dogwood and red maple.",
        "summer": "78-88°F, warm pleasant Delaware forest summer days.",
        "fall": "55-72°F, mild crisp autumn weather.",
        "winter": "32-45°F, mild coastal plain winter."
      },
      "dangers_and_hazards": [
        "Ticks in summer months (use permethrin)"
      ],
      "acoustic_environment": {
        "quietness_rating": "8/10 - Forest wind and woodland bird calls",
        "common_human_made_sounds": ["Distant highway traffic on US 13"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Loblolly Pine", "White Oak", "American Holly (Delaware state tree)", "Sweetgum"],
        "common_animals": ["Delmarva Fox Squirrel", "White-tailed Deer", "Wild Turkey", "Red-tailed Hawk"]
      },
      "human_demographics_and_culture": "Lenni-Lenape ancestral lands, Delaware outdoorsmen, digital nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Traditional Lenni-Lenape territory honoring the ancient coastal oak forests of New Castle County.",
        "energetic_and_spiritual_features": "Relaxing coastal forest quietness, serene flat woodland trails."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Blackbird Forest Oak Loop Trail",
          "length_miles": 3.5,
          "difficulty": "Easy",
          "features": "Loblolly pine groves, mature oak canopy, wildlife observation"
        }
      ],
      "public_reviews_summary": "Delaware's premier free primitive camping site. Blazing 5G cell internet, flat easy driving, and 5 minutes to grocery stores in Smyrna.",
      "other_data": "Delaware Forest Service. Free permit required online.",
      "last_updated": "2026-09-12"
    }
  ],
  "florida.json": [
    {
      "id": "fl-apalachicola-nf-fort-gadsden",
      "name": "Fort Gadsden / River Landing Primitive Camping",
      "state": "Florida",
      "county": "Franklin County",
      "coordinates": { "latitude": 29.9412, "longitude": -85.0214, "elevation_ft": 25 },
      "management_agency": {
        "name": "US Forest Service - National Forests in Florida (Apalachicola District)",
        "type": "USFS",
        "phone": "(850) 926-3561",
        "website": "https://www.fs.usda.gov/florida"
      },
      "rules_and_regulations": {
        "cost": "100% Free - USFS Dispersed Primitive Camping (zero fee)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed primitive camping permitted along Apalachicola River landing pullouts. Camp 100ft minimum from river high water line."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6 inches deep in soil 200 feet from Apalachicola River. Pack out hygiene products.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down pine and oak wood collection permitted.",
        "safety_requirements": "Campfires in established rock fire rings only. Fully douse with water before vacating.",
        "seasonal_fire_bans": "Spring dry weather wildfire warnings."
      },
      "access_and_road_conditions": {
        "road_type": "Paved state route to graded gravel/dirt Forest Service roads",
        "road_conditions": "Graded gravel access roads, flat riverfront turnouts.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance vehicles.",
        "scores": { "road_grade": 1, "road_terrain_difficulty": 3, "supply_run_pain": 3 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / River Corridor Cell Signal",
        "verizon_reliability": "3-4 bars 4G LTE (15-35 Mbps download)",
        "att_reliability": "3-4 bars 4G LTE",
        "tmobile_reliability": "2-3 bars 4G LTE",
        "terrain_obstruction_risk": "Low across flat river delta",
        "distance_from_tower_corridor_miles": 3.5,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Apalachicola Riverfront Campsites",
        "Boat & Kayak Launching",
        "Live Oak & Spanish Moss Shade",
        "Stone Fire Rings"
      ],
      "location_scores": {
        "distance_to_groceries_score": 6,
        "distance_to_library_score": 6,
        "distance_to_gym_score": 5,
        "terrain_score": 9,
        "quietness_score": 9
      },
      "nearest_supply_towns": [
        {
          "town_name": "Eastpoint / Apalachicola, FL",
          "distance_miles": 16.0,
          "services_available": ["Piggly Wiggly", "Gas Stations", "Apalachicola Public Library", "Seafood Markets", "Restaurants"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "68-82°F, blooming wild azaleas and tupelo blossoms, mild sea breezes.",
        "summer": "85-92°F, warm humid Florida summer weather, shaded river canopy.",
        "fall": "65-80°F, prime pleasant camping weather.",
        "winter": "48-68°F, warm sunny winter weather, dry clear skies."
      },
      "dangers_and_hazards": [
        "Alligators in Apalachicola River (do not swim near riverbanks)",
        "Mosquitoes in summer months (use permethrin)"
      ],
      "acoustic_environment": {
        "quietness_rating": "9/10 - Rushing river flow and barred owl calls",
        "common_human_made_sounds": ["Occasional fishing boat on river"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Live Oak", "Spanish Moss", "Ogeechee Tupelo", "Cabbage Palm"],
        "common_animals": ["American Alligator", "Manatee", "Bald Eagle", "Osprey", "Barred Owl"]
      },
      "human_demographics_and_culture": "Muscogee Creek ancestral lands, Apalachicola oystermen and rivermen, Florida nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Historic Fort Gadsden National Historic Landmark location. Rich Seminole and Creek frontier history.",
        "energetic_and_spiritual_features": "Relaxing river delta energy, majestic live oak canopy tranquility."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Fort Gadsden Historic Trail",
          "length_miles": 2.5,
          "difficulty": "Easy",
          "features": "Apalachicola river vistas, live oak groves, historic interpretive markers"
        }
      ],
      "public_reviews_summary": "Fantastic free riverfront primitive camping in Apalachicola National Forest. Live oak shade, solid cell internet, and 15 minutes to Apalachicola's seafood markets.",
      "other_data": "Apalachicola National Forest. Free dispersed primitive camping.",
      "last_updated": "2026-09-12"
    }
  ]
}

for filename, sites in group_a.items():
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
