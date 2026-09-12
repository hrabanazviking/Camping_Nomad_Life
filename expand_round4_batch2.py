import json
import os

BASE_DIR = "/home/volmarr/.gemini/antigravity/scratch/Camping_Nomad_Life/states"

r4_batch2 = {
  "georgia.json": [
    {
      "id": "ga-cohutta-wilderness-jacks-river",
      "name": "Cohutta Wilderness Jacks River Primitive Camping",
      "state": "Georgia",
      "county": "Fannin / Murray County",
      "coordinates": { "latitude": 34.9412, "longitude": -84.6512, "elevation_ft": 1450 },
      "management_agency": {
        "name": "US Forest Service - Chattahoochee-Oconee National Forests (Conasauga Ranger District)",
        "type": "USFS",
        "phone": "(706) 695-6736",
        "website": "https://www.fs.usda.gov/conf"
      },
      "rules_and_regulations": {
        "cost": "100% Free - USFS Wilderness Dispersed Primitive Camping (zero fee)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed wilderness camping permitted throughout Cohutta Wilderness along Jacks River and Conasauga River corridors. Camp 100ft minimum from water."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6-8 inches deep in soil 200 feet from Jacks River. Pack out hygiene products.",
        "trash_policy": "Strict Leave No Trace."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down wood gathering permitted on site.",
        "safety_requirements": "Campfires in established rock fire rings only. Fully douse with water before vacating.",
        "seasonal_fire_bans": "Fall dry leaf fire warnings."
      },
      "access_and_road_conditions": {
        "road_type": "Paved county road to gravel Forest Service roads (FR 68)",
        "road_conditions": "Graded gravel access roads, flat trailhead parking.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance passenger cars.",
        "scores": { "road_grade": 3, "road_terrain_difficulty": 3, "supply_run_pain": 4 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Moderate / High Ridge Signal",
        "verizon_reliability": "3-4 bars 4G LTE on high wilderness ridges",
        "att_reliability": "3-4 bars 4G LTE",
        "tmobile_reliability": "2-3 bars 4G LTE",
        "terrain_obstruction_risk": "Moderate inside deep hemlock river gorge",
        "distance_from_tower_corridor_miles": 4.5,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Jacks River Falls & Gorge Overlooks",
        "Hemlock & Oak Wilderness Canopy",
        "Jacks River Trout Water Source (Filter mandatory)",
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
          "town_name": "Ellijay / Blue Ridge, GA",
          "distance_miles": 16.0,
          "services_available": ["Ingles Supermarket", "Gas Stations", "Gilmer County Library", "Hospital", "Restaurants"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "55-70°F, roaring waterfall flows, blooming mountain laurel.",
        "summer": "75-88°F, refreshing mountain river swimming weather.",
        "fall": "50-70°F, world-class North Georgia autumn foliage.",
        "winter": "30-48°F, mild winter, crisp mountain air."
      },
      "dangers_and_hazards": [
        "Black bears in Cohutta Wilderness (bear hang or canister mandatory)",
        "Flash flooding in Jacks River gorge during heavy thunderstorms"
      ],
      "acoustic_environment": {
        "quietness_rating": "10/10 - Roaring waterfall thunder and hemlock forest wind",
        "common_human_made_sounds": ["None inside wilderness boundary"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Eastern Hemlock", "Catawba Rhododendron", "White Oak", "Shortleaf Pine"],
        "common_animals": ["Black Bear", "Native Brook Trout", "White-tailed Deer", "Wild Turkey"]
      },
      "human_demographics_and_culture": "Cherokee ancestral lands, North Georgia wilderness woodsmen, backpackers, nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Largest wilderness area east of the Mississippi outside Florida. Sacred Cherokee territory honoring Jacks River Falls.",
        "energetic_and_spiritual_features": "Thunderous waterfall power, serene old-growth hemlock forest quietness."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Jacks River Trail",
          "length_miles": 16.0,
          "difficulty": "Strenuous",
          "features": "40+ river crossings, Jacks River Falls, old-growth hemlocks"
        }
      ],
      "public_reviews_summary": "Georgia's premier wilderness primitive camping. Roaring waterfalls, ancient hemlocks, fast cell internet on high ridges, and 100% free USFS access.",
      "other_data": "Chattahoochee National Forest. Free wilderness dispersed camping.",
      "last_updated": "2026-09-12"
    }
  ],
  "idaho.json": [
    {
      "id": "id-sawtooth-nf-pole-creek",
      "name": "Pole Creek Dispersed Camping Area",
      "state": "Idaho",
      "county": "Custer / Blaine County",
      "coordinates": { "latitude": 43.8812, "longitude": -114.6812, "elevation_ft": 7300 },
      "management_agency": {
        "name": "US Forest Service - Sawtooth National Forest (Sawtooth NRA)",
        "type": "USFS",
        "phone": "(208) 727-5000",
        "website": "https://www.fs.usda.gov/sawtooth"
      },
      "rules_and_regulations": {
        "cost": "100% Free - USFS Dispersed Primitive Camping (zero fee)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed primitive camping permitted at designated pullouts along Pole Creek Road (FR 197). Camp 100ft minimum from creek."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6-8 inches deep in mountain soil 200 feet from Pole Creek. Pack out all paper.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Abundant dead and down lodgepole pine wood gathering permitted.",
        "safety_requirements": "Campfires in established rock fire rings only. Fully douse with water before vacating.",
        "seasonal_fire_bans": "Summer dry mountain fire restrictions active July-September."
      },
      "access_and_road_conditions": {
        "road_type": "Paved ID 75 (Sawtooth Scenic Byway) to gravel Forest Service Road (FR 197)",
        "road_conditions": "Paved main highway access, smooth gravel forest road pullouts.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance passenger cars.",
        "scores": { "road_grade": 3, "road_terrain_difficulty": 3, "supply_run_pain": 4 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / Sawtooth Valley Tower Line",
        "verizon_reliability": "3-4 bars 4G LTE along ID 75 / Pole Creek valley entrance",
        "att_reliability": "3-4 bars 4G LTE",
        "tmobile_reliability": "2-3 bars 4G LTE",
        "terrain_obstruction_risk": "Low across open high Sawtooth valley basin",
        "distance_from_tower_corridor_miles": 3.5,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Unrivaled Sawtooth Peak Jagged Skyline Panoramas",
        "Lodgepole Pine Shade",
        "Flat Gravel RV & Van Pullouts",
        "Stone Fire Rings"
      ],
      "location_scores": {
        "distance_to_groceries_score": 6,
        "distance_to_library_score": 6,
        "distance_to_gym_score": 5,
        "terrain_score": 10,
        "quietness_score": 9
      },
      "nearest_supply_towns": [
        {
          "town_name": "Stanley, ID",
          "distance_miles": 18.0,
          "services_available": ["Mountain Village Mercantile", "Gas Stations", "Stanley Community Library", "Restaurants", "Outfitters"]
        },
        {
          "town_name": "Ketchum / Sun Valley, ID",
          "distance_miles": 34.0,
          "services_available": ["Atkinsons' Market", "Full Resort City Services", "St. Luke's Hospital", "24/7 Gyms"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "38-52°F, snow melt in Sawtooth valley, crisp mountain air.",
        "summer": "70-84°F, prime Idaho mountain camping, clear blue skies.",
        "fall": "45-65°F, golden quaking aspen foliage, chilly starry nights.",
        "winter": "10-25°F, heavy snowpack, road closed to wheeled vehicles."
      },
      "dangers_and_hazards": [
        "Black bears and wolves in Sawtooth NRA (store food securely)",
        "High altitude sun exposure (7,300+ ft)"
      ],
      "acoustic_environment": {
        "quietness_rating": "9/10 - Mountain wind and Pole Creek cascades",
        "common_human_made_sounds": ["Occasional vehicle on Pole Creek road"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Lodgepole Pine", "Quaking Aspen", "Douglas Fir", "Idaho Syringa"],
        "common_animals": ["Elk", "Mule Deer", "Gray Wolf", "Osprey", "Chinook Salmon", "Bald Eagle"]
      },
      "human_demographics_and_culture": "Shoshone-Bannock ancestral lands, Sawtooth NRA guides, Idaho outdoorsmen, nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Sacred ancestral territory of the Shoshone and Bannock tribes honoring the sharp granite spires of the Sawtooth range.",
        "energetic_and_spiritual_features": "Profound Sawtooth mountain peak reflection energy, crystalline mountain creek clarity."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Pole Creek to Galena Summit Trail",
          "length_miles": 6.5,
          "difficulty": "Moderate",
          "features": "Sawtooth valley vistas, alpine meadows, lodgepole forest"
        }
      ],
      "public_reviews_summary": "Idaho's single best free Sawtooth peak view boondocking. Jagged mountain skyline views, fast cell internet near Stanley, and 100% free USFS access.",
      "other_data": "Sawtooth National Forest Sawtooth NRA. Free dispersed primitive camping.",
      "last_updated": "2026-09-12"
    }
  ]
}

for filename, sites in r4_batch2.items():
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
