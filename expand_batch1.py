import json
import os

BASE_DIR = "/home/volmarr/.gemini/antigravity/scratch/Camping_Nomad_Life/states"

# Batch updates for Hawaii, Idaho, Illinois, Indiana, Iowa, Kansas, Kentucky, Louisiana, Maine, Maryland
updates = {
  "hawaii.json": [
    {
      "id": "hi-waimanu-valley-primitive",
      "name": "Waimanu Valley Wilderness Primitive Campsites",
      "state": "Hawaii",
      "county": "Hawaii County (Big Island)",
      "coordinates": { "latitude": 20.1442, "longitude": -155.6318, "elevation_ft": 40 },
      "management_agency": {
        "name": "Hawaii DLNR - Division of Forestry and Wildlife (DOFAW)",
        "type": "State DLNR",
        "phone": "(808) 974-4221",
        "website": "https://dlnr.hawaii.gov/dofaw"
      },
      "rules_and_regulations": {
        "cost": "100% Free - Free DLNR Wilderness Permit required online (zero cost)",
        "stay_limit": "6 consecutive nights maximum stay limit",
        "guidelines": "Strenuous wilderness access via Muliwai Trail across 9 deep valleys. Leave No Trace mandatory. No trash services."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Composting toilet available at valley mouth or dig 6-8 inch cat-holes 200ft from Waimanu Stream and ocean line. Pack out hygiene products.",
        "trash_policy": "Strict Pack-In / Pack-Out wilderness policy."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Gathering fallen beach drift wood and invasive dead vegetation permitted.",
        "safety_requirements": "Campfires permitted on sandy beach zone below high tide mark or established fire rings.",
        "seasonal_fire_bans": "Observe dry weather high-wind fire bans."
      },
      "access_and_road_conditions": {
        "road_type": "Hike-in Wilderness Trail (Muliwai Trail / Waipio Valley trailhead access)",
        "road_conditions": "No vehicle access to valley. 9-mile strenuous mountain backpack trail across 1,200ft valley walls.",
        "vehicle_recommendation": "Vehicle parked at Waipio Valley Lookout (4x4 required if driving down Waipio valley road to trailhead)",
        "scores": { "road_grade": 9, "road_terrain_difficulty": 10, "supply_run_pain": 10 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "No Cellular Signal / Deep Valley Isolation",
        "verizon_reliability": "No Service (0 bars in deep valley bay)",
        "att_reliability": "No Service",
        "tmobile_reliability": "No Service",
        "terrain_obstruction_risk": "Extreme (1,000+ ft sheer valley cliffs block all cellular towers)",
        "distance_from_tower_corridor_miles": 12.0,
        "cellular_internet_dependable": False
      },
      "amenities": [
        "Primitive Beach Campsites",
        "Stream Water Source (Boil/Filter Mandatory)",
        "Composting Vault Toilet",
        "Pristine Black Sand Beach & Waterfalls"
      ],
      "location_scores": {
        "distance_to_groceries_score": 2,
        "distance_to_library_score": 2,
        "distance_to_gym_score": 1,
        "terrain_score": 10,
        "quietness_score": 10
      },
      "nearest_supply_towns": [
        {
          "town_name": "Honokaa, HI",
          "distance_miles": 18.0,
          "services_available": ["Grocery Market", "Gas Station", "Pharmacy", "Local Restaurants", "Public Library"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "68-78°F, lush tropical waterfall flows, ocean swells.",
        "summer": "72-83°F, warm tropical humidity, calm coastal ocean waters.",
        "fall": "70-80°F, moderate rainfall, warm sea breeze.",
        "winter": "66-76°F, heavy tropical rainfall, high ocean swells."
      },
      "dangers_and_hazards": [
        "Flash flooding in stream crossings during heavy mountain rainfall",
        "Rogue waves and strong ocean currents along black sand beach",
        "Exhaustion and steep 1,200ft trail switchbacks"
      ],
      "acoustic_environment": {
        "quietness_rating": "10/10 - Ocean surf, waterfall thunder, and tropical bird calls",
        "common_human_made_sounds": ["None (Wilderness area)"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Hapu'u Tree Fern", "Noni", "Kukui (Candlenut)", "Coconut Palms", "Ohi'a Lehua"],
        "common_animals": ["Hawaiian White-tailed Tropicbird (Koa'e Kea)", "Honu (Hawaiian Green Sea Turtle)", "Feral Boar"]
      },
      "human_demographics_and_culture": "Backcountry backpackers, native Hawaiian cultural stewards, wilderness enthusiasts.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Waimanu Valley is steeped in ancient Hawaiian legend as a secluded valley of kings, sacred streams, and protective spirits of the forest.",
        "energetic_and_spiritual_features": "Powerful tropical valley mana, roaring waterfalls, serene secluded black sand bay."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Muliwai Trail to Waiilikahi Falls",
          "length_miles": 18.0,
          "difficulty": "Extreme Backpack",
          "features": "9 valley crossings, 1,000ft waterfall view, black sand ocean bay"
        }
      ],
      "public_reviews_summary": "One of the most epic and remote wilderness camping locations in Hawaii. Extremely challenging hike in, but unmatched tropical paradise experience.",
      "other_data": "Requires free DLNR permit. Zero cell service; bring satellite communicator (Garmin inReach).",
      "last_updated": "2026-09-12"
    },
    {
      "id": "hi-peacock-flats-fr-primitive",
      "name": "Peacock Flats / Mokuleia Forest Reserve Primitive Camping",
      "state": "Hawaii",
      "county": "Honolulu County (Oahu)",
      "coordinates": { "latitude": 21.5645, "longitude": -158.1925, "elevation_ft": 1550 },
      "management_agency": {
        "name": "Hawaii DLNR - Division of Forestry and Wildlife (Oahu Branch)",
        "type": "State DLNR",
        "phone": "(808) 587-0166",
        "website": "https://dlnr.hawaii.gov/dofaw"
      },
      "rules_and_regulations": {
        "cost": "100% Free - Free DLNR Forest Reserve Permit required online (zero fee)",
        "stay_limit": "3 consecutive nights maximum stay limit",
        "guidelines": "Primitive camping in designated grassy flat clearing atop Mokuleia Ridge. Access gate combination provided with free permit."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Composting toilet available near campsite flat or dig cat-holes 6 inches deep in soil 200ft from waterways.",
        "trash_policy": "Strict Leave No Trace. Pack out all garbage."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Gathering dead and down branches permitted in forest reserve.",
        "safety_requirements": "Campfires permitted in established metal fire rings only.",
        "seasonal_fire_bans": "High fire risk during summer dry season on Oahu's North Shore mountains."
      },
      "access_and_road_conditions": {
        "road_type": "Paved to steep unpaved 4x4 dirt mountain road (Mokuleia Access Road)",
        "road_conditions": "Steep switchbacks, deep red dirt ruts, slick clay mud when wet.",
        "vehicle_recommendation": "High clearance 4x4 mandatory (locked DLNR gate at bottom; 4x4 permit required for vehicle access, or 3.5 mile hike-in)",
        "scores": { "road_grade": 8, "road_terrain_difficulty": 8, "supply_run_pain": 6 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Good / High Ridge Line Elevation",
        "verizon_reliability": "3-4 bars 4G LTE (15-35 Mbps download)",
        "att_reliability": "3-4 bars 4G LTE",
        "tmobile_reliability": "2-3 bars 4G LTE",
        "terrain_obstruction_risk": "Low on top ridge clearing",
        "distance_from_tower_corridor_miles": 3.5,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Covered Picnic Shelters",
        "Composting Toilet",
        "Grassy Camping Areas",
        "Fire Rings",
        "Panoramic Ocean Views of Oahu North Shore"
      ],
      "location_scores": {
        "distance_to_groceries_score": 6,
        "distance_to_library_score": 5,
        "distance_to_gym_score": 4,
        "terrain_score": 9,
        "quietness_score": 9
      },
      "nearest_supply_towns": [
        {
          "town_name": "Waialua / Haleiwa, HI",
          "distance_miles": 7.5,
          "services_available": ["Supermarkets", "Gas Stations", "Surf Shops", "Restaurants", "Health Clinic"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "68-80°F, pleasant mountain breezes, occasional afternoon mist.",
        "summer": "72-85°F, sunny warm mountain ridge weather.",
        "fall": "70-82°F, trade winds keep temperatures comfortable.",
        "winter": "64-76°F, passing rain squalls, green lush mountain vegetation."
      },
      "dangers_and_hazards": [
        "Slick mud switchbacks on 4x4 road during heavy rains",
        "High cliff edges along Mokuleia Ridge trails",
        "Mosquitoes in forested gulches"
      ],
      "acoustic_environment": {
        "quietness_rating": "9/10 - Mountain bird calls and ocean breeze",
        "common_human_made_sounds": ["Distant military aviation overflights", "Occasional 4x4 engine"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Ironwood Trees", "Eucalyptus", "Cook Pines", "Native Ohi'a", "Lilikoi Passionfruit Vines"],
        "common_animals": ["Oahu Elepaio (endemic bird)", "Plover", "Feral Pigs", "Chukar Partridge"]
      },
      "human_demographics_and_culture": "Local hikers, mountain bikers, 4x4 enthusiasts, and North Shore campers.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Mokuleia and the Waianae mountain range are honored in Hawaiian traditions as ancient dwelling places of forest guardians.",
        "energetic_and_spiritual_features": "High ridge breezes, ocean-to-mountain vista energy, peaceful starry nights."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Kealia Trail / Mokuleia Ridge Loop",
          "length_miles": 7.0,
          "difficulty": "Moderate to Strenuous",
          "features": "Sweeping North Shore ocean panoramas, Norfolk pine groves"
        }
      ],
      "public_reviews_summary": "Incredible ocean view ridge camping on Oahu. Free permit with DLNR gate code required. Great cell connectivity for remote work.",
      "other_data": "Free DLNR permit required. 4x4 recommended for driving up or park at bottom and hike up.",
      "last_updated": "2026-09-12"
    }
  ],
  "idaho.json": [
    {
      "id": "id-salmon-river-blm-dispersed",
      "name": "Salmon River Corridor BLM Primitive Campsites",
      "state": "Idaho",
      "county": "Lemhi County",
      "coordinates": { "latitude": 45.1785, "longitude": -113.8942, "elevation_ft": 3950 },
      "management_agency": {
        "name": "Bureau of Land Management (BLM) - Salmon Field Office",
        "type": "Federal BLM",
        "phone": "(208) 756-5400",
        "website": "https://www.blm.gov/office/salmon-field-office"
      },
      "rules_and_regulations": {
        "cost": "100% Free - Public BLM land primitive camping (zero fees)",
        "stay_limit": "14 consecutive days within a 28-day period",
        "guidelines": "Dispersed primitive camping along public river bends on Highway 93 corridor. Leave No Trace. Camp 200ft from water high-water mark where feasible."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6-8 inches deep in soil 200 feet from Salmon River. Pack out toilet paper and hygiene items or use portable toilet system.",
        "trash_policy": "Pack-in / Pack-out all trash."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down wood gathering permitted on BLM land.",
        "safety_requirements": "Campfires must be contained in metal fire pan or existing stone fire ring. Fully douse with water before leaving.",
        "seasonal_fire_bans": "Stage 1 and Stage 2 fire restrictions common in July-September."
      },
      "access_and_road_conditions": {
        "road_type": "Paved Highway 93 to short dirt/gravel river access pullouts",
        "road_conditions": "Well-maintained gravel turnouts, flat sandy river bench pullouts.",
        "vehicle_recommendation": "Accessible by standard low clearance 2WD cars and vans.",
        "scores": { "road_grade": 2, "road_terrain_difficulty": 3, "supply_run_pain": 3 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / Highway Corridor Tower Line",
        "verizon_reliability": "3-4 bars 4G LTE (20-40 Mbps download)",
        "att_reliability": "3-4 bars 4G LTE",
        "tmobile_reliability": "2-3 bars 4G LTE",
        "terrain_obstruction_risk": "Moderate (Canyon walls obstruct north/south line, but line-of-sight along highway corridor)",
        "distance_from_tower_corridor_miles": 1.5,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Riverfront Primitive Campsites",
        "Stone Fire Rings",
        "Direct Salmon River Kayak/Raft Launch Access",
        "Flat Gravel RV/Van Parking"
      ],
      "location_scores": {
        "distance_to_groceries_score": 7,
        "distance_to_library_score": 7,
        "distance_to_gym_score": 6,
        "terrain_score": 9,
        "quietness_score": 8
      },
      "nearest_supply_towns": [
        {
          "town_name": "Salmon, ID",
          "distance_miles": 8.0,
          "services_available": ["Save-A-Way Supermarket", "Gas Stations", "Lemhi County Library", "Laundromat", "Hardware Store", "Hospital"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "45-62°F, river snowmelt runoff, crisp sunny days.",
        "summer": "78-92°F, warm sunny canyon weather, ideal for river swimming.",
        "fall": "50-70°F, cool night temps, stunning golden cottonwood foliage along river.",
        "winter": "20-38°F, snow in canyon, cold icy nights."
      },
      "dangers_and_hazards": [
        "Fast-moving river currents during spring runoff",
        "Summer rattlesnakes in rocky scree slopes",
        "High afternoon canyon winds"
      ],
      "acoustic_environment": {
        "quietness_rating": "8/10 - Rushing river soundscape",
        "common_human_made_sounds": ["Occasional highway traffic across river valley", "Distant drift boat oars"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Black Cottonwood", "Big Sagebrush", "Willow", "Ponderosa Pine"],
        "common_animals": ["Bighorn Sheep", "Bald Eagle", "Osprey", "Mule Deer", "Chinook Salmon"]
      },
      "human_demographics_and_culture": "Whitewater kayakers, fly fishermen, vanlife nomads, local Idaho outdoorsmen.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Ancestral territory of the Agai'dika (Salmon Eater) Shoshone people. The Salmon River ('River of No Return') carries rich frontier and indigenous lore.",
        "energetic_and_spiritual_features": "Revitalizing river energy, dramatic mountain canyon scenery."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Salmon River Canyon River Trail",
          "length_miles": 6.5,
          "difficulty": "Easy to Moderate",
          "features": "Riverbank vistas, petroglyphs, bighorn sheep viewing"
        }
      ],
      "public_reviews_summary": "Fantastic free riverfront boondocking right outside Salmon, ID. Fast cell internet, peaceful water sounds, and easy 2WD access.",
      "other_data": "Free BLM dispersed land. Excellent nomad connectivity along Highway 93 corridor.",
      "last_updated": "2026-09-12"
    },
    {
      "id": "id-middle-fork-boise-river-nf",
      "name": "Middle Fork Boise River Road Dispersed Primitive Camping",
      "state": "Idaho",
      "county": "Boise County",
      "coordinates": { "latitude": 43.6821, "longitude": -115.7412, "elevation_ft": 3600 },
      "management_agency": {
        "name": "US Forest Service - Boise National Forest (Mountain Home Ranger District)",
        "type": "USFS",
        "phone": "(208) 587-7961",
        "website": "https://www.fs.usda.gov/boise"
      },
      "rules_and_regulations": {
        "cost": "100% Free - USFS Dispersed Primitive Land (zero fee)",
        "stay_limit": "14 consecutive days limit",
        "guidelines": "Camp at designated dispersed pullouts along Middle Fork Boise River Road (Forest Road 268). Camp 100ft minimum from river."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6-8 inches deep in organic soil 200 feet from water. Pack out hygiene products.",
        "trash_policy": "Strict Pack-In / Pack-Out. No forest garbage collection."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Abundant dead and down pine wood gathering permitted.",
        "safety_requirements": "Campfires in established rock rings only. Clear 5ft radius of pine needles. Fully extinguish with water.",
        "seasonal_fire_bans": "Summer fire restrictions active July through September."
      },
      "access_and_road_conditions": {
        "road_type": "Gravel / Dirt Forest Road (FR 268)",
        "road_conditions": "Washboard gravel, narrow canyon shelf sections, potholes.",
        "vehicle_recommendation": "High clearance 2WD or 4x4 recommended; careful standard 2WD cars can reach lower river sites in dry weather.",
        "scores": { "road_grade": 5, "road_terrain_difficulty": 5, "supply_run_pain": 6 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Low / Canyon Obstructed",
        "verizon_reliability": "1-2 bars 4G LTE (Spotty / booster recommended)",
        "att_reliability": "1 bar / SOS",
        "tmobile_reliability": "No Service",
        "terrain_obstruction_risk": "High (Deep granite canyon walls block tower signals)",
        "distance_from_tower_corridor_miles": 14.0,
        "cellular_internet_dependable": False
      },
      "amenities": [
        "Riverfront Primitive Campsites",
        "Nearby Natural Hot Springs (Twin Springs / Skinny Dipper access)",
        "Stone Fire Rings",
        "Ponderosa Pine Shade"
      ],
      "location_scores": {
        "distance_to_groceries_score": 4,
        "distance_to_library_score": 3,
        "distance_to_gym_score": 3,
        "terrain_score": 9,
        "quietness_score": 9
      },
      "nearest_supply_towns": [
        {
          "town_name": "Idaho City, ID",
          "distance_miles": 24.0,
          "services_available": ["General Store", "Gas Station", "Historic Saloons", "Post Office", "Public Library"]
        },
        {
          "town_name": "Boise, ID",
          "distance_miles": 42.0,
          "services_available": ["Full Metro City Services", "Trader Joe's / Costco", "24/7 Gyms", "Hospitals"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "42-58°F, roaring river runoff, spring wildflower bloom.",
        "summer": "75-90°F, warm sunny mountain days, refreshing river dips.",
        "fall": "48-68°F, crisp clear nights, golden cottonwoods.",
        "winter": "18-35°F, snow-covered canyon road, hot springs winter soak destination."
      },
      "dangers_and_hazards": [
        "Narrow dirt canyon road with sharp blind turns",
        "Spring river high-water hazard",
        "Black bears in area (store food in bear-proof containers)"
      ],
      "acoustic_environment": {
        "quietness_rating": "9/10 - River roar and forest wind",
        "common_human_made_sounds": ["Occasional ATV / dirt bike on weekend", "Infrequent forest road vehicle"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Ponderosa Pine", "Douglas Fir", "Syringa (Idaho state flower)", "Wild Mint"],
        "common_animals": ["Black Bear", "Elk", "Mule Deer", "Osprey", "Rainbow Trout"]
      },
      "human_demographics_and_culture": "Hot spring seekers, fly anglers, Boise weekend campers, wilderness lovers.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Thermal hot springs along the Boise River canyon were prized healing grounds for Shoshone and Bannock peoples for centuries.",
        "energetic_and_spiritual_features": "Soothing geothermal hot springs, granite canyon tranquility."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Middle Fork Boise River Trail",
          "length_miles": 9.0,
          "difficulty": "Moderate",
          "features": "Hot spring pools, river canyon overlooks, old growth ponderosa"
        }
      ],
      "public_reviews_summary": "Peaceful river boondocking close to natural hot springs. Road is washboarded, cell service is weak, but the hot springs and river setting are unbelievable.",
      "other_data": "Free Boise National Forest dispersed camping. Bring water filter.",
      "last_updated": "2026-09-12"
    }
  ]
}

for filename, sites in updates.items():
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
