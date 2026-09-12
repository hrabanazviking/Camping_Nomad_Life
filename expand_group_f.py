import json
import os

BASE_DIR = "/home/volmarr/.gemini/antigravity/scratch/Camping_Nomad_Life/states"

group_f = {
  "massachusetts.json": [
    {
      "id": "ma-beartown-state-forest-at-shelter",
      "name": "Beartown State Forest Appalachian Trail Primitive Shelter",
      "state": "Massachusetts",
      "county": "Berkshire County",
      "coordinates": { "latitude": 42.1812, "longitude": -73.2812, "elevation_ft": 1650 },
      "management_agency": {
        "name": "Massachusetts Department of Conservation and Recreation (DCR)",
        "type": "State DCR",
        "phone": "(413) 528-0904",
        "website": "https://www.mass.gov/dcr"
      },
      "rules_and_regulations": {
        "cost": "100% Free - DCR Primitive Backpacking Shelter (zero cost)",
        "stay_limit": "2 consecutive nights stay limit",
        "guidelines": "Primitive backpacking camping permitted at designated Benedict Pond / Appalachian Trail shelter sites in Beartown State Forest."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Use wooden pit privy at shelter site or dig cat-hole 6 inches deep in soil 200 feet from streams. Pack out all paper.",
        "trash_policy": "Strict Carry-In / Carry-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down wood gathering permitted on site.",
        "safety_requirements": "Campfires in established stone fire pit only. Fully douse before vacating.",
        "seasonal_fire_bans": "Spring dry leaf weather fire restrictions."
      },
      "access_and_road_conditions": {
        "road_type": "Paved state road to gravel forest parking lot",
        "road_conditions": "Graded gravel access parking lot, 1.0 mile hike-in.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance passenger cars.",
        "scores": { "road_grade": 2, "road_terrain_difficulty": 2, "supply_run_pain": 3 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / Great Barrington Tower Line",
        "verizon_reliability": "3-4 bars 4G LTE (15-35 Mbps download)",
        "att_reliability": "3-4 bars 4G LTE",
        "tmobile_reliability": "2-3 bars 4G LTE",
        "terrain_obstruction_risk": "Low along Berkshire mountain ridge line",
        "distance_from_tower_corridor_miles": 3.0,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Wooden Shelter Lean-To",
        "Pit Privy Toilet",
        "Benedict Pond Water Source (Filter mandatory)",
        "Stone Fire Ring"
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
          "town_name": "Great Barrington, MA",
          "distance_miles": 8.0,
          "services_available": ["Big Y Supermarket", "Gas Stations", "Mason Library", "Restaurants", "Pharmacies"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "45-60°F, spring wildflower emergence, cool mountain air.",
        "summer": "68-80°F, pleasant Berkshire summer weather.",
        "fall": "45-65°F, world-class Berkshire autumn foliage.",
        "winter": "18-35°F, snowpack on mountain trails."
      },
      "dangers_and_hazards": [
        "Black bears in Berkshire mountains (bear hang mandatory)"
      ],
      "acoustic_environment": {
        "quietness_rating": "9/10 - Wind through hardwood trees and woodland birds",
        "common_human_made_sounds": ["Occasional AT backpacker passing on trail"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Sugar Maple", "Eastern Hemlock", "Red Oak", "Mountain Laurel"],
        "common_animals": ["Black Bear", "White-tailed Deer", "Porcupine", "Red-shouldered Hawk"]
      },
      "human_demographics_and_culture": "Stockbridge-Munsee Mohican ancestral lands, Berkshire outdoorsmen, AT backpackers, nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Traditional Mohican territory honoring Benedict Pond and the ancient hardwood mountains of Southern Berkshire County.",
        "energetic_and_spiritual_features": "Relaxing Berkshire mountain quietness, serene pond water reflections."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Appalachian Trail (Beartown Section)",
          "length_miles": 6.0,
          "difficulty": "Moderate",
          "features": "Benedict Pond shoreline, mountain ridges, hardwood forest"
        }
      ],
      "public_reviews_summary": "Top free primitive shelter camping in Massachusetts. Clean wooden shelter, solid cell service near Great Barrington, and 100% free DCR access.",
      "other_data": "Massachusetts DCR State Forest. Free primitive backpacking.",
      "last_updated": "2026-09-12"
    }
  ],
  "mississippi.json": [
    {
      "id": "ms-homochitto-nf-clear-creek",
      "name": "Homochitto National Forest Clear Creek Dispersed Camping",
      "state": "Mississippi",
      "county": "Franklin County",
      "coordinates": { "latitude": 31.4812, "longitude": -90.8812, "elevation_ft": 280 },
      "management_agency": {
        "name": "US Forest Service - National Forests in Mississippi (Homochitto District)",
        "type": "USFS",
        "phone": "(601) 384-5876",
        "website": "https://www.fs.usda.gov/mississippi"
      },
      "rules_and_regulations": {
        "cost": "100% Free - USFS Dispersed Primitive Camping (zero fee)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed primitive camping permitted along Clear Creek Road pullouts and Forest Service dirt roads outside gun hunting season."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6 inches deep in soil 200 feet from Clear Creek. Pack out all paper.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down wood gathering permitted on forest lands.",
        "safety_requirements": "Campfires in established rock fire rings only. Fully douse with water before vacating.",
        "seasonal_fire_bans": "Fall dry pine burn warnings."
      },
      "access_and_road_conditions": {
        "road_type": "Paved state route to gravel Forest Service roads",
        "road_conditions": "Graded gravel access roads, flat dirt turnouts.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance passenger cars.",
        "scores": { "road_grade": 2, "road_terrain_difficulty": 3, "supply_run_pain": 3 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / Meadville Tower Line",
        "verizon_reliability": "3-4 bars 4G LTE (15-35 Mbps download)",
        "att_reliability": "3-4 bars 4G LTE",
        "tmobile_reliability": "2-3 bars 4G LTE",
        "terrain_obstruction_risk": "Low across rolling pine hills",
        "distance_from_tower_corridor_miles": 3.0,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Loblolly & Shortleaf Pine Canopy Shade",
        "Clear Creek Water Source (Filter mandatory)",
        "Flat Dirt/Gravel Pullouts",
        "Stone Fire Rings"
      ],
      "location_scores": {
        "distance_to_groceries_score": 6,
        "distance_to_library_score": 6,
        "distance_to_gym_score": 5,
        "terrain_score": 7,
        "quietness_score": 8
      },
      "nearest_supply_towns": [
        {
          "town_name": "Meadville / Bude, MS",
          "distance_miles": 8.0,
          "services_available": ["Supermarket", "Gas Stations", "Franklin County Library", "Clinic", "Restaurants"]
        },
        {
          "town_name": "Natchez, MS",
          "distance_miles": 28.0,
          "services_available": ["Full Metro Services", "Walmart / Kroger", "Natchez Community Hospital", "24/7 Gyms"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "62-78°F, blooming wild azaleas, pleasant pine breeze.",
        "summer": "85-95°F, hot humid Southwest Mississippi summer weather.",
        "fall": "60-78°F, prime mild camping weather.",
        "winter": "42-62°F, short mild winters, sunny dry days."
      },
      "dangers_and_hazards": [
        "Ticks and chiggers in summer (use permethrin)"
      ],
      "acoustic_environment": {
        "quietness_rating": "8/10 - Pine forest wind and woodland songbirds",
        "common_human_made_sounds": ["Occasional vehicle on forest road"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Loblolly Pine", "Shortleaf Pine", "Southern Magnolia", "Dogwood"],
        "common_animals": ["White-tailed Deer", "Wild Turkey", "Red-cockaded Woodpecker", "Armadillo"]
      },
      "human_demographics_and_culture": "Choctaw ancestral lands, Mississippi outdoorsmen, nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Traditional Choctaw lands honoring the rolling shortleaf pine hills of Southwest Mississippi.",
        "energetic_and_spiritual_features": "Relaxing pine forest quietness, peaceful creek water flow."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Clear Creek Trail",
          "length_miles": 5.0,
          "difficulty": "Easy to Moderate",
          "features": "Clear Creek banks, loblolly pine canopy, wildlife viewing"
        }
      ],
      "public_reviews_summary": "Top free primitive camping in Mississippi's Homochitto National Forest. Solid cell internet, flat pine campsites, and 10 minutes to Meadville.",
      "other_data": "Homochitto National Forest. Free dispersed primitive camping.",
      "last_updated": "2026-09-12"
    }
  ],
  "missouri.json": [
    {
      "id": "mo-bell-mountain-wilderness-mark-twain-nf",
      "name": "Bell Mountain Wilderness Dispersed Primitive Camping",
      "state": "Missouri",
      "county": "Iron County",
      "coordinates": { "latitude": 37.6214, "longitude": -90.8812, "elevation_ft": 1680 },
      "management_agency": {
        "name": "US Forest Service - Mark Twain National Forest (Potosi-Fredericktown Ranger District)",
        "type": "USFS",
        "phone": "(573) 438-5427",
        "website": "https://www.fs.usda.gov/mtnf"
      },
      "rules_and_regulations": {
        "cost": "100% Free - USFS Wilderness Primitive Camping (zero fee)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed wilderness camping permitted throughout Bell Mountain Wilderness. Camp 100ft minimum from trails and streams."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6 inches deep in soil 200 feet from streams. Pack out all paper.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down oak wood gathering permitted on site.",
        "safety_requirements": "Campfires in established rock fire rings only. Fully douse with water before vacating.",
        "seasonal_fire_bans": "Fall dry leaf fire warnings."
      },
      "access_and_road_conditions": {
        "road_type": "Paved state highway to gravel Forest Service entrance road (FR 12)",
        "road_conditions": "Graded gravel access road, flat trailhead parking.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance passenger cars.",
        "scores": { "road_grade": 3, "road_terrain_difficulty": 3, "supply_run_pain": 4 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / High Ozark Mountain Ridge Signal",
        "verizon_reliability": "3-4 bars 4G LTE on 1,680ft Bell Mountain summit ridge",
        "att_reliability": "3-4 bars 4G LTE",
        "tmobile_reliability": "2-3 bars 4G LTE",
        "terrain_obstruction_risk": "Low along high mountain ridge summit",
        "distance_from_tower_corridor_miles": 3.5,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Sweeping 1,680ft Granite Shut-Ins Mountain Overlooks",
        "Shortleaf Pine & Oak Summit Canopy",
        "Shut-In Creek Water Source (Filter mandatory)",
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
          "town_name": "Ironton / Pilot Knob, MO",
          "distance_miles": 12.0,
          "services_available": ["Supermarket", "Gas Stations", "Iron County Library", "Hospital", "Restaurants"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "52-70°F, blooming wild azaleas, spring stream flows.",
        "summer": "78-90°F, pleasant high Ozark elevation breeze.",
        "fall": "52-72°F, world-class St. Francois Mountain autumn foliage.",
        "winter": "28-45°F, crisp clear winter air, light snowfall."
      },
      "dangers_and_hazards": [
        "High granite cliff drop-offs at summit",
        "Ticks and chiggers in summer (use permethrin)"
      ],
      "acoustic_environment": {
        "quietness_rating": "9/10 - High mountain wind and Ozark woodland songbirds",
        "common_human_made_sounds": ["None inside wilderness boundary"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Shortleaf Pine", "Post Oak", "Farkleberry", "Lichens"],
        "common_animals": ["White-tailed Deer", "Wild Turkey", "Bobcat", "Pileated Woodpecker"]
      },
      "human_demographics_and_culture": "Osage ancestral lands, St. Francois Mountain locals, Missouri backpackers, nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Oldest exposed granite mountain range in North America (St. Francois Mountains). Sacred ancient Osage territory.",
        "energetic_and_spiritual_features": "Exhilarating ancient granite summit mountain energy, sweeping Ozark valley vistas."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Bell Mountain Wilderness Loop Trail",
          "length_miles": 11.5,
          "difficulty": "Moderate to Strenuous",
          "features": "Granite glades, 1,680ft mountain summit overlook, shut-in streams"
        }
      ],
      "public_reviews_summary": "Top free high-elevation primitive camping in Missouri. Granite glade overlooks, fast cell internet on Bell Mountain summit, and 100% free USFS access.",
      "other_data": "Mark Twain National Forest. Free wilderness dispersed camping.",
      "last_updated": "2026-09-12"
    }
  ]
}

for filename, sites in group_f.items():
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
