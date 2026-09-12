import json
import os

BASE_DIR = "/home/volmarr/.gemini/antigravity/scratch/Camping_Nomad_Life/states"

b3_expansion = {
  "massachusetts.json": [
    {
      "id": "ma-october-mountain-state-forest-backpack",
      "name": "October Mountain State Forest Primitive Backpack Shelter",
      "state": "Massachusetts",
      "county": "Berkshire County",
      "coordinates": { "latitude": 42.3412, "longitude": -73.1812, "elevation_ft": 1820 },
      "management_agency": {
        "name": "Massachusetts Department of Conservation and Recreation (DCR)",
        "type": "State DCR",
        "phone": "(413) 243-1778",
        "website": "https://www.mass.gov/dcr"
      },
      "rules_and_regulations": {
        "cost": "100% Free - DCR Primitive Backpacking Shelter (zero cost)",
        "stay_limit": "2 consecutive nights stay limit",
        "guidelines": "Primitive backpacking camping permitted at designated Appalachian Trail / Washington Mountain shelter sites. Carry in / carry out."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Use wooden pit privy at shelter site or dig cat-hole 6 inches deep in soil 200 feet from streams. Pack out hygiene products.",
        "trash_policy": "Strict Carry-In / Carry-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down wood gathering permitted on site.",
        "safety_requirements": "Campfires in established stone fire pit only. Fully extinguish before departing.",
        "seasonal_fire_bans": "Spring dry leaf weather fire restrictions."
      },
      "access_and_road_conditions": {
        "road_type": "Paved town road to gravel forest road parking area",
        "road_conditions": "Graded gravel access lot, 1.5 mile hike-in on trail.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance vehicles.",
        "scores": { "road_grade": 2, "road_terrain_difficulty": 3, "supply_run_pain": 3 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / High Berkshire Mountain Ridge",
        "verizon_reliability": "3-4 bars 4G LTE (15-35 Mbps download)",
        "att_reliability": "3-4 bars 4G LTE",
        "tmobile_reliability": "2-3 bars 4G LTE",
        "terrain_obstruction_risk": "Low along high mountain ridge trail",
        "distance_from_tower_corridor_miles": 3.0,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Wooden Lean-To Shelter",
        "Pit Privy Toilet",
        "Mountain Stream Water Source (Filter mandatory)",
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
          "town_name": "Lee / Lenox, MA",
          "distance_miles": 8.0,
          "services_available": ["Big Y Supermarket", "Gas Stations", "Lee Public Library", "Restaurants", "Pharmacies"]
        },
        {
          "town_name": "Pittsfield, MA",
          "distance_miles": 12.0,
          "services_available": ["Full Metro City Services", "Berkshire Medical Center", "Planet Fitness", "Hardware Stores"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "42-58°F, spring wildflower emergence, misty mountain mornings.",
        "summer": "68-80°F, pleasant Berkshire mountain summer breeze.",
        "fall": "45-65°F, world-class New England fall foliage colors.",
        "winter": "15-32°F, mountain snowpack, peaceful snowshoeing."
      },
      "dangers_and_hazards": [
        "Black bears in Berkshire mountains (bear hang for food mandatory)",
        "Ticks in summer months"
      ],
      "acoustic_environment": {
        "quietness_rating": "9/10 - Wind through hardwood forest and mountain bird calls",
        "common_human_made_sounds": ["Occasional AT backpacker passing on trail"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Sugar Maple", "American Beech", "Eastern Hemlock", "Mountain Laurel"],
        "common_animals": ["Black Bear", "White-tailed Deer", "Porcupine", "Broad-winged Hawk"]
      },
      "human_demographics_and_culture": "Mahican ancestral lands, Berkshire culture, Appalachian Trail long-distance hikers.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Herman Melville wrote 'Moby Dick' overlooking October Mountain. Rich Berkshire literary and indigenous folklore.",
        "energetic_and_spiritual_features": "Inspiring New England hardwood ridge energy, tranquil autumn mountain foliage."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Appalachian Trail (October Mountain Section)",
          "length_miles": 6.5,
          "difficulty": "Moderate",
          "features": "Hardwood forest ridges, mountain vistas, pristine brooks"
        }
      ],
      "public_reviews_summary": "Incredible free primitive shelter camping in the Berkshires. Great cell service, clean wooden lean-to, and just 15 minutes to Lee and Pittsfield.",
      "other_data": "Massachusetts DCR State Forest. Free primitive backpacking.",
      "last_updated": "2026-09-12"
    }
  ],
  "missouri.json": [
    {
      "id": "mo-paddy-creek-wilderness-mark-twain-nf",
      "name": "Paddy Creek Wilderness Dispersed Primitive Camping",
      "state": "Missouri",
      "county": "Texas County",
      "coordinates": { "latitude": 37.5812, "longitude": -92.0412, "elevation_ft": 1150 },
      "management_agency": {
        "name": "US Forest Service - Mark Twain National Forest (Houston Ranger District)",
        "type": "USFS",
        "phone": "(417) 967-4194",
        "website": "https://www.fs.usda.gov/mtnf"
      },
      "rules_and_regulations": {
        "cost": "100% Free - USFS Wilderness Primitive Camping (zero fee)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed wilderness camping permitted throughout Paddy Creek Wilderness. Camp 100ft minimum from trails and streams."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6 inches deep in soil 200 feet from Paddy Creek. Pack out all paper.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down oak wood gathering permitted on site.",
        "safety_requirements": "Campfires in established rock fire rings only. Fully douse with water before vacating.",
        "seasonal_fire_bans": "Fall dry leaf fire warnings observed."
      },
      "access_and_road_conditions": {
        "road_type": "Paved state highway to gravel Forest Service roads (FR 220)",
        "road_conditions": "Graded gravel access roads, flat trailhead parking.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance vehicles.",
        "scores": { "road_grade": 3, "road_terrain_difficulty": 3, "supply_run_pain": 4 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Fair to Moderate / Ozark Ridge Signal",
        "verizon_reliability": "2-3 bars 4G LTE on high forest ridges",
        "att_reliability": "2-3 bars 4G LTE",
        "tmobile_reliability": "1-2 bars 4G LTE",
        "terrain_obstruction_risk": "Moderate in deep Ozark stream hollows",
        "distance_from_tower_corridor_miles": 5.0,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Ozark Pine & Hardwood Ridge Campsites",
        "Paddy Creek Water Source (Filter mandatory)",
        "Bluff Overlook Views",
        "Stone Fire Rings"
      ],
      "location_scores": {
        "distance_to_groceries_score": 6,
        "distance_to_library_score": 6,
        "distance_to_gym_score": 5,
        "terrain_score": 8,
        "quietness_score": 9
      },
      "nearest_supply_towns": [
        {
          "town_name": "Houston, MO",
          "distance_miles": 14.0,
          "services_available": ["Town & Country Supermarket", "Gas Stations", "Texas County Library", "Hospital", "Restaurants"]
        },
        {
          "town_name": "Rolla, MO",
          "distance_miles": 28.0,
          "services_available": ["Walmart Supercenter", "Kroger / ALDI", "Missouri S&T Metro", "24/7 Gyms"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "52-70°F, blooming dogwood and redbuds, spring stream flows.",
        "summer": "78-92°F, warm Ozark summer weather, shaded oak forest canopy.",
        "fall": "52-72°F, spectacular Ozark hardwood autumn foliage.",
        "winter": "28-48°F, crisp clear winter air, light snowfall."
      },
      "dangers_and_hazards": [
        "Flash flooding in creek hollows during thunderstorms",
        "Ticks and chiggers in summer (use permethrin)",
        "Bluff cliff drop-offs"
      ],
      "acoustic_environment": {
        "quietness_rating": "9/10 - Creek water trickles and Ozark woodland birds",
        "common_human_made_sounds": ["None inside wilderness boundary"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Shortleaf Pine (Missouri's native pine)", "Post Oak", "Flowering Dogwood", "Wild Azalea"],
        "common_animals": ["White-tailed Deer", "Wild Turkey", "Bobcat", "Pileated Woodpecker", "Smallmouth Bass"]
      },
      "human_demographics_and_culture": "Osage ancestral lands, Ozark mountain locals, Missouri backpackers, nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Rich Ozark mountain folklore honoring the ancient pine hollows and crystal spring waters of Texas County.",
        "energetic_and_spiritual_features": "Peaceful Ozark ridge solitude, pristine pine hollow air."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Paddy Creek Wilderness Loop Trail",
          "length_miles": 17.0,
          "difficulty": "Moderate to Strenuous",
          "features": "Sandstone bluffs, pine ridges, pristine creek crossings"
        }
      ],
      "public_reviews_summary": "Ozark wilderness primitive camping at its finest. Free USFS access, serene pine ridges, and easy drive to Houston and Rolla.",
      "other_data": "Mark Twain National Forest. Free wilderness dispersed camping.",
      "last_updated": "2026-09-12"
    }
  ],
  "pennsylvania.json": [
    {
      "id": "pa-allegheny-nf-minister-creek",
      "name": "Minister Creek Trail Dispersed Primitive Camping",
      "state": "Pennsylvania",
      "county": "Warren County",
      "coordinates": { "latitude": 41.7412, "longitude": -79.1412, "elevation_ft": 1580 },
      "management_agency": {
        "name": "US Forest Service - Allegheny National Forest (Marienville Ranger District)",
        "type": "USFS",
        "phone": "(814) 927-6628",
        "website": "https://www.fs.usda.gov/allegheny"
      },
      "rules_and_regulations": {
        "cost": "100% Free - USFS Dispersed Primitive Camping (zero fee)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed primitive camping permitted along Minister Creek Trail corridor and Forest Road 420. Camp 100ft minimum from trail and creek."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6-8 inches deep in organic soil 200 feet from Minister Creek. Pack out hygiene products.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down wood gathering permitted on forest lands.",
        "safety_requirements": "Campfires in established rock fire rings only. Fully douse with water before vacating.",
        "seasonal_fire_bans": "Spring/autumn leaf weather fire warnings."
      },
      "access_and_road_conditions": {
        "road_type": "Paved PA Route 666 to gravel Forest Road 420",
        "road_conditions": "Paved main access, graded gravel forest pullouts.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance passenger cars.",
        "scores": { "road_grade": 2, "road_terrain_difficulty": 3, "supply_run_pain": 3 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Moderate / High Overlook Elevation",
        "verizon_reliability": "3-4 bars 4G LTE at Minister Creek Overlook summit",
        "att_reliability": "3-4 bars 4G LTE",
        "tmobile_reliability": "2-3 bars 4G LTE",
        "terrain_obstruction_risk": "Moderate in deep hemlock stream valleys",
        "distance_from_tower_corridor_miles": 3.5,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Gigantic Mossy Sandstone Conglomerate Boulder Overlooks",
        "Hemlock & Black Cherry Forest Canopy",
        "Minister Creek Water Source (Filter mandatory)",
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
          "town_name": "Warren, PA",
          "distance_miles": 15.0,
          "services_available": ["Tops Friendly Markets / Walmart", "Gas Stations", "Warren Public Library", "Warren General Hospital", "Restaurants"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "45-62°F, spring mountain stream runoff, lush hemlock green.",
        "summer": "70-82°F, cool Allegheny forest canopy escape from summer heat.",
        "fall": "48-65°F, magnificent black cherry and maple autumn foliage.",
        "winter": "20-35°F, heavy snowfall, winter woods trail hiking."
      },
      "dangers_and_hazards": [
        "Giant sandstone rock crevasse drop-offs (watch footing at overlooks)",
        "Black bears in Allegheny NF (bear hang for food recommended)"
      ],
      "acoustic_environment": {
        "quietness_rating": "9/10 - Rushing creek water and forest wind",
        "common_human_made_sounds": ["Occasional backpacker on trail"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Black Cherry (world famous Allegheny cherry wood)", "Eastern Hemlock", "American Beech", "Mountain Laurel"],
        "common_animals": ["Black Bear", "White-tailed Deer", "Porcupine", "Ruffed Grouse", "Native Brook Trout"]
      },
      "human_demographics_and_culture": "Seneca Nation ancestral territory, Pennsylvania lumber history, Allegheny backpackers, nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Seneca (Iroquois) lands honoring the ancient hemlock forest and giant sandstone rock labyrinths.",
        "energetic_and_spiritual_features": "Enchanting mossy boulder energy, sweeping valley outlook serenity."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Minister Creek Loop Trail",
          "length_miles": 6.6,
          "difficulty": "Moderate",
          "features": "Giant sandstone boulder labyrinths, valley overlook, stream valley"
        }
      ],
      "public_reviews_summary": "One of Pennsylvania's best free primitive camping spots. Giant mossy rock formations, fast cell service on the ridge overlook, and easy drive to Warren.",
      "other_data": "Allegheny National Forest. Free dispersed camping.",
      "last_updated": "2026-09-12"
    }
  ],
  "west_virginia.json": [
    {
      "id": "wv-monongahela-nf-dolly-sods",
      "name": "Dolly Sods Wilderness Dispersed Primitive Camping",
      "state": "West Virginia",
      "county": "Tucker / Grant County",
      "coordinates": { "latitude": 39.0214, "longitude": -79.3214, "elevation_ft": 4050 },
      "management_agency": {
        "name": "US Forest Service - Monongahela National Forest (Cheat-Potomac Ranger District)",
        "type": "USFS",
        "phone": "(304) 257-1663",
        "website": "https://www.fs.usda.gov/mnf"
      },
      "rules_and_regulations": {
        "cost": "100% Free - Monongahela NF Wilderness Dispersed Primitive Camping (zero fee)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed wilderness camping permitted along FR 75 corridor pullouts and interior wilderness trails. Camp 100ft minimum from roads and streams."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6-8 inches deep in peaty soil 200 feet from Red Creek and bogs. Pack out hygiene products.",
        "trash_policy": "Strict Leave No Trace wilderness policy."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down spruce and birch wood gathering permitted.",
        "safety_requirements": "Campfires in small rock rings using dead wood only. Fully douse with water before vacating.",
        "seasonal_fire_bans": "High mountain wind autumn dry leaf fire warnings."
      },
      "access_and_road_conditions": {
        "road_type": "Unpaved Gravel Dirt Mountain Ridge Road (Forest Road 75)",
        "road_conditions": "Washboard gravel dirt, steep mountain grade switchbacks, potholed in spots.",
        "vehicle_recommendation": "High clearance recommended; standard 2WD vehicles can access FR 75 carefully in dry weather.",
        "scores": { "road_grade": 6, "road_terrain_difficulty": 5, "supply_run_pain": 5 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / 4,000ft High Ridge Line",
        "verizon_reliability": "3-4 bars 4G LTE along FR 75 high crest pullouts",
        "att_reliability": "3-4 bars 4G LTE",
        "tmobile_reliability": "2-3 bars 4G LTE",
        "terrain_obstruction_risk": "Low along 4,000ft high plateau crest",
        "distance_from_tower_corridor_miles": 4.5,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "High-Elevation Sub-Alpine Bog & Heath Barren Landscapes",
        "Sweeping Allegheny Mountain Panoramas",
        "Red Creek Headwaters Access",
        "Stone Fire Rings"
      ],
      "location_scores": {
        "distance_to_groceries_score": 5,
        "distance_to_library_score": 5,
        "distance_to_gym_score": 4,
        "terrain_score": 10,
        "quietness_score": 10
      },
      "nearest_supply_towns": [
        {
          "town_name": "Davis / Thomas, WV",
          "distance_miles": 16.0,
          "services_available": ["Shop 'n Save Supermarket", "Gas Stations", "Five Davis Library", "Craft Breweries", "Restaurants"]
        },
        {
          "town_name": "Elkins, WV",
          "distance_miles": 34.0,
          "services_available": ["Walmart Supercenter", "Davis Medical Center", "Full City Services", "Hardware Stores"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "40-55°F, misty bog rains, blooming mountain laurel.",
        "summer": "65-78°F, cool sub-alpine summer climate, wild blueberry picking.",
        "fall": "42-60°F, world-class crimson huckleberry and maple fall foliage.",
        "winter": "10-30°F, severe Canadian-like freezing winds, snow-covered tundra landscape."
      },
      "dangers_and_hazards": [
        "Sudden severe high-elevation mountain fog and weather changes",
        "High wind gusts along exposed 4,000ft plateau",
        "Unexploded ordnance warning (historical WWII artillery testing site; stay on established trails)"
      ],
      "acoustic_environment": {
        "quietness_rating": "10/10 - High plateau mountain wind and raven calls",
        "common_human_made_sounds": ["Occasional 4x4 on FR 75 dirt road"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Red Spruce (one-sided wind-flagged trees)", "Wild Huckleberry", "Cranberry", "Mountain Ash", "Sphagnum Moss"],
        "common_animals": ["Black Bear", "Snowshoe Hare", "Raven", "Cheat Mountain Salamander", "Timber Rattlesnake"]
      },
      "human_demographics_and_culture": "Monongahela ancestral lands, West Virginia mountain outdoorsmen, wilderness backpackers, nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Unique Canadian tundra-like ecology in the heart of West Virginia. Known as one of the most ecologically distinct high plateaus in North America.",
        "energetic_and_spiritual_features": "Exhilarating sub-alpine tundra energy, vast open sky horizons, majestic sunrise vistas."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Bear Rocks to Black Sky Wilderness Loop",
          "length_miles": 11.2,
          "difficulty": "Strenuous",
          "features": "Wind-flagged spruce groves, red sandstone hoodoos, sphagnum bogs"
        }
      ],
      "public_reviews_summary": "Unrivaled sub-alpine wilderness camping in West Virginia. High 4,000ft ridge elevation with fast cell signal, wild blueberries, and Canadian-like landscapes.",
      "other_data": "Monongahela National Forest. Free wilderness dispersed camping.",
      "last_updated": "2026-09-12"
    }
  ]
}

for filename, sites in b3_expansion.items():
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
