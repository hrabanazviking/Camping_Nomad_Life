import json

def load_state(name):
    path = f'/home/volmarr/.gemini/antigravity/scratch/Camping_Nomad_Life/states/{name}.json'
    with open(path, 'r') as f:
        return json.load(f), path

def save_state(data, path):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

# Illinois +2 sites (reach 5)
ill_data, ill_path = load_state('illinois')
ill_data.append({
  "id": "illinois-004",
  "name": "One Horse Gap Backpacking Primitive Zone - Shawnee National Forest",
  "state": "Illinois",
  "county": "Pope",
  "coordinates": {
    "latitude": 37.5214,
    "longitude": -88.4532,
    "elevation_ft": 540.0
  },
  "management_agency": {
    "name": "U.S. Forest Service - Shawnee National Forest (Hidden Springs Ranger District)",
    "type": "Federal",
    "phone": "(618) 658-2111",
    "website": "https://www.fs.usda.gov/shawnee"
  },
  "rules_and_regulations": {
    "cost": "Free ($0/night, no fee for primitive dispersed camping)",
    "stay_limit": "14 days maximum stay within a 30-day period",
    "guidelines": "Primitive backcountry dispersed camping permitted at least 150 feet away from trails and water sources. Leave No Trace."
  },
  "waste_disposal_rules": {
    "poop_disposal": "Bury waste 6-8 inches deep in a cat-hole at least 200 feet from streams. Pack out all paper products.",
    "trash_policy": "Pack it in, pack it out."
  },
  "campfire_rules": {
    "permitted": True,
    "firewood_policy": "Dead and down wood collection permitted.",
    "safety_requirements": "Use established rock fire rings. Douse cold with water.",
    "seasonal_fire_bans": "Subject to USFS dry autumn fire restrictions."
  },
  "access_and_road_conditions": {
    "road_type": "Gravel forest service road to trailhead",
    "road_conditions": "Well-maintained gravel road; short 0.8-mile hike required to primitive rock gap campsites.",
    "vehicle_recommendation": "Any standard FWD compact car can reach trailhead parking lot.",
    "scores": {
      "road_grade": 3,
      "road_terrain_difficulty": 3,
      "supply_run_pain": 5
    }
  },
  "nomad_connectivity_rating": {
    "overall_rating": "Fair (2.5/5 Stars)",
    "verizon_reliability": "2 bars 4G LTE on ridge tops, spotty in hollows",
    "att_reliability": "1-2 bars 4G LTE",
    "tmobile_reliability": "1 bar 4G LTE",
    "terrain_obstruction_risk": "Moderate - sandstone bluffs and hardwood forest canopy",
    "distance_from_tower_corridor_miles": 7.5,
    "cellular_internet_dependable": False
  },
  "amenities": [
    "Sandstone Rock Formations",
    "Primitive Fire Rings",
    "Scenic Bluff Overlooks"
  ],
  "location_scores": {
    "distance_to_groceries_score": 5,
    "distance_to_library_score": 5,
    "distance_to_gym_score": 4,
    "terrain_score": 7,
    "quietness_score": 9
  },
  "nearest_supply_towns": [
    {
      "town_name": "Golconda, IL",
      "distance_miles": 14.2,
      "services_available": [
        "Grocery Store",
        "Gas Station",
        "Restaurants"
      ]
    },
    {
      "town_name": "Harrisburg, IL",
      "distance_miles": 22.8,
      "services_available": [
        "Supercenter",
        "Hospital",
        "Public Library",
        "Gym & Fitness Center"
      ]
    }
  ],
  "seasonal_weather_effects": {
    "spring": "Lush greenery with wild bluffs and spring blossoms; wet trail conditions.",
    "summer": "Warm and humid (82-90°F) with dense canopy shade.",
    "fall": "Vibrant southern Illinois autumn leaves; crisp nights.",
    "winter": "Cold (25-40°F) with light snow revealing sandstone hoodoos."
  },
  "dangers_and_hazards": [
    "Venomous Snakes (Copperheads)",
    "Ticks",
    "Slippery Sandstone Bluffs"
  ],
  "acoustic_environment": {
    "quietness_rating": "Deep Forest Quiet (Quietness Score: 9/10)",
    "common_human_made_sounds": [
      "Occasional distant equestrian rider",
      "High altitude airplanes"
    ]
  },
  "flora_and_fauna": {
    "common_plants_and_trees": [
      "Post Oak",
      "Shortleaf Pine",
      "Sparkleberry",
      "Sandstone Cedar"
    ],
    "common_animals": [
      "White-tailed Deer",
      "Wild Turkey",
      "Gray Fox",
      "Pileated Woodpecker"
    ]
  },
  "human_demographics_and_culture": "Shawnee hills timber and agrarian culture with rich natural sandstone history.",
  "spiritual_and_folklore_data": {
    "nature_spirits_and_mythological_lore": "Indigenous legend of ancient natural stone portals along gap ridges.",
    "energetic_and_spiritual_features": "Dramatic sandstone natural gaps create a secluded, peaceful retreat."
  },
  "nearby_hiking_trails": [
    {
      "trail_name": "One Horse Gap Trail to River to River Trail",
      "length_miles": 4.5,
      "difficulty": "Moderate",
      "features": "Narrow sandstone slot gaps, pine groves, high bluff views"
    }
  ],
  "public_reviews_summary": "Unbelievable natural rock slot formations and complete quiet, though cell service is spotty.",
  "other_data": "Equestrian riders also use main trail corridors; yield trail right-of-way to horses.",
  "last_updated": "2026-09-12"
})

ill_data.append({
  "id": "illinois-005",
  "name": "Hanover Bluff Nature Preserve Dispersed Primitive Zone",
  "state": "Illinois",
  "county": "Jo Daviess",
  "coordinates": {
    "latitude": 42.2458,
    "longitude": -90.2841,
    "elevation_ft": 820.0
  },
  "management_agency": {
    "name": "Illinois Department of Natural Resources (IDNR)",
    "type": "State",
    "phone": "(815) 777-1030",
    "website": "https://dnr.illinois.gov"
  },
  "rules_and_regulations": {
    "cost": "Free ($0/night, no fee for primitive trailside camping)",
    "stay_limit": "3 consecutive nights limit",
    "guidelines": "Primitive camping permitted for backpackers along driftless bluff trails. Carry in, carry out."
  },
  "waste_disposal_rules": {
    "poop_disposal": "Bury waste 6-8 inches deep at least 200 feet from springs and bluffs.",
    "trash_policy": "Strict Pack-It-In Pack-It-Out rule."
  },
  "campfire_rules": {
    "permitted": False,
    "firewood_policy": "No wood campfires allowed to protect rare hill prairie plants.",
    "safety_requirements": "Portable gas stoves allowed.",
    "seasonal_fire_bans": "Year-round fire prohibition on open wood fires."
  },
  "access_and_road_conditions": {
    "road_type": "Paved county road to trailhead",
    "road_conditions": "Paved road access with small gravel parking lot.",
    "vehicle_recommendation": "Accessible by standard FWD low clearance cars.",
    "scores": {
      "road_grade": 2,
      "road_terrain_difficulty": 2,
      "supply_run_pain": 4
    }
  },
  "nomad_connectivity_rating": {
    "overall_rating": "Good (3.5/5 Stars)",
    "verizon_reliability": "3 bars 4G LTE",
    "att_reliability": "3 bars 4G LTE",
    "tmobile_reliability": "2 bars 4G LTE",
    "terrain_obstruction_risk": "Moderate - high Mississippi River driftless bluffs",
    "distance_from_tower_corridor_miles": 4.1,
    "cellular_internet_dependable": True
  },
  "amenities": [
    "Trailhead Parking",
    "Panoramic Driftless Bluff Views",
    "Hill Prairie Flora"
  ],
  "location_scores": {
    "distance_to_groceries_score": 6,
    "distance_to_library_score": 6,
    "distance_to_gym_score": 5,
    "terrain_score": 8,
    "quietness_score": 8
  },
  "nearest_supply_towns": [
    {
      "town_name": "Galena, IL",
      "distance_miles": 14.5,
      "services_available": [
        "Grocery Store",
        "Gas Station",
        "Public Library",
        "Historic Downtown",
        "Restaurants"
      ]
    },
    {
      "town_name": "Dubuque, IA",
      "distance_miles": 26.2,
      "services_available": [
        "Supercenter",
        "Hospital",
        "Gym & Fitness Center",
        "Auto Repair"
      ]
    }
  ],
  "seasonal_weather_effects": {
    "spring": "Green hill prairies with wild prairie flowers blooming.",
    "summer": "Warm days (78-86°F) with gentle Mississippi valley breezes.",
    "fall": "Spectacular driftless autumn leaf display over rolling valleys.",
    "winter": "Cold and snowy (15-30°F) with frozen river views."
  },
  "dangers_and_hazards": [
    "Steep Bluff Drop-offs",
    "Timber Rattlesnakes (Hill Prairies)",
    "Icy Trails in Winter"
  ],
  "acoustic_environment": {
    "quietness_rating": "Peaceful Bluff Elevation (Quietness Score: 8/10)",
    "common_human_made_sounds": [
      "Distant Mississippi barge horn",
      "Passing valley vehicles"
    ]
  },
  "flora_and_fauna": {
    "common_plants_and_trees": [
      "Side-oats Grama",
      "Big Bluestem",
      "Chinkapin Oak",
      "Pale Purple Coneflower"
    ],
    "common_animals": [
      "Bald Eagle",
      "Red-tailed Hawk",
      "White-tailed Deer",
      "Badger"
    ]
  },
  "human_demographics_and_culture": "Illinois Driftless area historic lead mining and scenic bluff tourism heritage.",
  "spiritual_and_folklore_data": {
    "nature_spirits_and_mythological_lore": "Native lore honors high driftless bluffs as watch posts of celestial spirit eagles.",
    "energetic_and_spiritual_features": "Expansive views across unglaciated valleys instill a strong sense of freedom."
  },
  "nearby_hiking_trails": [
    {
      "trail_name": "Hanover Bluff Prairie Trail",
      "length_miles": 2.8,
      "difficulty": "Moderate",
      "features": "Driftless bluff climbing path, hill prairie ecosystem, eagle vistas"
    }
  ],
  "public_reviews_summary": "Stunning views of the unglaciated driftless terrain and strong cell signal for working nomads.",
  "other_data": "Stay strictly on designated trails to preserve fragile hill prairie soils.",
  "last_updated": "2026-09-12"
})
save_state(ill_data, ill_path)

# Indiana +2 sites (reach 5)
ind_data, ind_path = load_state('indiana')
ind_data.append({
  "id": "indiana-004",
  "name": "Pike State Forest Dispersed Primitive Campsites",
  "state": "Indiana",
  "county": "Pike",
  "coordinates": {
    "latitude": 38.3142,
    "longitude": -87.1652,
    "elevation_ft": 480.0
  },
  "management_agency": {
    "name": "Indiana Department of Natural Resources (DNR) - Division of Forestry",
    "type": "State",
    "phone": "(812) 367-1524",
    "website": "https://www.in.gov/dnr/forestry"
  },
  "rules_and_regulations": {
    "cost": "Free ($0/night, no fees required for dispersed camping)",
    "stay_limit": "14 days maximum stay within a 30-day period",
    "guidelines": "Primitive camping permitted in designated pullout zones and trailside areas. Maintain 100 feet distance from water bodies."
  },
  "waste_disposal_rules": {
    "poop_disposal": "Bury waste in 6-8 inch cat-holes at least 200 feet from water. Pack out hygiene products.",
    "trash_policy": "Carry in, carry out policy."
  },
  "campfire_rules": {
    "permitted": True,
    "firewood_policy": "Gather dead and down wood locally.",
    "safety_requirements": "Campfires allowed in existing stone rings. Extinguish fully.",
    "seasonal_fire_bans": "Subject to Indiana DNR dry weather burn advisories."
  },
  "access_and_road_conditions": {
    "road_type": "Gravel forest roads",
    "road_conditions": "Smooth gravel road access with small pullout turnouts.",
    "vehicle_recommendation": "Accessible by standard FWD passenger car.",
    "scores": {
      "road_grade": 2,
      "road_terrain_difficulty": 3,
      "supply_run_pain": 4
    }
  },
  "nomad_connectivity_rating": {
    "overall_rating": "Good (3.5/5 Stars)",
    "verizon_reliability": "3 bars 4G LTE",
    "att_reliability": "3 bars 4G LTE",
    "tmobile_reliability": "2-3 bars 4G LTE",
    "terrain_obstruction_risk": "Low - rolling timber hill country",
    "distance_from_tower_corridor_miles": 3.5,
    "cellular_internet_dependable": True
  },
  "amenities": [
    "Gravel Pullouts",
    "Primitive Fire Rings",
    "Shaded Oak Canopy"
  ],
  "location_scores": {
    "distance_to_groceries_score": 6,
    "distance_to_library_score": 6,
    "distance_to_gym_score": 5,
    "terrain_score": 5,
    "quietness_score": 8
  },
  "nearest_supply_towns": [
    {
      "town_name": "Petersburg, IN",
      "distance_miles": 9.4,
      "services_available": [
        "Grocery Store",
        "Gas Station",
        "Hardware Store",
        "Local Dining"
      ]
    },
    {
      "town_name": "Jasper, IN",
      "distance_miles": 18.6,
      "services_available": [
        "Supercenter",
        "Hospital",
        "Public Library",
        "Gym & Fitness Center"
      ]
    }
  ],
  "seasonal_weather_effects": {
    "spring": "Lush green southern Indiana hardwood forest blooming.",
    "summer": "Warm and humid (80-88°F) with cicada soundscapes.",
    "fall": "Rich autumn leaf colors; warm days and cool nights.",
    "winter": "Chilly (22-38°F) with light periodic snow."
  },
  "dangers_and_hazards": [
    "Ticks",
    "Poison Ivy",
    "Mosquitoes near Patoka River"
  ],
  "acoustic_environment": {
    "quietness_rating": "Peaceful Forest (Quietness Score: 8/10)",
    "common_human_made_sounds": [
      "Distant agricultural machinery",
      "Occasional passing vehicle"
    ]
  },
  "flora_and_fauna": {
    "common_plants_and_trees": [
      "Tulip Tree (Indiana State Tree)",
      "White Oak",
      "Sugar Maple",
      "Black Walnut"
    ],
    "common_animals": [
      "White-tailed Deer",
      "Wild Turkey",
      "Gray Squirrel",
      "Eastern Bluebird"
    ]
  },
  "human_demographics_and_culture": "Southern Indiana rural timberland and agricultural heritage.",
  "spiritual_and_folklore_data": {
    "nature_spirits_and_mythological_lore": "Folklore tells of quiet spirit lights seen over old Patoka River bottomlands.",
    "energetic_and_spiritual_features": "Gentle hardwood hills providing a relaxing, grounded ambiance."
  },
  "nearby_hiking_trails": [
    {
      "trail_name": "Pike State Forest Multi-Use Trail",
      "length_miles": 5.2,
      "difficulty": "Easy to Moderate",
      "features": "Rolling hardwood hills, creek crossings, pine plantations"
    }
  ],
  "public_reviews_summary": "Very quiet state forest with easy access and reliable cell service for remote work.",
  "other_data": "Bring potable water as forest sources are non-potable.",
  "last_updated": "2026-09-12"
})

ind_data.append({
  "id": "indiana-005",
  "name": "Greene-Sullivan State Forest Primitive Dispersed Campsites",
  "state": "Indiana",
  "county": "Greene / Sullivan",
  "coordinates": {
    "latitude": 39.0215,
    "longitude": -87.2148,
    "elevation_ft": 520.0
  },
  "management_agency": {
    "name": "Indiana Department of Natural Resources (DNR) - Division of Forestry",
    "type": "State",
    "phone": "(812) 648-2698",
    "website": "https://www.in.gov/dnr/forestry"
  },
  "rules_and_regulations": {
    "cost": "Free ($0/night, primitive backcountry sites are free of charge)",
    "stay_limit": "14 days maximum stay limit",
    "guidelines": "Primitive camping allowed near over 120 reclaimed strip-mine lakes. Leave No Trace."
  },
  "waste_disposal_rules": {
    "poop_disposal": "Use vault toilets at main sites or bury 6-8 inches deep 200 ft from lakes.",
    "trash_policy": "Pack it in, pack it out."
  },
  "campfire_rules": {
    "permitted": True,
    "firewood_policy": "Dead and down wood collection permitted.",
    "safety_requirements": "Use established fire rings. Douse with water.",
    "seasonal_fire_bans": "Subject to Indiana DNR burn bans."
  },
  "access_and_road_conditions": {
    "road_type": "Gravel forest roads",
    "road_conditions": "Well-maintained gravel roads connecting lake basins.",
    "vehicle_recommendation": "Standard low-clearance FWD car accessible.",
    "scores": {
      "road_grade": 2,
      "road_terrain_difficulty": 2,
      "supply_run_pain": 3
    }
  },
  "nomad_connectivity_rating": {
    "overall_rating": "Great (4/5 Stars)",
    "verizon_reliability": "4 bars 5G/4G LTE",
    "att_reliability": "3-4 bars 4G LTE",
    "tmobile_reliability": "3 bars 4G LTE",
    "terrain_obstruction_risk": "Low - open lake shorelines and gentle hills",
    "distance_from_tower_corridor_miles": 2.4,
    "cellular_internet_dependable": True
  },
  "amenities": [
    "Primitive Fire Rings",
    "Lake Shoreline Access",
    "Fishing Pier Access",
    "Vault Toilets nearby"
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
      "town_name": "Linton, IN",
      "distance_miles": 6.2,
      "services_available": [
        "Grocery Store",
        "Gas Station",
        "Hardware Store",
        "Restaurants"
      ]
    },
    {
      "town_name": "Terre Haute, IN",
      "distance_miles": 32.5,
      "services_available": [
        "Supercenters",
        "Hospital",
        "Public Library",
        "Gym & Fitness Center",
        "Auto Repair"
      ]
    }
  ],
  "seasonal_weather_effects": {
    "spring": "Lakes fill with spring rain; excellent bluegill and bass fishing.",
    "summer": "Warm (82-90°F) with clear lake waters for paddling.",
    "fall": "Cool, crisp fall days with reflecting autumn foliage on lakes.",
    "winter": "Cold (20-35°F); lakes freeze over periodically."
  },
  "dangers_and_hazards": [
    "Deep Mine Pit Lakes (Sudden Drop-offs)",
    "Ticks",
    "Mosquitoes"
  ],
  "acoustic_environment": {
    "quietness_rating": "Tranquil Water Soundscape (Quietness Score: 8/10)",
    "common_human_made_sounds": [
      "Distant trolling motor hum",
      "Occasional passing car"
    ]
  },
  "flora_and_fauna": {
    "common_plants_and_trees": [
      "Cottonwood",
      "Black Willow",
      "Sycamore",
      "Cattails"
    ],
    "common_animals": [
      "Largemouth Bass",
      "Beaver",
      "Great Blue Heron",
      "White-tailed Deer"
    ]
  },
  "human_demographics_and_culture": "Southwestern Indiana coal mining heritage turned conservation and angling paradise.",
  "spiritual_and_folklore_data": {
    "nature_spirits_and_mythological_lore": "Stories of legendary giant bass lurking in the crystal waters of reclaimed deep pit lakes.",
    "energetic_and_spiritual_features": "Calm, mirror-like lakes provide peaceful reflection."
  },
  "nearby_hiking_trails": [
    {
      "trail_name": "Greene-Sullivan Lake Trail",
      "length_miles": 3.8,
      "difficulty": "Easy",
      "features": "Winding lakeside path around reclaimed pristine fishing lakes"
    }
  ],
  "public_reviews_summary": "Incredible spot for kayak camping, fishing, and working remotely with strong cell coverage.",
  "other_data": "Indiana fishing license required for angling in state forest lakes.",
  "last_updated": "2026-09-12"
})
save_state(ind_data, ind_path)

# Iowa +2 sites (reach 5)
iowa_data, iowa_path = load_state('iowa')
iowa_data.append({
  "id": "iowa-004",
  "name": "Preparation Canyon State Park Backcountry Primitive Sites",
  "state": "Iowa",
  "county": "Monona",
  "coordinates": {
    "latitude": 41.9842,
    "longitude": -95.9685,
    "elevation_ft": 1180.0
  },
  "management_agency": {
    "name": "Iowa Department of Natural Resources (DNR)",
    "type": "State",
    "phone": "(712) 423-2829",
    "website": "https://www.iowadnr.gov"
  },
  "rules_and_regulations": {
    "cost": "Free ($0/night, no fees required for primitive walk-in backcountry sites)",
    "stay_limit": "14 days maximum stay",
    "guidelines": "Walk-in primitive hike-in camping permitted at designated hike-in sites. Pack out all trash."
  },
  "waste_disposal_rules": {
    "poop_disposal": "Use trailhead pit latrine or bury waste 6-8 inches deep 200 ft from trails.",
    "trash_policy": "Strict Carry-In, Carry-Out rule."
  },
  "campfire_rules": {
    "permitted": True,
    "firewood_policy": "Gather small dead and down firewood near hike-in sites.",
    "safety_requirements": "Campfires permitted only in designated metal fire rings at hike-in sites.",
    "seasonal_fire_bans": "Subject to Iowa DNR burn warnings."
  },
  "access_and_road_conditions": {
    "road_type": "Paved state highway to gravel parking lot",
    "road_conditions": "Paved roads lead to trailhead parking lot; 0.5 to 1.5 mile hike required to reach campsites.",
    "vehicle_recommendation": "Any standard front-wheel drive low clearance vehicle can park at main lot.",
    "scores": {
      "road_grade": 2,
      "road_terrain_difficulty": 3,
      "supply_run_pain": 4
    }
  },
  "nomad_connectivity_rating": {
    "overall_rating": "Good (3.5/5 Stars)",
    "verizon_reliability": "3 bars 4G LTE on ridge sites",
    "att_reliability": "3 bars 4G LTE",
    "tmobile_reliability": "2 bars 4G LTE",
    "terrain_obstruction_risk": "Moderate - steep Loess Hills topography",
    "distance_from_tower_corridor_miles": 3.8,
    "cellular_internet_dependable": True
  },
  "amenities": [
    "Hike-in Primitive Sites",
    "Metal Fire Rings",
    "Loess Hills Scenic Vistas",
    "Trailhead Parking"
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
      "town_name": "Moorhead, IA",
      "distance_miles": 5.1,
      "services_available": [
        "Gas Station",
        "Local Cafe",
        "Post Office"
      ]
    },
    {
      "town_name": "Onawa, IA",
      "distance_miles": 14.8,
      "services_available": [
        "Grocery Store",
        "Hospital",
        "Public Library",
        "Hardware Store"
      ]
    }
  ],
  "seasonal_weather_effects": {
    "spring": "Wild prairie flowers blooming across steep windblown loess ridges.",
    "summer": "Warm days (80-88°F) with prairie breezes.",
    "fall": "Dramatic autumn colors; cool, clear prairie nights.",
    "winter": "Cold and snowy (15-30°F); snowshoes helpful on steep ridge trails."
  },
  "dangers_and_hazards": [
    "Steep Loess Ridge Drop-offs",
    "Ticks",
    "High Prairie Winds"
  ],
  "acoustic_environment": {
    "quietness_rating": "Wind-Swept Prairie Quiet (Quietness Score: 9/10)",
    "common_human_made_sounds": [
      "Distant farm tractor in valley",
      "High altitude jet contrails"
    ]
  },
  "flora_and_fauna": {
    "common_plants_and_trees": [
      "Yucca (Soapweed)",
      "Little Bluestem",
      "Bur Oak",
      "Prairie Goldenrod"
    ],
    "common_animals": [
      "White-tailed Deer",
      "Coyote",
      "Bobcat",
      "Red-tailed Hawk"
    ]
  },
  "human_demographics_and_culture": "Loess Hills pioneer history named after the 1850s Mormon settlement of Preparation.",
  "spiritual_and_folklore_data": {
    "nature_spirits_and_mythological_lore": "Local history recalls 1850s religious pioneer seeker Charles B. Thompson founding the holy city of Preparation.",
    "energetic_and_spiritual_features": "Windblown loess ridges offer a meditative, wide-open prairie perspective."
  },
  "nearby_hiking_trails": [
    {
      "trail_name": "Preparation Canyon Ridge Trail",
      "length_miles": 3.6,
      "difficulty": "Moderate to Strenuous",
      "features": "Steep loess ridge crests, deep forest ravines, panoramic valley views"
    }
  ],
  "public_reviews_summary": "One of Iowa's premier backcountry hike-in spots with incredible loess ridge scenery and quiet night skies.",
  "other_data": "Pack in all drinking water as backcountry sites lack water hydrants.",
  "last_updated": "2026-09-12"
})

iowa_data.append({
  "id": "iowa-005",
  "name": "Stephens State Forest Dispersed Pack-In Primitive Zone",
  "state": "Iowa",
  "county": "Lucas",
  "coordinates": {
    "latitude": 41.0125,
    "longitude": -93.3852,
    "elevation_ft": 990.0
  },
  "management_agency": {
    "name": "Iowa Department of Natural Resources (DNR) - Forestry Bureau",
    "type": "State",
    "phone": "(641) 774-4570",
    "website": "https://www.iowadnr.gov"
  },
  "rules_and_regulations": {
    "cost": "Free ($0/night, free pack-in primitive backpacking sites)",
    "stay_limit": "14 days maximum stay limit",
    "guidelines": "Primitive pack-in camping permitted at designated pack-in unit sites across Lucas and Whitebreast Units. Leave No Trace."
  },
  "waste_disposal_rules": {
    "poop_disposal": "Bury waste 6-8 inches deep in cat-holes at least 200 feet from streams.",
    "trash_policy": "Carry-in carry-out policy strictly enforced."
  },
  "campfire_rules": {
    "permitted": True,
    "firewood_policy": "Dead and down firewood collection allowed.",
    "safety_requirements": "Fire permitted in metal rings at pack-in sites. Douse with water.",
    "seasonal_fire_bans": "Subject to state dry season burn restrictions."
  },
  "access_and_road_conditions": {
    "road_type": "Gravel forest roads leading to pack-in trailheads",
    "road_conditions": "Well-graded gravel roads; short hike required from parking spot.",
    "vehicle_recommendation": "Standard FWD compact car accessible.",
    "scores": {
      "road_grade": 2,
      "road_terrain_difficulty": 3,
      "supply_run_pain": 4
    }
  },
  "nomad_connectivity_rating": {
    "overall_rating": "Good (3/5 Stars)",
    "verizon_reliability": "3 bars 4G LTE",
    "att_reliability": "2-3 bars 4G LTE",
    "tmobile_reliability": "2 bars 4G LTE",
    "terrain_obstruction_risk": "Low - gentle rolling timber hills",
    "distance_from_tower_corridor_miles": 5.2,
    "cellular_internet_dependable": True
  },
  "amenities": [
    "Primitive Fire Rings",
    "Pack-in Tent Sites",
    "Trailhead Parking"
  ],
  "location_scores": {
    "distance_to_groceries_score": 6,
    "distance_to_library_score": 6,
    "distance_to_gym_score": 5,
    "terrain_score": 5,
    "quietness_score": 8
  },
  "nearest_supply_towns": [
    {
      "town_name": "Chariton, IA",
      "distance_miles": 8.4,
      "services_available": [
        "Grocery Store",
        "Gas Station",
        "Hardware Store",
        "Public Library",
        "Restaurants"
      ]
    },
    {
      "town_name": "Des Moines, IA",
      "distance_miles": 48.0,
      "services_available": [
        "International Airport",
        "Major Supercenters",
        "Hospitals",
        "Gym Chains",
        "Auto Repair"
      ]
    }
  ],
  "seasonal_weather_effects": {
    "spring": "Lush green hardwood forest emergence and spring wild mushroom hunting.",
    "summer": "Warm (80-86°F) with shady oak-hickory canopy.",
    "fall": "Rich autumn foliage and crisp night air.",
    "winter": "Cold snow-covered woods (18-32°F); quiet winter camping."
  },
  "dangers_and_hazards": [
    "Ticks",
    "Poison Ivy",
    "Freezing Winter Temps"
  ],
  "acoustic_environment": {
    "quietness_rating": "Peaceful Forest Solitude (Quietness Score: 8/10)",
    "common_human_made_sounds": [
      "Distant gravel road traffic",
      "High altitude jets"
    ]
  },
  "flora_and_fauna": {
    "common_plants_and_trees": [
      "White Oak",
      "Shagbark Hickory",
      "Walnut",
      "Wild Plum"
    ],
    "common_animals": [
      "White-tailed Deer",
      "Wild Turkey",
      "Racoon",
      "Barred Owl"
    ]
  },
  "human_demographics_and_culture": "Southern Iowa agricultural and state forest timber management country.",
  "spiritual_and_folklore_data": {
    "nature_spirits_and_mythological_lore": "Pioneer trail stories speak of friendly woodland spirits watching over early travelers.",
    "energetic_and_spiritual_features": "Serene oak groves offer deep peace and stillness."
  },
  "nearby_hiking_trails": [
    {
      "trail_name": "Whitebreast Backpacking Trail",
      "length_miles": 6.2,
      "difficulty": "Moderate",
      "features": "Rolling hardwood hills, quiet pine groves, secluded pond loops"
    }
  ],
  "public_reviews_summary": "Iowa's largest state forest offers peace, solitude, easy pack-in camping, and decent cell service.",
  "other_data": "Water must be brought in or treated from forest ponds.",
  "last_updated": "2026-09-12"
})
save_state(iowa_data, iowa_path)

# Kansas +2 sites (reach 5)
ks_data, ks_path = load_state('kansas')
ks_data.append({
  "id": "kansas-004",
  "name": "Cimarron National Grassland Dispersed Primitive Zone",
  "state": "Kansas",
  "county": "Morton",
  "coordinates": {
    "latitude": 37.1425,
    "longitude": -101.8541,
    "elevation_ft": 3450.0
  },
  "management_agency": {
    "name": "U.S. Forest Service - Cimarron National Grassland",
    "type": "Federal",
    "phone": "(620) 697-4621",
    "website": "https://www.fs.usda.gov/psicc"
  },
  "rules_and_regulations": {
    "cost": "Free ($0/night, no fee for primitive dispersed grassland camping)",
    "stay_limit": "14 days maximum stay limit",
    "guidelines": "Dispersed camping allowed across 108,000 acres of shortgrass prairie outside developed areas. Maintain 100 feet distance from water tanks and windmills."
  },
  "waste_disposal_rules": {
    "poop_disposal": "Bury human waste 6-8 inches deep in cat-holes at least 200 feet from Cimarron River and windmills.",
    "trash_policy": "Strict Pack-It-In Pack-It-Out policy."
  },
  "campfire_rules": {
    "permitted": True,
    "firewood_policy": "Dead and down wood collection permitted along river bottom cottonwoods.",
    "safety_requirements": "Clear ground 10 feet around campfire. Extinguish thoroughly with water due to high prairie wind hazard.",
    "seasonal_fire_bans": "Subject to USFS high prairie fire danger restrictions."
  },
  "access_and_road_conditions": {
    "road_type": "Gravel and dirt prairie roads",
    "road_conditions": "Flat gravel roads; sandy dirt spur roads can become muddy after rain.",
    "vehicle_recommendation": "Standard FWD car fine on main gravel roads; 4WD recommended for sandy river bed spurs.",
    "scores": {
      "road_grade": 3,
      "road_terrain_difficulty": 4,
      "supply_run_pain": 6
    }
  },
  "nomad_connectivity_rating": {
    "overall_rating": "Fair (2.5/5 Stars)",
    "verizon_reliability": "2 bars 4G LTE",
    "att_reliability": "1-2 bars 4G LTE",
    "tmobile_reliability": "1 bar 4G LTE",
    "terrain_obstruction_risk": "Low - vast open high plains",
    "distance_from_tower_corridor_miles": 12.4,
    "cellular_internet_dependable": False
  },
  "amenities": [
    "Endless Horizon Prairie Views",
    "Historic Santa Fe Trail Ruts",
    "Dark Sky Star Observation"
  ],
  "location_scores": {
    "distance_to_groceries_score": 4,
    "distance_to_library_score": 4,
    "distance_to_gym_score": 3,
    "terrain_score": 4,
    "quietness_score": 10
  },
  "nearest_supply_towns": [
    {
      "town_name": "Elkhart, KS",
      "distance_miles": 11.2,
      "services_available": [
        "Grocery Store",
        "Gas Station",
        "Hardware Store",
        "Public Library",
        "Local Restaurants"
      ]
    },
    {
      "town_name": "Liberal, KS",
      "distance_miles": 52.6,
      "services_available": [
        "Supercenter",
        "Hospital",
        "Gym & Fitness Center",
        "Auto Repair Shops"
      ]
    }
  ],
  "seasonal_weather_effects": {
    "spring": "Vast prairie winds and spring blooming yucca.",
    "summer": "Hot high plains weather (90-100°F) with intense sun and cool prairie nights.",
    "fall": "Crisp, clear autumn days with golden shortgrass plains.",
    "winter": "Cold, windy high plains winter (15-35°F) with periodic blizzards."
  },
  "dangers_and_hazards": [
    "High Prairie Winds & Rapid Wildfire Spread",
    "Prairie Rattlesnakes",
    "Dehydration & Severe Heat Exposure",
    "Sudden Severe Thunderstorms / Tornadoes"
  ],
  "acoustic_environment": {
    "quietness_rating": "Vast Prairie Wind Silence (Quietness Score: 10/10)",
    "common_human_made_sounds": [
      "Distant cattle windmill click",
      "High altitude transcontinental flights"
    ]
  },
  "flora_and_fauna": {
    "common_plants_and_trees": [
      "Buffalograss",
      "Blue Grama",
      "Plains Cottonwood",
      "Soapweed Yucca",
      "Prickly Pear Cactus"
    ],
    "common_animals": [
      "Pronghorn Antelope",
      "Lesser Prairie-Chicken",
      "Black-tailed Prairie Dog",
      "Coyote",
      "Ferruginous Hawk"
    ]
  },
  "human_demographics_and_culture": "High Plains pioneer and Santa Fe Trail historic trading heritage.",
  "spiritual_and_folklore_data": {
    "nature_spirits_and_mythological_lore": "Pioneer history recalls Point of Rocks as a crucial landmark guide along the arid Cimarron Cutoff of the Santa Fe Trail.",
    "energetic_and_spiritual_features": "360-degree prairie horizons create a humbling sense of cosmic expanse."
  },
  "nearby_hiking_trails": [
    {
      "trail_name": "Santa Fe Companion National Historic Trail",
      "length_miles": 10.5,
      "difficulty": "Easy to Moderate",
      "features": "Historic 1800s wagon ruts, Point of Rocks overlook, prairie wildlife"
    }
  ],
  "public_reviews_summary": "Vast open shortgrass prairie with mind-blowing starry night skies, but high winds and hot sun require full prep.",
  "other_data": "Bring plenty of fresh water and check fire danger ratings before lighting any camp stove.",
  "last_updated": "2026-09-12"
})

ks_data.append({
  "id": "kansas-005",
  "name": "Kanopolis Lake Wildlife Area Primitive Dispersed Spots",
  "state": "Kansas",
  "county": "Ellsworth",
  "coordinates": {
    "latitude": 38.6415,
    "longitude": -97.9852,
    "elevation_ft": 1480.0
  },
  "management_agency": {
    "name": "Kansas Department of Wildlife and Parks (KDWP)",
    "type": "State",
    "phone": "(785) 546-2565",
    "website": "https://ksoutdoors.com"
  },
  "rules_and_regulations": {
    "cost": "Free ($0/night primitive camping in designated wildlife management areas)",
    "stay_limit": "14 days maximum stay limit",
    "guidelines": "Dispersed primitive camping permitted in designated wildlife area access points around the Smoky Hill River arm. Leave No Trace."
  },
  "waste_disposal_rules": {
    "poop_disposal": "Bury waste 6-8 inches deep at least 200 feet from water bodies. Pack out hygiene products.",
    "trash_policy": "Strict Pack-It-In Pack-It-Out rule."
  },
  "campfire_rules": {
    "permitted": True,
    "firewood_policy": "Dead and down timber collection permitted.",
    "safety_requirements": "Use established rock fire rings. Douse completely cold.",
    "seasonal_fire_bans": "Subject to county burn bans during dry periods."
  },
  "access_and_road_conditions": {
    "road_type": "Gravel and dirt wildlife access roads",
    "road_conditions": "Well-maintained gravel roads lead to flat prairie river pullouts.",
    "vehicle_recommendation": "Standard low-clearance FWD car accessible in dry conditions.",
    "scores": {
      "road_grade": 3,
      "road_terrain_difficulty": 3,
      "supply_run_pain": 4
    }
  },
  "nomad_connectivity_rating": {
    "overall_rating": "Good (3.5/5 Stars)",
    "verizon_reliability": "3 bars 4G LTE",
    "att_reliability": "3 bars 4G LTE",
    "tmobile_reliability": "2-3 bars 4G LTE",
    "terrain_obstruction_risk": "Low - red sandstone canyon rim and rolling prairie",
    "distance_from_tower_corridor_miles": 4.5,
    "cellular_internet_dependable": True
  },
  "amenities": [
    "Smoky Hill River Access",
    "Sandstone Bluff Views",
    "Primitive Fire Rings"
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
      "town_name": "Ellsworth, KS",
      "distance_miles": 12.8,
      "services_available": [
        "Grocery Store",
        "Gas Station",
        "Hospital",
        "Hardware Store",
        "Restaurants"
      ]
    },
    {
      "town_name": "Salina, KS",
      "distance_miles": 34.2,
      "services_available": [
        "Supercenters",
        "Public Library",
        "Gym & Fitness Center",
        "Auto Repair"
      ]
    }
  ],
  "seasonal_weather_effects": {
    "spring": "Lush green prairie river valley with blooming wild flowers.",
    "summer": "Warm to hot (85-94°F); swimming and fishing in river and lake.",
    "fall": "Crisp autumn air and golden cottonwood foliage.",
    "winter": "Cold prairie weather (20-38°F) with light snow."
  },
  "dangers_and_hazards": [
    "High Prairie Winds",
    "Ticks",
    "Flash Flooding along Smoky Hill River"
  ],
  "acoustic_environment": {
    "quietness_rating": "Peaceful Prairie Valley (Quietness Score: 8/10)",
    "common_human_made_sounds": [
      "Distant motorboat on main lake body",
      "Passing farm vehicles"
    ]
  },
  "flora_and_fauna": {
    "common_plants_and_trees": [
      "Plains Cottonwood",
      "Red Cedar",
      "Switchgrass",
      "Compass Plant"
    ],
    "common_animals": [
      "White-tailed Deer",
      "Wild Turkey",
      "Channel Catfish",
      "Bald Eagle",
      "Coyote"
    ]
  },
  "human_demographics_and_culture": "Central Kansas red sandstone country steeped in cattle drive history and frontier army posts (Fort Harker).",
  "spiritual_and_folklore_data": {
    "nature_spirits_and_mythological_lore": "Indigenous Pawnee lore reveres red sandstone bluffs along the river as sacred ceremonial sites.",
    "energetic_and_spiritual_features": "Red sandstone canyons contrasting with golden prairie fields provide an invigorating energy."
  },
  "nearby_hiking_trails": [
    {
      "trail_name": "Horsethief Canyon Trail",
      "length_miles": 4.8,
      "difficulty": "Moderate",
      "features": "Red sandstone bluffs, cave overhangs, prairie river crossings"
    }
  ],
  "public_reviews_summary": "Beautiful red rock canyon backdrop with great fishing and dependable cell connectivity.",
  "other_data": "Avoid parking in low river bottoms if heavy rain is forecasted upstream.",
  "last_updated": "2026-09-12"
})
save_state(ks_data, ks_path)

# Kentucky +2 sites (reach 5)
ky_data, ky_path = load_state('kentucky')
ky_data.append({
  "id": "kentucky-004",
  "name": "Indian Creek Dispersed Primitive Camping Area - Daniel Boone National Forest",
  "state": "Kentucky",
  "county": "Menifee",
  "coordinates": {
    "latitude": 37.8912,
    "longitude": -83.6541,
    "elevation_ft": 820.0
  },
  "management_agency": {
    "name": "U.S. Forest Service - Daniel Boone National Forest (Cumberland Ranger District)",
    "type": "Federal",
    "phone": "(606) 663-8100",
    "website": "https://www.fs.usda.gov/dbnf"
  },
  "rules_and_regulations": {
    "cost": "Free ($0/night, no permit or fee for primitive dispersed creek sites)",
    "stay_limit": "14 days maximum stay within a 30-day window",
    "guidelines": "Dispersed primitive camping allowed at pullout sites along Indian Creek Road (FS 9A/9B). Camp at least 300 feet away from Red River Gorge geological area boundary."
  },
  "waste_disposal_rules": {
    "poop_disposal": "Bury waste 6-8 inches deep at least 200 feet from Indian Creek. Pack out paper products.",
    "trash_policy": "Strict Pack-It-In Pack-It-Out policy."
  },
  "campfire_rules": {
    "permitted": True,
    "firewood_policy": "Dead and down wood collection permitted.",
    "safety_requirements": "Campfires permitted in existing stone fire rings. Extinguish fully with creek water.",
    "seasonal_fire_bans": "Subject to USFS dry spring/fall burn restrictions."
  },
  "access_and_road_conditions": {
    "road_type": "Gravel forest service road",
    "road_conditions": "Gravel road with occasional pot holes and shallow creek crossing.",
    "vehicle_recommendation": "Accessible by standard FWD passenger car in dry weather; CUV/SUV helpful.",
    "scores": {
      "road_grade": 4,
      "road_terrain_difficulty": 4,
      "supply_run_pain": 5
    }
  },
  "nomad_connectivity_rating": {
    "overall_rating": "Fair (2/5 Stars)",
    "verizon_reliability": "1-2 bars 4G LTE spotty near ridge pullouts",
    "att_reliability": "1 bar 4G LTE",
    "tmobile_reliability": "No signal in creek gorge",
    "terrain_obstruction_risk": "High - steep sandstone canyon walls and dense hardwood canopy",
    "distance_from_tower_corridor_miles": 8.5,
    "cellular_internet_dependable": False
  },
  "amenities": [
    "Creek Water Source",
    "Stone Fire Rings",
    "Shaded Sandstone Gorge Sites"
  ],
  "location_scores": {
    "distance_to_groceries_score": 5,
    "distance_to_library_score": 5,
    "distance_to_gym_score": 4,
    "terrain_score": 8,
    "quietness_score": 9
  },
  "nearest_supply_towns": [
    {
      "town_name": "Frenchburg, KY",
      "distance_miles": 11.4,
      "services_available": [
        "Grocery Store",
        "Gas Station",
        "Hardware Store",
        "Local Dining"
      ]
    },
    {
      "town_name": "Morehead, KY",
      "distance_miles": 28.6,
      "services_available": [
        "Supercenter",
        "Hospital",
        "Public Library",
        "Gym & Fitness Center"
      ]
    }
  ],
  "seasonal_weather_effects": {
    "spring": "Rushing creek water and blooming mountain laurel; mild spring days.",
    "summer": "Warm (80-88°F) with high canopy shade and refreshing creek swimming holes.",
    "fall": "World-class autumn foliage among cliff lines and sandstone arches.",
    "winter": "Cold (22-38°F) with icicles hanging from rock overhangs."
  },
  "dangers_and_hazards": [
    "Copperheads & Timber Rattlesnakes",
    "Black Bears",
    "Flash Floods in Creek Bottoms",
    "Falling Rock/Cliff Hazards"
  ],
  "acoustic_environment": {
    "quietness_rating": "Serene Canyon Creek (Quietness Score: 9/10)",
    "common_human_made_sounds": [
      "Occasional passing 4x4 vehicle",
      "High altitude jet contrails"
    ]
  },
  "flora_and_fauna": {
    "common_plants_and_trees": [
      "Tulip Poplar",
      "Eastern Hemlock",
      "Rhododendron",
      "White White Pine"
    ],
    "common_animals": [
      "Black Bear",
      "White-tailed Deer",
      "Wild Turkey",
      "Green Salamander"
    ]
  },
  "human_demographics_and_culture": "Eastern Kentucky Appalachian mountain culture steeped in rock climbing, timber, and bluegrass music traditions.",
  "spiritual_and_folklore_data": {
    "nature_spirits_and_mythological_lore": "Appalachian folklore tells of ancient spirit arches and hidden rock shelters along Indian Creek.",
    "energetic_and_spiritual_features": "Towering sandstone bluffs and rushing waters generate an inspiring natural sanctuary."
  },
  "nearby_hiking_trails": [
    {
      "trail_name": "Indian Creek Trail to Auxier Ridge Loop",
      "length_miles": 6.8,
      "difficulty": "Moderate to Strenuous",
      "features": "Sandstone cliff ridge walk, double arch vistas, deep gorge views"
    }
  ],
  "public_reviews_summary": "Gorgeous creek-side primitive spots near Red River Gorge without crowds or fees, though cell service is weak.",
  "other_data": "Store food securely in bear canisters or vehicle trunks.",
  "last_updated": "2026-09-12"
})

ky_data.append({
  "id": "kentucky-005",
  "name": "Kaler Bottoms Wildlife Management Area Primitive Spot",
  "state": "Kentucky",
  "county": "Graves",
  "coordinates": {
    "latitude": 36.8412,
    "longitude": -88.5412,
    "elevation_ft": 360.0
  },
  "management_agency": {
    "name": "Kentucky Department of Fish and Wildlife Resources (KDFWR)",
    "type": "State",
    "phone": "(800) 858-1549",
    "website": "https://fw.ky.gov"
  },
  "rules_and_regulations": {
    "cost": "Free ($0/night primitive camping allowed for outdoorsmen)",
    "stay_limit": "14 days maximum stay limit",
    "guidelines": "Primitive dispersed camping allowed at designated gravel parking pullouts. Leave No Trace."
  },
  "waste_disposal_rules": {
    "poop_disposal": "Bury waste 6-8 inches deep 200 feet from wetlands.",
    "trash_policy": "Strict Pack-It-In Pack-It-Out rule."
  },
  "campfire_rules": {
    "permitted": True,
    "firewood_policy": "Gather dead and down wood locally.",
    "safety_requirements": "Campfires permitted in cleared ground rings. Douse cold.",
    "seasonal_fire_bans": "Subject to Kentucky state fall burn laws (Oct 1 - Dec 15)."
  },
  "access_and_road_conditions": {
    "road_type": "Paved county road to short gravel parking pullouts",
    "road_conditions": "Flat paved road access to gravel parking areas.",
    "vehicle_recommendation": "Accessible by standard FWD passenger car.",
    "scores": {
      "road_grade": 1,
      "road_terrain_difficulty": 1,
      "supply_run_pain": 3
    }
  },
  "nomad_connectivity_rating": {
    "overall_rating": "Great (4/5 Stars)",
    "verizon_reliability": "4 bars 5G/4G LTE",
    "att_reliability": "3-4 bars 4G LTE",
    "tmobile_reliability": "3-4 bars 4G LTE",
    "terrain_obstruction_risk": "Low - flat wetland basin and agricultural bottoms",
    "distance_from_tower_corridor_miles": 2.1,
    "cellular_internet_dependable": True
  },
  "amenities": [
    "Gravel Parking Flat Spot",
    "Wetland Waterfowl Watching",
    "Information Sign"
  ],
  "location_scores": {
    "distance_to_groceries_score": 7,
    "distance_to_library_score": 7,
    "distance_to_gym_score": 6,
    "terrain_score": 3,
    "quietness_score": 7
  },
  "nearest_supply_towns": [
    {
      "town_name": "Mayfield, KY",
      "distance_miles": 9.2,
      "services_available": [
        "Supermarket",
        "Gas Station",
        "Hardware Store",
        "Public Library",
        "Restaurants"
      ]
    },
    {
      "town_name": "Paducah, KY",
      "distance_miles": 21.4,
      "services_available": [
        "Major Supercenters",
        "Hospital",
        "Gym & Fitness Center",
        "Auto Repair"
      ]
    }
  ],
  "seasonal_weather_effects": {
    "spring": "Mild with wet cypress-tupelo bottomland flooding.",
    "summer": "Warm and humid (84-92°F); heavy insect activity.",
    "fall": "Crisp autumn weather with waterfowl migration.",
    "winter": "Cool to chilly (30-45°F) with light snow."
  },
  "dangers_and_hazards": [
    "Mosquitoes and Biting Insects",
    "Cottonmouth Snakes (Wetlands)",
    "Seasonal Flooding"
  ],
  "acoustic_environment": {
    "quietness_rating": "Peaceful Bottomland (Quietness Score: 7/10)",
    "common_human_made_sounds": [
      "Distant highway traffic",
      "Agricultural tractors"
    ]
  },
  "flora_and_fauna": {
    "common_plants_and_trees": [
      "Bald Cypress",
      "Water Tupelo",
      "Overcup Oak",
      "Buttonbush"
    ],
    "common_animals": [
      "Wood Duck",
      "Mallard",
      "White-tailed Deer",
      "Beaver",
      "Barred Owl"
    ]
  },
  "human_demographics_and_culture": "Western Kentucky Jackson Purchase agrarian and waterfowl hunting country.",
  "spiritual_and_folklore_data": {
    "nature_spirits_and_mythological_lore": "Tales of swamp spirits and ancient cypress grove guardians in the Clarks River basin.",
    "energetic_and_spiritual_features": "Quiet wetland waters provide a peaceful, rhythmic pulse."
  },
  "nearby_hiking_trails": [
    {
      "trail_name": "Kaler Bottoms Wetland Access Trail",
      "length_miles": 2.2,
      "difficulty": "Easy",
      "features": "Flat wetland boardwalk and dike trail, duck observation perches"
    }
  ],
  "public_reviews_summary": "Super convenient stopover with fast 5G cell signal and zero cost, though bring bug spray in summer.",
  "other_data": "Wear bright hunter orange during fall shotgun and archery deer seasons.",
  "last_updated": "2026-09-12"
})
save_state(ky_data, ky_path)

# Louisiana +2 sites (reach 5)
la_data, la_path = load_state('louisiana')
la_data.append({
  "id": "louisiana-004",
  "name": "Kisatchie Hills Wilderness Primitive Trailside Zone",
  "state": "Louisiana",
  "county": "Natchitoches",
  "coordinates": {
    "latitude": 31.4821,
    "longitude": -93.0142,
    "elevation_ft": 280.0
  },
  "management_agency": {
    "name": "U.S. Forest Service - Kisatchie National Forest (Kisatchie Ranger District)",
    "type": "Federal",
    "phone": "(318) 472-1840",
    "website": "https://www.fs.usda.gov/kisatchie"
  },
  "rules_and_regulations": {
    "cost": "Free ($0/night wilderness dispersed camping)",
    "stay_limit": "14 days maximum stay limit",
    "guidelines": "Dispersed primitive camping allowed along Backbone Trail within Kisatchie Hills Wilderness ('Little Grand Canyon of Louisiana'). Camp 100 ft from trail. Leave No Trace."
  },
  "waste_disposal_rules": {
    "poop_disposal": "Bury waste 6-8 inches deep in cat-holes 200 feet from Bayou Cypre and trail. Pack out paper.",
    "trash_policy": "Strict Pack-It-In Pack-It-Out rule."
  },
  "campfire_rules": {
    "permitted": True,
    "firewood_policy": "Dead and down wood collection allowed.",
    "safety_requirements": "Use existing rock rings. Douse cold with water.",
    "seasonal_fire_bans": "Subject to USFS dry season burn bans."
  },
  "access_and_road_conditions": {
    "road_type": "Gravel forest service roads (Longleaf Trail Scenic Byway)",
    "road_conditions": "Paved Longleaf Scenic Byway to gravel trailhead parking lot.",
    "vehicle_recommendation": "Accessible by standard FWD passenger car.",
    "scores": {
      "road_grade": 2,
      "road_terrain_difficulty": 3,
      "supply_run_pain": 5
    }
  },
  "nomad_connectivity_rating": {
    "overall_rating": "Fair (2.5/5 Stars)",
    "verizon_reliability": "2 bars 4G LTE on high sandstone ridges",
    "att_reliability": "2 bars 4G LTE",
    "tmobile_reliability": "1 bar 4G LTE",
    "terrain_obstruction_risk": "Moderate - longleaf pine ridges and sandstone outcrops",
    "distance_from_tower_corridor_miles": 7.8,
    "cellular_internet_dependable": False
  },
  "amenities": [
    "Sandstone Ridge Vistas",
    "Longleaf Pine Canopy",
    "Primitive Fire Rings"
  ],
  "location_scores": {
    "distance_to_groceries_score": 5,
    "distance_to_library_score": 5,
    "distance_to_gym_score": 4,
    "terrain_score": 7,
    "quietness_score": 9
  },
  "nearest_supply_towns": [
    {
      "town_name": "Natchitoches, LA",
      "distance_miles": 21.8,
      "services_available": [
        "Supermarket",
        "Hospital",
        "Public Library",
        "Historic District",
        "Restaurants"
      ]
    },
    {
      "town_name": "Alexandria, LA",
      "distance_miles": 42.5,
      "services_available": [
        "Supercenters",
        "Airport",
        "Gym & Fitness Center",
        "Auto Repair"
      ]
    }
  ],
  "seasonal_weather_effects": {
    "spring": "Pleasant spring weather with blooming dogwood and wild azalea.",
    "summer": "Hot and humid (90-96°F); heavy sun exposure on open pine ridges.",
    "fall": "Mild, crisp autumn weather with rustling pine breezes.",
    "winter": "Mild winter temperatures (40-60°F); great winter backpacking."
  },
  "dangers_and_hazards": [
    "High Summer Heat & Humidity",
    "Venomous Snakes (Copperheads, Pygmy Rattlesnakes)",
    "Ticks and Chiggers"
  ],
  "acoustic_environment": {
    "quietness_rating": "Pine Whispering Quiet (Quietness Score: 9/10)",
    "common_human_made_sounds": [
      "High altitude military jets from Barksdale AFB",
      "Wind through longleaf needles"
    ]
  },
  "flora_and_fauna": {
    "common_plants_and_trees": [
      "Longleaf Pine",
      "Blackjack Oak",
      "Red Cockaded Woodpecker Habitat",
      "Wild Azalea"
    ],
    "common_animals": [
      "White-tailed Deer",
      "Red-cockaded Woodpecker",
      "Louisiana Pine Snake",
      "Gray Fox"
    ]
  },
  "human_demographics_and_culture": "Central Louisiana Creole and timber heritage along the historic El Camino Real trail corridor.",
  "spiritual_and_folklore_data": {
    "nature_spirits_and_mythological_lore": "Local legends recall indigenous Caddo reverence for the high sandstone hills of Kisatchie.",
    "energetic_and_spiritual_features": "Open longleaf pine savannas provide an expansive, sun-filled wilderness energy."
  },
  "nearby_hiking_trails": [
    {
      "trail_name": "Backbone Wilderness Trail",
      "length_miles": 7.3,
      "difficulty": "Moderate",
      "features": "Sandstone ridge top vistas, longleaf pine savannas, dry creek bed ravines"
    }
  ],
  "public_reviews_summary": "Surprising elevation changes and open pine savanna views unique in Louisiana, with peaceful backcountry solitude.",
  "other_data": "Water sources in wilderness are seasonal; carry ample drinking water.",
  "last_updated": "2026-09-12"
})

la_data.append({
  "id": "louisiana-005",
  "name": "Pearl River Wildlife Management Area Primitive Spot",
  "state": "Louisiana",
  "county": "St. Tammany",
  "coordinates": {
    "latitude": 30.3812,
    "longitude": -89.7452,
    "elevation_ft": 25.0
  },
  "management_agency": {
    "name": "Louisiana Department of Wildlife and Fisheries (LDWF)",
    "type": "State",
    "phone": "(985) 543-4777",
    "website": "https://www.wlf.louisiana.gov"
  },
  "rules_and_regulations": {
    "cost": "Free ($0/night, free WMA access permit required online)",
    "stay_limit": "14 consecutive days limit",
    "guidelines": "Primitive camping allowed at designated primitive boat launch campsites along the Honey Island swamp corridor. Leave No Trace."
  },
  "waste_disposal_rules": {
    "poop_disposal": "Bury waste 6-8 inches deep at least 200 feet from Pearl River.",
    "trash_policy": "Strict Carry-In Carry-Out policy."
  },
  "campfire_rules": {
    "permitted": True,
    "firewood_policy": "Gather dead and down wood locally.",
    "safety_requirements": "Campfires permitted in cleared ground rings. Extinguish cold.",
    "seasonal_fire_bans": "Subject to LDWF dry season burn bans."
  },
  "access_and_road_conditions": {
    "road_type": "Paved state highway to gravel WMA access road",
    "road_conditions": "Flat gravel road leading to river boat launch parking area.",
    "vehicle_recommendation": "Accessible by standard FWD passenger car.",
    "scores": {
      "road_grade": 1,
      "road_terrain_difficulty": 2,
      "supply_run_pain": 3
    }
  },
  "nomad_connectivity_rating": {
    "overall_rating": "Great (4/5 Stars)",
    "verizon_reliability": "4 bars 5G/4G LTE",
    "att_reliability": "4 bars 5G",
    "tmobile_reliability": "3-4 bars 5G",
    "terrain_obstruction_risk": "Low - coastal cypress swamp basin",
    "distance_from_tower_corridor_miles": 2.5,
    "cellular_internet_dependable": True
  },
  "amenities": [
    "Boat Launch Access",
    "Gravel Flat Campsites",
    "Swamp Waterway Views"
  ],
  "location_scores": {
    "distance_to_groceries_score": 8,
    "distance_to_library_score": 8,
    "distance_to_gym_score": 7,
    "terrain_score": 4,
    "quietness_score": 7
  },
  "nearest_supply_towns": [
    {
      "town_name": "Slidell, LA",
      "distance_miles": 8.4,
      "services_available": [
        "Supercenter",
        "Hospital",
        "Public Library",
        "Gym & Fitness Center",
        "Auto Repair"
      ]
    },
    {
      "town_name": "New Orleans, LA",
      "distance_miles": 38.0,
      "services_available": [
        "International Airport",
        "Major Hospitals",
        "Metropolitan Amenities"
      ]
    }
  ],
  "seasonal_weather_effects": {
    "spring": "Mild weather with booming frog choruses and lush swamp greenery.",
    "summer": "Hot and humid (88-95°F) with afternoon rain squalls.",
    "fall": "Pleasant, mild weather; excellent fishing and paddling.",
    "winter": "Mild winter climate (45-65°F) with occasional cool fronts."
  },
  "dangers_and_hazards": [
    "Alligators",
    "Mosquitoes and Biting Flies",
    "Venomous Cottonmouth Snakes",
    "High Swamp Humidity"
  ],
  "acoustic_environment": {
    "quietness_rating": "Swamp Audio Symphony (Quietness Score: 7/10)",
    "common_human_made_sounds": [
      "Distant I-10 traffic hum",
      "Outboard motorboats on river"
    ]
  },
  "flora_and_fauna": {
    "common_plants_and_trees": [
      "Bald Cypress",
      "Water Tupelo",
      "Spanish Moss",
      "Palmetto"
    ],
    "common_animals": [
      "American Alligator",
      "Wild Boar",
      "Barred Owl",
      "Swamp Rabbit",
      "Prothonotary Warbler"
    ]
  },
  "human_demographics_and_culture": "Honey Island swamp folklore and Louisiana Cajun/Creole sportsman culture.",
  "spiritual_and_folklore_data": {
    "nature_spirits_and_mythological_lore": "Famous Louisiana folklore of the 'Honey Island Swamp Monster', a legendary bipedal cryptid said to haunt cypress bayous.",
    "energetic_and_spiritual_features": "Ancient moss-draped cypress trees generate a mysterious, enchanting atmosphere."
  },
  "nearby_hiking_trails": [
    {
      "trail_name": "Pearl River Honey Island Swamp Trail",
      "length_miles": 3.4,
      "difficulty": "Easy",
      "features": "Moss-draped cypress sloughs, river boardwalks, alligator viewing"
    }
  ],
  "public_reviews_summary": "Superb cell signal close to Slidell and New Orleans, authentic cypress swamp atmosphere, zero cost.",
  "other_data": "Keep food secured from raccoons and maintain safe distance from alligators.",
  "last_updated": "2026-09-12"
})
save_state(la_data, la_path)

# Maine +2 sites (reach 5)
me_data, me_path = load_state('maine')
me_data.append({
  "id": "maine-004",
  "name": "Debsconeag Lakes Wilderness Primitive Dispersed Sites",
  "state": "Maine",
  "county": "Piscataquis",
  "coordinates": {
    "latitude": 45.7812,
    "longitude": -69.0142,
    "elevation_ft": 640.0
  },
  "management_agency": {
    "name": "Maine Bureau of Parks and Lands / Nature Conservancy",
    "type": "State / Non-Profit",
    "phone": "(207) 287-3821",
    "website": "https://www.maine.gov/dacf/parks/"
  },
  "rules_and_regulations": {
    "cost": "Free ($0/night for primitive backcountry watercraft sites)",
    "stay_limit": "14 consecutive days limit",
    "guidelines": "Primitive camping at designated backcountry lake sites accessible by watercraft or foot. Leave No Trace."
  },
  "waste_disposal_rules": {
    "poop_disposal": "Utilize primitive wilderness box privies where available, or bury 6-8 inches deep 200 ft from lake.",
    "trash_policy": "Strict Pack-It-In Pack-It-Out policy."
  },
  "campfire_rules": {
    "permitted": True,
    "firewood_policy": "Dead and down wood collection permitted on site.",
    "safety_requirements": "Campfires permitted only in metal/stone fire rings. Douse with lake water until dead out.",
    "seasonal_fire_bans": "Subject to Maine Forest Service dry weather bans."
  },
  "access_and_road_conditions": {
    "road_type": "Unpaved timber logging gravel road (Golden Road corridor)",
    "road_conditions": "Active logging gravel road; rough washboards and logging truck right-of-way.",
    "vehicle_recommendation": "High clearance CUV/SUV recommended; standard FWD cars must drive carefully.",
    "scores": {
      "road_grade": 6,
      "road_terrain_difficulty": 6,
      "supply_run_pain": 7
    }
  },
  "nomad_connectivity_rating": {
    "overall_rating": "Poor (1/5 Stars)",
    "verizon_reliability": "1 bar 4G LTE spotty on open lake waters",
    "att_reliability": "No signal in deep forest",
    "tmobile_reliability": "No signal",
    "terrain_obstruction_risk": "High - dense spruce-fir forest and Mount Katahdin valley terrain",
    "distance_from_tower_corridor_miles": 22.0,
    "cellular_internet_dependable": False
  },
  "amenities": [
    "Wilderness Lake Shoreline",
    "Box Privy",
    "Metal Fire Ring",
    "Canoe Access"
  ],
  "location_scores": {
    "distance_to_groceries_score": 3,
    "distance_to_library_score": 3,
    "distance_to_gym_score": 2,
    "terrain_score": 9,
    "quietness_score": 10
  },
  "nearest_supply_towns": [
    {
      "town_name": "Millinocket, ME",
      "distance_miles": 24.5,
      "services_available": [
        "Grocery Store",
        "Gas Station",
        "Outfitter",
        "Hardware Store",
        "Local Dining"
      ]
    },
    {
      "town_name": "Bangor, ME",
      "distance_miles": 92.0,
      "services_available": [
        "International Airport",
        "Major Supercenters",
        "Hospitals",
        "Full Urban Amenities"
      ]
    }
  ],
  "seasonal_weather_effects": {
    "spring": "Blackfly season in May/June; cold lake water and melting snowpack.",
    "summer": "Pleasant summer weather (70-80°F) with warm lake swimming and loon calls.",
    "fall": "World-class vibrant foliage reflection on pristine north woods lakes.",
    "winter": "Severe sub-zero winter (-10 to 20°F); heavy snow pack."
  },
  "dangers_and_hazards": [
    "Black Bears & Moose (Bears canisters recommended)",
    "Blackflies & Mosquitoes (June)",
    "Logging Truck Traffic on Access Roads",
    "Severe Cold Night Temps in Shoulder Seasons"
  ],
  "acoustic_environment": {
    "quietness_rating": "Pristine North Woods Silence (Quietness Score: 10/10)",
    "common_human_made_sounds": [
      "Occasional floatplane high overhead"
    ]
  },
  "flora_and_fauna": {
    "common_plants_and_trees": [
      "Red Spruce",
      "Balsam Fir",
      "Paper Birch",
      "Eastern White Pine"
    ],
    "common_animals": [
      "Moose",
      "Common Loon",
      "Black Bear",
      "Lynx",
      "Pine Marten"
    ]
  },
  "human_demographics_and_culture": "Maine North Woods logging, sporting camp, and wilderness conservation heritage near Baxter State Park.",
  "spiritual_and_folklore_data": {
    "nature_spirits_and_mythological_lore": "Penobscot nation sacred reverence for Katahdin and surrounding wilderness waters, home of Pamola, spirit of the mountain.",
    "energetic_and_spiritual_features": "Crystal clear glacial lakes reflecting ancient granite peaks generate profound peace."
  },
  "nearby_hiking_trails": [
    {
      "trail_name": "Debsconeag Ice Caves Trail",
      "length_miles": 2.2,
      "difficulty": "Moderate",
      "features": "Deep granite ice caves holding ice year-round, pristine lake views"
    }
  ],
  "public_reviews_summary": "Incredible Maine wilderness experience with loons singing and views of Katahdin, but requires full self-reliance.",
  "other_data": "Always yield immediately to loaded logging trucks on the Golden Road.",
  "last_updated": "2026-09-12"
})

me_data.append({
  "id": "maine-005",
  "name": "Duck Lake Public Reserve Land Primitive Campsites",
  "state": "Maine",
  "county": "Hancock",
  "coordinates": {
    "latitude": 45.1412,
    "longitude": -68.0812,
    "elevation_ft": 410.0
  },
  "management_agency": {
    "name": "Maine Bureau of Parks and Lands",
    "type": "State",
    "phone": "(207) 941-4412",
    "website": "https://www.maine.gov/dacf/parks/"
  },
  "rules_and_regulations": {
    "cost": "Free ($0/night primitive public reserve camping)",
    "stay_limit": "14 days maximum stay limit",
    "guidelines": "Dispersed primitive camping permitted at established lake access pullouts on Duck Lake and Gassabias Lake. Leave No Trace."
  },
  "waste_disposal_rules": {
    "poop_disposal": "Bury waste 6-8 inches deep 200 feet from lake shores. Pack out toilet paper.",
    "trash_policy": "Strict Pack-It-In Pack-It-Out policy."
  },
  "campfire_rules": {
    "permitted": True,
    "firewood_policy": "Gather dead and down firewood locally.",
    "safety_requirements": "Use existing stone fire rings. Extinguish cold with lake water.",
    "seasonal_fire_bans": "Subject to Maine Forest Service fire warnings."
  },
  "access_and_road_conditions": {
    "road_type": "Gravel forest service roads",
    "road_conditions": "Graded gravel forest roads; accessible during dry seasons.",
    "vehicle_recommendation": "Standard FWD car accessible with careful driving.",
    "scores": {
      "road_grade": 4,
      "road_terrain_difficulty": 4,
      "supply_run_pain": 6
    }
  },
  "nomad_connectivity_rating": {
    "overall_rating": "Fair (2/5 Stars)",
    "verizon_reliability": "1-2 bars 4G LTE near lake shores",
    "att_reliability": "1 bar 4G LTE",
    "tmobile_reliability": "No signal",
    "terrain_obstruction_risk": "Moderate - rolling spruce forest terrain",
    "distance_from_tower_corridor_miles": 14.2,
    "cellular_internet_dependable": False
  },
  "amenities": [
    "Primitive Stone Fire Rings",
    "Pristine Lake Water Access",
    "Gravel Parking Pullouts"
  ],
  "location_scores": {
    "distance_to_groceries_score": 4,
    "distance_to_library_score": 4,
    "distance_to_gym_score": 3,
    "terrain_score": 7,
    "quietness_score": 9
  },
  "nearest_supply_towns": [
    {
      "town_name": "Lincoln, ME",
      "distance_miles": 22.4,
      "services_available": [
        "Supermarket",
        "Gas Station",
        "Hospital",
        "Hardware Store",
        "Restaurants"
      ]
    },
    {
      "town_name": "Bangor, ME",
      "distance_miles": 58.0,
      "services_available": [
        "International Airport",
        "Major Retail Chains",
        "Gym & Fitness Center"
      ]
    }
  ],
  "seasonal_weather_effects": {
    "spring": "Cool spring with loon arrivals and blooming blueberry barrens.",
    "summer": "Warm summer weather (75-82°F) ideal for canoeing and lake swimming.",
    "fall": "Brilliant Maine autumn foliage; cool night temperatures.",
    "winter": "Cold winter with snow and ice fishing on frozen lakes."
  },
  "dangers_and_hazards": [
    "Black Bears",
    "Mosquitoes and Blackflies (June)",
    "Rough Dirt Roads"
  ],
  "acoustic_environment": {
    "quietness_rating": "Quiet Lake Atmosphere (Quietness Score: 9/10)",
    "common_human_made_sounds": [
      "Distant outboard motor on lake",
      "Passing logging truck"
    ]
  },
  "flora_and_fauna": {
    "common_plants_and_trees": [
      "White Pine",
      "Balsam Fir",
      "Wild Blueberry",
      "Bunchberry"
    ],
    "common_animals": [
      "Moose",
      "Common Loon",
      "White-tailed Deer",
      "Bald Eagle"
    ]
  },
  "human_demographics_and_culture": "Down East Maine inland lake and forest timber tradition.",
  "spiritual_and_folklore_data": {
    "nature_spirits_and_mythological_lore": "Passamaquoddy tales honor quiet lakes guarded by nature spirits.",
    "energetic_and_spiritual_features": "Peaceful water reflections and pine breezes foster quiet introspection."
  },
  "nearby_hiking_trails": [
    {
      "trail_name": "Duck Mountain Trail",
      "length_miles": 3.8,
      "difficulty": "Moderate",
      "features": "Summit fire tower view over surrounding lakes and Maine timberlands"
    }
  ],
  "public_reviews_summary": "Peaceful, free public land camping with great fishing and loon songs, far from coastal tourist crowds.",
  "other_data": "Boil or filter all water taken from lakes.",
  "last_updated": "2026-09-12"
})
save_state(me_data, me_path)

# Maryland +2 sites (reach 5)
md_data, md_path = load_state('maryland')
md_data.append({
  "id": "maryland-004",
  "name": "Green Ridge State Forest Dispersed Backpacking Primitive Zone",
  "state": "Maryland",
  "county": "Allegany",
  "coordinates": {
    "latitude": 39.6125,
    "longitude": -78.4512,
    "elevation_ft": 1120.0
  },
  "management_agency": {
    "name": "Maryland Department of Natural Resources (DNR) - Forest Service",
    "type": "State",
    "phone": "(301) 478-3124",
    "website": "https://dnr.maryland.gov/forests"
  },
  "rules_and_regulations": {
    "cost": "Free ($0/night primitive trailside backpacking along C&O Canal & Green Ridge Trail)",
    "stay_limit": "14 days maximum stay limit",
    "guidelines": "Primitive dispersed backpacking permitted at designated trailside sites at least 100 feet from trails and water. Self-register at forest HQ."
  },
  "waste_disposal_rules": {
    "poop_disposal": "Bury waste 6-8 inches deep in cat-holes at least 200 feet from Potomac River and streams.",
    "trash_policy": "Strict Pack-It-In Pack-It-Out policy."
  },
  "campfire_rules": {
    "permitted": True,
    "firewood_policy": "Gather dead and down wood locally within forest.",
    "safety_requirements": "Campfires allowed in existing stone fire rings. Extinguish cold.",
    "seasonal_fire_bans": "Subject to Maryland DNR dry season fire warnings."
  },
  "access_and_road_conditions": {
    "road_type": "Paved state road to gravel trailhead parking",
    "road_conditions": "Paved roads to gravel forest parking lots; hike required to primitive trail sites.",
    "vehicle_recommendation": "Accessible by standard FWD passenger car.",
    "scores": {
      "road_grade": 2,
      "road_terrain_difficulty": 3,
      "supply_run_pain": 4
    }
  },
  "nomad_connectivity_rating": {
    "overall_rating": "Good (3.5/5 Stars)",
    "verizon_reliability": "3-4 bars 4G LTE on ridge lines",
    "att_reliability": "3 bars 4G LTE",
    "tmobile_reliability": "2-3 bars 4G LTE",
    "terrain_obstruction_risk": "Moderate - Ridge and Valley Appalachian terrain",
    "distance_from_tower_corridor_miles": 3.8,
    "cellular_internet_dependable": True
  },
  "amenities": [
    "Potomac River Vistas",
    "Trailhead Parking",
    "Primitive Stone Fire Rings"
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
      "town_name": "Hancock, MD",
      "distance_miles": 12.5,
      "services_available": [
        "Grocery Store",
        "Gas Station",
        "Hardware Store",
        "Restaurants"
      ]
    },
    {
      "town_name": "Cumberland, MD",
      "distance_miles": 24.8,
      "services_available": [
        "Supercenter",
        "Hospital",
        "Public Library",
        "Gym & Fitness Center",
        "Auto Repair"
      ]
    }
  ],
  "seasonal_weather_effects": {
    "spring": "Lush green Appalachian hardwood emergence and spring wildflowers.",
    "summer": "Warm days (80-88°F) with cool Potomac river breezes.",
    "fall": "Stunning Ridge & Valley fall foliage colors.",
    "winter": "Cold (22-38°F) with light snow on mountain ridges."
  },
  "dangers_and_hazards": [
    "Copperheads & Timber Rattlesnakes",
    "Black Bears",
    "Ticks"
  ],
  "acoustic_environment": {
    "quietness_rating": "Appalachian Ridge Quiet (Quietness Score: 8/10)",
    "common_human_made_sounds": [
      "Distant CSX train horn along Potomac river valley",
      "High altitude commercial flights"
    ]
  },
  "flora_and_fauna": {
    "common_plants_and_trees": [
      "Chestnut Oak",
      "Virginia Pine",
      "Mountain Laurel",
      "Pawpaw"
    ],
    "common_animals": [
      "White-tailed Deer",
      "Black Bear",
      "Wild Turkey",
      "Bald Eagle"
    ]
  },
  "human_demographics_and_culture": "Western Maryland mountain and C&O Canal historic transportation heritage.",
  "spiritual_and_folklore_data": {
    "nature_spirits_and_mythological_lore": "Civil War history and canal boat legends echo along the Potomac river bends.",
    "energetic_and_spiritual_features": "High ridge overlooks provide invigorating panoramic views."
  },
  "nearby_hiking_trails": [
    {
      "trail_name": "Green Ridge Backpacking Trail",
      "length_miles": 8.5,
      "difficulty": "Moderate",
      "features": "Appalachian ridge line walk, Potomac river overlooks, pine forests"
    }
  ],
  "public_reviews_summary": "Extensive state forest with easy access from I-68, scenic overlooks, and solid cell coverage.",
  "other_data": "Self-register at forest headquarters kiosk prior to backcountry camping.",
  "last_updated": "2026-09-12"
})

md_data.append({
  "id": "maryland-005",
  "name": "Idylwild Wildlife Management Area Primitive Spot",
  "state": "Maryland",
  "county": "Caroline",
  "coordinates": {
    "latitude": 38.7125,
    "longitude": -75.7412,
    "elevation_ft": 40.0
  },
  "management_agency": {
    "name": "Maryland Department of Natural Resources (DNR) - Wildlife & Heritage Service",
    "type": "State",
    "phone": "(410) 822-8370",
    "website": "https://dnr.maryland.gov/wildlife"
  },
  "rules_and_regulations": {
    "cost": "Free ($0/night primitive camping allowed for outdoor recreationalists)",
    "stay_limit": "3 consecutive nights limit",
    "guidelines": "Primitive dispersed camping allowed near parking access areas. Leave No Trace."
  },
  "waste_disposal_rules": {
    "poop_disposal": "Bury waste 6-8 inches deep 200 feet from Marshyhope Creek.",
    "trash_policy": "Strict Pack-It-In Pack-It-Out rule."
  },
  "campfire_rules": {
    "permitted": True,
    "firewood_policy": "Gather dead and down wood locally.",
    "safety_requirements": "Campfires allowed in cleared ground rings. Extinguish cold.",
    "seasonal_fire_bans": "Subject to Maryland state fire advisories."
  },
  "access_and_road_conditions": {
    "road_type": "Paved county road to dirt/gravel access lot",
    "road_conditions": "Flat paved road access to gravel parking lot.",
    "vehicle_recommendation": "Accessible by standard FWD passenger car.",
    "scores": {
      "road_grade": 1,
      "road_terrain_difficulty": 1,
      "supply_run_pain": 3
    }
  },
  "nomad_connectivity_rating": {
    "overall_rating": "Great (4/5 Stars)",
    "verizon_reliability": "4 bars 5G/4G LTE",
    "att_reliability": "4 bars 5G",
    "tmobile_reliability": "3-4 bars 5G",
    "terrain_obstruction_risk": "Low - flat eastern shore coastal plain",
    "distance_from_tower_corridor_miles": 1.5,
    "cellular_internet_dependable": True
  },
  "amenities": [
    "Gravel Flat Campsite",
    "Creek Kayak Launch",
    "Wildlife Watching"
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
      "town_name": "Federalsburg, MD",
      "distance_miles": 4.2,
      "services_available": [
        "Grocery Store",
        "Gas Station",
        "Post Office",
        "Restaurants"
      ]
    },
    {
      "town_name": "Denton, MD",
      "distance_miles": 16.5,
      "services_available": [
        "Supermarket",
        "Hospital",
        "Public Library",
        "Gym & Fitness Center",
        "Auto Repair"
      ]
    }
  ],
  "seasonal_weather_effects": {
    "spring": "Mild spring weather with songbird migrations.",
    "summer": "Warm and humid (82-88°F); mosquitoes present near creek.",
    "fall": "Pleasant autumn days; great paddling conditions.",
    "winter": "Chilly (32-45°F) with light coastal breezes."
  },
  "dangers_and_hazards": [
    "Ticks",
    "Mosquitoes",
    "Poison Ivy"
  ],
  "acoustic_environment": {
    "quietness_rating": "Quiet Eastern Shore Countryside (Quietness Score: 7/10)",
    "common_human_made_sounds": [
      "Passing rural traffic",
      "Farm equipment"
    ]
  },
  "flora_and_fauna": {
    "common_plants_and_trees": [
      "Loblolly Pine",
      "Sweetgum",
      "American Holly",
      "Mountain Laurel"
    ],
    "common_animals": [
      "White-tailed Deer",
      "Delmarva Fox Squirrel",
      "Wild Turkey",
      "Wood Duck"
    ]
  },
  "human_demographics_and_culture": "Maryland Eastern Shore agricultural and marshland paddling heritage.",
  "spiritual_and_folklore_data": {
    "nature_spirits_and_mythological_lore": "Nanticoke river legends celebrate peaceful wetland forest guardians.",
    "energetic_and_spiritual_features": "Calm coastal plain forest providing a tranquil, restful setting."
  },
  "nearby_hiking_trails": [
    {
      "trail_name": "Idylwild Wildlife Trail",
      "length_miles": 3.2,
      "difficulty": "Easy",
      "features": "Flat pine forest path, Marshyhope Creek views, rare plant habitats"
    }
  ],
  "public_reviews_summary": "Extremely fast 5G internet, zero fees, and peaceful Eastern Shore pine forest atmosphere.",
  "other_data": "Fluorescent orange required during deer hunting seasons.",
  "last_updated": "2026-09-12"
})
save_state(md_data, md_path)

print("Batch 2 expansion complete! Illinois, Indiana, Iowa, Kansas, Kentucky, Louisiana, Maine, and Maryland now have 5 primitive campsites each!")
