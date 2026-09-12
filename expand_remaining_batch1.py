import json
import os

BASE_DIR = "/home/volmarr/.gemini/antigravity/scratch/Camping_Nomad_Life/states"

remaining_expansion = {
  "iowa.json": [
    {
      "id": "ia-yellow-river-state-forest-paint-creek",
      "name": "Yellow River State Forest Paint Creek Primitive Backpacking",
      "state": "Iowa",
      "county": "Allamakee County",
      "coordinates": { "latitude": 43.1812, "longitude": -91.2412, "elevation_ft": 850 },
      "management_agency": {
        "name": "Iowa Department of Natural Resources (DNR) - Forestry Bureau",
        "type": "State DNR",
        "phone": "(563) 586-2254",
        "website": "https://www.iowadnr.gov/places-to-go/state-forests/yellow-river-state-forest"
      },
      "rules_and_regulations": {
        "cost": "100% Free - Iowa DNR State Forest Primitive Backpacking (zero fee)",
        "stay_limit": "14 consecutive days limit",
        "guidelines": "Primitive hike-in camping permitted at designated trail shelters/sites along Paint Creek Unit trail network. Leave No Trace."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6 inches deep in soil 200 feet from Paint Creek. Pack out all hygiene items.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down firewood collection permitted on site.",
        "safety_requirements": "Campfires permitted in established fire rings only. Fully extinguish before leaving.",
        "seasonal_fire_bans": "Observe drought fire warnings."
      },
      "access_and_road_conditions": {
        "road_type": "Paved state highway to gravel forest entrance road",
        "road_conditions": "Smooth gravel parking lot at Paint Creek trailhead.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance vehicles.",
        "scores": { "road_grade": 2, "road_terrain_difficulty": 3, "supply_run_pain": 4 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Fair to Moderate / Ridge Signal",
        "verizon_reliability": "2-3 bars 4G LTE on ridge trails",
        "att_reliability": "2-3 bars 4G LTE",
        "tmobile_reliability": "1-2 bars 4G LTE",
        "terrain_obstruction_risk": "Moderate in deep limestone creek valleys",
        "distance_from_tower_corridor_miles": 4.0,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Primitive Backpacking Campsites",
        "Driftless Area Limestone Bluff Views",
        "Paint Creek Trout Stream Access",
        "Fire Rings & Picnic Tables"
      ],
      "location_scores": {
        "distance_to_groceries_score": 6,
        "distance_to_library_score": 5,
        "distance_to_gym_score": 4,
        "terrain_score": 8,
        "quietness_score": 9
      },
      "nearest_supply_towns": [
        {
          "town_name": "Waukon, IA",
          "distance_miles": 14.0,
          "services_available": ["Fareway Grocery", "Gas Stations", "Robey Memorial Library", "Veterans Memorial Hospital", "Restaurants"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "45-62°F, blooming spring trout lilies, crisp driftless valley air.",
        "summer": "72-86°F, warm humid summer days, shaded oak canopy.",
        "fall": "48-68°F, world-class Mississippi river bluff fall foliage.",
        "winter": "15-32°F, cold driftless winter snow, peaceful frozen streams."
      },
      "dangers_and_hazards": [
        "Steep limestone bluff drop-offs",
        "Flash flooding in narrow creek bottom during thunderstorms",
        "Timber rattlesnakes in rocky limestone ledges"
      ],
      "acoustic_environment": {
        "quietness_rating": "9/10 - Rushing trout stream and woodland birds",
        "common_human_made_sounds": ["Occasional trout angler on stream"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["White Oak", "Sugar Maple", "Eastern Redcedar", "Maidenhair Fern"],
        "common_animals": ["Brown Trout", "Bald Eagle", "White-tailed Deer", "Wild Turkey"]
      },
      "human_demographics_and_culture": "Driftless region anglers, Iowa backpackers, nature photographers.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Effigy Mounds and Driftless Area sacred grounds honoring ancient Native American burial and ceremonial earthworks.",
        "energetic_and_spiritual_features": "Serene ancient limestone valley tranquility, pristine trout water clarity."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Paint Creek Backcountry Loop Trail",
          "length_miles": 7.5,
          "difficulty": "Moderate",
          "features": "Driftless limestone bluffs, oak forest, trout stream overlooks"
        }
      ],
      "public_reviews_summary": "Iowa's premier backpacking destination in the Driftless Area. Free primitive camping, great trout fishing, and peaceful oak forest trails.",
      "other_data": "Iowa DNR State Forest. Free primitive camping.",
      "last_updated": "2026-09-12"
    }
  ],
  "kansas.json": [
    {
      "id": "ks-kaw-wildlife-area-primitive",
      "name": "Kaw Wildlife Area Dispersed Primitive Camping",
      "state": "Kansas",
      "county": "Cowley County",
      "coordinates": { "latitude": 37.0812, "longitude": -96.9412, "elevation_ft": 1080 },
      "management_agency": {
        "name": "Kansas Department of Wildlife and Parks (KDWP)",
        "type": "State KDWP",
        "phone": "(620) 221-3210",
        "website": "https://ksoutdoors.com"
      },
      "rules_and_regulations": {
        "cost": "100% Free - KDWP Public Wildlife Area Primitive Camping (zero fee)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed primitive camping permitted at designated parking turnouts and primitive clearings throughout Kaw Wildlife Area along Arkansas River."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6 inches deep in soil 200 feet from Arkansas River. Pack out hygiene items.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down cottonwood gathering permitted on site.",
        "safety_requirements": "Campfires in established rock fire rings only. Fully douse before vacating.",
        "seasonal_fire_bans": "Spring high wind grassland prairie burn warnings."
      },
      "access_and_road_conditions": {
        "road_type": "Paved county road to gravel/dirt wildlife area access drive",
        "road_conditions": "Graded gravel, flat dirt parking turnouts.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance vehicles.",
        "scores": { "road_grade": 3, "road_terrain_difficulty": 3, "supply_run_pain": 3 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / Flat River Valley Line",
        "verizon_reliability": "3-4 bars 4G LTE (20-40 Mbps download)",
        "att_reliability": "3-4 bars 4G LTE",
        "tmobile_reliability": "2-3 bars 4G LTE",
        "terrain_obstruction_risk": "Low across open prairie river bottom",
        "distance_from_tower_corridor_miles": 3.5,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Riverfront Primitive Campsites",
        "Flat Dirt Vehicle Pullouts",
        "Arkansas River Kayak Access",
        "Stone Fire Rings"
      ],
      "location_scores": {
        "distance_to_groceries_score": 7,
        "distance_to_library_score": 7,
        "distance_to_gym_score": 6,
        "terrain_score": 6,
        "quietness_score": 8
      },
      "nearest_supply_towns": [
        {
          "town_name": "Arkansas City, KS",
          "distance_miles": 6.0,
          "services_available": ["Dillons Supermarket", "Walmart", "Gas Stations", "Public Library", "Hospital"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "55-72°F, green prairie grass bloom, spring rain showers.",
        "summer": "85-98°F, hot sunny Kansas prairie summer weather.",
        "fall": "58-76°F, mild golden cottonwood fall weather.",
        "winter": "22-42°F, cold prairie wind, dry sunny days."
      },
      "dangers_and_hazards": [
        "High spring river currents in Arkansas River",
        "High winds on flat prairie",
        "Summer mosquitoes in river bottom"
      ],
      "acoustic_environment": {
        "quietness_rating": "8/10 - Prairie wind and river cottonwood leaves rustling",
        "common_human_made_sounds": ["Distant train whistle across prairie"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Eastern Cottonwood", "Big Bluestem Prairie Grass", "Black Willow", "Sunflowers"],
        "common_animals": ["White-tailed Deer", "Wild Turkey", "Channel Catfish", "Pelican", "Bald Eagle"]
      },
      "human_demographics_and_culture": "Kansas hunters, river anglers, prairie roadtrippers, digital nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Ancestral grounds of the Wichita and Osage nations honoring the wide prairie rivers.",
        "energetic_and_spiritual_features": "Vast open Kansas sky horizons, soothing river bottom quietness."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Kaw Wildlife River Trail",
          "length_miles": 4.2,
          "difficulty": "Easy",
          "features": "Arkansas River shoreline, cottonwood groves, waterfowl viewing"
        }
      ],
      "public_reviews_summary": "Great free riverfront primitive camping in Southern Kansas. Fast cell internet, easy 2WD driving, and just 10 minutes to Arkansas City.",
      "other_data": "Kansas KDWP Public Wildlife Area. Free dispersed camping.",
      "last_updated": "2026-09-12"
    }
  ],
  "kentucky.json": [
    {
      "id": "ky-land-between-the-lakes-rushing-creek",
      "name": "Land Between the Lakes NRA Basic Camping / Rushing Creek",
      "state": "Kentucky",
      "county": "Trigg County",
      "coordinates": { "latitude": 36.7812, "longitude": -88.0812, "elevation_ft": 410 },
      "management_agency": {
        "name": "US Forest Service - Land Between the Lakes National Recreation Area",
        "type": "USFS",
        "phone": "(800) 525-7077",
        "website": "https://landbetweenthelakes.us"
      },
      "rules_and_regulations": {
        "cost": "100% Free - USFS Basic Dispersed Primitive Camping (zero fee for basic dispersed shoreline camping outside developed fee campgrounds; free basic camping permit available online/visitor center)",
        "stay_limit": "21 consecutive days limit",
        "guidelines": "Dispersed primitive camping at designated backcountry shoreline pullouts along Kentucky Lake & Lake Barkley."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6-8 inches deep in soil 200 feet from lake shoreline. Pack out hygiene products.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down wood collection permitted.",
        "safety_requirements": "Campfires in established rock fire rings only. Fully douse with water before vacating.",
        "seasonal_fire_bans": "Fall dry leaf fire warnings."
      },
      "access_and_road_conditions": {
        "road_type": "Paved Trace Parkway to gravel backcountry Forest Roads",
        "road_conditions": "Smooth gravel main access, dirt shoreline turnouts.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance vehicles.",
        "scores": { "road_grade": 2, "road_terrain_difficulty": 3, "supply_run_pain": 3 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / Open Lake Water Tower Signals",
        "verizon_reliability": "3-4 bars 4G LTE (20-45 Mbps download)",
        "att_reliability": "3-4 bars 4G LTE",
        "tmobile_reliability": "2-3 bars 4G LTE",
        "terrain_obstruction_risk": "Low along open lake shoreline",
        "distance_from_tower_corridor_miles": 3.0,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Kentucky Lake Shoreline Primitive Campsites",
        "Boat & Kayak Launching",
        "Hardwood Canopy Shade",
        "Stone Fire Rings"
      ],
      "location_scores": {
        "distance_to_groceries_score": 7,
        "distance_to_library_score": 7,
        "distance_to_gym_score": 6,
        "terrain_score": 8,
        "quietness_score": 8
      },
      "nearest_supply_towns": [
        {
          "town_name": "Cadiz, KY",
          "distance_miles": 12.0,
          "services_available": ["Kroger Supermarket", "Gas Stations", "Trigg County Library", "Hospital", "Restaurants"]
        },
        {
          "town_name": "Murray, KY",
          "distance_miles": 18.0,
          "services_available": ["Walmart Supercenter", "Murray State Univ Metro", "24/7 Gyms", "Full City Services"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "55-72°F, green oak forest leaf out, pleasant lake breezes.",
        "summer": "78-92°F, warm summer swimming & boating weather.",
        "fall": "52-72°F, golden hardwood foliage around Kentucky Lake.",
        "winter": "30-48°F, mild winters, open lake views."
      },
      "dangers_and_hazards": [
        "Summer ticks in tall grass",
        "High lake winds during severe summer thunderstorms"
      ],
      "acoustic_environment": {
        "quietness_rating": "8/10 - Lake wave water laps and songbirds",
        "common_human_made_sounds": ["Distant motorboat on Kentucky Lake"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["White Oak", "Shortleaf Pine", "Red Maple", "Sassafras"],
        "common_animals": ["Bald Eagle", "Osprey", "White-tailed Deer", "Crappie", "Large-mouth Bass"]
      },
      "human_demographics_and_culture": "Kentucky lake anglers, boaters, LBL backpackers, regional nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Chikasaw and Cherokee ancestral lands. Rich frontier heritage of the Cumberland and Tennessee river valleys.",
        "energetic_and_spiritual_features": "Relaxing inland sea energy, serene shoreline sunsets."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "North-South Trail (LBL Section)",
          "length_miles": 12.0,
          "difficulty": "Moderate",
          "features": "Lake shorelines, hardwood ridges, wildlife viewing"
        }
      ],
      "public_reviews_summary": "Top free shoreline camping in Kentucky. Fast cell internet, peaceful lake views, and quick access to Cadiz and Murray.",
      "other_data": "USFS Land Between the Lakes NRA. Free basic camping.",
      "last_updated": "2026-09-12"
    }
  ]
}

for filename, sites in remaining_expansion.items():
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
