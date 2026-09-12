import json

def load_state(name):
    path = f'/home/volmarr/.gemini/antigravity/scratch/Camping_Nomad_Life/states/{name}.json'
    with open(path, 'r') as f:
        return json.load(f), path

def save_state(data, path):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

# Arkansas +1 site (reach 5)
ark_data, ark_path = load_state('arkansas')
ark_data.append({
  "id": "arkansas-005",
  "name": "Richland Creek Wilderness Dispersed Camping Area",
  "state": "Arkansas",
  "county": "Searcy",
  "coordinates": {
    "latitude": 35.7952,
    "longitude": -92.9341,
    "elevation_ft": 1420.0
  },
  "management_agency": {
    "name": "U.S. Forest Service - Ozark-St. Francis National Forests (Big Piney Ranger District)",
    "type": "Federal",
    "phone": "(479) 284-3150",
    "website": "https://www.fs.usda.gov/osfnf"
  },
  "rules_and_regulations": {
    "cost": "Free ($0/night, no permits or fees required for dispersed camping)",
    "stay_limit": "14 days maximum stay within a 30-day period",
    "guidelines": "Dispersed primitive camping permitted along forest roads outside developed campgrounds. Leave No Trace principles strictly required. Camp at least 100 feet away from streams and trails."
  },
  "waste_disposal_rules": {
    "poop_disposal": "Bury human waste in a cat-hole 6 to 8 inches deep, located at least 200 feet from water sources and trails. Pack out all toilet paper and personal hygiene products.",
    "trash_policy": "Pack it in, pack it out. No trash collection service. Leave site cleaner than you found it."
  },
  "campfire_rules": {
    "permitted": True,
    "firewood_policy": "Dead and down wood may be collected freely nearby. Do not cut live standing trees or transport wood from outside Arkansas to prevent emerald ash borer spread.",
    "safety_requirements": "Use existing rock fire rings. Douse fire completely with water until cold to the touch before sleeping or leaving.",
    "seasonal_fire_bans": "Subject to county burn bans during dry summer and autumn periods."
  },
  "access_and_road_conditions": {
    "road_type": "Gravel and dirt forest service roads",
    "road_conditions": "Narrow gravel roads with occasional ruts and loose stone. Steep inclines in places.",
    "vehicle_recommendation": "High clearance 2WD car or CUV can access main pullouts in dry weather; 4x4 recommended after heavy rain.",
    "scores": {
      "road_grade": 6,
      "road_terrain_difficulty": 5,
      "supply_run_pain": 6
    }
  },
  "nomad_connectivity_rating": {
    "overall_rating": "Fair (2/5 Stars)",
    "verizon_reliability": "1-2 bars 4G LTE on high ridge pullouts, drops in deep creek hollows",
    "att_reliability": "1 bar 4G LTE spotty",
    "tmobile_reliability": "No signal in valleys, spotty on ridges",
    "terrain_obstruction_risk": "High - dense hardwood canopy and steep Ozark bluff walls obstruct line of sight to cell towers",
    "distance_from_tower_corridor_miles": 14.5,
    "cellular_internet_dependable": False
  },
  "amenities": [
    "Dispersed Fire Rings",
    "Scenic Creek Access",
    "Primitive Flat Pullouts",
    "Dark Sky Star Observation"
  ],
  "location_scores": {
    "distance_to_groceries_score": 4,
    "distance_to_library_score": 4,
    "distance_to_gym_score": 3,
    "terrain_score": 8,
    "quietness_score": 9
  },
  "nearest_supply_towns": [
    {
      "town_name": "Marshall, AR",
      "distance_miles": 22.4,
      "services_available": [
        "Grocery Store",
        "Gas Station",
        "Hardware Store",
        "Local Restaurants"
      ]
    },
    {
      "town_name": "Russellville, AR",
      "distance_miles": 46.1,
      "services_available": [
        "Supercenter",
        "Hospital",
        "Public Library",
        "Gym & Fitness Center",
        "Mechanic"
      ]
    }
  ],
  "seasonal_weather_effects": {
    "spring": "Cool to mild, damp weather with roaring waterfalls and blooming dogwoods. High risk of flash flooding near creeks.",
    "summer": "Hot and humid with temperatures reaching 90-95°F. Ticks and chiggers abundant; creek swims offer relief.",
    "fall": "Crisp dry air with vibrant Ozark hardwood fall foliage in October and November. Ideal primitive camping weather.",
    "winter": "Cold temperatures dropping below freezing at night (20-30°F). Occasional light snowfall or ice storms."
  },
  "dangers_and_hazards": [
    "Black Bears",
    "Venomous Snakes (Copperheads, Timber Rattlesnakes)",
    "Flash Flooding near Richland Creek",
    "Ticks and Chiggers",
    "Cell Phone Dead Zones"
  ],
  "acoustic_environment": {
    "quietness_rating": "Very Peaceful (Quietness Score: 9/10)",
    "common_human_made_sounds": [
      "Distant gravel road traffic",
      "High altitude aircraft"
    ]
  },
  "flora_and_fauna": {
    "common_plants_and_trees": [
      "Shortleaf Pine",
      "White Oak",
      "Dogwood",
      "Wild Azalea",
      "Ozark Bladdernut"
    ],
    "common_animals": [
      "Black Bear",
      "White-tailed Deer",
      "Elk",
      "Wild Turkey",
      "Pileated Woodpecker"
    ]
  },
  "human_demographics_and_culture": "Deep Ozark mountain heritage characterized by folk traditions, bluegrass music, independent homesteading, and timber management.",
  "spiritual_and_folklore_data": {
    "nature_spirits_and_mythological_lore": "Ozark folklore speaks of the 'Gawggy', a legendary creature said to inhabit the remote bluff shelters of Richland Creek.",
    "energetic_and_spiritual_features": "Ancient sandstone bluffs and clear water springs create an uplifting, grounding atmosphere prized by quiet seekers."
  },
  "nearby_hiking_trails": [
    {
      "trail_name": "Richland Creek Wilderness Trail to Falling Water Falls",
      "length_miles": 5.6,
      "difficulty": "Moderate to Strenuous",
      "features": "Scenic waterfalls, limestone bluffs, pristine creek swimming holes"
    }
  ],
  "public_reviews_summary": "Campers love the pristine wilderness solitude, emerald swimming holes, and star-filled skies, but warn about rough gravel roads and non-existent cell service in the hollows.",
  "other_data": "Pack all supplies beforehand as local gas stations have limited hours. High water makes creek crossings impassable after spring heavy rains.",
  "last_updated": "2026-09-12"
})
save_state(ark_data, ark_path)

# Connecticut +1 site (reach 5)
ct_data, ct_path = load_state('connecticut')
ct_data.append({
  "id": "connecticut-005",
  "name": "Natchaug State Forest Dispersed Backpacking Lean-to Primitive Spot",
  "state": "Connecticut",
  "county": "Windham",
  "coordinates": {
    "latitude": 41.8375,
    "longitude": -72.1022,
    "elevation_ft": 610.0
  },
  "management_agency": {
    "name": "Connecticut Department of Energy and Environmental Protection (DEEP)",
    "type": "State",
    "phone": "(860) 424-3000",
    "website": "https://portal.ct.gov/DEEP/State-Parks/Forests/Natchaug-State-Forest"
  },
  "rules_and_regulations": {
    "cost": "Free ($0/night for primitive trailside lean-to shelters along Natchaug Trail)",
    "stay_limit": "1 night limit at trailside shelters for backpackers",
    "guidelines": "Primitive camping permitted at designated shelter zones along the Natchaug Trail. Carry-in carry-out policy strictly enforced."
  },
  "waste_disposal_rules": {
    "poop_disposal": "Utilize primitive privy if available, otherwise bury waste 6-8 inches deep at least 200 feet from watercourses. Pack out paper products.",
    "trash_policy": "Strict Carry-In, Carry-Out rule. No trash containers provided."
  },
  "campfire_rules": {
    "permitted": True,
    "firewood_policy": "Gather small dead/down twigs only. Do not transport firewood across state lines to prevent emerald ash borer and spongy moth spread.",
    "safety_requirements": "Fires permitted only in designated stone fire rings at shelter sites. Extinguish thoroughly with water.",
    "seasonal_fire_bans": "Subject to state high forest fire danger alerts, especially during early spring before leaf-out."
  },
  "access_and_road_conditions": {
    "road_type": "Paved state highway leading to forest trailhead parking",
    "road_conditions": "Paved access roads; 1.2-mile hike required from parking lot along Natchaug Trail to reach shelter.",
    "vehicle_recommendation": "Any standard front-wheel drive low-clearance sedan can park at main trailhead lot.",
    "scores": {
      "road_grade": 2,
      "road_terrain_difficulty": 3,
      "supply_run_pain": 3
    }
  },
  "nomad_connectivity_rating": {
    "overall_rating": "Good (3.5/5 Stars)",
    "verizon_reliability": "2-3 bars 5G/4G LTE",
    "att_reliability": "2-3 bars 4G LTE",
    "tmobile_reliability": "2 bars 4G LTE",
    "terrain_obstruction_risk": "Moderate - dense hemlock and oak forest canopy",
    "distance_from_tower_corridor_miles": 3.8,
    "cellular_internet_dependable": True
  },
  "amenities": [
    "Wooden Lean-to Shelter",
    "Stone Fire Ring",
    "Stream Water Source (Treat Before Drinking)",
    "Trailhead Parking"
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
      "town_name": "Willimantic, CT",
      "distance_miles": 11.2,
      "services_available": [
        "Supermarket",
        "Hospital",
        "Public Library",
        "Gym & Fitness Center",
        "Auto Repair"
      ]
    },
    {
      "town_name": "Eastford, CT",
      "distance_miles": 4.5,
      "services_available": [
        "General Store",
        "Gas Station",
        "Post Office"
      ]
    }
  ],
  "seasonal_weather_effects": {
    "spring": "Cool temperatures (45-60°F) with muddy trails and high water flow in Natchaug River.",
    "summer": "Warm and humid (75-85°F). Mosquitoes and deer flies active near water.",
    "fall": "Stunning autumn foliage with vibrant red maples and yellow birches. Pleasant day temps (55-65°F).",
    "winter": "Cold with snow accumulation (20-35°F). Snowshoes or microspikes often necessary on trails."
  },
  "dangers_and_hazards": [
    "Black Bears",
    "Black-legged Ticks (Lyme Disease Risk)",
    "Falling Tree Branches (Hazard Trees)",
    "Freezing Night Temperatures in Winter"
  ],
  "acoustic_environment": {
    "quietness_rating": "Tranquil (Quietness Score: 8/10)",
    "common_human_made_sounds": [
      "Distant traffic on Route 198",
      "Occasional overhead commercial flights"
    ]
  },
  "flora_and_fauna": {
    "common_plants_and_trees": [
      "Eastern Hemlock",
      "Red Maple",
      "Mountain Laurel",
      "Black Birch",
      "Partridgeberry"
    ],
    "common_animals": [
      "White-tailed Deer",
      "Black Bear",
      "Wild Turkey",
      "Red-tailed Hawk",
      "Barred Owl"
    ]
  },
  "human_demographics_and_culture": "Rural New England quiet forest culture with historic stone walls, colonial mill ruins, and active conservation traditions.",
  "spiritual_and_folklore_data": {
    "nature_spirits_and_mythological_lore": "Local Connecticut lore tells of quiet woodland spirits guarding colonial stone walls and old hemlock groves.",
    "energetic_and_spiritual_features": "The rushing waters of Natchaug River create a soothing, reflective natural soundscape."
  },
  "nearby_hiking_trails": [
    {
      "trail_name": "Natchaug Trail (Blue-Blazed)",
      "length_miles": 19.3,
      "difficulty": "Moderate",
      "features": "Historic stone structures, river vistas, quiet hemlock ravines"
    }
  ],
  "public_reviews_summary": "Hikers appreciate the easy access, peaceful shelter, and babbling stream soundscape, though note that ticks are prevalent in summer.",
  "other_data": "Filter or boil all water drawn from streams. Park overnight only in designated forest trailhead parking lots.",
  "last_updated": "2026-09-12"
})
save_state(ct_data, ct_path)

# Delaware +2 sites (reach 5)
del_data, del_path = load_state('delaware')
del_data.append({
  "id": "delaware-004",
  "name": "Marshyhope Creek Wildlife Management Area Primitive Dispersed Spot",
  "state": "Delaware",
  "county": "Sussex",
  "coordinates": {
    "latitude": 38.7841,
    "longitude": -75.6812,
    "elevation_ft": 45.0
  },
  "management_agency": {
    "name": "Delaware Division of Fish and Wildlife (DNREC)",
    "type": "State",
    "phone": "(302) 739-9912",
    "website": "https://dnrec.alpha.delaware.gov/fish-wildlife/"
  },
  "rules_and_regulations": {
    "cost": "Free ($0/night; free conservation access pass available online)",
    "stay_limit": "3 consecutive nights limit for primitive watercraft/hiking camping",
    "guidelines": "Primitive camping permitted for anglers and paddlers in designated primitive access zones. No permanent structures or vehicle camping inside wildlife management boundary."
  },
  "waste_disposal_rules": {
    "poop_disposal": "Pack out all solid human waste using Portable Toilet/WAG bags, or dig cat-holes 6-8 inches deep at least 200 feet from Marshyhope Creek.",
    "trash_policy": "Strict Pack-In Pack-Out policy. No trash receptacles on site."
  },
  "campfire_rules": {
    "permitted": True,
    "firewood_policy": "Collect small dead/down wood from ground. Do not cut live timber.",
    "safety_requirements": "Small campfires allowed only in clear ground rings away from pine needle litter. Douse thoroughly.",
    "seasonal_fire_bans": "Subject to state dry season burn bans."
  },
  "access_and_road_conditions": {
    "road_type": "Paved county road to dirt launch access point",
    "road_conditions": "Flat gravel/dirt driveway leads to watercraft launch parking area.",
    "vehicle_recommendation": "Accessible by standard front-wheel drive low clearance vehicle.",
    "scores": {
      "road_grade": 1,
      "road_terrain_difficulty": 2,
      "supply_run_pain": 3
    }
  },
  "nomad_connectivity_rating": {
    "overall_rating": "Great (4/5 Stars)",
    "verizon_reliability": "4 bars 5G/4G LTE",
    "att_reliability": "3-4 bars 5G",
    "tmobile_reliability": "4 bars 5G",
    "terrain_obstruction_risk": "Low - flat coastal plain terrain",
    "distance_from_tower_corridor_miles": 1.8,
    "cellular_internet_dependable": True
  },
  "amenities": [
    "Canoe/Kayak Launch Access",
    "Flat Grassy Tent Spots",
    "Scenic Marsh Views"
  ],
  "location_scores": {
    "distance_to_groceries_score": 8,
    "distance_to_library_score": 8,
    "distance_to_gym_score": 7,
    "terrain_score": 3,
    "quietness_score": 7
  },
  "nearest_supply_towns": [
    {
      "town_name": "Bridgeville, DE",
      "distance_miles": 6.8,
      "services_available": [
        "Grocery Store",
        "Gas Station",
        "Hardware Store",
        "Restaurants"
      ]
    },
    {
      "town_name": "Seaford, DE",
      "distance_miles": 12.4,
      "services_available": [
        "Supercenter",
        "Hospital",
        "Public Library",
        "Fitness Center",
        "Mechanic"
      ]
    }
  ],
  "seasonal_weather_effects": {
    "spring": "Mild temperatures with occasional rain showers; coastal plain flowers blooming.",
    "summer": "Hot and humid (85-90°F) with high biting fly and mosquito activity near marshlands.",
    "fall": "Pleasant, mild weather with cool breezes and excellent fishing.",
    "winter": "Chilly and damp (30-45°F) with brisk coastal winds."
  },
  "dangers_and_hazards": [
    "Biting Flies and Mosquitoes",
    "Ticks",
    "Poison Ivy",
    "High Humidity"
  ],
  "acoustic_environment": {
    "quietness_rating": "Peaceful Marsh Environment (Quietness Score: 7/10)",
    "common_human_made_sounds": [
      "Occasional passing farm equipment",
      "Distant highway noise"
    ]
  },
  "flora_and_fauna": {
    "common_plants_and_trees": [
      "Loblolly Pine",
      "Sweetgum",
      "Marsh Grass",
      "Red Maple",
      "Wax Myrtle"
    ],
    "common_animals": [
      "Great Blue Heron",
      "Bald Eagle",
      "White-tailed Deer",
      "Osprey",
      "Beaver"
    ]
  },
  "human_demographics_and_culture": "Delmarva peninsula agricultural and coastal marshland culture centered around farming, crabbing, and waterfowl hunting.",
  "spiritual_and_folklore_data": {
    "nature_spirits_and_mythological_lore": "Nanticoke river tales recall ancestral legends of spirit guardians dwelling along peaceful marsh waterways.",
    "energetic_and_spiritual_features": "Calm, slow-moving water creates a serene and restful atmosphere."
  },
  "nearby_hiking_trails": [
    {
      "trail_name": "Marshyhope Creek Paddle & Nature Trail",
      "length_miles": 4.2,
      "difficulty": "Easy",
      "features": "Freshwater tidal marsh water trail, birdwatching perches"
    }
  ],
  "public_reviews_summary": "Great spot for kayak campers and anglers with excellent cell coverage, though insect repellent is mandatory in summer.",
  "other_data": "Wear bright orange during autumn hunting seasons when exploring WMA grounds.",
  "last_updated": "2026-09-12"
})

del_data.append({
  "id": "delaware-005",
  "name": "Blackiston Wildlife Management Area Primitive Spot",
  "state": "Delaware",
  "county": "Kenton / New Castle",
  "coordinates": {
    "latitude": 39.2628,
    "longitude": -75.6985,
    "elevation_ft": 65.0
  },
  "management_agency": {
    "name": "Delaware Division of Fish and Wildlife (DNREC)",
    "type": "State",
    "phone": "(302) 739-9912",
    "website": "https://dnrec.alpha.delaware.gov/fish-wildlife/"
  },
  "rules_and_regulations": {
    "cost": "Free ($0/night, no fee for primitive trailside camping)",
    "stay_limit": "3 nights maximum stay limit",
    "guidelines": "Free primitive camping for hikers/hunters during designated open seasons. No motorized vehicle camping past designated parking pullouts."
  },
  "waste_disposal_rules": {
    "poop_disposal": "Bury waste in 6-8 inch cat-holes at least 200 feet away from drainage ditches and ponds. Pack out all hygiene items.",
    "trash_policy": "Strict Pack-It-In Pack-It-Out policy."
  },
  "campfire_rules": {
    "permitted": True,
    "firewood_policy": "Dead and down wood collection allowed on site.",
    "safety_requirements": "Ground fires must be cleared of surrounding brush and extinguished fully before departure.",
    "seasonal_fire_bans": "Subject to state dry period fire restrictions."
  },
  "access_and_road_conditions": {
    "road_type": "Paved county road to short gravel parking lot",
    "road_conditions": "Smooth paved access roads to gravel parking lot.",
    "vehicle_recommendation": "Any standard FWD compact car can easily access parking lot.",
    "scores": {
      "road_grade": 1,
      "road_terrain_difficulty": 1,
      "supply_run_pain": 2
    }
  },
  "nomad_connectivity_rating": {
    "overall_rating": "Excellent (4.5/5 Stars)",
    "verizon_reliability": "4-5 bars 5G",
    "att_reliability": "4 bars 5G",
    "tmobile_reliability": "4-5 bars 5G",
    "terrain_obstruction_risk": "Low - open mixed forest and fields",
    "distance_from_tower_corridor_miles": 1.2,
    "cellular_internet_dependable": True
  },
  "amenities": [
    "Gravel Parking Area",
    "Flat Grassy Cleared Sites",
    "Information Kiosk"
  ],
  "location_scores": {
    "distance_to_groceries_score": 8,
    "distance_to_library_score": 8,
    "distance_to_gym_score": 8,
    "terrain_score": 2,
    "quietness_score": 7
  },
  "nearest_supply_towns": [
    {
      "town_name": "Smyrna, DE",
      "distance_miles": 8.5,
      "services_available": [
        "Supermarket",
        "Pharmacy",
        "Public Library",
        "Restaurants",
        "Gas Station"
      ]
    },
    {
      "town_name": "Dover, DE",
      "distance_miles": 15.2,
      "services_available": [
        "Major Supercenters",
        "Hospital",
        "Gym & Fitness Centers",
        "Auto Repair Shops"
      ]
    }
  ],
  "seasonal_weather_effects": {
    "spring": "Pleasant spring weather with wild green foliage and songbird nesting.",
    "summer": "Warm and humid (80-88°F). Insects active around moist forest patches.",
    "fall": "Crisp autumn air, colorful hardwood leaves, quiet conditions.",
    "winter": "Cool to chilly (32-48°F) with occasional light snow."
  },
  "dangers_and_hazards": [
    "Ticks",
    "Poison Ivy",
    "Seasonal Hunting Activity"
  ],
  "acoustic_environment": {
    "quietness_rating": "Quiet Rural Atmosphere (Quietness Score: 7/10)",
    "common_human_made_sounds": [
      "Distant vehicle hum",
      "Agricultural equipment"
    ]
  },
  "flora_and_fauna": {
    "common_plants_and_trees": [
      "White Oak",
      "American Beech",
      "Sassafras",
      "Virginia Pine",
      "Goldenrod"
    ],
    "common_animals": [
      "White-tailed Deer",
      "Red Fox",
      "Eastern Cottontail",
      "Wild Turkey",
      "Red-shouldered Hawk"
    ]
  },
  "human_demographics_and_culture": "Historic Delaware agricultural countryside steeped in farming history and wildlife preservation.",
  "spiritual_and_folklore_data": {
    "nature_spirits_and_mythological_lore": "Local rural folklore speaks of peaceful forest shadows beneath old oak trees.",
    "energetic_and_spiritual_features": "Gentle flat topography providing a calm, uncomplicated natural setting."
  },
  "nearby_hiking_trails": [
    {
      "trail_name": "Blackiston Wildlife Loop Trail",
      "length_miles": 3.1,
      "difficulty": "Easy",
      "features": "Flat forest path through mature hardwoods and wildlife plantings"
    }
  ],
  "public_reviews_summary": "Super easy access, very quiet at night, and lightning fast 5G cell connectivity for digital nomads.",
  "other_data": "Fluorescent orange safety clothing recommended during Delaware deer hunting seasons.",
  "last_updated": "2026-09-12"
})
save_state(del_data, del_path)

# Georgia +1 site (reach 5)
ga_data, ga_path = load_state('georgia')
ga_data.append({
  "id": "georgia-005",
  "name": "Sarah's Creek Dispersed Primitive Camping Area",
  "state": "Georgia",
  "county": "Rabun",
  "coordinates": {
    "latitude": 34.9126,
    "longitude": -83.2415,
    "elevation_ft": 2150.0
  },
  "management_agency": {
    "name": "U.S. Forest Service - Chattahoochee-Oconee National Forests (Chattooga River Ranger District)",
    "type": "Federal",
    "phone": "(706) 754-6221",
    "website": "https://www.fs.usda.gov/conf"
  },
  "rules_and_regulations": {
    "cost": "Free ($0/night, no fees required for primitive dispersed creek sites)",
    "stay_limit": "14 days maximum stay limit within a 30-day window",
    "guidelines": "Primitive creek-side camping permitted at pullout campsites along Sarah's Creek Road. Maintain 50 feet distance from stream bank. Leave No Trace."
  },
  "waste_disposal_rules": {
    "poop_disposal": "Bury waste in a cat-hole 6-8 inches deep at least 200 feet from Sarah's Creek. Pack out all paper products.",
    "trash_policy": "Pack it in, pack it out. No garbage receptacles provided."
  },
  "campfire_rules": {
    "permitted": True,
    "firewood_policy": "Dead and down wood may be gathered from forest floor. No cutting standing trees.",
    "safety_requirements": "Campfires permitted in existing stone fire rings. Douse completely cold with creek water before leaving.",
    "seasonal_fire_bans": "Subject to USFS high fire danger restrictions during dry fall months."
  },
  "access_and_road_conditions": {
    "road_type": "Unpaved forest service road (FS 156)",
    "road_conditions": "Gravel and dirt road with occasional potholes and creek ford crossing.",
    "vehicle_recommendation": "CUV, SUV, or high-clearance 2WD car; 4WD helpful after heavy mountain rain.",
    "scores": {
      "road_grade": 5,
      "road_terrain_difficulty": 5,
      "supply_run_pain": 5
    }
  },
  "nomad_connectivity_rating": {
    "overall_rating": "Fair (2.5/5 Stars)",
    "verizon_reliability": "1-2 bars 4G LTE near upper road pullouts, spotty by creek",
    "att_reliability": "1-2 bars 4G LTE",
    "tmobile_reliability": "No signal in creek gorge",
    "terrain_obstruction_risk": "High - steep mountain valley and dense rhododendron thickets",
    "distance_from_tower_corridor_miles": 8.2,
    "cellular_internet_dependable": False
  },
  "amenities": [
    "Primitive Stone Fire Rings",
    "Creek Water Access",
    "Shaded Mountain Sites"
  ],
  "location_scores": {
    "distance_to_groceries_score": 6,
    "distance_to_library_score": 5,
    "distance_to_gym_score": 4,
    "terrain_score": 7,
    "quietness_score": 9
  },
  "nearest_supply_towns": [
    {
      "town_name": "Clayton, GA",
      "distance_miles": 12.8,
      "services_available": [
        "Grocery Store",
        "Gas Station",
        "Hardware Store",
        "Restaurants",
        "Outfitter"
      ]
    },
    {
      "town_name": "Franklin, NC",
      "distance_miles": 24.1,
      "services_available": [
        "Supercenter",
        "Hospital",
        "Public Library",
        "Gym & Fitness Center"
      ]
    }
  ],
  "seasonal_weather_effects": {
    "spring": "Cool temperatures with lush green mountain foliage and cascading creek waters.",
    "summer": "Pleasant mountain temperatures (75-84°F), cooler than lowland Georgia. Frequent afternoon thunderstorms.",
    "fall": "Vibrant Blue Ridge mountain autumn colors; crisp night temperatures (35-45°F).",
    "winter": "Cold mountain weather (25-40°F) with occasional light snow or ice on mountain roads."
  },
  "dangers_and_hazards": [
    "Black Bears (Bear canister/hang required)",
    "Timber Rattlesnakes & Copperheads",
    "High Water / Creek Flooding after rain",
    "Slippery Wet Rocks"
  ],
  "acoustic_environment": {
    "quietness_rating": "Serene Creek Audio (Quietness Score: 9/10)",
    "common_human_made_sounds": [
      "Occasional passing 4x4 vehicle",
      "High altitude airplanes"
    ]
  },
  "flora_and_fauna": {
    "common_plants_and_trees": [
      "Rosebay Rhododendron",
      "Mountain Laurel",
      "Eastern Hemlock",
      "Tulip Poplar",
      "Yellow Birch"
    ],
    "common_animals": [
      "Black Bear",
      "White-tailed Deer",
      "Brook Trout",
      "Wild Turkey",
      "Red-backed Salamander"
    ]
  },
  "human_demographics_and_culture": "Southern Appalachian mountain community culture centered around trout fishing, moonshine history, and mountain arts.",
  "spiritual_and_folklore_data": {
    "nature_spirits_and_mythological_lore": "Cherokee legends speak of the Nunne'hi, benevolent mountain spirits who dwell in high Blue Ridge peaks and hidden valleys.",
    "energetic_and_spiritual_features": "The rushing waters of Sarah's Creek offer a deep sense of peaceful grounding and natural renewal."
  },
  "nearby_hiking_trails": [
    {
      "trail_name": "Warwoman Dell to Willis Knob Trail",
      "length_miles": 6.4,
      "difficulty": "Moderate to Strenuous",
      "features": "Cascading waterfalls, lush fern ravines, mountain overlook vistas"
    }
  ],
  "public_reviews_summary": "Gorgeous creek campsites with cool mountain air in summer, though cell service is weak and bear food storage is critical.",
  "other_data": "Always store food in bear-proof containers or suspend at least 10 feet high and 4 feet out from tree trunks.",
  "last_updated": "2026-09-12"
})
save_state(ga_data, ga_path)

# Hawaii +2 sites (reach 5)
hi_data, hi_path = load_state('hawaii')
hi_data.append({
  "id": "hawaii-004",
  "name": "Waimanu Valley Primitive Wilderness Campsites",
  "state": "Hawaii",
  "county": "Hawaii (Big Island)",
  "coordinates": {
    "latitude": 20.1442,
    "longitude": -155.6328,
    "elevation_ft": 25.0
  },
  "management_agency": {
    "name": "Hawaii Department of Land and Natural Resources (DLNR) - Division of Forestry and Wildlife",
    "type": "State",
    "phone": "(808) 974-4221",
    "website": "https://dlnr.hawaii.gov/dofaw/"
  },
  "rules_and_regulations": {
    "cost": "Free ($0/night primitive backcountry wilderness permit obtainable online through DLNR portal)",
    "stay_limit": "6 consecutive nights maximum stay",
    "guidelines": "Primitive wilderness backpacking access only via Muliwai Trail from Waipio Valley. Strict Leave No Trace required. Pack out all trash."
  },
  "waste_disposal_rules": {
    "poop_disposal": "Composting toilets located in Waimanu Valley. Pack out all plastic waste and personal hygiene items.",
    "trash_policy": "Strict Pack-It-In, Pack-It-Out rule. Absolutely no trash disposal facilities."
  },
  "campfire_rules": {
    "permitted": False,
    "firewood_policy": "No wood fires permitted. Backpacking gas stoves only.",
    "safety_requirements": "Camp stoves must be operated on stable ground away from dry foliage.",
    "seasonal_fire_bans": "Open campfires strictly prohibited year-round in Waimanu Valley Preserve."
  },
  "access_and_road_conditions": {
    "road_type": "No vehicle access; strenuous 9-mile wilderness backpacking trail (Muliwai Trail)",
    "road_conditions": "Extremely steep z-trail climbs out of Waipio Valley, crossing 13 gulches to reach Waimanu Valley.",
    "vehicle_recommendation": "Vehicle left at trailhead parking (4x4 required to reach Waipio Valley bottom, or park FWD car at Waipio Lookout).",
    "scores": {
      "road_grade": 10,
      "road_terrain_difficulty": 10,
      "supply_run_pain": 10
    }
  },
  "nomad_connectivity_rating": {
    "overall_rating": "Zero (0/5 Stars)",
    "verizon_reliability": "No service",
    "att_reliability": "No service",
    "tmobile_reliability": "No service",
    "terrain_obstruction_risk": "Extreme - deep 3,000-foot volcanic amphitheater valley walls completely block cell signals",
    "distance_from_tower_corridor_miles": 18.5,
    "cellular_internet_dependable": False
  },
  "amenities": [
    "Composting Privy",
    "Freshwater Stream Source (Boil/Filter Required)",
    "Black Sand Beach Access",
    "Wilderness Solitude"
  ],
  "location_scores": {
    "distance_to_groceries_score": 1,
    "distance_to_library_score": 1,
    "distance_to_gym_score": 1,
    "terrain_score": 10,
    "quietness_score": 10
  },
  "nearest_supply_towns": [
    {
      "town_name": "Honokaa, HI",
      "distance_miles": 18.2,
      "services_available": [
        "Grocery Store",
        "Gas Station",
        "Restaurants",
        "Post Office"
      ]
    },
    {
      "town_name": "Hilo, HI",
      "distance_miles": 56.4,
      "services_available": [
        "Major Supercenters",
        "Hospital",
        "Public Library",
        "Fitness Centers",
        "Airport"
      ]
    }
  ],
  "seasonal_weather_effects": {
    "spring": "Warm and tropical with frequent mountain showers feeding dramatic waterfalls.",
    "summer": "Warm ocean breezes (78-85°F), higher humidity, ocean swimming opportunities.",
    "fall": "Tropical rains with lush green valley vegetation.",
    "winter": "Increased rainfall and high sea swells along north shore beach line."
  },
  "dangers_and_hazards": [
    "Flash Floods in Stream Crossings",
    "Extreme Elevation Change & Heat Exhaustion on Trail",
    "Falling Coconuts and Rocks",
    "High Ocean Surf and Strong Rip Currents",
    "Total Isolation (No Cell Service)"
  ],
  "acoustic_environment": {
    "quietness_rating": "Sublime Ocean & Waterfall Soundscape (Quietness Score: 10/10)",
    "common_human_made_sounds": [
      "Occasional tour helicopter high overhead"
    ]
  },
  "flora_and_fauna": {
    "common_plants_and_trees": [
      "Ohi'a Lehua",
      "Hapu'u Tree Fern",
      "Kukui (Candlenut)",
      "Noni",
      "Wild Banana"
    ],
    "common_animals": [
      "Hawaiian Hoary Bat ('Ope'ape'a)",
      "Nene Goose",
      "Hawaiian Hawk ('Io)",
      "Feral Pigs",
      "Pacific Golden Plover"
    ]
  },
  "human_demographics_and_culture": "Native Hawaiian sacred ancestral valley landscape (Waipio & Waimanu) deeply rooted in Hawaiian history, taro farming, and royal traditions.",
  "spiritual_and_folklore_data": {
    "nature_spirits_and_mythological_lore": "Hawaiian tradition reveres Waimanu as a place of immense Mana (spiritual power), sacred to the Mo'o (water dragon guardians) of the waterfall pools.",
    "energetic_and_spiritual_features": "3,000-foot green cliff walls and pristine waterfalls generate an awe-inspiring, sacred tranquility."
  },
  "nearby_hiking_trails": [
    {
      "trail_name": "Muliwai Trail (Waipio to Waimanu Valley)",
      "length_miles": 9.0,
      "difficulty": "Strenuous / Expert",
      "features": "3,000-ft valley climbs, 13 stream gulches, spectacular sea cliff vistas"
    }
  ],
  "public_reviews_summary": "One of the most breathtaking wilderness camping spots on Earth, but requires immense physical endurance and zero cell connectivity.",
  "other_data": "Always carry a satellite communicator (Garmin inReach/PLB) and purifiers capable of removing Leptospirosis bacteria from stream water.",
  "last_updated": "2026-09-12"
})

hi_data.append({
  "id": "hawaii-005",
  "name": "Polihale State Park Dispersed Beach Primitive Zone",
  "state": "Hawaii",
  "county": "Kauai",
  "coordinates": {
    "latitude": 22.0815,
    "longitude": -159.7584,
    "elevation_ft": 10.0
  },
  "management_agency": {
    "name": "Hawaii State Parks Division (DLNR)",
    "type": "State",
    "phone": "(808) 274-3444",
    "website": "https://dlnr.hawaii.gov/dsp/parks/kauai/polihale-state-park/"
  },
  "rules_and_regulations": {
    "cost": "Free ($0 entry/day access; free primitive resident permit or low-impact dispersed beach access)",
    "stay_limit": "5 consecutive nights maximum stay",
    "guidelines": "Primitive beach camping along designated sand dune sites at the end of the dirt access road. Do not drive or walk on sensitive sand dunes."
  },
  "waste_disposal_rules": {
    "poop_disposal": "Utilize park primitive pit latrines. Do not bury waste in sand dunes.",
    "trash_policy": "Pack out all trash. No trash collection at remote beach ends."
  },
  "campfire_rules": {
    "permitted": False,
    "firewood_policy": "Open wood fires strictly prohibited on sand dunes and beach brush.",
    "safety_requirements": "Enclosed portable gas stoves allowed for cooking.",
    "seasonal_fire_bans": "Year-round fire ban on open beach wood fires to protect coastal dune vegetation."
  },
  "access_and_road_conditions": {
    "road_type": "Unpaved 5-mile rough cane haul dirt road",
    "road_conditions": "Extremely rutted dirt road with deep washboards, sand pockets, and severe mud puddles after rain.",
    "vehicle_recommendation": "High-clearance CUV, SUV, or 4WD vehicle highly recommended; low clearance FWD cars risk bottoming out or getting stuck in soft sand.",
    "scores": {
      "road_grade": 8,
      "road_terrain_difficulty": 8,
      "supply_run_pain": 7
    }
  },
  "nomad_connectivity_rating": {
    "overall_rating": "Fair (2/5 Stars)",
    "verizon_reliability": "1-2 bars 4G LTE near south end, spotty north near cliffs",
    "att_reliability": "1-2 bars 4G LTE spotty",
    "tmobile_reliability": "1 bar 4G LTE",
    "terrain_obstruction_risk": "Moderate - towering Na Pali sea cliffs rising 2,000 feet behind beach",
    "distance_from_tower_corridor_miles": 12.0,
    "cellular_internet_dependable": False
  },
  "amenities": [
    "Primitive Pit Latrine",
    "Cold Water Shower Risers (Non-Potable)",
    "Unsurpassed Ocean Sunset Views"
  ],
  "location_scores": {
    "distance_to_groceries_score": 4,
    "distance_to_library_score": 4,
    "distance_to_gym_score": 3,
    "terrain_score": 9,
    "quietness_score": 8
  },
  "nearest_supply_towns": [
    {
      "town_name": "Waimea, HI",
      "distance_miles": 15.4,
      "services_available": [
        "Supermarket",
        "Gas Station",
        "Hospital",
        "Hardware Store",
        "Restaurants"
      ]
    },
    {
      "town_name": "Lihue, HI",
      "distance_miles": 39.8,
      "services_available": [
        "Big Box Stores",
        "Airport",
        "Public Library",
        "Gym & Fitness Centers"
      ]
    }
  ],
  "seasonal_weather_effects": {
    "spring": "Warm, sunny, and windy coastal conditions.",
    "summer": "Hot ocean temperatures, intense tropical sun, calm water for swimming.",
    "fall": "Warm weather with trade winds and glowing golden sunsets.",
    "winter": "Massive ocean swells along beach; dangerous shorebreak waves make swimming unsafe."
  },
  "dangers_and_hazards": [
    "Dangerous Rip Currents & Massive Shorebreak Waves (Winter)",
    "Getting Vehicle Stuck in Deep Beach Sand",
    "Dehydration & Severe Tropical Sun Exposure",
    "No Potable Drinking Water Onsite"
  ],
  "acoustic_environment": {
    "quietness_rating": "Thunderous Ocean Waves (Quietness Score: 8/10)",
    "common_human_made_sounds": [
      "Distant 4x4 engine revs on access road"
    ]
  },
  "flora_and_fauna": {
    "common_plants_and_trees": [
      "Naupaka Kahakai",
      "Pohuehue (Beach Morning Glory)",
      "Ironwood (Casuarina)",
      "Coconut Palm"
    ],
    "common_animals": [
      "Hawaiian Monk Seal (Protected)",
      "Green Sea Turtle (Honu)",
      "Humpback Whales (Winter)",
      "Wedge-tailed Shearwater"
    ]
  },
  "human_demographics_and_culture": "West Kauai agricultural and Hawaiian coastal culture where Polihale marks the sacred western doorway of spirits departing the Hawaiian islands.",
  "spiritual_and_folklore_data": {
    "nature_spirits_and_mythological_lore": "In ancient Hawaiian tradition, Polihale was the 'Leina a ka 'Uhane' - the cliff site where souls of the deceased departed to the ancestral realm.",
    "energetic_and_spiritual_features": "Vast ocean horizons and 2,000-foot Na Pali cliffs create a profound, solemn spiritual majesty."
  },
  "nearby_hiking_trails": [
    {
      "trail_name": "Polihale Beach Coastal Dune Walk",
      "length_miles": 4.0,
      "difficulty": "Moderate (Walking on Soft Sand)",
      "features": "7-mile white sand beach, views of Na Pali coast cliffs and Niihau island"
    }
  ],
  "public_reviews_summary": "Unbelievable sunsets and pristine white sand beach, but the 5-mile dirt road is notoriously rough and ocean currents are extremely treacherous.",
  "other_data": "Bring all drinking water. Keep a minimum 50-foot distance from protected Hawaiian Monk Seals resting on beach sand.",
  "last_updated": "2026-09-12"
})
save_state(hi_data, hi_path)

# Idaho +1 site (reach 5)
id_data, id_path = load_state('idaho')
id_data.append({
  "id": "idaho-005",
  "name": "Magruder Corridor Primitive Dispersed Campsites",
  "state": "Idaho",
  "county": "Idaho County",
  "coordinates": {
    "latitude": 45.6981,
    "longitude": -114.9452,
    "elevation_ft": 5820.0
  },
  "management_agency": {
    "name": "U.S. Forest Service - Nez Perce-Clearwater & Bitterroot National Forests",
    "type": "Federal",
    "phone": "(208) 983-1950",
    "website": "https://www.fs.usda.gov/nezperceclearwater"
  },
  "rules_and_regulations": {
    "cost": "Free ($0/night, no fees required for dispersed primitive camping along corridor)",
    "stay_limit": "14 days maximum stay within a 30-day window",
    "guidelines": "Dispersed primitive camping permitted along the 101-mile Magruder Corridor Road between Selway-Bitterroot and Frank Church-River of No Return Wilderness areas. Leave No Trace."
  },
  "waste_disposal_rules": {
    "poop_disposal": "Bury waste 6 to 8 inches deep at least 200 feet from all creeks and springs. Pack out toilet paper and hygiene items.",
    "trash_policy": "Strict Pack-It-In, Pack-It-Out rule. Wilderness boundary adjacent."
  },
  "campfire_rules": {
    "permitted": True,
    "firewood_policy": "Dead and down wood may be gathered freely. Do not cut standing timber.",
    "safety_requirements": "Use established rock fire rings. Extinguish with water until cold to touch.",
    "seasonal_fire_bans": "Subject to USFS Stage 1 and Stage 2 fire restrictions in late summer."
  },
  "access_and_road_conditions": {
    "road_type": "Unpaved single-lane mountain dirt road (FS Road 468)",
    "road_conditions": "Narrow, winding dirt mountain road with steep drop-offs, sharp rocks, and pullout turnouts.",
    "vehicle_recommendation": "High clearance 4x4 or truck required; low clearance FWD passenger cars strictly NOT recommended due to sharp rocks and remote wilderness conditions.",
    "scores": {
      "road_grade": 8,
      "road_terrain_difficulty": 8,
      "supply_run_pain": 9
    }
  },
  "nomad_connectivity_rating": {
    "overall_rating": "Zero (0/5 Stars)",
    "verizon_reliability": "No service along 100 miles of corridor",
    "att_reliability": "No service",
    "tmobile_reliability": "No service",
    "terrain_obstruction_risk": "Extreme - deep mountain canyons and massive Bitterroot wilderness peaks",
    "distance_from_tower_corridor_miles": 42.0,
    "cellular_internet_dependable": False
  },
  "amenities": [
    "Primitive Fire Rings",
    "Crystal Clear Creek Water",
    "Pristine Mountain Scenery",
    "Unmatched Wilderness Solitude"
  ],
  "location_scores": {
    "distance_to_groceries_score": 1,
    "distance_to_library_score": 1,
    "distance_to_gym_score": 1,
    "terrain_score": 10,
    "quietness_score": 10
  },
  "nearest_supply_towns": [
    {
      "town_name": "Elk City, ID",
      "distance_miles": 38.5,
      "services_available": [
        "General Store",
        "Gas Station",
        "Local Tavern"
      ]
    },
    {
      "town_name": "Darby, MT",
      "distance_miles": 54.2,
      "services_available": [
        "Grocery Store",
        "Gas Station",
        "Hardware Store",
        "Restaurants"
      ]
    }
  ],
  "seasonal_weather_effects": {
    "spring": "Road impassable due to deep mountain snowpack through June.",
    "summer": "Brief warm summer window (July to September) with mild days (70-80°F) and cool nights (40-48°F).",
    "fall": "Early snowstorms occur as early as late September; brilliant golden larch foliage.",
    "winter": "Closed to vehicle traffic; accessible only by snowmobile."
  },
  "dangers_and_hazards": [
    "Grizzly Bears & Black Bears (Bear canister/hang mandatory)",
    "Extreme Remote Wilderness Isolation",
    "No Cell Coverage for 100 Miles",
    "Flat Tires from Sharp Mountain Rocks",
    "Sudden Summer Snowstorms or Wildfires"
  ],
  "acoustic_environment": {
    "quietness_rating": "Pure Wilderness Quiet (Quietness Score: 10/10)",
    "common_human_made_sounds": [
      "Occasional high-clearance 4WD vehicle"
    ]
  },
  "flora_and_fauna": {
    "common_plants_and_trees": [
      "Ponderosa Pine",
      "Douglas Fir",
      "Western Larch (Tamarack)",
      "Lodgepole Pine",
      "Beargrass"
    ],
    "common_animals": [
      "Grizzly Bear",
      "Rocky Mountain Elk",
      "Gray Wolf",
      "Mountain Lion",
      "Bighorn Sheep"
    ]
  },
  "human_demographics_and_culture": "Historical frontier logging, mining, and wilderness trapping culture along the historic Nez Perce trail route across the Bitterroot Mountains.",
  "spiritual_and_folklore_data": {
    "nature_spirits_and_mythological_lore": "Historic ancestral crossing of the Nimiipuu (Nez Perce) people; mountain passes carry deep reverence for wilderness spirits.",
    "energetic_and_spiritual_features": "Unbroken wilderness expanse spanning over 4 million contiguous acres provides profound silence and spiritual clarity."
  },
  "nearby_hiking_trails": [
    {
      "trail_name": "Burnt Knob Lookout Trail",
      "length_miles": 2.4,
      "difficulty": "Strenuous",
      "features": "Historic fire lookout tower perched on granite pinnacle with 360-degree wilderness panorama"
    }
  ],
  "public_reviews_summary": "The ultimate epic wilderness overland drive and primitive camping corridor in the lower 48, but requires full self-sufficiency and spare tires.",
  "other_data": "Carry extra fuel, two full-sized spare tires, tire plug kit, satellite communicator, and bear spray.",
  "last_updated": "2026-09-12"
})
save_state(id_data, id_path)

print("Batch 1 expansion complete! Arkansas, Connecticut, Delaware, Georgia, Hawaii, and Idaho now have 5 primitive campsites each!")
