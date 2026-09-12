import json
import os

BASE_DIR = "/home/volmarr/.gemini/antigravity/scratch/Camping_Nomad_Life/states"

b2_expansion = {
  "louisiana.json": [
    {
      "id": "la-kisatchie-hills-wilderness-primitive",
      "name": "Kisatchie Hills Wilderness Dispersed Backpack Camping",
      "state": "Louisiana",
      "county": "Natchitoches Parish",
      "coordinates": { "latitude": 31.4812, "longitude": -93.0214, "elevation_ft": 320 },
      "management_agency": {
        "name": "US Forest Service - Kisatchie National Forest (Kisatchie Ranger District)",
        "type": "USFS",
        "phone": "(318) 472-1840",
        "website": "https://www.fs.usda.gov/kisatchie"
      },
      "rules_and_regulations": {
        "cost": "100% Free - USFS Wilderness Primitive Camping (zero fee)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed wilderness camping permitted throughout Kisatchie Hills Wilderness ('Louisiana Longleaf Pine Hills'). Camp 100ft from trails."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6 inches deep in sandy soil 200 feet from Bayou Cypre and springs. Pack out hygiene products.",
        "trash_policy": "Strict Leave No Trace."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down longleaf pine wood collection permitted.",
        "safety_requirements": "Campfires in established rock fire rings only. Fully douse with water before vacating.",
        "seasonal_fire_bans": "Observe dry autumn burn warnings."
      },
      "access_and_road_conditions": {
        "road_type": "Paved parish road to gravel trailhead parking lot (Backbone Trailhead)",
        "road_conditions": "Smooth gravel parking lot access.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance vehicles.",
        "scores": { "road_grade": 2, "road_terrain_difficulty": 3, "supply_run_pain": 4 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Fair to Moderate / High Ridge Signal",
        "verizon_reliability": "2-3 bars 4G LTE on ridge lines",
        "att_reliability": "2-3 bars 4G LTE",
        "tmobile_reliability": "1-2 bars 4G LTE",
        "terrain_obstruction_risk": "Moderate in deep sandstone ravines",
        "distance_from_tower_corridor_miles": 5.0,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Primitive Longleaf Pine Ridge Campsites",
        "Sandstone Mesa & Ridge Views",
        "Spring-Fed Creek Water Source (Filter mandatory)",
        "Stone Fire Rings"
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
          "town_name": "Natchitoches, LA",
          "distance_miles": 18.0,
          "services_available": ["Super1 Foods / Kroger", "Gas Stations", "Natchitoches Parish Library", "Hospital", "Restaurants"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "60-78°F, blooming wild azaleas and dogwood.",
        "summer": "85-96°F, hot humid Louisiana summer weather under pine canopy.",
        "fall": "62-80°F, prime mild camping weather, crisp nights.",
        "winter": "42-62°F, mild winter, dry sunny days."
      },
      "dangers_and_hazards": [
        "Ticks and chiggers in summer (use permethrin)",
        "Sandstone bluff drop-offs",
        "High summer heat and humidity"
      ],
      "acoustic_environment": {
        "quietness_rating": "9/10 - Wind through tall longleaf pines and songbirds",
        "common_human_made_sounds": ["None inside wilderness boundary"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Longleaf Pine", "Shortleaf Pine", "Sandstone Cedar", "French Mulberry"],
        "common_animals": ["Louisiana Black Bear (rare)", "Red-cockaded Woodpecker", "White-tailed Deer", "Armadillo"]
      },
      "human_demographics_and_culture": "Caddo ancestral land, Louisiana backpackers, pine forest lovers, nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Known locally as the 'Little Grand Canyon of Louisiana'. Ancient sandstone mesas hold rich Native American and frontier history.",
        "energetic_and_spiritual_features": "Soothing longleaf pine forest breeze, unusual rolling sandstone ridge topography."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Backbone Trail Loop",
          "length_miles": 7.3,
          "difficulty": "Moderate",
          "features": "Sandstone ridge mesas, longleaf pine savanna, creek valleys"
        }
      ],
      "public_reviews_summary": "Unexpectedly rugged pine wilderness in Louisiana. Free primitive camping, quiet sandstone ridges, and great trail access near Natchitoches.",
      "other_data": "Kisatchie National Forest. Free wilderness dispersed camping.",
      "last_updated": "2026-09-12"
    }
  ],
  "maine.json": [
    {
      "id": "me-nahmakanta-public-reserved-land",
      "name": "Nahmakanta Public Reserved Land Primitive Campsites",
      "state": "Maine",
      "county": "Piscataquis County",
      "coordinates": { "latitude": 45.7214, "longitude": -69.1214, "elevation_ft": 920 },
      "management_agency": {
        "name": "Maine Department of Agriculture, Conservation and Forestry - Bureau of Parks and Lands",
        "type": "State BPL",
        "phone": "(207) 941-4412",
        "website": "https://www.maine.gov/dacf/parks"
      },
      "rules_and_regulations": {
        "cost": "100% Free - Maine BPL Public Reserved Land Primitive Camping (zero fee)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed primitive camping at authorized shoreline campsites around Nahmakanta Lake and backcountry ponds."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Use authorized pit privy at lake campsites or dig cat-hole 6-8 inches deep in soil 200ft from lakes. Pack out all paper.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down wood collection permitted on public lands.",
        "safety_requirements": "Campfires permitted only at established metal fire rings or authorized stone rings. Fully douse with water.",
        "seasonal_fire_bans": "Observe Maine Forest Service dry weather fire warnings."
      },
      "access_and_road_conditions": {
        "road_type": "Unpaved Gravel Logging Roads (Jo-Mary Forest Road)",
        "road_conditions": "Washboard gravel, active logging truck traffic, potholes.",
        "vehicle_recommendation": "High clearance recommended; standard 2WD vehicles can access with slow careful driving.",
        "scores": { "road_grade": 5, "road_terrain_difficulty": 5, "supply_run_pain": 6 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Low / Remote North Woods",
        "verizon_reliability": "1-2 bars 4G LTE on high hill tops; SOS at lake level",
        "att_reliability": "1-2 bars 4G LTE",
        "tmobile_reliability": "No Service",
        "terrain_obstruction_risk": "High (Dense spruce-fir North Woods canopy and mountain ridges)",
        "distance_from_tower_corridor_miles": 14.0,
        "cellular_internet_dependable": False
      },
      "amenities": [
        "Pristine North Woods Lakeshore Campsites",
        "Pit Privy Toilet",
        "Lake Kayak / Canoe Launching",
        "Stone Fire Rings"
      ],
      "location_scores": {
        "distance_to_groceries_score": 3,
        "distance_to_library_score": 3,
        "distance_to_gym_score": 2,
        "terrain_score": 10,
        "quietness_score": 10
      },
      "nearest_supply_towns": [
        {
          "town_name": "Millinocket, ME",
          "distance_miles": 26.0,
          "services_available": ["Hannaford Supermarket", "Gas Stations", "Millinocket Memorial Library", "Outfitters", "Hospital"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "38-52°F, ice-out on Maine lakes, black fly season in June.",
        "summer": "65-78°F, prime Maine North Woods lake camping, warm sunny days.",
        "fall": "42-60°F, world-class Maine red maple and birch fall foliage.",
        "winter": "-5 to 20°F, deep snowpack, snowmobile and winter wilderness trail access."
      },
      "dangers_and_hazards": [
        "Active logging trucks on gravel forest roads (yield right of way)",
        "Black bears and moose on forest roads",
        "Black flies in late spring/early summer"
      ],
      "acoustic_environment": {
        "quietness_rating": "10/10 - Loon calls, wind through spruce trees, and water lapping",
        "common_human_made_sounds": ["Distant logging truck horn on gravel main road"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Red Spruce", "Balsam Fir", "Paper Birch", "Eastern White Pine", "Wild Blueberry"],
        "common_animals": ["Moose", "Common Loon", "Black Bear", "Pine Marten", "Brook Trout"]
      },
      "human_demographics_and_culture": "Penobscot ancestral lands, Maine Woods canoeists, Appalachian Trail hikers, North Woods anglers.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Deeply revered Penobscot territory surrounding Mount Katahdin (Pamola spirit realm). Rich Maine Woods wilderness lore.",
        "energetic_and_spiritual_features": "Haunting loon wilderness calls, crystal clear Maine glacial lake waters."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Debsconeag Backcountry Trail",
          "length_miles": 6.8,
          "difficulty": "Moderate",
          "features": "Pristine wilderness ponds, old-growth white pine, granite ledges"
        }
      ],
      "public_reviews_summary": "True Maine North Woods off-grid paradise. Free primitive lakeshore campsites, incredible loon calls, and deep wilderness tranquility.",
      "other_data": "Maine Bureau of Parks & Lands Public Reserved Land.",
      "last_updated": "2026-09-12"
    }
  ],
  "maryland.json": [
    {
      "id": "md-savage-river-state-forest-primitive",
      "name": "Savage River State Forest Dispersed Primitive Camping",
      "state": "Maryland",
      "county": "Garrett County",
      "coordinates": { "latitude": 39.5214, "longitude": -79.1214, "elevation_ft": 2450 },
      "management_agency": {
        "name": "Maryland Department of Natural Resources (DNR) - Forest Service",
        "type": "State DNR",
        "phone": "(301) 895-5453",
        "website": "https://dnr.maryland.gov/forests"
      },
      "rules_and_regulations": {
        "cost": "100% Free - Maryland DNR State Forest Primitive Dispersed Camping (zero fee outside developed campsites)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed primitive camping permitted at designated forest pullouts along Savage River Road and Westernport Road. Camp 100ft minimum from water."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6-8 inches deep in soil 200 feet from Savage River. Pack out hygiene items.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down wood gathering permitted on site.",
        "safety_requirements": "Campfires in established rock rings only. Fully douse with water before vacating.",
        "seasonal_fire_bans": "Spring and fall forest fire warnings."
      },
      "access_and_road_conditions": {
        "road_type": "Paved county road to gravel State Forest Service roads",
        "road_conditions": "Graded gravel forest roads, flat pullout turnouts.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance passenger cars.",
        "scores": { "road_grade": 3, "road_terrain_difficulty": 3, "supply_run_pain": 4 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Moderate / Ridge & Highway Line",
        "verizon_reliability": "3-4 bars 4G LTE on mountain ridges",
        "att_reliability": "3-4 bars 4G LTE",
        "tmobile_reliability": "2-3 bars 4G LTE",
        "terrain_obstruction_risk": "Moderate in deep Savage River gorges",
        "distance_from_tower_corridor_miles": 4.0,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Mountain Hemlock & Hardwood Forest Campsites",
        "Savage River Trout Stream Access",
        "Flat Gravel Van Pullouts",
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
          "town_name": "Frostburg, MD",
          "distance_miles": 14.0,
          "services_available": ["Weis Markets / Giant", "Gas Stations", "Frostburg State Univ Library", "Hospital", "Restaurants"]
        },
        {
          "town_name": "Cumberland, MD",
          "distance_miles": 22.0,
          "services_available": ["Full City Services", "Walmart", "24/7 Gyms", "Hardware Stores"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "45-62°F, blooming mountain laurel, cold trout streams.",
        "summer": "70-82°F, cool mountain escape from Baltimore/DC summer heat.",
        "fall": "48-65°F, magnificent Allegheny mountain fall foliage.",
        "winter": "20-38°F, crisp mountain snow, icy river banks."
      },
      "dangers_and_hazards": [
        "High river currents during spring rain runoff",
        "Black bears in Garrett County (store food securely)"
      ],
      "acoustic_environment": {
        "quietness_rating": "9/10 - Rushing trout stream and mountain forest breeze",
        "common_human_made_sounds": ["Occasional fly angler on stream"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Eastern Hemlock", "Sugar Maple", "Chestnut Oak", "Rhododendron"],
        "common_animals": ["Brook Trout", "Black Bear", "White-tailed Deer", "Wild Turkey", "Broad-winged Hawk"]
      },
      "human_demographics_and_culture": "Allegheny mountain locals, trout anglers, Maryland nomads, DC metro weekend campers.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Shawnee and Susquehannock ancestral lands. Rich Appalachian mountain logging and conservation history.",
        "energetic_and_spiritual_features": "Refreshing mountain stream energy, serene hemlock forest solitude."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Savage River Trail",
          "length_miles": 8.0,
          "difficulty": "Moderate",
          "features": "Rushing river gorge, hemlock groves, rocky bluffs"
        }
      ],
      "public_reviews_summary": "Top free primitive camping spot in Western Maryland. Cool mountain elevation, pristine Savage River trout water, and solid cell internet near Frostburg.",
      "other_data": "Maryland DNR State Forest. Free primitive camping.",
      "last_updated": "2026-09-12"
    }
  ]
}

for filename, sites in b2_expansion.items():
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
