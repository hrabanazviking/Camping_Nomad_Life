import json

def load_state(name):
    path = f'/home/volmarr/.gemini/antigravity/scratch/Camping_Nomad_Life/states/{name}.json'
    with open(path, 'r') as f:
        return json.load(f), path

def save_state(data, path):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

# Montana (+5 sites -> 10 total)
mt, mt_path = load_state('montana')
mt.extend([
  {
    "id": "montana-006",
    "name": "Custer Gallatin National Forest Hyalite Canyon Dispersed Zone",
    "state": "Montana",
    "county": "Gallatin",
    "coordinates": {"latitude": 45.4812, "longitude": -110.9512, "elevation_ft": 6850.0},
    "management_agency": {"name": "U.S. Forest Service - Custer Gallatin National Forest (Bozeman Ranger District)", "type": "Federal", "phone": "(406) 522-2520", "website": "https://www.fs.usda.gov/gallatin"},
    "rules_and_regulations": {"cost": "Free ($0/night primitive dispersed forest camping)", "stay_limit": "14 days maximum stay within a 30-day window", "guidelines": "Dispersed primitive camping allowed along Hyalite Creek Road (FR 62) pullouts outside developed fee loops. Leave No Trace."},
    "waste_disposal_rules": {"poop_disposal": "Bury waste 6-8 inches deep 200 ft from Hyalite Creek. Pack out toilet paper.", "trash_policy": "Strict Pack-It-In Pack-It-Out policy. Food storage order strictly enforced."},
    "campfire_rules": {"permitted": True, "firewood_policy": "Gather dead and down wood locally.", "safety_requirements": "Campfires permitted in cleared stone rings. Extinguish cold.", "seasonal_fire_bans": "Subject to USFS dry summer fire bans."},
    "access_and_road_conditions": {"road_type": "Paved canyon road to gravel forest service roads", "road_conditions": "Paved access road to smooth gravel reservoir pullouts.", "vehicle_recommendation": "Accessible by standard FWD passenger car.", "scores": {"road_grade": 3, "road_terrain_difficulty": 3, "supply_run_pain": 3}},
    "nomad_connectivity_rating": {"overall_rating": "Good (3/5 Stars)", "verizon_reliability": "3 bars 4G LTE near reservoir rim", "att_reliability": "2-3 bars 4G LTE", "tmobile_reliability": "2 bars 4G LTE", "terrain_obstruction_risk": "Moderate - Gallatin mountain canyon walls", "distance_from_tower_corridor_miles": 5.5, "cellular_internet_dependable": True},
    "amenities": ["Hyalite Reservoir Water Access", "10,000-ft Gallatin Peak Views", "Waterfall Trail Access"],
    "location_scores": {"distance_to_groceries_score": 7, "distance_to_library_score": 7, "distance_to_gym_score": 6, "terrain_score": 10, "quietness_score": 8},
    "nearest_supply_towns": [{"town_name": "Bozeman, MT", "distance_miles": 14.5, "services_available": ["International Airport", "Major Supercenters", "Hospital", "Public Library", "Gym & Fitness Centers", "University Amenities"]}],
    "seasonal_weather_effects": {"spring": "High mountain snowmelt thaws through June.", "summer": "Pleasant summer weather (74-82°F) with reservoir canoeing and cool night air.", "fall": "Golden larch and aspen foliage in September.", "winter": "Cold mountain winter (10-25°F); world-class ice climbing hub."},
    "dangers_and_hazards": ["Grizzly Bears & Black Bears (Food storage order enforced)", "Cold Reservoir Waters"],
    "acoustic_environment": {"quietness_rating": "Gallatin Canyon Audio (Quietness Score: 8/10)", "common_human_made_sounds": ["Occasional forest road car", "High altitude commercial flights"]},
    "flora_and_fauna": {
      "common_plants_and_trees": ["Lodgepole Pine", "Engelmann Spruce", "Douglas Fir", "Quaking Aspen"],
      "common_animals": ["Grizzly Bear", "Black Bear", "Elk", "Moose", "Cutthroat Trout"]
    },
    "human_demographics_and_culture": "Bozeman mountain town, Montana State University, ice climbing, and Gallatin wilderness culture.",
    "spiritual_and_folklore_data": {
      "nature_spirits_and_mythological_lore": "Crow and Salish traditions honor the Gallatin Range as sacred high mountain hunting grounds.",
      "energetic_and_spiritual_features": "Glacial turquoise reservoir surrounded by 10,000-foot alpine peaks generates an invigorating mountain energy."
    },
    "nearby_hiking_trails": [{"trail_name": "Hyalite Creek Trail to Palisade Falls & Blackmore Peak", "length_miles": 5.5, "difficulty": "Moderate to Strenuous", "features": "Cascading waterfalls, subalpine cirque basins, 10,000-ft peak views"}],
    "public_reviews_summary": "Top-tier free camping spot near Bozeman with reservoir views, waterfalls, and solid cell coverage.",
    "other_data": "Grizzly bear food storage required by USFS.",
    "last_updated": "2026-09-12"
  },
  {
    "id": "montana-007",
    "name": "Kootenai National Forest Yaak River Primitive Zone",
    "state": "Montana",
    "county": "Lincoln",
    "coordinates": {"latitude": 48.8412, "longitude": -115.9125, "elevation_ft": 2850.0},
    "management_agency": {"name": "U.S. Forest Service - Kootenai National Forest (Three Rivers Ranger District)", "type": "Federal", "phone": "(406) 295-4693", "website": "https://www.fs.usda.gov/kootenai"},
    "rules_and_regulations": {"cost": "Free ($0/night primitive dispersed forest camping)", "stay_limit": "14 days maximum stay within a 30-day window", "guidelines": "Dispersed primitive camping allowed along Yaak River Road (FR 92) pullouts outside developed fee loops. Leave No Trace."},
    "waste_disposal_rules": {"poop_disposal": "Bury waste 6-8 inches deep 200 ft from Yaak River. Pack out toilet paper.", "trash_policy": "Strict Pack-It-In Pack-It-Out policy. Bear food storage required."},
    "campfire_rules": {"permitted": True, "firewood_policy": "Gather dead and down wood locally.", "safety_requirements": "Campfires permitted in cleared stone rings. Extinguish cold with river water.", "seasonal_fire_bans": "Subject to USFS dry summer fire bans."},
    "access_and_road_conditions": {"road_type": "Paved county road to gravel forest service roads", "road_conditions": "Paved main access road to smooth gravel river pullouts.", "vehicle_recommendation": "Accessible by standard FWD passenger car.", "scores": {"road_grade": 2, "road_terrain_difficulty": 3, "supply_run_pain": 5}},
    "nomad_connectivity_rating": {"overall_rating": "Fair (2/5 Stars)", "verizon_reliability": "1-2 bars 4G LTE spotty", "att_reliability": "1 bar 4G LTE", "tmobile_reliability": "No signal", "terrain_obstruction_risk": "High - Yaak River valley gorge and dense larch-fir forest", "distance_from_tower_corridor_miles": 18.0, "cellular_internet_dependable": False},
    "amenities": ["Yaak River Trout Access", "Yaak Falls Access", "Old-Growth Forest Canopy"],
    "location_scores": {"distance_to_groceries_score": 4, "distance_to_library_score": 4, "distance_to_gym_score": 3, "terrain_score": 9, "quietness_score": 10},
    "nearest_supply_towns": [{"town_name": "Troy, MT", "distance_miles": 18.5, "services_available": ["Grocery Store", "Gas Station", "Hardware Store", "Restaurants"]}, {"town_name": "Libby, MT", "distance_miles": 34.0, "services_available": ["Supermarket", "Hospital", "Public Library", "Gym & Fitness Center"]}],
    "seasonal_weather_effects": {"spring": "Lush Pacific Northwest rainforest greening; roaring Yaak Falls runoff.", "summer": "Pleasant summer weather (76-84°F) with river swimming holes.", "fall": "Spectacular golden western larch foliage in October.", "winter": "Cold mountain winter (15-30°F) with heavy snow pack."},
    "dangers_and_hazards": ["Grizzly Bears & Black Bears (Mandatory Bear Storage Order)", "Cold River Whitewater Currents"],
    "acoustic_environment": {"quietness_rating": "Yaak Valley Wilderness Silence (Quietness Score: 10/10)", "common_human_made_sounds": ["Occasional forest road car"]},
    "flora_and_fauna": {
      "common_plants_and_trees": ["Western Larch (Tamarack)", "Douglas Fir", "Western Red Cedar", "Huckleberry"],
      "common_animals": ["Grizzly Bear", "Moose", "Wolverine", "Harlequin Duck", "Bull Trout"]
    },
    "human_demographics_and_culture": "Northwest Montana Yaak Valley timber, remote wilderness living, and trout conservation culture.",
    "spiritual_and_folklore_data": {
      "nature_spirits_and_mythological_lore": "Kutenai (Ktunaxa) traditions honor the Yaak River valley as a sacred ancestral wilderness refuge.",
      "energetic_and_spiritual_features": "Dense ancient larch-cedar forest and rushing Yaak Falls generate deep, untouched wilderness peace."
    },
    "nearby_hiking_trails": [{"trail_name": "Yaak Falls Trail & Northwest Peak Trail", "length_miles": 4.5, "difficulty": "Moderate", "features": "Cascading Yaak River falls, old-growth cedar groves, Canadian border views"}],
    "public_reviews_summary": "Pristine Pacific Northwest-style Montana wilderness river camping with Yaak Falls and zero crowds.",
    "other_data": "Grizzly bear food storage strictly required by USFS.",
    "last_updated": "2026-09-12"
  },
  {
    "id": "montana-008",
    "name": "Beaverhead-Deerlodge National Forest Big Hole Primitive Zone",
    "state": "Montana",
    "county": "Beaverhead",
    "coordinates": {"latitude": 45.3412, "longitude": -113.4125, "elevation_ft": 6120.0},
    "management_agency": {"name": "U.S. Forest Service - Beaverhead-Deerlodge National Forest (Wisdom Ranger District)", "type": "Federal", "phone": "(406) 689-3243", "website": "https://www.fs.usda.gov/bdnf"},
    "rules_and_regulations": {"cost": "Free ($0/night primitive dispersed forest camping)", "stay_limit": "14 days maximum stay within a 30-day window", "guidelines": "Dispersed primitive camping allowed along Big Hole River roads and forest turnouts. Camp 100 ft from river. Leave No Trace."},
    "waste_disposal_rules": {"poop_disposal": "Bury waste 6-8 inches deep 200 ft from Big Hole River. Pack out toilet paper.", "trash_policy": "Strict Pack-It-In Pack-It-Out policy. Bear food storage required."},
    "campfire_rules": {"permitted": True, "firewood_policy": "Gather dead and down wood locally.", "safety_requirements": "Campfires permitted in cleared stone rings. Extinguish cold.", "seasonal_fire_bans": "Subject to USFS dry summer fire bans."},
    "access_and_road_conditions": {"road_type": "Paved MT-43 to gravel forest service roads", "road_conditions": "Paved highway access to flat gravel river turnouts.", "vehicle_recommendation": "Accessible by standard FWD passenger car.", "scores": {"road_grade": 2, "road_terrain_difficulty": 2, "supply_run_pain": 4}},
    "nomad_connectivity_rating": {"overall_rating": "Good (3/5 Stars)", "verizon_reliability": "3 bars 4G LTE", "att_reliability": "2-3 bars 4G LTE", "tmobile_reliability": "2 bars 4G LTE", "terrain_obstruction_risk": "Low - vast open Big Hole mountain valley basin", "distance_from_tower_corridor_miles": 5.2, "cellular_internet_dependable": True},
    "amenities": ["Big Hole Blue-Ribbon Trout River Access", "Anaconda-Pintler Wilderness Views", "Primitive Stone Fire Rings"],
    "location_scores": {"distance_to_groceries_score": 5, "distance_to_library_score": 5, "distance_to_gym_score": 4, "terrain_score": 9, "quietness_score": 10},
    "nearest_supply_towns": [{"town_name": "Wisdom, MT", "distance_miles": 7.5, "services_available": ["Grocery Store", "Gas Station", "Hardware Store", "Historic Saloon & Dining"]}, {"town_name": "Dillon, MT", "distance_miles": 46.0, "services_available": ["Supermarket", "Hospital", "Public Library", "Gym & Fitness Center", "College Amenities"]}],
    "seasonal_weather_effects": {"spring": "Cool high valley spring; salmonfly hatch on Big Hole River in June.", "summer": "Pleasant summer weather (75-82°F) with cool mountain night air (38°F).", "fall": "Crisp autumn weather with golden willow and aspen banks.", "winter": "Severe cold winter (-20 to 15°F); 'Valley of 10,000 Haystacks'."},
    "dangers_and_hazards": ["Grizzly Bears & Black Bears", "Extreme Winter Cold", "Biting Flies in Early Summer"],
    "acoustic_environment": {"quietness_rating": "Big Hole Valley Silence (Quietness Score: 10/10)", "common_human_made_sounds": ["Occasional rancher truck or fly angler car"]},
    "flora_and_fauna": {
      "common_plants_and_trees": ["Lodgepole Pine", "Quaking Aspen", "Sandbar Willow", "Mountain Big Sagebrush"],
      "common_animals": ["Grizzly Bear", "Moose", "Arctic Grayling (Native Species)", "Brown Trout", "Sandhill Crane"]
    },
    "human_demographics_and_culture": "Southwest Montana Big Hole cattle ranching, Nez Perce National Historic Trail, and world-class fly fishing culture.",
    "spiritual_and_folklore_data": {
      "nature_spirits_and_mythological_lore": "Nez Perce (Nimiipuu) historic sacred site (Big Hole National Battlefield) honors ancestors of the 1877 campaign.",
      "energetic_and_spiritual_features": "Vast mountain valley framed by the Anaconda-Pintler peaks and meandering trout waters produces solemn majesty."
    },
    "nearby_hiking_trails": [{"trail_name": "Big Hole Battlefield Trail & Anaconda-Pintler Wilderness Access", "length_miles": 4.8, "difficulty": "Easy to Moderate", "features": "Historic 1877 Nez Perce battlefield trails, trout river meanders, mountain panoramas"}],
    "public_reviews_summary": "World-class trout stream camping in Montana's famous Big Hole valley with great cell signal and quiet night skies.",
    "other_data": "Carry bear spray and respect historic site guidelines.",
    "last_updated": "2026-09-12"
  },
  {
    "id": "montana-009",
    "name": "Bitterroot National Forest West Fork Primitive Zone",
    "state": "Montana",
    "county": "Ravalli",
    "coordinates": {"latitude": 45.7812, "longitude": -114.2812, "elevation_ft": 4450.0},
    "management_agency": {"name": "U.S. Forest Service - Bitterroot National Forest (West Fork Ranger District)", "type": "Federal", "phone": "(406) 821-3269", "website": "https://www.fs.usda.gov/bitterroot"},
    "rules_and_regulations": {"cost": "Free ($0/night primitive dispersed forest camping)", "stay_limit": "14 days maximum stay within a 30-day window", "guidelines": "Dispersed primitive camping allowed along West Fork Road (FR 473) pullouts outside developed fee loops. Leave No Trace."},
    "waste_disposal_rules": {"poop_disposal": "Bury waste 6-8 inches deep 200 ft from West Fork river. Pack out toilet paper.", "trash_policy": "Strict Pack-It-In Pack-It-Out policy. Bear food storage required."},
    "campfire_rules": {"permitted": True, "firewood_policy": "Gather dead and down wood locally.", "safety_requirements": "Campfires permitted in cleared stone rings. Extinguish cold.", "seasonal_fire_bans": "Subject to USFS dry summer fire bans."},
    "access_and_road_conditions": {"road_type": "Paved county road to gravel forest service roads", "road_conditions": "Paved access roads to smooth gravel river pullouts.", "vehicle_recommendation": "Accessible by standard FWD passenger car.", "scores": {"road_grade": 2, "road_terrain_difficulty": 3, "supply_run_pain": 4}},
    "nomad_connectivity_rating": {"overall_rating": "Good (3/5 Stars)", "verizon_reliability": "3 bars 4G LTE", "att_reliability": "2-3 bars 4G LTE", "tmobile_reliability": "2 bars 4G LTE", "terrain_obstruction_risk": "Moderate - Bitterroot mountain canyon walls", "distance_from_tower_corridor_miles": 5.8, "cellular_internet_dependable": True},
    "amenities": ["West Fork Bitterroot River Trout Access", "Bitterroot Mountain Ridge Views", "Primitive Stone Fire Rings"],
    "location_scores": {"distance_to_groceries_score": 6, "distance_to_library_score": 6, "distance_to_gym_score": 5, "terrain_score": 9, "quietness_score": 9},
    "nearest_supply_towns": [{"town_name": "Darby, MT", "distance_miles": 14.5, "services_available": ["Grocery Store", "Gas Station", "Hardware Store", "Outfitters", "Restaurants"]}, {"town_name": "Hamilton, MT", "distance_miles": 32.0, "services_available": ["Supermarket", "Hospital", "Public Library", "Gym & Fitness Center"]}],
    "seasonal_weather_effects": {"spring": "Lush mountain valley greening with rushing river melt.", "summer": "Pleasant summer weather (78-85°F) with fly fishing and river floating.", "fall": "Vibrant golden larch and aspen foliage in October.", "winter": "Cold mountain winter (20-35°F) with snowpack."},
    "dangers_and_hazards": ["Grizzly Bears & Black Bears", "Cold River Currents", "High Summer Wildfire Risk"],
    "acoustic_environment": {"quietness_rating": "Bitterroot River Audio (Quietness Score: 9/10)", "common_human_made_sounds": ["Occasional forest road car", "High altitude commercial flights"]},
    "flora_and_fauna": {
      "common_plants_and_trees": ["Ponderosa Pine", "Douglas Fir", "Western Larch", "Bitterroot (State Flower)"],
      "common_animals": ["Grizzly Bear", "Elk", "Bighorn Sheep", "West slope Cutthroat Trout", "Osprey"]
    },
    "human_demographics_and_culture": "Western Montana Bitterroot Valley timber, fly fishing, and mountain ranching culture.",
    "spiritual_and_folklore_data": {
      "nature_spirits_and_mythological_lore": "Salish traditions honor the Bitterroot River valley as sacred ancestral home of bitterroot plant gatherers.",
      "energetic_and_spiritual_features": "Towering Bitterroot mountain granite peaks above clear river waters generate serene clarity."
    },
    "nearby_hiking_trails": [{"trail_name": "Painted Rocks State Park Trail & Trapper Peak Access", "length_miles": 6.2, "difficulty": "Moderate to Strenuous", "features": "10,157-ft Trapper Peak vistas, granite cliff formations, trout river pools"}],
    "public_reviews_summary": "Fantastic Bitterroot riverfront primitive camping near Darby with solid cell service and blue-ribbon fly fishing.",
    "other_data": "Store food in bear canisters.",
    "last_updated": "2026-09-12"
  },
  {
    "id": "montana-010",
    "name": "BLM Upper Missouri River Breaks Dispersed Primitive Zone",
    "state": "Montana",
    "county": "Fergus / Chouteau",
    "coordinates": {"latitude": 47.7812, "longitude": -109.6812, "elevation_ft": 2840.0},
    "management_agency": {"name": "Bureau of Land Management (BLM) - Lewistown Field Office", "type": "Federal", "phone": "(406) 538-1900", "website": "https://www.blm.gov/montana-dakotas"},
    "rules_and_regulations": {"cost": "Free ($0/night primitive BLM dispersed camping)", "stay_limit": "14 days maximum stay within a 28-day window", "guidelines": "Dispersed primitive camping allowed along Missouri River breaks dirt roads and river float access sites. Leave No Trace."},
    "waste_disposal_rules": {"poop_disposal": "Bury waste 6-8 inches deep 200 ft from Missouri River. Pack out toilet paper.", "trash_policy": "Strict Pack-It-In Pack-It-Out policy."},
    "campfire_rules": {"permitted": True, "firewood_policy": "Gather dead and down cottonwood locally.", "safety_requirements": "Campfires permitted in cleared stone rings. Extinguish cold with river water.", "seasonal_fire_bans": "Subject to BLM Stage 1 & 2 fire bans during dry summer."},
    "access_and_road_conditions": {"road_type": "Gravel and dirt prairie break roads", "road_conditions": "Graded gravel road to dirt river pullouts; gumbo dirt roads get slick when wet.", "vehicle_recommendation": "Accessible by standard FWD car in dry weather; 4WD required when wet.", "scores": {"road_grade": 4, "road_terrain_difficulty": 4, "supply_run_pain": 6}},
    "nomad_connectivity_rating": {"overall_rating": "Fair (2/5 Stars)", "verizon_reliability": "1-2 bars 4G LTE spotty on high break rims", "att_reliability": "1 bar 4G LTE", "tmobile_reliability": "No signal", "terrain_obstruction_risk": "High - white sandstone cliff canyon and badland breaks", "distance_from_tower_corridor_miles": 18.0, "cellular_internet_dependable": False},
    "amenities": ["Historic Lewis & Clark River Route", "White Cliffs Sandstone Overlooks", "Dark Sky Star Observation"],
    "location_scores": {"distance_to_groceries_score": 4, "distance_to_library_score": 4, "distance_to_gym_score": 3, "terrain_score": 10, "quietness_score": 10},
    "nearest_supply_towns": [{"town_name": "Fort Benton, MT", "distance_miles": 26.5, "services_available": ["Grocery Store", "Gas Station", "Hardware Store", "Historic Museums & Dining"]}, {"town_name": "Lewistown, MT", "distance_miles": 48.0, "services_available": ["Supermarket", "Hospital", "Public Library", "Gym & Fitness Center"]}],
    "seasonal_weather_effects": {"spring": "Lush green prairie breaks; river floating season thaws.", "summer": "Hot dry prairie summer (88-96°F) with cool river night air.", "fall": "Crisp autumn weather with golden cottonwood trees along river.", "winter": "Cold prairie winter (10-28°F) with light snow."},
    "dangers_and_hazards": ["Gumbo Dirt Roads Impassable when Wet", "Prairie Rattlesnakes", "Remote Prairie Isolation"],
    "acoustic_environment": {"quietness_rating": "Missouri River Breaks Silence (Quietness Score: 10/10)", "common_human_made_sounds": ["Occasional float trip canoeist", "High altitude jet contrails"]},
    "flora_and_fauna": {
      "common_plants_and_trees": ["Plains Cottonwood", "Rocky Mountain Juniper", "Ponderosa Pine", "Big Sagebrush"],
      "common_animals": ["Bighorn Sheep", "Elk", "Mule Deer", "Bald Eagle", "Pelican"]
    },
    "human_demographics_and_culture": "Central Montana Missouri River breaks, Lewis & Clark National Historic Trail, and cattle ranching culture.",
    "spiritual_and_folklore_data": {
      "nature_spirits_and_mythological_lore": "Blackfeet and Gros Ventre traditions honor the White Cliffs of the Missouri as sacred spirit rock portals described in Lewis & Clark journals.",
      "energetic_and_spiritual_features": "Towering white sandstone cliffs carved by the Missouri River generate timeless wilderness majesty."
    },
    "nearby_hiking_trails": [{"trail_name": "White Cliffs & Hole-in-the-Wall Trail", "length_miles": 5.4, "difficulty": "Moderate", "features": "White sandstone rock formations, Missouri River canyon vistas, bighorn sheep"}],
    "public_reviews_summary": "Historic Lewis & Clark river canyon scenery and complete quietness on Montana's Missouri River Breaks.",
    "other_data": "Do not drive on gumbo clay roads during rain.",
    "last_updated": "2026-09-12"
  }
])
save_state(mt, mt_path)

# Nevada (+5 sites -> 10 total)
nv, nv_path = load_state('nevada')
nv.extend([
  {
    "id": "nevada-006",
    "name": "BLM Logandale Trails Primitive Dispersed Zone",
    "state": "Nevada",
    "county": "Clark",
    "coordinates": {"latitude": 36.5812, "longitude": -114.4812, "elevation_ft": 1850.0},
    "management_agency": {"name": "Bureau of Land Management (BLM) - Las Vegas Field Office", "type": "Federal", "phone": "(702) 515-5000", "website": "https://www.blm.gov/nevada"},
    "rules_and_regulations": {"cost": "Free ($0/night primitive BLM dispersed camping)", "stay_limit": "14 days maximum stay within a 28-day window", "guidelines": "Dispersed primitive camping allowed along Logandale Trails dirt roads among red sandstone hoodoos outside Valley of Fire state park. Leave No Trace."},
    "waste_disposal_rules": {"poop_disposal": "Bury waste 6-8 inches deep 200 ft from washes or pack out using WAG bags.", "trash_policy": "Strict Pack-It-In Pack-It-Out policy."},
    "campfire_rules": {"permitted": True, "firewood_policy": "Bring firewood; no wood collecting in desert area.", "safety_requirements": "Campfires permitted in cleared metal or stone rings. Extinguish cold.", "seasonal_fire_bans": "Subject to BLM Stage 1 & 2 fire restrictions during summer."},
    "access_and_road_conditions": {"road_type": "Gravel and sand desert wash roads", "road_conditions": "Graded gravel access road; soft sand spots require careful driving.", "vehicle_recommendation": "CUV, SUV, or FWD passenger car fine on main gravel road; 4WD helpful for soft sand.", "scores": {"road_grade": 3, "road_terrain_difficulty": 4, "supply_run_pain": 3}},
    "nomad_connectivity_rating": {"overall_rating": "Great (4/5 Stars)", "verizon_reliability": "4 bars 5G/4G LTE", "att_reliability": "3-4 bars 4G LTE", "tmobile_reliability": "3-4 bars 4G LTE", "terrain_obstruction_risk": "Low to Moderate - red sandstone rock formations", "distance_from_tower_corridor_miles": 2.8, "cellular_internet_dependable": True},
    "amenities": ["Aztec Red Sandstone Hoodoo Views", "Ancient Petroglyph Viewing nearby", "Dark Sky Astronomy"],
    "location_scores": {"distance_to_groceries_score": 7, "distance_to_library_score": 7, "distance_to_gym_score": 6, "terrain_score": 10, "quietness_score": 8},
    "nearest_supply_towns": [{"town_name": "Logandale / Overton, NV", "distance_miles": 6.8, "services_available": ["Grocery Store", "Gas Station", "Hardware Store", "Restaurants"]}, {"town_name": "Las Vegas, NV", "distance_miles": 52.0, "services_available": ["International Airport", "Major Hospitals", "Full Urban Amenities"]}],
    "seasonal_weather_effects": {"spring": "Ideal spring weather (75-84°F) with blooming desert flora.", "summer": "Extremely hot desert summer (105-112°F); dangerous heat.", "fall": "Warm sunny days and cool desert nights.", "winter": "Ideal winter climate (58-68°F); popular nomad winter hub."},
    "dangers_and_hazards": ["Extreme Summer Heat", "Rattlesnakes", "Getting Stuck in Soft Sand"],
    "acoustic_environment": {"quietness_rating": "Red Rock Canyon Quiet (Quietness Score: 8/10)", "common_human_made_sounds": ["Occasional OHV vehicle", "Distant I-15 traffic hum"]},
    "flora_and_fauna": {
      "common_plants_and_trees": ["Creosote Bush", "White Bursage", "Joshua Tree", "Beaver tail Cactus"],
      "common_animals": ["Desert Tortoise (Protected)", "Desert Bighorn Sheep", "Gambel's Quail", "Coyote"]
    },
    "human_demographics_and_culture": "Southern Nevada Moapa Valley, Southern Paiute, and OHV desert recreation culture.",
    "spiritual_and_folklore_data": {
      "nature_spirits_and_mythological_lore": "Southern Paiute traditions honor the Aztec red sandstone formations as sacred ancestral spirit lands.",
      "energetic_and_spiritual_features": "Vivid fiery red sandstone cliffs and natural petroglyph arches generate an energizing desert power."
    },
    "nearby_hiking_trails": [{"trail_name": "Logandale Petroglyph & Red Rock Canyon Trail", "length_miles": 3.8, "difficulty": "Easy to Moderate", "features": "Aztec red sandstone hoodoos, ancient Native petroglyphs, desert wash canyons"}],
    "public_reviews_summary": "Valley of Fire scenery without the state park fees, plus blazing fast 5G cell internet near Las Vegas.",
    "other_data": "Do not touch or alter protected petroglyphs.",
    "last_updated": "2026-09-12"
  },
  {
    "id": "nevada-007",
    "name": "BLM Fairview Peak Dispersed Primitive Zone",
    "state": "Nevada",
    "county": "Churchill",
    "coordinates": {"latitude": 39.2148, "longitude": -118.1214, "elevation_ft": 5250.0},
    "management_agency": {"name": "Bureau of Land Management (BLM) - Carson City District", "type": "Federal", "phone": "(775) 885-6000", "website": "https://www.blm.gov/nevada"},
    "rules_and_regulations": {"cost": "Free ($0/night primitive BLM dispersed camping)", "stay_limit": "14 days maximum stay within a 28-day window", "guidelines": "Dispersed primitive camping allowed on open BLM lands along Fairview Peak Road off US-50 ('Loneliest Road in America'). Leave No Trace."},
    "waste_disposal_rules": {"poop_disposal": "Bury waste 6-8 inches deep 200 ft from dry washes. Pack out toilet paper.", "trash_policy": "Strict Pack-It-In Pack-It-Out policy."},
    "campfire_rules": {"permitted": True, "firewood_policy": "Gather dead and down pinyon-juniper wood.", "safety_requirements": "Campfires permitted in cleared stone rings. Extinguish cold.", "seasonal_fire_bans": "Subject to BLM Stage 1 & 2 fire restrictions during summer."},
    "access_and_road_conditions": {"road_type": "Paved US-50 to gravel BLM dirt roads", "road_conditions": "Paved highway access to graded gravel basin turnouts.", "vehicle_recommendation": "Accessible by standard FWD passenger car.", "scores": {"road_grade": 2, "road_terrain_difficulty": 3, "supply_run_pain": 4}},
    "nomad_connectivity_rating": {"overall_rating": "Great (4/5 Stars)", "verizon_reliability": "4 bars 4G LTE on high valley basin rim", "att_reliability": "3-4 bars 4G LTE", "tmobile_reliability": "3 bars 4G LTE", "terrain_obstruction_risk": "Low - vast open Great Basin valley floor", "distance_from_tower_corridor_miles": 2.5, "cellular_internet_dependable": True},
    "amenities": ["1.4-Billion-Year-Old Fault Scarp Views", "Dark Sky Astronomy", "Great Basin Mountain Vistas"],
    "location_scores": {"distance_to_groceries_score": 6, "distance_to_library_score": 6, "distance_to_gym_score": 5, "terrain_score": 8, "quietness_score": 10},
    "nearest_supply_towns": [{"town_name": "Fallon, NV", "distance_miles": 38.0, "services_available": ["Supermarket", "Hospital", "Public Library", "Gym & Fitness Center", "Hardware Store", "Naval Air Station Amenities"]}],
    "seasonal_weather_effects": {"spring": "Cool dry Great Basin spring weather (65-75°F).", "summer": "Warm to hot dry summer (90-96°F) with cool desert nights (52°F).", "fall": "Crisp autumn days with crystal clear stargazing skies.", "winter": "Cold high desert winter (25-42°F) with light snow."},
    "dangers_and_hazards": ["Great Basin Rattlesnakes", "Remote Desert Travel", "High Desert Sun Exposure"],
    "acoustic_environment": {"quietness_rating": "Great Basin Wind Silence (Quietness Score: 10/10)", "common_human_made_sounds": ["High altitude Top Gun naval fighter jets from Fallon NAS", "Occasional US-50 car"]},
    "flora_and_fauna": {
      "common_plants_and_trees": ["Single-leaf Pinyon Pine", "Utah Juniper", "Great Basin Sagebrush", "Mormon Tea"],
      "common_animals": ["Wild Horses (Mustangs)", "Pronghorn Antelope", "Chukar", "Desert Horned Lizard", "Coyote"]
    },
    "human_demographics_and_culture": "Central Nevada Pony Express history, 1954 earthquake fault scarp geology, and 'Loneliest Road' highway culture.",
    "spiritual_and_folklore_data": {
      "nature_spirits_and_mythological_lore": "Northern Paiute and Shoshone traditions honor Fairview Peak as a high mountain sentinel of starlight.",
      "energetic_and_spiritual_features": "Historic 1954 earthquake fault scarps and wide open desert basin generate humbling geological energy."
    },
    "nearby_hiking_trails": [{"trail_name": "Fairview Peak Earthquake Scarp & Summit Trail", "length_miles": 4.5, "difficulty": "Moderate", "features": "1954 earthquake fault line scarps, 8,300-ft summit fire lookout views"}],
    "public_reviews_summary": "Solid 4G cell signal along US-50, incredible night skies, wild horses roaming, and zero fees.",
    "other_data": "Bring fresh drinking water and extra fuel.",
    "last_updated": "2026-09-12"
  },
  {
    "id": "nevada-008",
    "name": "BLM Black Rock Desert Edge Dispersed Zone",
    "state": "Nevada",
    "county": "Humboldt / Washoe",
    "coordinates": {"latitude": 40.9812, "longitude": -119.0142, "elevation_ft": 3920.0},
    "management_agency": {"name": "Bureau of Land Management (BLM) - Winnemucca District", "type": "Federal", "phone": "(775) 623-1500", "website": "https://www.blm.gov/nevada"},
    "rules_and_regulations": {"cost": "Free ($0/night primitive BLM dispersed camping outside Burning Man event period)", "stay_limit": "14 days maximum stay within a 28-day window", "guidelines": "Dispersed primitive camping allowed along Soldier Meadows Road and playa edge pullouts. Do not drive on wet playa surface. Leave No Trace."},
    "waste_disposal_rules": {"poop_disposal": "Pack out human waste using WAG bags / Portable Toilet due to flat alkali playa soils.", "trash_policy": "Strict Pack-It-In Pack-It-Out policy. Absolute Leave No Trace."},
    "campfire_rules": {"permitted": True, "firewood_policy": "Bring firewood; no collecting on playa.", "safety_requirements": "Campfires permitted ONLY in raised metal burn pans to prevent playa scars. Extinguish cold.", "seasonal_fire_bans": "Subject to BLM Stage 1 & 2 fire restrictions during summer."},
    "access_and_road_conditions": {"road_type": "Gravel and alkali dirt playa roads", "road_conditions": "Graded gravel access road along playa edge; playa surface becomes impassable sticky mud when wet.", "vehicle_recommendation": "Accessible by standard FWD passenger car in dry weather; 4WD required when wet.", "scores": {"road_grade": 3, "road_terrain_difficulty": 4, "supply_run_pain": 6}},
    "nomad_connectivity_rating": {"overall_rating": "Fair (2/5 Stars)", "verizon_reliability": "1-2 bars 4G LTE spotty near Gerlach highway corridor", "att_reliability": "1 bar 4G LTE", "tmobile_reliability": "No signal", "terrain_obstruction_risk": "Low - vast flat alkali playa expanse", "distance_from_tower_corridor_miles": 18.0, "cellular_internet_dependable": False},
    "amenities": ["Vast Alkali Playa Horizons", "Dark Sky Astronomy", "Geothermal Hot Springs nearby"],
    "location_scores": {"distance_to_groceries_score": 3, "distance_to_library_score": 3, "distance_to_gym_score": 2, "terrain_score": 10, "quietness_score": 10},
    "nearest_supply_towns": [{"town_name": "Gerlach, NV", "distance_miles": 14.5, "services_available": ["General Store", "Gas Station", "Local Saloon & Dining"]}, {"town_name": "Winnemucca, NV", "distance_miles": 85.0, "services_available": ["Supermarket", "Hospital", "Public Library", "Gym & Fitness Center"]}],
    "seasonal_weather_effects": {"spring": "Playa holds standing water thaws; impassable mud.", "summer": "Hot dry desert summer (95-104°F) with dust storms ('whiteouts').", "fall": "Crisp dry autumn weather; ideal playa exploration weather.", "winter": "Cold winter (20-38°F) with snow thaws turning playa to mud."},
    "dangers_and_hazards": ["Getting Vehicle Stuck in Wet Alkali Mud", "Severe Dust Storms (Whiteouts)", "Extreme Remote Desert Isolation"],
    "acoustic_environment": {"quietness_rating": "Playa Horizon Silence (Quietness Score: 10/10)", "common_human_made_sounds": ["Occasional high altitude aircraft"]},
    "flora_and_fauna": {
      "common_plants_and_trees": ["Black Greasewood", "Shadscale", "Fourwing Saltbush", "Iodine Bush"],
      "common_animals": ["Pronghorn Antelope", "Wild Horses", "Kit Fox", "Raven", "Great Basin Rattlesnake"]
    },
    "human_demographics_and_culture": "Black Rock Desert High Rock Canyon Emigrant Trail history, Burning Man art culture, and land speed record testing grounds.",
    "spiritual_and_folklore_data": {
      "nature_spirits_and_mythological_lore": "Northern Paiute traditions honor the Black Rock Desert as a sacred dry lake realm of ancient winds.",
      "energetic_and_spiritual_features": "360-degree flat alkali playa extending to infinity under cosmic night skies generates unforgettable surreal freedom."
    },
    "nearby_hiking_trails": [{"trail_name": "Applegate-Lassen Historic Emigrant Trail", "length_miles": 12.0, "difficulty": "Moderate", "features": "1840s wagon ruts, Black Rock point landmark, hot spring pools"}],
    "public_reviews_summary": "Surreal alien landscape with unmatched dark skies, but requires complete desert self-sufficiency and dry weather.",
    "other_data": "Never drive onto the playa if there is any moisture.",
    "last_updated": "2026-09-12"
  },
  {
    "id": "nevada-009",
    "name": "BLM Sand Mountain Recreation Dispersed Buffer Zone",
    "state": "Nevada",
    "county": "Churchill",
    "coordinates": {"latitude": 39.2812, "longitude": -118.4125, "elevation_ft": 4120.0},
    "management_agency": {"name": "Bureau of Land Management (BLM) - Carson City District", "type": "Federal", "phone": "(775) 885-6000", "website": "https://www.blm.gov/nevada"},
    "rules_and_regulations": {"cost": "Free ($0/night primitive BLM dispersed camping outside central sand dune OHV fee area)", "stay_limit": "14 days maximum stay within a 28-day window", "guidelines": "Dispersed primitive camping allowed along US-50 pullouts outside Sand Mountain Recreation Area fee entrance. Leave No Trace."},
    "waste_disposal_rules": {"poop_disposal": "Bury waste 6-8 inches deep 200 ft from dry washes or pack out using WAG bags.", "trash_policy": "Strict Pack-It-In Pack-It-Out policy."},
    "campfire_rules": {"permitted": True, "firewood_policy": "Bring firewood; no wood on dunes.", "safety_requirements": "Campfires permitted in cleared metal or stone rings. Extinguish cold.", "seasonal_fire_bans": "Subject to BLM Stage 1 & 2 fire restrictions in summer."},
    "access_and_road_conditions": {"road_type": "Paved US-50 to hard-packed gravel pullouts", "road_conditions": "Smooth paved main road to gravel pullouts.", "vehicle_recommendation": "Accessible by standard FWD passenger car, camper vans, and rigs.", "scores": {"road_grade": 1, "road_terrain_difficulty": 2, "supply_run_pain": 3}},
    "nomad_connectivity_rating": {"overall_rating": "Great (4/5 Stars)", "verizon_reliability": "4 bars 5G/4G LTE along US-50 highway corridor", "att_reliability": "4 bars 4G LTE", "tmobile_reliability": "3-4 bars 4G LTE", "terrain_obstruction_risk": "Low - open desert basin looking towards 600-foot singing sand dune", "distance_from_tower_corridor_miles": 1.8, "cellular_internet_dependable": True},
    "amenities": ["600-ft Singing Sand Dune Views", "Pony Express Station Ruins nearby", "Dark Sky Astronomy"],
    "location_scores": {"distance_to_groceries_score": 7, "distance_to_library_score": 7, "distance_to_gym_score": 6, "terrain_score": 9, "quietness_score": 8},
    "nearest_supply_towns": [{"town_name": "Fallon, NV", "distance_miles": 22.4, "services_available": ["Supermarket", "Hospital", "Public Library", "Gym & Fitness Center", "Hardware Store", "Restaurants"]}],
    "seasonal_weather_effects": {"spring": "Mild dry desert spring weather (68-78°F).", "summer": "Hot dry summer (94-102°F) with cool night breezes.", "fall": "Crisp sunny autumn days.", "winter": "Cool high desert winter (42-52°F)."},
    "dangers_and_hazards": ["Getting Vehicle Stuck in Deep Sand Off-Road", "Rattlesnakes", "High Summer Heat"],
    "acoustic_environment": {"quietness_rating": "Desert Basin Audio (Quietness Score: 8/10)", "common_human_made_sounds": ["Distant US-50 traffic hum", "Occasional OHV sand dune motor hum"]},
    "flora_and_fauna": {
      "common_plants_and_trees": ["Sand Mountain Blue Butterfly Habitat", "Fourwing Saltbush", "Creosote Bush", "Indian Ricegrass"],
      "common_animals": ["Sand Mountain Blue Butterfly (Endemic)", "Wild Horses", "Desert Horned Lizard", "Coyote"]
    },
    "human_demographics_and_culture": "Central Nevada Pony Express historical trail, sand dune OHV riding, and Great Basin geological culture.",
    "spiritual_and_folklore_data": {
      "nature_spirits_and_mythological_lore": "Northern Paiute traditions honor Sand Mountain as a sacred 'Singing Dune' that hums when sand avalanches glide down slopes.",
      "energetic_and_spiritual_features": "600-foot white sand dune rising out of a dark volcanic basin produces a mesmerizing, resonant energy."
    },
    "nearby_hiking_trails": [{"trail_name": "Sand Mountain Dune Ridge Walk & Sand Springs Pony Express Trail", "length_miles": 3.8, "difficulty": "Moderate (Walking on Soft Sand)", "features": "600-ft sand dune ridge walk, 1860 Pony Express stone station ruins"}],
    "public_reviews_summary": "Blazing fast cell service right off US-50 with views of the famous 600-foot singing sand dune.",
    "other_data": "Do not drive off paved/gravel roads onto soft sand without airing down tires.",
    "last_updated": "2026-09-12"
  },
  {
    "id": "nevada-010",
    "name": "BLM Snake Valley Primitive Dispersed Zone",
    "state": "Nevada",
    "county": "White Pine",
    "coordinates": {"latitude": 38.9125, "longitude": -114.1214, "elevation_ft": 5320.0},
    "management_agency": {"name": "Bureau of Land Management (BLM) - Ely District", "type": "Federal", "phone": "(775) 289-1800", "website": "https://www.blm.gov/nevada"},
    "rules_and_regulations": {"cost": "Free ($0/night primitive BLM dispersed camping)", "stay_limit": "14 days maximum stay within a 28-day window", "guidelines": "Dispersed primitive camping allowed along Sacramento Pass / Snake Valley dirt roads outside Great Basin National Park boundary. Leave No Trace."},
    "waste_disposal_rules": {"poop_disposal": "Bury waste 6-8 inches deep 200 ft from mountain streams. Pack out toilet paper.", "trash_policy": "Strict Pack-It-In Pack-It-Out policy."},
    "campfire_rules": {"permitted": True, "firewood_policy": "Gather dead and down pinyon-juniper wood locally.", "safety_requirements": "Campfires permitted in cleared stone rings. Extinguish cold.", "seasonal_fire_bans": "Subject to BLM Stage 1 & 2 fire restrictions in summer."},
    "access_and_road_conditions": {"road_type": "Paved US-50 to gravel BLM roads", "road_conditions": "Paved highway access to smooth gravel basin turnouts.", "vehicle_recommendation": "Accessible by standard FWD passenger car.", "scores": {"road_grade": 2, "road_terrain_difficulty": 2, "supply_run_pain": 4}},
    "nomad_connectivity_rating": {"overall_rating": "Good (3/5 Stars)", "verizon_reliability": "3 bars 4G LTE", "att_reliability": "2-3 bars 4G LTE", "tmobile_reliability": "2 bars 4G LTE", "terrain_obstruction_risk": "Low to Moderate - broad Snake Valley basin looking towards 13,063-ft Wheeler Peak", "distance_from_tower_corridor_miles": 4.5, "cellular_internet_dependable": True},
    "amenities": ["13,063-ft Wheeler Peak Views", "Dark Sky Reserve Stargazing", "Great Basin National Park Access"],
    "location_scores": {"distance_to_groceries_score": 5, "distance_to_library_score": 5, "distance_to_gym_score": 4, "terrain_score": 10, "quietness_score": 10},
    "nearest_supply_towns": [{"town_name": "Baker, NV", "distance_miles": 8.5, "services_available": ["General Store", "Gas Station", "National Park Visitor Center", "Local Dining"]}, {"town_name": "Ely, NV", "distance_miles": 58.0, "services_available": ["Supermarket", "Hospital", "Public Library", "Gym & Fitness Center", "Hardware Store"]}],
    "seasonal_weather_effects": {"spring": "Cool high desert spring weather (60-70°F) with snowcapped Wheeler Peak.", "summer": "Pleasant summer weather (78-85°F) with cool mountain night air (48°F).", "fall": "Crisp autumn weather with golden aspen foliage on Wheeler Peak.", "winter": "Cold winter (20-38°F) with snow on mountain slopes."},
    "dangers_and_hazards": ["High Altitude Weather Shifts on Nearby Peaks", "Great Basin Rattlesnakes", "Remote Desert Distance"],
    "acoustic_environment": {"quietness_rating": "Great Basin National Park Silence (Quietness Score: 10/10)", "common_human_made_sounds": ["High altitude commercial flights"]},
    "flora_and_fauna": {
      "common_plants_and_trees": ["Single-leaf Pinyon Pine", "Utah Juniper", "Great Basin Sagebrush", "Bristlecone Pine (High Peaks)"],
      "common_animals": ["Pronghorn Antelope", "Mule Deer", "Rocky Mountain Bighorn Sheep", "Bonneville Cutthroat Trout"]
    },
    "human_demographics_and_culture": "Eastern Nevada Great Basin National Park gateway, Lehman Caves exploration, and dark sky astronomy culture.",
    "spiritual_and_folklore_data": {
      "nature_spirits_and_mythological_lore": "Western Shoshone traditions honor 13,063-foot Wheeler Peak as a sacred cosmic mountain of ancient bristlecone pine spirits.",
      "energetic_and_spiritual_features": "Certified International Dark Sky Park corridor beneath 13,000-foot peaks generates unmatched cosmic silence."
    },
    "nearby_hiking_trails": [{"trail_name": "Wheeler Peak Summit & Ancient Bristlecone Pine Grove Trail", "length_miles": 8.2, "difficulty": "Strenuous", "features": "4,900-year-old ancient bristlecone pine trees, 13,063-ft summit, alpine glacier cirque"}],
    "public_reviews_summary": "Sublime mountain views of Wheeler Peak, world-class dark sky stargazing, and decent cell service outside Great Basin NP.",
    "other_data": "Bring fresh drinking water.",
    "last_updated": "2026-09-12"
  }
])
save_state(nv, nv_path)

print("Montana and Nevada expanded to 10 campsites each!")
