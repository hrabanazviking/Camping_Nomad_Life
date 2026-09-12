import json

def load_state(name):
    path = f'/home/volmarr/.gemini/antigravity/scratch/Camping_Nomad_Life/states/{name}.json'
    with open(path, 'r') as f:
        return json.load(f), path

def save_state(data, path):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

# Colorado (+5 sites -> 10 total)
co, co_path = load_state('colorado')
co.extend([
  {
    "id": "colorado-006",
    "name": "San Juan National Forest Hermosa Creek Dispersed Zone",
    "state": "Colorado",
    "county": "La Plata",
    "coordinates": {"latitude": 37.4412, "longitude": -107.8512, "elevation_ft": 7820.0},
    "management_agency": {"name": "U.S. Forest Service - San Juan National Forest (Columbine Ranger District)", "type": "Federal", "phone": "(970) 884-2512", "website": "https://www.fs.usda.gov/sanjuan"},
    "rules_and_regulations": {"cost": "Free ($0/night primitive dispersed forest camping)", "stay_limit": "14 days maximum stay within a 30-day window", "guidelines": "Dispersed primitive camping allowed along Hermosa Park Road (FR 578) pullouts outside Hermosa Creek Special Management Area boundary. Leave No Trace."},
    "waste_disposal_rules": {"poop_disposal": "Bury waste 6-8 inches deep 200 ft from Hermosa Creek. Pack out toilet paper.", "trash_policy": "Strict Pack-It-In Pack-It-Out policy."},
    "campfire_rules": {"permitted": True, "firewood_policy": "Gather dead and down wood locally.", "safety_requirements": "Campfires permitted in cleared stone rings. Extinguish cold with creek water.", "seasonal_fire_bans": "Subject to USFS Stage 1 & 2 fire restrictions during dry summer/fall."},
    "access_and_road_conditions": {"road_type": "Gravel forest service road (FR 578)", "road_conditions": "Graded gravel road with steep mountain grades and flat pullouts.", "vehicle_recommendation": "CUV, SUV, or standard FWD passenger car driven carefully.", "scores": {"road_grade": 4, "road_terrain_difficulty": 4, "supply_run_pain": 4}},
    "nomad_connectivity_rating": {"overall_rating": "Fair (2.5/5 Stars)", "verizon_reliability": "2 bars 4G LTE on high ridge pullouts", "att_reliability": "2 bars 4G LTE", "tmobile_reliability": "1 bar 4G LTE", "terrain_obstruction_risk": "High - San Juan mountain canyon walls and aspen-spruce canopy", "distance_from_tower_corridor_miles": 8.2, "cellular_internet_dependable": False},
    "amenities": ["Hermosa Creek Water Access", "San Juan Mountain Overlooks", "Aspen Canopy"],
    "location_scores": {"distance_to_groceries_score": 6, "distance_to_library_score": 6, "distance_to_gym_score": 5, "terrain_score": 10, "quietness_score": 9},
    "nearest_supply_towns": [{"town_name": "Durango, CO", "distance_miles": 18.5, "services_available": ["Supercenters", "Hospital", "Public Library", "Gym & Fitness Center", "Outfitters", "College Amenities"]}],
    "seasonal_weather_effects": {"spring": "High snowmelt thaw through June; muddy roads.", "summer": "Pleasant 7,800-ft mountain summer (72-80°F) with cool mountain night air (42°F).", "fall": "World-class golden aspen leaf display in late September.", "winter": "Snowbound road; accessible by snowmobile or ski touring."},
    "dangers_and_hazards": ["Black Bears (Bear canisters/hang recommended)", "High Altitude Weather Shifts", "Flash Floods in Creek Beds"],
    "acoustic_environment": {"quietness_rating": "San Juan Mountain Quiet (Quietness Score: 9/10)", "common_human_made_sounds": ["Occasional forest road car", "High altitude jet contrails"]},
    "flora_and_fauna": {
      "common_plants_and_trees": ["Quaking Aspen", "Ponderosa Pine", "Douglas Fir", "Colorado Blue Spruce"],
      "common_animals": ["Elk", "Mule Deer", "Black Bear", "Pine Marten", "Cutthroat Trout"]
    },
    "human_demographics_and_culture": "Southwestern Colorado Durango mountain biking, skiing, and San Juan wilderness conservation culture.",
    "spiritual_and_folklore_data": {
      "nature_spirits_and_mythological_lore": "Ute traditions honor the San Juan mountains as sacred high sky peak realms.",
      "energetic_and_spiritual_features": "Giant aspen groves framed by 13,000-foot red sandstone and granite peaks generate an awe-inspiring sanctuary."
    },
    "nearby_hiking_trails": [{"trail_name": "Hermosa Creek National Recreation Trail", "length_miles": 18.5, "difficulty": "Moderate to Strenuous", "features": "Pristine mountain stream, aspen forests, San Juan peak vistas"}],
    "public_reviews_summary": "Incredible golden aspen foliage and mountain stream primitive camping near Durango with zero cost.",
    "other_data": "Filter all drinking water taken from Hermosa Creek.",
    "last_updated": "2026-09-12"
  },
  {
    "id": "colorado-007",
    "name": "Uncompahgre National Forest Divide Road Primitive Zone",
    "state": "Colorado",
    "county": "Montrose",
    "coordinates": {"latitude": 38.3812, "longitude": -108.1852, "elevation_ft": 8920.0},
    "management_agency": {"name": "U.S. Forest Service - Grand Mesa, Uncompahgre, and Gunnison National Forests (Ouray Ranger District)", "type": "Federal", "phone": "(970) 240-5300", "website": "https://www.fs.usda.gov/gmug"},
    "rules_and_regulations": {"cost": "Free ($0/night primitive dispersed forest camping)", "stay_limit": "14 days maximum stay within a 30-day window", "guidelines": "Dispersed primitive camping allowed along Divide Road (FR 503) pullouts across Uncompahgre Plateau. Leave No Trace."},
    "waste_disposal_rules": {"poop_disposal": "Bury waste 6-8 inches deep 200 ft from mountain ponds and springs. Pack out toilet paper.", "trash_policy": "Strict Pack-It-In Pack-It-Out policy."},
    "campfire_rules": {"permitted": True, "firewood_policy": "Gather dead and down wood locally.", "safety_requirements": "Campfires permitted in cleared stone rings. Extinguish cold.", "seasonal_fire_bans": "Subject to USFS Stage 1 & 2 fire restrictions during dry summer."},
    "access_and_road_conditions": {"road_type": "Gravel forest service road (Divide Road / FR 503)", "road_conditions": "Graded gravel road along plateau rim; flat turnouts.", "vehicle_recommendation": "Accessible by standard FWD passenger car in dry weather.", "scores": {"road_grade": 3, "road_terrain_difficulty": 3, "supply_run_pain": 4}},
    "nomad_connectivity_rating": {"overall_rating": "Great (4/5 Stars)", "verizon_reliability": "4 bars 5G/4G LTE due to high 9,000-ft plateau elevation overlooking Montrose basin", "att_reliability": "3-4 bars 4G LTE", "tmobile_reliability": "3 bars 4G LTE", "terrain_obstruction_risk": "Low - high plateau rim line", "distance_from_tower_corridor_miles": 3.1, "cellular_internet_dependable": True},
    "amenities": ["San Juan & Grand Mesa Panorama Views", "Golden Aspen Canopy", "Primitive Stone Fire Rings"],
    "location_scores": {"distance_to_groceries_score": 6, "distance_to_library_score": 6, "distance_to_gym_score": 5, "terrain_score": 9, "quietness_score": 9},
    "nearest_supply_towns": [{"town_name": "Montrose, CO", "distance_miles": 16.5, "services_available": ["Supercenters", "Hospital", "Public Library", "Gym & Fitness Center", "Airport", "Hardware Store"]}],
    "seasonal_weather_effects": {"spring": "Snow thaws through late May; muddy plateau dirt.", "summer": "Cool 8,900-ft summer weather (70-78°F) with crisp mountain nights.", "fall": "Spectacular golden aspen leaf changes in late September.", "winter": "Closed to vehicle traffic due to deep snowpack; snowmobiling hub."},
    "dangers_and_hazards": ["Black Bears", "High Elevation Summer Lightning Storms", "Freezing Night Temps"],
    "acoustic_environment": {"quietness_rating": "High Plateau Silence (Quietness Score: 9/10)", "common_human_made_sounds": ["Occasional forest road car", "High altitude commercial flights"]},
    "flora_and_fauna": {
      "common_plants_and_trees": ["Quaking Aspen", "Engelmann Spruce", "Ponderosa Pine", "Mountain Big Sagebrush"],
      "common_animals": ["Elk", "Mule Deer", "Black Bear", "Golden Eagle", "Coyote"]
    },
    "human_demographics_and_culture": "Western Colorado Uncompahgre Plateau cattle ranching, timber, and outdoor recreation culture.",
    "spiritual_and_folklore_data": {
      "nature_spirits_and_mythological_lore": "Ute Chief Ouray history honors the Uncompahgre Plateau as ancient summer hunting grounds.",
      "energetic_and_spiritual_features": "High 9,000-foot plateau rim overlooking the entire San Juan mountain range produces a majestic perspective."
    },
    "nearby_hiking_trails": [{"trail_name": "Uncompahgre Plateau Divide Trail", "length_miles": 12.0, "difficulty": "Moderate", "features": "Panoramic views of San Juan peaks and Grand Mesa, massive aspen groves"}],
    "public_reviews_summary": "Cool 70-degree summer plateau camping with blazing fast 5G cell internet overlooking Montrose.",
    "other_data": "Bring fresh drinking water.",
    "last_updated": "2026-09-12"
  },
  {
    "id": "colorado-008",
    "name": "White River National Forest Shrine Pass Dispersed Zone",
    "state": "Colorado",
    "county": "Eagle / Summit",
    "coordinates": {"latitude": 39.5412, "longitude": -106.2148, "elevation_ft": 10850.0},
    "management_agency": {"name": "U.S. Forest Service - White River National Forest (Eagle-Holy Cross Ranger District)", "type": "Federal", "phone": "(970) 827-5715", "website": "https://www.fs.usda.gov/whiteriver"},
    "rules_and_regulations": {"cost": "Free ($0/night primitive dispersed forest camping in designated Shrine Pass pullouts)", "stay_limit": "14 days maximum stay within a 30-day window", "guidelines": "Dispersed primitive camping allowed along Shrine Pass Road (FR 709) outside Vail Pass recreation fee area. Leave No Trace."},
    "waste_disposal_rules": {"poop_disposal": "Bury waste 6-8 inches deep 200 ft from alpine streams and wildflower meadows. Pack out toilet paper.", "trash_policy": "Strict Pack-It-In Pack-It-Out policy."},
    "campfire_rules": {"permitted": True, "firewood_policy": "Gather dead and down wood locally.", "safety_requirements": "Campfires permitted in cleared stone rings. Extinguish cold.", "seasonal_fire_bans": "Subject to USFS dry summer fire bans."},
    "access_and_road_conditions": {"road_type": "Gravel mountain road (Shrine Pass Road / FR 709)", "road_conditions": "Graded gravel road connecting Vail Pass to Red Cliff; accessible in summer.", "vehicle_recommendation": "Accessible by standard FWD passenger car in dry summer months.", "scores": {"road_grade": 4, "road_terrain_difficulty": 3, "supply_run_pain": 4}},
    "nomad_connectivity_rating": {"overall_rating": "Great (4/5 Stars)", "verizon_reliability": "4 bars 5G/4G LTE due to high 10,800-ft pass summit overlooking I-70 corridor", "att_reliability": "4 bars 4G LTE", "tmobile_reliability": "3-4 bars 4G LTE", "terrain_obstruction_risk": "Low - open subalpine meadow pass summit", "distance_from_tower_corridor_miles": 2.2, "cellular_internet_dependable": True},
    "amenities": ["10,850-ft Alpine Wildflower Meadows", "Mount of the Holy Cross Vistas", "Subalpine Fir Canopy"],
    "location_scores": {"distance_to_groceries_score": 6, "distance_to_library_score": 6, "distance_to_gym_score": 5, "terrain_score": 10, "quietness_score": 9},
    "nearest_supply_towns": [{"town_name": "Vail, CO", "distance_miles": 12.4, "services_available": ["Supermarket", "Hospital", "Public Library", "Gym & Fitness Center", "Outfitters", "Restaurants"]}, {"town_name": "Frisco, CO", "distance_miles": 18.0, "services_available": ["Supercenters", "Full Resort Amenities"]}],
    "seasonal_weather_effects": {"spring": "Pass snowbound through late June.", "summer": "World-class alpine wildflower bloom in July/August with cool 68-74°F day temps and cold night air (38°F).", "fall": "Golden subalpine larch and aspen foliage in September.", "winter": "Closed to vehicle traffic; popular snowmobile and cross-country ski route."},
    "dangers_and_hazards": ["High Altitude Hypothermia & Weather Shifts", "Lightning Hazard in Wildflower Meadows", "Sub-Freezing Summer Night Temps"],
    "acoustic_environment": {"quietness_rating": "Subalpine Pass Silence (Quietness Score: 9/10)", "common_human_made_sounds": ["Occasional mountain road vehicle", "High altitude commercial flights"]},
    "flora_and_fauna": {
      "common_plants_and_trees": ["Subalpine Fir", "Engelmann Spruce", "Colorado Columbine (State Flower)", "Paintbrush", "Indian Paintbrush"],
      "common_animals": ["Rocky Mountain Bighorn Sheep", "Elk", "Pika", "Yellow-bellied Marmot", "Ptarmigan"]
    },
    "human_demographics_and_culture": "Colorado Rocky Mountain high alpine pass history (10th Mountain Division historical ski training grounds near Camp Hale).",
    "spiritual_and_folklore_data": {
      "nature_spirits_and_mythological_lore": "10th Mountain Division ski troop history and Ute legends honor Shrine Pass as a high sacred mountain pass.",
      "energetic_and_spiritual_features": "10,850-foot subalpine wildflower meadows with views of Mount of the Holy Cross evoke divine grandeur."
    },
    "nearby_hiking_trails": [{"trail_name": "Shrine Mountain Trail & Shrine Pass Ridge", "length_miles": 4.2, "difficulty": "Moderate", "features": "360-degree views of Sawatch range, Gore range, and Mount of the Holy Cross"}],
    "public_reviews_summary": "Unbelievable alpine wildflower meadows at 10,800 feet with blazing fast 5G cell internet near Vail.",
    "other_data": "Dress warmly as night temperatures drop into the 30s even in July.",
    "last_updated": "2026-09-12"
  },
  {
    "id": "colorado-009",
    "name": "Comanche National Grassland Carrizo Canyon Primitive Zone",
    "state": "Colorado",
    "county": "Baca",
    "coordinates": {"latitude": 37.1412, "longitude": -103.0142, "elevation_ft": 4420.0},
    "management_agency": {"name": "U.S. Forest Service - Pike and San Isabel National Forests, Cimarron and Comanche National Grasslands (Carrizo Ranger District)", "type": "Federal", "phone": "(719) 523-6591", "website": "https://www.fs.usda.gov/psicc"},
    "rules_and_regulations": {"cost": "Free ($0/night primitive dispersed grassland canyon camping)", "stay_limit": "14 days maximum stay limit", "guidelines": "Dispersed primitive camping allowed along Carrizo Canyon dirt roads and picnic area buffer. Camp 100 ft from creek wash. Leave No Trace."},
    "waste_disposal_rules": {"poop_disposal": "Utilize vault toilet at Carrizo picnic area or bury 6-8 inches deep 200 ft from creek wash.", "trash_policy": "Strict Pack-It-In Pack-It-Out policy."},
    "campfire_rules": {"permitted": True, "firewood_policy": "Gather dead and down cottonwood and juniper wood locally.", "safety_requirements": "Campfires permitted in cleared stone rings. Extinguish cold due to prairie wind hazard.", "seasonal_fire_bans": "Subject to USFS high prairie fire bans."},
    "access_and_road_conditions": {"road_type": "Gravel prairie roads", "road_conditions": "Graded gravel access roads to dirt canyon turnouts.", "vehicle_recommendation": "Accessible by standard FWD passenger car.", "scores": {"road_grade": 3, "road_terrain_difficulty": 3, "supply_run_pain": 5}},
    "nomad_connectivity_rating": {"overall_rating": "Fair (2.5/5 Stars)", "verizon_reliability": "2 bars 4G LTE on high canyon rims", "att_reliability": "2 bars 4G LTE", "tmobile_reliability": "1 bar 4G LTE", "terrain_obstruction_risk": "Moderate - sandstone canyon walls and cottonwood groves", "distance_from_tower_corridor_miles": 8.5, "cellular_internet_dependable": False},
    "amenities": ["Red Sandstone Canyon Walls", "Native Petroglyph Viewing nearby", "Cottonwood Shade", "Vault Toilet nearby"],
    "location_scores": {"distance_to_groceries_score": 5, "distance_to_library_score": 5, "distance_to_gym_score": 4, "terrain_score": 8, "quietness_score": 10},
    "nearest_supply_towns": [{"town_name": "Springfield, CO", "distance_miles": 22.4, "services_available": ["Grocery Store", "Gas Station", "Hardware Store", "Hospital", "Restaurants"]}, {"town_name": "Lamar, CO", "distance_miles": 64.0, "services_available": ["Supercenters", "Public Library", "Gym & Fitness Center"]}],
    "seasonal_weather_effects": {"spring": "Lush canyon greening with spring blooming yucca.", "summer": "Hot high plains weather (88-98°F) with cool canyon evening breezes.", "fall": "Golden cottonwood leaf display in October.", "winter": "Cool to cold high plains winter (20-40°F)."},
    "dangers_and_hazards": ["Flash Floods in Canyon Wash", "Prairie Rattlesnakes", "High Prairie Wildfire Hazard"],
    "acoustic_environment": {"quietness_rating": "Canyon Prairie Silence (Quietness Score: 10/10)", "common_human_made_sounds": ["High altitude jet contrails"]},
    "flora_and_fauna": {
      "common_plants_and_trees": ["Plains Cottonwood", "Tree Cholla Cactus", "Soapweed Yucca", "Blue Grama"],
      "common_animals": ["Pronghorn Antelope", "Tarantula", "Golden Eagle", "Mule Deer", "Coyote"]
    },
    "human_demographics_and_culture": "Southeast Colorado Santa Fe Trail, Comanche history, and high plains cattle ranching heritage.",
    "spiritual_and_folklore_data": {
      "nature_spirits_and_mythological_lore": "Comanche and Kiowa traditions honor Carrizo Canyon as an ancient sheltered oasis along shortgrass prairie trading routes.",
      "energetic_and_spiritual_features": "Red sandstone canyon walls tucked into vast prairie plains radiate peaceful, ancient shelter."
    },
    "nearby_hiking_trails": [{"trail_name": "Carrizo Canyon & Picture Canyon Trail", "length_miles": 4.5, "difficulty": "Easy to Moderate", "features": "Native American petroglyphs, red sandstone arches, cottonwood creek wash"}],
    "public_reviews_summary": "Peaceful red sandstone canyon hidden in Southeast Colorado's grasslands with zero cost and petroglyphs.",
    "other_data": "Carry fresh drinking water.",
    "last_updated": "2026-09-12"
  },
  {
    "id": "colorado-010",
    "name": "Gunnison National Forest Kebler Pass Primitive Zone",
    "state": "Colorado",
    "county": "Gunnison",
    "coordinates": {"latitude": 38.8812, "longitude": -107.1214, "elevation_ft": 9850.0},
    "management_agency": {"name": "U.S. Forest Service - Grand Mesa, Uncompahgre, and Gunnison National Forests (Gunnison Ranger District)", "type": "Federal", "phone": "(970) 641-0471", "website": "https://www.fs.usda.gov/gmug"},
    "rules_and_regulations": {"cost": "Free ($0/night primitive dispersed forest camping)", "stay_limit": "14 days maximum stay within a 30-day window", "guidelines": "Dispersed primitive camping allowed along Kebler Pass Road (FR 12) pullouts. Camp 100 ft from streams. Leave No Trace."},
    "waste_disposal_rules": {"poop_disposal": "Bury waste 6-8 inches deep 200 ft from streams. Pack out toilet paper.", "trash_policy": "Strict Pack-It-In Pack-It-Out policy."},
    "campfire_rules": {"permitted": True, "firewood_policy": "Gather dead and down aspen wood locally.", "safety_requirements": "Campfires permitted in cleared stone rings. Extinguish cold.", "seasonal_fire_bans": "Subject to USFS dry summer fire bans."},
    "access_and_road_conditions": {"road_type": "Gravel mountain road (Kebler Pass Road / FR 12)", "road_conditions": "Graded gravel scenic road connecting Crested Butte to Paonia; flat pullouts.", "vehicle_recommendation": "Accessible by standard FWD passenger car in summer.", "scores": {"road_grade": 4, "road_terrain_difficulty": 3, "supply_run_pain": 4}},
    "nomad_connectivity_rating": {"overall_rating": "Fair (2.5/5 Stars)", "verizon_reliability": "2 bars 4G LTE on high pass pullouts", "att_reliability": "2 bars 4G LTE", "tmobile_reliability": "1 bar 4G LTE", "terrain_obstruction_risk": "Moderate to High - West Elk mountain peaks and world's largest aspen grove", "distance_from_tower_corridor_miles": 8.0, "cellular_internet_dependable": False},
    "amenities": ["World's Largest Aspen Grove Vistas", "Ruby Range Mountain Views", "Primitive Stone Fire Rings"],
    "location_scores": {"distance_to_groceries_score": 6, "distance_to_library_score": 6, "distance_to_gym_score": 5, "terrain_score": 10, "quietness_score": 9},
    "nearest_supply_towns": [{"town_name": "Crested Butte, CO", "distance_miles": 11.2, "services_available": ["Grocery Store", "Gas Station", "Hardware Store", "Outfitters", "Restaurants"]}, {"town_name": "Gunnison, CO", "distance_miles": 32.0, "services_available": ["Supercenter", "Hospital", "Public Library", "Gym & Fitness Center", "Airport"]}],
    "seasonal_weather_effects": {"spring": "Pass snowbound through mid-June.", "summer": "Cool mountain summer (70-76°F) with wildflower meadows.", "fall": "World-famous peak aspen foliage in late September (largest contiguous aspen grove in North America).", "winter": "Closed to vehicle traffic; snowmobile and ski route."},
    "dangers_and_hazards": ["Black Bears", "High Elevation Weather Shifts", "Freezing Night Temps"],
    "acoustic_environment": {"quietness_rating": "Aspen Forest Quiet (Quietness Score: 9/10)", "common_human_made_sounds": ["Occasional scenic byway car", "High altitude commercial flights"]},
    "flora_and_fauna": {
      "common_plants_and_trees": ["Quaking Aspen (Largest Clonal Colony)", "Engelmann Spruce", "Subalpine Fir", "Wild Lupine"],
      "common_animals": ["Elk", "Mule Deer", "Black Bear", "Pine Marten", "Red-tailed Hawk"]
    },
    "human_demographics_and_culture": "Crested Butte wildflower capital, ski culture, and West Elk wilderness conservation heritage.",
    "spiritual_and_folklore_data": {
      "nature_spirits_and_mythological_lore": "Ute traditions honor the West Elk mountains as sacred high autumn hunting grounds.",
      "energetic_and_spiritual_features": "Surrounded by millions of interconnected golden aspen trees beneath the jagged Ruby Range produces breathtaking natural magic."
    },
    "nearby_hiking_trails": [{"trail_name": "Three Lakes Trail & Kebler Pass Crest", "length_miles": 5.4, "difficulty": "Moderate", "features": "Pristine backcountry mountain lakes, giant aspen forest, Ruby Crest vistas"}],
    "public_reviews_summary": "Hands-down the single best fall aspen foliage camping location in North America.",
    "other_data": "Filter all water and store food in bear canisters.",
    "last_updated": "2026-09-12"
  }
])
save_state(co, co_path)

# Idaho (+5 sites -> 10 total)
idaho, id_path = load_state('idaho')
idaho.extend([
  {
    "id": "idaho-006",
    "name": "Sawtooth National Forest Valley Road Dispersed Zone",
    "state": "Idaho",
    "county": "Custer",
    "coordinates": {"latitude": 44.2148, "longitude": -114.9125, "elevation_ft": 6480.0},
    "management_agency": {"name": "U.S. Forest Service - Sawtooth National Forest (Sawtooth National Recreation Area)", "type": "Federal", "phone": "(208) 727-5000", "website": "https://www.fs.usda.gov/sawtooth"},
    "rules_and_regulations": {"cost": "Free ($0/night primitive dispersed forest camping)", "stay_limit": "14 days maximum stay within a 30-day window", "guidelines": "Dispersed primitive camping allowed along Valley Road (FR 208) outside Stanley basin fee loops. Camp 100 ft from Salmon River. Leave No Trace."},
    "waste_disposal_rules": {"poop_disposal": "Bury waste 6-8 inches deep 200 ft from Salmon River. Pack out toilet paper.", "trash_policy": "Strict Pack-It-In Pack-It-Out policy."},
    "campfire_rules": {"permitted": True, "firewood_policy": "Gather dead and down wood locally.", "safety_requirements": "Campfires permitted in cleared stone rings. Extinguish cold with river water.", "seasonal_fire_bans": "Subject to USFS dry summer fire bans."},
    "access_and_road_conditions": {"road_type": "Gravel forest service road (FR 208)", "road_conditions": "Graded gravel road with flat mountain meadow pullouts.", "vehicle_recommendation": "Accessible by standard FWD passenger car.", "scores": {"road_grade": 2, "road_terrain_difficulty": 3, "supply_run_pain": 4}},
    "nomad_connectivity_rating": {"overall_rating": "Fair (2.5/5 Stars)", "verizon_reliability": "2 bars 4G LTE near Stanley valley highway turnoff", "att_reliability": "1-2 bars 4G LTE", "tmobile_reliability": "1 bar 4G LTE", "terrain_obstruction_risk": "High - 10,000-foot jagged Sawtooth Mountain wall", "distance_from_tower_corridor_miles": 7.5, "cellular_internet_dependable": False},
    "amenities": ["10,000-ft Sawtooth Jagged Peak Views", "Salmon River Headwaters Access", "Dark Sky Reserve Observation"],
    "location_scores": {"distance_to_groceries_score": 5, "distance_to_library_score": 5, "distance_to_gym_score": 4, "terrain_score": 10, "quietness_score": 10},
    "nearest_supply_towns": [{"town_name": "Stanley, ID", "distance_miles": 8.5, "services_available": ["Grocery Store", "Gas Station", "Hardware Store", "Outfitters", "Restaurants"]}, {"town_name": "Ketchum / Sun Valley, ID", "distance_miles": 52.0, "services_available": ["Supermarket", "Hospital", "Public Library", "Gym & Fitness Center", "Full Resort Amenities"]}],
    "seasonal_weather_effects": {"spring": "Valley thaws in May/June; roaring snowmelt in Salmon River.", "summer": "Pleasant mountain summer (74-82°F) with cool mountain nights (38°F).", "fall": "Golden larch and cottonwood foliage in late September.", "winter": "Cold sub-zero winter (-15 to 20°F); snowmobile and ski hub."},
    "dangers_and_hazards": ["Black Bears & Wolves", "Freezing Night Temps", "Cold Salmon River Currents"],
    "acoustic_environment": {"quietness_rating": "Sawtooth Wilderness Silence (Quietness Score: 10/10)", "common_human_made_sounds": ["Occasional forest road car", "High altitude commercial flights"]},
    "flora_and_fauna": {
      "common_plants_and_trees": ["Lodgepole Pine", "Douglas Fir", "Subalpine Fir", "Idaho Fescue"],
      "common_animals": ["Rocky Mountain Elk", "Gray Wolf", "Black Bear", "Chinook Salmon", "Osprey"]
    },
    "human_demographics_and_culture": "Central Idaho Sawtooth Wilderness, Salmon River salmon conservation, and mountain outdoor culture.",
    "spiritual_and_folklore_data": {
      "nature_spirits_and_mythological_lore": "Shoshone and Bannock traditions honor the Sawtooth Range as sacred high mountain hunting grounds.",
      "energetic_and_spiritual_features": "Jagged 10,000-foot Sawtooth granite needles rising directly behind mountain meadows generate world-class majestic power."
    },
    "nearby_hiking_trails": [{"trail_name": "Sawtooth Lake & Fishhook Creek Trail", "length_miles": 8.5, "difficulty": "Moderate to Strenuous", "features": "Alpine granite glacial lakes, Sawtooth peak wall reflections, lodgepole pine forest"}],
    "public_reviews_summary": "Unbelievable views of the Sawtooth Mountains right from your campsite with quiet night skies.",
    "other_data": "Store food in bear containers and carry paper maps.",
    "last_updated": "2026-09-12"
  },
  {
    "id": "idaho-007",
    "name": "Salmon River BLM Dispersed Corridor Zone",
    "state": "Idaho",
    "county": "Lemhi",
    "coordinates": {"latitude": 45.1812, "longitude": -113.8812, "elevation_ft": 3950.0},
    "management_agency": {"name": "Bureau of Land Management (BLM) - Salmon Field Office", "type": "Federal", "phone": "(208) 756-5400", "website": "https://www.blm.gov/idaho"},
    "rules_and_regulations": {"cost": "Free ($0/night primitive BLM dispersed camping)", "stay_limit": "14 days maximum stay limit", "guidelines": "Dispersed primitive camping allowed along Salmon River Road (US-93 / Highway 28 corridor) pullouts outside developed fee recreation loops. Leave No Trace."},
    "waste_disposal_rules": {"poop_disposal": "Utilize BLM river vault toilets where available, or bury 6-8 inches deep 200 ft from Salmon River.", "trash_policy": "Strict Pack-It-In Pack-It-Out policy."},
    "campfire_rules": {"permitted": True, "firewood_policy": "Gather dead and down wood locally.", "safety_requirements": "Campfires permitted in cleared stone rings. Extinguish cold with river water.", "seasonal_fire_bans": "Subject to BLM Stage 1 & 2 dry summer fire bans."},
    "access_and_road_conditions": {"road_type": "Paved highway to gravel river turnouts", "road_conditions": "Paved access roads with flat river bank pullouts.", "vehicle_recommendation": "Accessible by standard FWD passenger car, camper vans, and rigs.", "scores": {"road_grade": 2, "road_terrain_difficulty": 2, "supply_run_pain": 3}},
    "nomad_connectivity_rating": {"overall_rating": "Great (4/5 Stars)", "verizon_reliability": "4 bars 4G LTE along river highway corridor", "att_reliability": "3-4 bars 4G LTE", "tmobile_reliability": "3 bars 4G LTE", "terrain_obstruction_risk": "Low to Moderate - broad Salmon River mountain valley", "distance_from_tower_corridor_miles": 2.2, "cellular_internet_dependable": True},
    "amenities": ["Salmon River Whitewater & Trout Access", "River Bank Flat Campsite", "Vault Toilet nearby"],
    "location_scores": {"distance_to_groceries_score": 7, "distance_to_library_score": 7, "distance_to_gym_score": 6, "terrain_score": 9, "quietness_score": 8},
    "nearest_supply_towns": [{"town_name": "Salmon, ID", "distance_miles": 8.5, "services_available": ["Supermarket", "Hospital", "Public Library", "Gym & Fitness Center", "Outfitters", "Hardware Store"]}],
    "seasonal_weather_effects": {"spring": "Lush valley greening with roaring whitewater runoff.", "summer": "Warm sunny days (82-90°F) with river swimming and rafting.", "fall": "Crisp autumn weather with golden cottonwood foliage.", "winter": "Cool to cold valley winter (22-38°F)."},
    "dangers_and_hazards": ["Cold Whitewater River Currents", "Rattlesnakes", "Black Bears"],
    "acoustic_environment": {"quietness_rating": "River Canyon Rushing Audio (Quietness Score: 8/10)", "common_human_made_sounds": ["Distant highway US-93 traffic hum", "Occasional raft launch"]},
    "flora_and_fauna": {
      "common_plants_and_trees": ["Plains Cottonwood", "Ponderosa Pine", "Big Sagebrush", "Syringa (State Flower)"],
      "common_animals": ["Bighorn Sheep", "Rocky Mountain Elk", "Chinook Salmon", "Osprey", "Bald Eagle"]
    },
    "human_demographics_and_culture": "Salmon River whitewaters ('River of No Return'), Lewis & Clark Expedition history (Sacajawea birthplace), and Idaho fly fishing heritage.",
    "spiritual_and_folklore_data": {
      "nature_spirits_and_mythological_lore": "Agai-Dika Shoshone traditions honor the Salmon River as the sacred lifeline of salmon people.",
      "energetic_and_spiritual_features": "Rushing waters of the Salmon River framed by steep mountain walls generate an invigorating energy."
    },
    "nearby_hiking_trails": [{"trail_name": "Salmon River Canyon Trail & Goldbug Hot Springs Trail", "length_miles": 4.2, "difficulty": "Moderate", "features": "Natural thermal hot spring waterfalls, river canyon vistas"}],
    "public_reviews_summary": "Top choice for digital nomads wanting free riverfront camping with reliable cell coverage near Salmon, Idaho.",
    "other_data": "Boil or treat river water.",
    "last_updated": "2026-09-12"
  },
  {
    "id": "idaho-008",
    "name": "Caribou-Targhee National Forest Big Springs Primitive Zone",
    "state": "Idaho",
    "county": "Fremont",
    "coordinates": {"latitude": 44.5125, "longitude": -111.2812, "elevation_ft": 6380.0},
    "management_agency": {"name": "U.S. Forest Service - Caribou-Targhee National Forest (Ashton-Island Park Ranger District)", "type": "Federal", "phone": "(208) 652-7442", "website": "https://www.fs.usda.gov/ctnf"},
    "rules_and_regulations": {"cost": "Free ($0/night primitive dispersed forest camping)", "stay_limit": "14 days maximum stay within a 30-day window", "guidelines": "Dispersed primitive camping allowed along Big Springs Road and forest service roads outside Yellowstone National Park boundary. Leave No Trace."},
    "waste_disposal_rules": {"poop_disposal": "Bury waste 6-8 inches deep 200 ft from springs and Henrys Fork river. Pack out paper.", "trash_policy": "Strict Pack-It-In Pack-It-Out policy. Bear food storage order strictly enforced."},
    "campfire_rules": {"permitted": True, "firewood_policy": "Gather dead and down wood locally.", "safety_requirements": "Campfires permitted in cleared stone rings. Extinguish cold.", "seasonal_fire_bans": "Subject to USFS dry summer fire bans."},
    "access_and_road_conditions": {"road_type": "Paved US-20 to gravel forest service roads", "road_conditions": "Paved access roads to smooth gravel forest pullouts.", "vehicle_recommendation": "Accessible by standard FWD passenger car.", "scores": {"road_grade": 2, "road_terrain_difficulty": 2, "supply_run_pain": 3}},
    "nomad_connectivity_rating": {"overall_rating": "Good (3.5/5 Stars)", "verizon_reliability": "3-4 bars 4G LTE", "att_reliability": "3 bars 4G LTE", "tmobile_reliability": "2-3 bars 4G LTE", "terrain_obstruction_risk": "Low to Moderate - gentle lodgepole pine plateau", "distance_from_tower_corridor_miles": 3.8, "cellular_internet_dependable": True},
    "amenities": ["Henrys Fork River Water Access", "Lodgepole Pine Shade", "Yellowstone Gateway Access"],
    "location_scores": {"distance_to_groceries_score": 7, "distance_to_library_score": 7, "distance_to_gym_score": 6, "terrain_score": 8, "quietness_score": 8},
    "nearest_supply_towns": [{"town_name": "Island Park, ID", "distance_miles": 6.5, "services_available": ["Grocery Store", "Gas Station", "Hardware Store", "Outfitters", "Restaurants"]}, {"town_name": "West Yellowstone, MT", "distance_miles": 22.0, "services_available": ["Supermarket", "Medical Center", "Public Library", "Yellowstone Gateway Amenities"]}],
    "seasonal_weather_effects": {"spring": "Snow thaws through May; crystal clear natural springs flow.", "summer": "Pleasant summer weather (75-82°F) with fly fishing on Henrys Fork.", "fall": "Crisp autumn weather with golden lodgepole pine needle drop.", "winter": "Cold mountain winter (10-25°F) with heavy snowpack; snowmobile capital."},
    "dangers_and_hazards": ["Grizzly Bears & Black Bears (Mandatory USFS Bear Food Storage Order)", "Moose on Forest Roads"],
    "acoustic_environment": {"quietness_rating": "Lodgepole Forest Quiet (Quietness Score: 8/10)", "common_human_made_sounds": ["Occasional passing forest road car", "High altitude commercial flights"]},
    "flora_and_fauna": {
      "common_plants_and_trees": ["Lodgepole Pine", "Douglas Fir", "Quaking Aspen", "Fireweed"],
      "common_animals": ["Grizzly Bear", "Moose", "Rainbow Trout", "Bald Eagle", "Trumpeter Swan"]
    },
    "human_demographics_and_culture": "Island Park Yellowstone gateway, Henrys Fork fly fishing, and lodgepole timber culture.",
    "spiritual_and_folklore_data": {
      "nature_spirits_and_mythological_lore": "Shoshone legends honor Big Springs as a sacred crystal water source flowing continuously from beneath the earth.",
      "energetic_and_spiritual_features": "120 million gallons per day of crystal clear 52-degree spring water emerging from volcanic rock creates a serene life energy."
    },
    "nearby_hiking_trails": [{"trail_name": "Big Springs Waterway & Johnny Sack Cabin Trail", "length_miles": 2.5, "difficulty": "Easy", "features": "Massive freshwater spring headwaters, historic 1930s log cabin, giant trout viewing"}],
    "public_reviews_summary": "Great free camping spot near West Yellowstone with good cell service, giant pine shade, and crystal springs.",
    "other_data": "Grizzly bear food storage order strictly enforced by USFS rangers.",
    "last_updated": "2026-09-12"
  },
  {
    "id": "idaho-009",
    "name": "BLM Morley Nelson Snake River Birds of Prey Primitive Zone",
    "state": "Idaho",
    "county": "Ada / Elmore",
    "coordinates": {"latitude": 43.2812, "longitude": -116.1412, "elevation_ft": 3120.0},
    "management_agency": {"name": "Bureau of Land Management (BLM) - Four Rivers Field Office", "type": "Federal", "phone": "(208) 384-3300", "website": "https://www.blm.gov/idaho"},
    "rules_and_regulations": {"cost": "Free ($0/night primitive BLM dispersed camping)", "stay_limit": "14 days maximum stay within a 28-day window", "guidelines": "Dispersed primitive camping allowed along Swan Falls Road and canyon rim dirt roads outside day-use park boundary. Leave No Trace."},
    "waste_disposal_rules": {"poop_disposal": "Bury waste 6-8 inches deep 200 ft from Snake River gorge rim. Pack out paper.", "trash_policy": "Strict Pack-It-In Pack-It-Out policy."},
    "campfire_rules": {"permitted": True, "firewood_policy": "Bring firewood; no wood collecting on sagebrush plain.", "safety_requirements": "Campfires permitted in cleared metal or stone rings. Extinguish cold.", "seasonal_fire_bans": "Subject to BLM Stage 1 & 2 fire bans during dry summer."},
    "access_and_road_conditions": {"road_type": "Paved Swan Falls Road to gravel dirt rim pullouts", "road_conditions": "Paved road access to flat gravel plateau rim pullouts.", "vehicle_recommendation": "Accessible by standard FWD passenger car.", "scores": {"road_grade": 2, "road_terrain_difficulty": 2, "supply_run_pain": 3}},
    "nomad_connectivity_rating": {"overall_rating": "Great (4/5 Stars)", "verizon_reliability": "4 bars 5G/4G LTE on high gorge plateau rim", "att_reliability": "4 bars 4G LTE", "tmobile_reliability": "3-4 bars 4G LTE", "terrain_obstruction_risk": "Low on high plateau rim; high down inside Snake River canyon bottom", "distance_from_tower_corridor_miles": 2.5, "cellular_internet_dependable": True},
    "amenities": ["Snake River 700-ft Basalt Canyon Vistas", "Raptor Birdwatching Access", "Dark Sky Astronomy"],
    "location_scores": {"distance_to_groceries_score": 7, "distance_to_library_score": 7, "distance_to_gym_score": 6, "terrain_score": 9, "quietness_score": 8},
    "nearest_supply_towns": [{"town_name": "Kuna, ID", "distance_miles": 14.5, "services_available": ["Grocery Store", "Gas Station", "Hardware Store", "Restaurants"]}, {"town_name": "Boise, ID", "distance_miles": 28.0, "services_available": ["State Capital Amenities", "Airport", "Hospitals", "Full Urban Facilities"]}],
    "seasonal_weather_effects": {"spring": "Lush sagebrush greening with peak nesting raptor watching (April/May).", "summer": "Warm to hot desert summer (90-98°F) with cool canyon evening breezes.", "fall": "Crisp dry autumn weather.", "winter": "Cool high desert winter (35-48°F) with light snow."},
    "dangers_and_hazards": ["700-ft Vertical Basalt Canyon Drop-offs", "Prairie Rattlesnakes", "High Summer Heat"],
    "acoustic_environment": {"quietness_rating": "Canyon Rim Quiet (Quietness Score: 8/10)", "common_human_made_sounds": ["Occasional passing canyon road car", "High altitude commercial flights"]},
    "flora_and_fauna": {
      "common_plants_and_trees": ["Big Sagebrush", "Winterfat", "Cheatgrass", "Peachleaf Willow"],
      "common_animals": ["Prairie Falcon (Highest nesting density in North America)", "Golden Eagle", "Red-tailed Hawk", "Piute Ground Squirrel", "Coyote"]
    },
    "human_demographics_and_culture": "Boise Metro outdoor escape, raptor conservation research, and Snake River hydroelectric canyon heritage.",
    "spiritual_and_folklore_data": {
      "nature_spirits_and_mythological_lore": "Northern Shoshone traditions honor the Snake River basalt canyon as sacred raptor sky grounds.",
      "energetic_and_spiritual_features": "700-foot vertical volcanic basalt gorge with soaring golden eagles generates an inspiring, free energy."
    },
    "nearby_hiking_trails": [{"trail_name": "Swan Falls Dam & Snake River Canyon Rim Trail", "length_miles": 5.2, "difficulty": "Easy to Moderate", "features": "700-ft basalt canyon views, raptor nesting cliffs, Snake River hydroelectric dam"}],
    "public_reviews_summary": "Incredible raptor watching over a 700-foot basalt gorge with fast 5G cell internet near Boise.",
    "other_data": "Stay back from un-barricaded canyon cliff edges.",
    "last_updated": "2026-09-12"
  },
  {
    "id": "idaho-010",
    "name": "Idaho Panhandle National Forest Priest Lake Primitive Zone",
    "state": "Idaho",
    "county": "Bonner",
    "coordinates": {"latitude": 48.6125, "longitude": -116.9125, "elevation_ft": 2480.0},
    "management_agency": {"name": "U.S. Forest Service - Idaho Panhandle National Forests (Priest Lake Ranger District)", "type": "Federal", "phone": "(208) 443-2512", "website": "https://www.fs.usda.gov/ipnf"},
    "rules_and_regulations": {"cost": "Free ($0/night primitive dispersed forest camping)", "stay_limit": "14 days maximum stay within a 30-day window", "guidelines": "Dispersed primitive camping allowed along Eastside Road (FR 437) and forest service roads outside developed lake fee loops. Leave No Trace."},
    "waste_disposal_rules": {"poop_disposal": "Bury waste 6-8 inches deep 200 ft from Priest Lake and streams. Pack out toilet paper.", "trash_policy": "Strict Pack-It-In Pack-It-Out policy. Bear food storage required."},
    "campfire_rules": {"permitted": True, "firewood_policy": "Gather dead and down wood locally.", "safety_requirements": "Campfires permitted in cleared stone rings. Extinguish cold with lake water.", "seasonal_fire_bans": "Subject to USFS dry summer fire bans."},
    "access_and_road_conditions": {"road_type": "Paved county road to gravel forest service roads", "road_conditions": "Paved access road to graded gravel lake forest turnouts.", "vehicle_recommendation": "Accessible by standard FWD passenger car.", "scores": {"road_grade": 2, "road_terrain_difficulty": 3, "supply_run_pain": 4}},
    "nomad_connectivity_rating": {"overall_rating": "Good (3/5 Stars)", "verizon_reliability": "3 bars 4G LTE", "att_reliability": "2-3 bars 4G LTE", "tmobile_reliability": "2 bars 4G LTE", "terrain_obstruction_risk": "Moderate - Selkirk mountain range and old-growth cedar forest canopy", "distance_from_tower_corridor_miles": 5.2, "cellular_internet_dependable": True},
    "amenities": ["Priest Lake Freshwater Access", "Selkirk Mountain Peak Vistas", "Old-Growth Cedar Canopy"],
    "location_scores": {"distance_to_groceries_score": 6, "distance_to_library_score": 6, "distance_to_gym_score": 5, "terrain_score": 10, "quietness_score": 9},
    "nearest_supply_towns": [{"town_name": "Priest River, ID", "distance_miles": 22.4, "services_available": ["Supermarket", "Gas Station", "Hardware Store", "Restaurants"]}, {"town_name": "Sandpoint, ID", "distance_miles": 42.0, "services_available": ["Hospital", "Public Library", "Gym & Fitness Center", "Full Resort Amenities"]}],
    "seasonal_weather_effects": {"spring": "Lush Pacific Northwest greening; mountain stream thaw.", "summer": "Pleasant summer weather (76-84°F) with pristine lake swimming and boating.", "fall": "Crisp mountain autumn foliage in October.", "winter": "Cold mountain winter (20-35°F) with heavy snowpack."},
    "dangers_and_hazards": ["Grizzly Bears & Black Bears (Food storage required)", "Cold Deep Lake Waters", "Falling Cedar Branches"],
    "acoustic_environment": {"quietness_rating": "Northwoods Lake Quiet (Quietness Score: 9/10)", "common_human_made_sounds": ["Distant outboard motor on lake", "Occasional forest road car"]},
    "flora_and_fauna": {
      "common_plants_and_trees": ["Western Red Cedar (Ancient Giant Cedars)", "Western Hemlock", "Douglas Fir", "Huckleberry"],
      "common_animals": ["Grizzly Bear", "Black Bear", "Moose", "Osprey", "Mackinaw Trout"]
    },
    "human_demographics_and_culture": "Idaho Panhandle timber, Selkirk mountain wilderness, and Priest Lake resort heritage.",
    "spiritual_and_folklore_data": {
      "nature_spirits_and_mythological_lore": "Kalispel traditions honor Priest Lake and the ancient giant cedar groves as sacred spirit water sanctuaries.",
      "energetic_and_spiritual_features": "Giant 800-year-old western red cedar groves reflecting in pristine glacial lake waters generate deep natural majesty."
    },
    "nearby_hiking_trails": [{"trail_name": "Roosevelt Ancient Grove Cedar Trail & Lakeshore Trail", "length_miles": 4.8, "difficulty": "Easy to Moderate", "features": "800-year-old giant cedar trees, waterfalls, pristine Priest Lake shoreline"}],
    "public_reviews_summary": "Magical old-growth cedar forest camping on Priest Lake with decent cell service and pristine water.",
    "other_data": "Store food in bear canisters.",
    "last_updated": "2026-09-12"
  }
])
save_state(idaho, id_path)

print("Colorado and Idaho expanded to 10 campsites each!")
