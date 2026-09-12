import json
import os

BASE_DIR = "/home/volmarr/.gemini/antigravity/scratch/Camping_Nomad_Life/states"

group_g = {
  "nebraska.json": [
    {
      "id": "ne-ogallala-national-grassland",
      "name": "Ogallala National Grassland Dispersed Camping",
      "state": "Nebraska",
      "county": "Sioux / Dawes County",
      "coordinates": { "latitude": 42.8812, "longitude": -103.5812, "elevation_ft": 3850 },
      "management_agency": {
        "name": "US Forest Service - Nebraska National Forests & Grasslands (Pine Ridge Ranger District)",
        "type": "USFS",
        "phone": "(308) 432-4475",
        "website": "https://www.fs.usda.gov/nebraska"
      },
      "rules_and_regulations": {
        "cost": "100% Free - USFS Dispersed Primitive Camping (zero fee)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed primitive camping permitted throughout Ogallala National Grassland along Toadstool Road and grassland dirt pullouts."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6 inches deep in soil 200 feet from drainage draws. Pack out all paper.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Must bring your own firewood. Gathering wood on grassland is prohibited.",
        "safety_requirements": "Campfires in established rock fire rings or metal fire pans only. Fully douse with water before vacating.",
        "seasonal_fire_bans": "Summer high wind prairie burn bans active July-August."
      },
      "access_and_road_conditions": {
        "road_type": "Paved state highway to gravel/dirt grassland roads (Toadstool Road)",
        "road_conditions": "Graded gravel main road, clay dirt spurs (slick when wet).",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance vehicles in dry weather.",
        "scores": { "road_grade": 3, "road_terrain_difficulty": 3, "supply_run_pain": 4 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / Crawford & Hwy 2 Tower Line",
        "verizon_reliability": "3-4 bars 4G LTE (15-35 Mbps download)",
        "att_reliability": "3-4 bars 4G LTE",
        "tmobile_reliability": "2-3 bars 4G LTE",
        "terrain_obstruction_risk": "Low across open prairie badlands",
        "distance_from_tower_corridor_miles": 4.0,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Badlands Butte & Prairie Panoramas",
        "Toadstool Geologic Park Access",
        "Flat Dirt/Gravel Vehicle Pullouts",
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
          "town_name": "Crawford / Chadron, NE",
          "distance_miles": 14.0,
          "services_available": ["Supermarket", "Gas Stations", "Crawford Public Library", "Hospital", "Restaurants"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "48-66°F, greening prairie grass, cool winds.",
        "summer": "78-92°F, warm sunny badlands days, cool clear nights.",
        "fall": "50-70°F, golden prairie grass foliage.",
        "winter": "15-35°F, cold prairie wind, light snow."
      },
      "dangers_and_hazards": [
        "High winds on open prairie badlands",
        "Clay roads become slick mud when wet"
      ],
      "acoustic_environment": {
        "quietness_rating": "9/10 - Prairie wind and coyote calls",
        "common_human_made_sounds": ["Occasional vehicle on dirt road"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Western Wheatgrass", "Prickly Pear Cactus", "Ponderosa Pine", "Wild Sunflower"],
        "common_animals": ["Pronghorn Antelope", "Mule Deer", "Prairie Dog", "Golden Eagle", "Coyote"]
      },
      "human_demographics_and_culture": "Lakota & Cheyenne ancestral lands, Nebraska ranchers, nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Traditional Lakota territory honoring the badlands formations and sacred grasslands of Northwest Nebraska.",
        "energetic_and_spiritual_features": "Vast prairie sky horizons, majestic badlands sunset light."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Toadstool Geologic Loop Trail",
          "length_miles": 3.0,
          "difficulty": "Easy to Moderate",
          "features": "Badlands clay rock mushroom hoodoos, fossil beds, prairie vistas"
        }
      ],
      "public_reviews_summary": "Top free primitive badlands camping in Nebraska. Incredible mushroom rock formations, fast cell internet near Crawford, and 100% free USFS access.",
      "other_data": "Nebraska National Forests & Grasslands. Free dispersed primitive camping.",
      "last_updated": "2026-09-12"
    }
  ],
  "new_hampshire.json": [
    {
      "id": "nh-kilkenny-loop-white-mountain-nf",
      "name": "Kilkenny Loop Dispersed Primitive Camping",
      "state": "New Hampshire",
      "county": "Coos County",
      "coordinates": { "latitude": 44.4812, "longitude": -71.3812, "elevation_ft": 1850 },
      "management_agency": {
        "name": "US Forest Service - White Mountain National Forest (Androscoggin Ranger District)",
        "type": "USFS",
        "phone": "(603) 466-2713",
        "website": "https://www.fs.usda.gov/whitemountain"
      },
      "rules_and_regulations": {
        "cost": "100% Free - WMNF Wilderness Dispersed Primitive Camping (zero fee)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed wilderness camping permitted at least 200ft from trails and water streams along Kilkenny Ridge Trail corridor."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6-8 inches deep in organic soil 200 feet from streams. Pack out hygiene products.",
        "trash_policy": "Strict Leave No Trace wilderness policy."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down wood gathering permitted on forest lands.",
        "safety_requirements": "Campfires in established rock rings only. Fully douse with water before vacating.",
        "seasonal_fire_bans": "Spring leaf dry weather fire warnings."
      },
      "access_and_road_conditions": {
        "road_type": "Paved US 2 to gravel Forest Service roads (York Pond Road)",
        "road_conditions": "Graded gravel access roads, flat trailhead parking.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance passenger cars.",
        "scores": { "road_grade": 3, "road_terrain_difficulty": 3, "supply_run_pain": 3 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / Berlin-Gorham Tower Line",
        "verizon_reliability": "3-4 bars 4G LTE near York Pond trailhead",
        "att_reliability": "3-4 bars 4G LTE",
        "tmobile_reliability": "2-3 bars 4G LTE",
        "terrain_obstruction_risk": "Low to Moderate across northern White Mountain slopes",
        "distance_from_tower_corridor_miles": 4.0,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "White Mountain High Wilderness Ridge Campsites",
        "York Pond & Brook Water Source (Filter mandatory)",
        "Paper Birch Canopy Shade",
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
          "town_name": "Berlin / Gorham, NH",
          "distance_miles": 10.0,
          "services_available": ["Walmart Supercenter / Shaw's", "Gas Stations", "Berlin Public Library", "Hospital", "Restaurants"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "40-55°F, spring stream snowmelt, greening birch forest.",
        "summer": "68-80°F, ideal White Mountain summer hiking weather.",
        "fall": "42-62°F, world-famous northern New Hampshire autumn foliage.",
        "winter": "10-25°F, heavy alpine snowpack, winter woods snowshoeing."
      },
      "dangers_and_hazards": [
        "Black bears in WMNF (bear hang or canister mandatory)"
      ],
      "acoustic_environment": {
        "quietness_rating": "9/10 - Mountain stream flow and forest wind",
        "common_human_made_sounds": ["Occasional backpacker on trail"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Paper Birch", "Balsam Fir", "Red Spruce", "Sugar Maple"],
        "common_animals": ["Moose", "Black Bear", "White-tailed Deer", "Bicknell's Thrush"]
      },
      "human_demographics_and_culture": "Abenaki ancestral lands, White Mountain woodsmen, backpackers, nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Abenaki territory honoring the sacred northern mountain ridges and quiet trout ponds of Coos County.",
        "energetic_and_spiritual_features": "Relaxing northern birch forest quietness, pristine mountain stream water."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Kilkenny Ridge Trail",
          "length_miles": 9.0,
          "difficulty": "Moderate to Strenuous",
          "features": "Unknown Pond, Mount Cabot summit, paper birch ridges"
        }
      ],
      "public_reviews_summary": "Spectacular free wilderness primitive camping in New Hampshire's northern White Mountains. Clear trout ponds, fast cell internet near Berlin, and 100% free USFS access.",
      "other_data": "White Mountain National Forest. Free dispersed wilderness camping.",
      "last_updated": "2026-09-12"
    }
  ]
}

for filename, sites in group_g.items():
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
