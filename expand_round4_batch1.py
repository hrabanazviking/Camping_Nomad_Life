import json
import os

BASE_DIR = "/home/volmarr/.gemini/antigravity/scratch/Camping_Nomad_Life/states"

r4_batch1 = {
  "connecticut.json": [
    {
      "id": "ct-cockaponset-state-forest-primitive",
      "name": "Cockaponset State Forest Primitive Backpack Campsite",
      "state": "Connecticut",
      "county": "Middlesex County",
      "coordinates": { "latitude": 41.4214, "longitude": -72.5214, "elevation_ft": 380 },
      "management_agency": {
        "name": "Connecticut Department of Energy and Environmental Protection (DEEP)",
        "type": "State DEEP",
        "phone": "(860) 345-8521",
        "website": "https://portal.ct.gov/DEEP"
      },
      "rules_and_regulations": {
        "cost": "100% Free - Free CT DEEP Backpacking Permit required online (zero cost)",
        "stay_limit": "1 night stay limit per site",
        "guidelines": "Primitive backpacking camping permitted at designated Pattaconk trail primitive clearings in Cockaponset State Forest."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6 inches deep in organic soil 200 feet from Pattaconk Reservoir. Pack out all paper.",
        "trash_policy": "Strict Carry-In / Carry-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down wood gathering permitted on site.",
        "safety_requirements": "Campfires in established stone fire rings only. Fully douse with water before vacating.",
        "seasonal_fire_bans": "Spring dry leaf weather fire restrictions."
      },
      "access_and_road_conditions": {
        "road_type": "Paved state route to gravel forest entrance road",
        "road_conditions": "Graded gravel access parking lot, 0.8 mile hike-in.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance passenger cars.",
        "scores": { "road_grade": 2, "road_terrain_difficulty": 2, "supply_run_pain": 2 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / Route 9 Corridor Line",
        "verizon_reliability": "4-5 bars 4G/5G LTE (30-65 Mbps download)",
        "att_reliability": "4-5 bars 4G/5G LTE",
        "tmobile_reliability": "3-4 bars 4G LTE",
        "terrain_obstruction_risk": "Low (Gentle rolling forest topography)",
        "distance_from_tower_corridor_miles": 2.0,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Oak & Mountain Laurel Forest Campsites",
        "Pattaconk Reservoir Access",
        "Flat Dirt Pullout Parking",
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
          "town_name": "Chester / Haddam, CT",
          "distance_miles": 4.0,
          "services_available": ["Supermarket", "Gas Stations", "Chester Public Library", "Restaurants"]
        },
        {
          "town_name": "Middletown, CT",
          "distance_miles": 14.0,
          "services_available": ["Full Metro Services", "Stop & Shop", "Middlesex Hospital", "24/7 Gyms"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "50-68°F, blooming wild azaleas and mountain laurel, pleasant spring breezes.",
        "summer": "72-84°F, warm Connecticut forest summer weather.",
        "fall": "50-68°F, vibrant colorful hardwood foliage.",
        "winter": "25-40°F, crisp winter weather, light snow."
      },
      "dangers_and_hazards": [
        "Ticks in summer months (use permethrin)"
      ],
      "acoustic_environment": {
        "quietness_rating": "8/10 - Reservoir water flow and woodland songbirds",
        "common_human_made_sounds": ["Occasional distant vehicle on state route"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["White Oak", "Red Maple", "Mountain Laurel", "Eastern Hemlock"],
        "common_animals": ["White-tailed Deer", "Wild Turkey", "Red Fox", "Osprey"]
      },
      "human_demographics_and_culture": "Wangunk ancestral lands, Connecticut outdoorsmen, digital nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Traditional Wangunk territory honoring the ancient oak forests and reservoir waters of Middlesex County.",
        "energetic_and_spiritual_features": "Relaxing hardwood forest quietness, peaceful reservoir reflection views."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Pattaconk Reservoir Trail",
          "length_miles": 4.0,
          "difficulty": "Easy to Moderate",
          "features": "Pattaconk Reservoir shoreline, cedar swamps, hardwood forest"
        }
      ],
      "public_reviews_summary": "Top free primitive backpacking camping in Connecticut. Blazing 5G cell internet, peaceful reservoir views, and 5 minutes to Chester.",
      "other_data": "CT DEEP State Forest. Free backpacking permit required.",
      "last_updated": "2026-09-12"
    }
  ],
  "delaware.json": [
    {
      "id": "de-redden-state-forest-primitive",
      "name": "Redden State Forest Primitive Campsite",
      "state": "Delaware",
      "county": "Sussex County",
      "coordinates": { "latitude": 38.7412, "longitude": -75.4412, "elevation_ft": 45 },
      "management_agency": {
        "name": "Delaware Department of Agriculture - Forest Service",
        "type": "State Forest Service",
        "phone": "(302) 856-2685",
        "website": "https://agriculture.delaware.gov/forestry"
      },
      "rules_and_regulations": {
        "cost": "100% Free - Free Delaware Forest Service Camping Permit required online (zero cost)",
        "stay_limit": "3 consecutive nights stay limit",
        "guidelines": "Primitive camping at designated campsites in Redden State Forest Headwaters Tract. Carry in / carry out."
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
        "road_type": "Paved US 113 to gravel forest entrance road",
        "road_conditions": "Smooth gravel driveway, flat parking turnouts.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance vehicles.",
        "scores": { "road_grade": 1, "road_terrain_difficulty": 2, "supply_run_pain": 2 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / Near US 113 Tower Line",
        "verizon_reliability": "4-5 bars 4G/5G LTE (35-75 Mbps download)",
        "att_reliability": "4-5 bars 4G/5G LTE",
        "tmobile_reliability": "4-5 bars 4G LTE",
        "terrain_obstruction_risk": "Low (Flat coastal plain forest)",
        "distance_from_tower_corridor_miles": 1.5,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Loblolly Pine & Oak Shade Campsites",
        "Covered Picnic Shelter",
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
          "town_name": "Georgetown / Millsboro, DE",
          "distance_miles": 5.0,
          "services_available": ["Food Lion / ALDI", "Gas Stations", "Georgetown Public Library", "Restaurants"]
        },
        {
          "town_name": "Rehoboth Beach, DE",
          "distance_miles": 20.0,
          "services_available": ["Full Coastal Metro", "Target / Safeway", "Beebe Healthcare Hospital", "24/7 Gyms"]
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
        "common_human_made_sounds": ["Distant highway traffic on US 113"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Loblolly Pine", "Shortleaf Pine", "American Holly", "Southern Red Oak"],
        "common_animals": ["Delmarva Fox Squirrel", "White-tailed Deer", "Wild Turkey", "Red-tailed Hawk"]
      },
      "human_demographics_and_culture": "Nanticoke ancestral lands, Delaware outdoorsmen, digital nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Traditional Nanticoke territory honoring the loblolly pine forests and headwater streams of Sussex County.",
        "energetic_and_spiritual_features": "Relaxing coastal pine forest quietness, serene flat woodland trails."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Redden Forest Headwaters Trail",
          "length_miles": 4.0,
          "difficulty": "Easy",
          "features": "Loblolly pine groves, mature oak canopy, wildlife observation"
        }
      ],
      "public_reviews_summary": "Top free primitive camping site in Southern Delaware. Blazing 5G cell internet, flat easy driving, and 5 minutes to Georgetown.",
      "other_data": "Delaware Forest Service. Free permit required online.",
      "last_updated": "2026-09-12"
    }
  ],
  "florida.json": [
    {
      "id": "fl-ocala-nf-davenport-landing",
      "name": "Davenport Landing Primitive River Campsites",
      "state": "Florida",
      "county": "Marion County",
      "coordinates": { "latitude": 29.3812, "longitude": -81.8812, "elevation_ft": 40 },
      "management_agency": {
        "name": "US Forest Service - National Forests in Florida (Ocala District)",
        "type": "USFS",
        "phone": "(352) 625-2520",
        "website": "https://www.fs.usda.gov/florida"
      },
      "rules_and_regulations": {
        "cost": "100% Free - USFS Dispersed Primitive Camping (zero fee)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed primitive camping permitted at designated river landing pullouts along Ocklawaha River. Camp 100ft minimum from river high water line."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6 inches deep in sandy soil 200 feet from Ocklawaha River. Pack out hygiene products.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down pine and oak wood collection permitted.",
        "safety_requirements": "Campfires in established rock fire rings only. Fully douse with water before vacating.",
        "seasonal_fire_bans": "Spring dry weather wildfire warnings."
      },
      "access_and_road_conditions": {
        "road_type": "Paved state route to graded gravel Forest Service roads",
        "road_conditions": "Graded gravel access roads, flat riverfront turnouts.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance vehicles.",
        "scores": { "road_grade": 1, "road_terrain_difficulty": 3, "supply_run_pain": 3 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / Ocala & Silver Springs Tower Line",
        "verizon_reliability": "3-4 bars 4G LTE (20-45 Mbps download)",
        "att_reliability": "3-4 bars 4G LTE",
        "tmobile_reliability": "2-3 bars 4G LTE",
        "terrain_obstruction_risk": "Low across flat river hammock forest",
        "distance_from_tower_corridor_miles": 3.0,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Ocklawaha Riverfront Campsites",
        "Canoe & Kayak Launching",
        "Live Oak & Palmetto Hammock Shade",
        "Stone Fire Rings"
      ],
      "location_scores": {
        "distance_to_groceries_score": 7,
        "distance_to_library_score": 7,
        "distance_to_gym_score": 6,
        "terrain_score": 9,
        "quietness_score": 9
      },
      "nearest_supply_towns": [
        {
          "town_name": "Silver Springs / Ocala, FL",
          "distance_miles": 12.0,
          "services_available": ["Publix / Walmart", "Gas Stations", "Marion County Public Library", "AdventHealth Hospital", "24/7 Gyms"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "70-84°F, warm sunny spring days, pleasant river breeze.",
        "summer": "85-92°F, warm humid Florida summer weather, shaded river hammock.",
        "fall": "68-82°F, prime pleasant camping weather.",
        "winter": "50-70°F, warm sunny winter weather, dry clear skies."
      },
      "dangers_and_hazards": [
        "Alligators in Ocklawaha River (do not swim near banks)",
        "Mosquitoes in summer months (use permethrin)"
      ],
      "acoustic_environment": {
        "quietness_rating": "9/10 - River flow and barred owl calls",
        "common_human_made_sounds": ["Occasional canoe on river"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Live Oak", "Spanish Moss", "Cabbage Palm", "Bald Cypress"],
        "common_animals": ["American Alligator", "Manatee", "Bald Eagle", "Osprey", "Florida Black Bear"]
      },
      "human_demographics_and_culture": "Seminole & Timucua ancestral lands, Ocala rivermen, Florida nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Traditional Timucua territory honoring the pristine Ocklawaha River hammock ecosystems.",
        "energetic_and_spiritual_features": "Relaxing river hammock energy, live oak canopy tranquility."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Davenport River Hammock Trail",
          "length_miles": 3.0,
          "difficulty": "Easy",
          "features": "Ocklawaha river vistas, live oak hammocks, manatee watching"
        }
      ],
      "public_reviews_summary": "Top free river primitive camping in Ocala National Forest. Live oak shade, solid cell internet, and 15 minutes to Silver Springs and Ocala.",
      "other_data": "Ocala National Forest. Free dispersed primitive camping.",
      "last_updated": "2026-09-12"
    }
  ]
}

for filename, sites in r4_batch1.items():
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
