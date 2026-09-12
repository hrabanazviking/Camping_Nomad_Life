import json
import os

BASE_DIR = "/home/volmarr/.gemini/antigravity/scratch/Camping_Nomad_Life/states"

# Complete campsite dictionary for expansion
dataset_expansion = {
  "illinois.json": [
    {
      "id": "il-lusk-creek-wilderness-dispersed",
      "name": "Lusk Creek Wilderness Dispersed Primitive Camping",
      "state": "Illinois",
      "county": "Pope County",
      "coordinates": { "latitude": 37.4789, "longitude": -88.5412, "elevation_ft": 520 },
      "management_agency": {
        "name": "US Forest Service - Shawnee National Forest (Hidden Springs Ranger District)",
        "type": "USFS",
        "phone": "(618) 658-2111",
        "website": "https://www.fs.usda.gov/shawnee"
      },
      "rules_and_regulations": {
        "cost": "100% Free - USFS Wilderness Primitive Camping (zero fee)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed wilderness camping permitted throughout Lusk Creek Wilderness. Camp at least 150ft from trails and water streams."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6 inches deep in soil 200 feet from Lusk Creek and water drainages. Pack out all toilet paper.",
        "trash_policy": "Strict Leave No Trace wilderness policy."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down wood gathering permitted.",
        "safety_requirements": "Campfires in small rock rings using dead wood only. Fully extinguish before departing.",
        "seasonal_fire_bans": "Dry autumn fire warnings observed."
      },
      "access_and_road_conditions": {
        "road_type": "Paved county road to gravel trailhead parking lot",
        "road_conditions": "Well-maintained gravel access lot at Eddyville trailhead.",
        "vehicle_recommendation": "Accessible by standard low clearance 2WD cars.",
        "scores": { "road_grade": 2, "road_terrain_difficulty": 3, "supply_run_pain": 4 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Fair to Moderate / Ridge Dependent",
        "verizon_reliability": "2-3 bars 4G LTE on ridge tops",
        "att_reliability": "2-3 bars 4G LTE",
        "tmobile_reliability": "1-2 bars 4G LTE",
        "terrain_obstruction_risk": "High in deep sandstone creek canyons; low on high forest ridges",
        "distance_from_tower_corridor_miles": 5.0,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Primitive Wilderness Campsites",
        "Scenic Sandstone Canyon Bluff Views",
        "Lusk Creek Water Source (Filter mandatory)",
        "Horse & Hiking Trailhead Access"
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
          "town_name": "Golconda, IL",
          "distance_miles": 14.0,
          "services_available": ["Grocery Store", "Gas Station", "Ohio River Marina", "Restaurants", "Public Library"]
        },
        {
          "town_name": "Harrisburg, IL",
          "distance_miles": 20.0,
          "services_available": ["Kroger Supermarket", "Walmart", "Hospital", "24/7 Gyms", "Hardware Stores"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "50-68°F, roaring canyon creeks, lush green dogwood bloom.",
        "summer": "75-90°F, humid Southern Illinois weather, shaded forest canopy.",
        "fall": "55-72°F, spectacular hardwood fall foliage colors.",
        "winter": "28-45°F, freezing nights, occasional light snowfall."
      },
      "dangers_and_hazards": [
        "High sandstone bluff cliffs (watch footing near edges)",
        "Flash flooding in narrow stream gorges during thunderstorms",
        "Venomous copperhead snakes in rocky talus"
      ],
      "acoustic_environment": {
        "quietness_rating": "9/10 - Creek water trickles and songbirds",
        "common_human_made_sounds": ["Occasional horseback rider on trail"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["White Oak", "Sugar Maple", "Sandstone Cedar", "Maidenhair Fern"],
        "common_animals": ["White-tailed Deer", "Wild Turkey", "Pileated Woodpecker", "Bobcat"]
      },
      "human_demographics_and_culture": "Equestrian trail riders, wilderness backpackers, nature photographers.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Native American bluff shelters throughout Pope County contain ancient rock art and sacred spiritual history.",
        "energetic_and_spiritual_features": "Peaceful oak-hickory forest bluffs, dramatic sandstone canyon energy."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Lusk Creek Canyon Loop Trail",
          "length_miles": 6.8,
          "difficulty": "Moderate",
          "features": "Indian Kitchen sandstone overlook, pristine creek canyon"
        }
      ],
      "public_reviews_summary": "Gorgeous wilderness canyon backpacking in Southern Illinois. Free primitive camping, quiet nature, easy drive to Harrisburg.",
      "other_data": "Shawnee National Forest wilderness area. No motorized vehicles permitted inside boundary.",
      "last_updated": "2026-09-12"
    }
  ],
  "indiana.json": [
    {
      "id": "in-tower-ridge-road-hoosier-nf",
      "name": "Tower Ridge Road Dispersed Campsites",
      "state": "Indiana",
      "county": "Monroe / Jackson County",
      "coordinates": { "latitude": 39.0215, "longitude": -86.3654, "elevation_ft": 820 },
      "management_agency": {
        "name": "US Forest Service - Hoosier National Forest (Brownstown Ranger District)",
        "type": "USFS",
        "phone": "(812) 275-5941",
        "website": "https://www.fs.usda.gov/hoosier"
      },
      "rules_and_regulations": {
        "cost": "100% Free - Hoosier National Forest Dispersed Camping (zero fee)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed camping at designated pullout sites along Tower Ridge Road. Camp 125ft minimum from roads and trails."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6-8 inches deep in soil 200 feet from drainage ravines. Pack out hygiene items.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down wood gathering permitted on forest lands.",
        "safety_requirements": "Campfires permitted in existing rock rings. Extinguish with water until cold to touch.",
        "seasonal_fire_bans": "Fall dry leaf fire warnings."
      },
      "access_and_road_conditions": {
        "road_type": "Gravel Forest Road (Tower Ridge Road / FR 15)",
        "road_conditions": "Smooth graded gravel, easy driving for all vehicles.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance passenger cars, vans, and small rigs.",
        "scores": { "road_grade": 2, "road_terrain_difficulty": 2, "supply_run_pain": 4 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / High Ridge Line",
        "verizon_reliability": "3-4 bars 4G LTE (15-30 Mbps download)",
        "att_reliability": "3-4 bars 4G LTE",
        "tmobile_reliability": "2-3 bars 4G LTE",
        "terrain_obstruction_risk": "Low along ridge line top road",
        "distance_from_tower_corridor_miles": 3.0,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Flat Grassy Vehicle Pullouts",
        "Stone Fire Rings",
        "Hardwood Forest Canopy",
        "Deam Wilderness Trailhead Access"
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
          "town_name": "Bedford, IN",
          "distance_miles": 16.0,
          "services_available": ["Walmart Supercenter", "Gas Stations", "Lawrence County Library", "Gyms", "Restaurants"]
        },
        {
          "town_name": "Bloomington, IN",
          "distance_miles": 22.0,
          "services_available": ["Kroger / Fresh Thyme", "Indiana University Metro", "Full Hospitals", "Planet Fitness"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "48-66°F, blooming redbuds and dogwoods, light rain.",
        "summer": "72-88°F, warm humid summer days under shaded hardwoods.",
        "fall": "50-70°F, crisp pleasant autumn foliage weather.",
        "winter": "22-40°F, dusting of snow, peaceful quiet woods."
      },
      "dangers_and_hazards": [
        "Falling dead ash tree limbs (examine overhead canopy before pitching tent)",
        "Ticks during summer months (use permethrin)"
      ],
      "acoustic_environment": {
        "quietness_rating": "8/10 - Forest songbirds and rustling leaves",
        "common_human_made_sounds": ["Occasional forest road vehicle passing"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Tulip Poplar (Indiana state tree)", "White Oak", "American Beech", "Mayapple"],
        "common_animals": ["White-tailed Deer", "Gray Squirrel", "Eastern Towhee", "Red Fox"]
      },
      "human_demographics_and_culture": "IU college backpackers, local hunters, nomad vanlifers, regional campers.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Hoosier National Forest hills hold rich pioneer history and local legends of hidden limestone caves and forest spirits.",
        "energetic_and_spiritual_features": "Gentle rolling ridge tranquility, historic woodland solitude."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Terrill Ridge / Deam Wilderness Trail",
          "length_miles": 5.2,
          "difficulty": "Easy to Moderate",
          "features": "Historic Terrill Cemetery, Monroe Lake scenic overlook"
        }
      ],
      "public_reviews_summary": "Top free spot near Bloomington and Monroe Lake. Easy gravel access, strong cell signal, flat parking pullouts.",
      "other_data": "Free Hoosier National Forest dispersed camping. No permit required.",
      "last_updated": "2026-09-12"
    }
  ],
  "michigan.json": [
    {
      "id": "mi-manistee-nf-nordhouse-dunes-wilderness",
      "name": "Nordhouse Dunes Wilderness Dispersed Primitive Camping",
      "state": "Michigan",
      "county": "Mason County",
      "coordinates": { "latitude": 44.0812, "longitude": -86.4412, "elevation_ft": 610 },
      "management_agency": {
        "name": "US Forest Service - Huron-Manistee National Forests (Manistee Ranger District)",
        "type": "USFS",
        "phone": "(231) 723-5511",
        "website": "https://www.fs.usda.gov/hmnf"
      },
      "rules_and_regulations": {
        "cost": "100% Free - USFS Wilderness Primitive Camping (zero fee for wilderness dispersed; nominal parking pass at trailhead or park on free forest road pullouts)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed wilderness camping permitted at least 400ft from Lake Michigan high water mark and 100ft from trails."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6-8 inches deep in forested dune soil 200ft from Lake Michigan and water channels. Pack out hygiene products.",
        "trash_policy": "Strict Leave No Trace wilderness rules."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down firewood collection permitted in forest zone.",
        "safety_requirements": "Campfires permitted using dead wood only. Keep fires small and bury completely with water and sand.",
        "seasonal_fire_bans": "Summer high dune wind fire advisories."
      },
      "access_and_road_conditions": {
        "road_type": "Paved county road to gravel/sand Forest Road (Nurnberg Road)",
        "road_conditions": "Washboard gravel and sand, easily drivable in summer.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance vehicles to Nurnberg Trailhead.",
        "scores": { "road_grade": 3, "road_terrain_difficulty": 4, "supply_run_pain": 4 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Moderate / Coastal Lake Signal",
        "verizon_reliability": "2-3 bars 4G LTE (10-25 Mbps download)",
        "att_reliability": "2-3 bars 4G LTE",
        "tmobile_reliability": "1-2 bars 4G LTE",
        "terrain_obstruction_risk": "Moderate (Sand dunes can block signal in low dune swales)",
        "distance_from_tower_corridor_miles": 4.5,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Freshwater Coastal Dune Wilderness",
        "Lake Michigan Sandy Beach Access",
        "Pristine Sunset Views",
        "Primitive Dune Campsites"
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
          "town_name": "Ludington, MI",
          "distance_miles": 14.0,
          "services_available": ["Meijer Supermarket", "Gas Stations", "Mason County District Library", "Laundromat", "Hospital", "Restaurants"]
        },
        {
          "town_name": "Manistee, MI",
          "distance_miles": 16.0,
          "services_available": ["Full City Services", "Hardware Stores", "Pharmacies", "Local Breweries"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "42-60°F, cool lake breezes, beach dunes thaw.",
        "summer": "70-84°F, prime Lake Michigan beach camping weather, warm clear water.",
        "fall": "48-65°F, stunning autumn colors on forested dunes, crisp clear air.",
        "winter": "18-32°F, heavy lake-effect snow, frozen coastal dune landscape."
      },
      "dangers_and_hazards": [
        "Poison ivy in dune swales",
        "Strong rip currents in Lake Michigan (swim with caution)",
        "Dehydrating dune sun exposure"
      ],
      "acoustic_environment": {
        "quietness_rating": "9/10 - Lake Michigan wave surf and forest breeze",
        "common_human_made_sounds": ["Distant freighter horn on Lake Michigan lakebed"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Pitcher's Thistle (threatened dune plant)", "Jack Pine", "Paper Birch", "Marram Grass", "Wild Blueberry"],
        "common_animals": ["Piping Plover", "Bald Eagle", "White-tailed Deer", "Porcupine", "Black Bear (rare)"]
      },
      "human_demographics_and_culture": "Wilderness backpackers, Great Lakes beach lovers, outdoor photographers, Michigan nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Anishinaabe / Odawa traditions revere Lake Michigan as a sacred inland sea with powerful water spirits (Mishipeshu).",
        "energetic_and_spiritual_features": "Expansive freshwater ocean horizons, majestic golden sunset energy."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Nordhouse Dunes Trail Loop",
          "length_miles": 6.2,
          "difficulty": "Moderate",
          "features": "Lake Michigan beach shore, high sand dunes, pine forest wilderness"
        }
      ],
      "public_reviews_summary": "Incredible freshwater beach wilderness camping in Michigan. Pitch a tent behind the sand dunes, watch Lake Michigan sunsets, and enjoy free wilderness access.",
      "other_data": "Huron-Manistee National Forest wilderness area.",
      "last_updated": "2026-09-12"
    }
  ],
  "minnesota.json": [
    {
      "id": "mn-superior-nf-dispersed-primitive",
      "name": "Superior National Forest Dispersed Primitive Camping",
      "state": "Minnesota",
      "county": "Cook / Lake County",
      "coordinates": { "latitude": 47.7812, "longitude": -90.6512, "elevation_ft": 1420 },
      "management_agency": {
        "name": "US Forest Service - Superior National Forest (Gunflint Ranger District)",
        "type": "USFS",
        "phone": "(218) 387-3200",
        "website": "https://www.fs.usda.gov/superior"
      },
      "rules_and_regulations": {
        "cost": "100% Free - USFS Dispersed Primitive Camping (zero fee outside Boundary Waters Canoe Area Wilderness)",
        "stay_limit": "14 consecutive days limit",
        "guidelines": "Dispersed camping at established forest road pullouts and rustic hunter sites throughout Superior National Forest outside BWCAW."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6-8 inches deep in glacial soil 200 feet from lakes and streams. Pack out all paper.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Abundant dead and down birch and pine wood gathering permitted.",
        "safety_requirements": "Campfires in established rock rings only. Soak completely with lake water before leaving.",
        "seasonal_fire_bans": "Spring/summer dry forest fire bans occasionally enforced."
      },
      "access_and_road_conditions": {
        "road_type": "Gravel / Dirt Forest Roads (FR 153 / Sawbill Trail pullouts)",
        "road_conditions": "Graded gravel, washboard sections, logging truck traffic.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance vehicles with care.",
        "scores": { "road_grade": 4, "road_terrain_difficulty": 4, "supply_run_pain": 5 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Fair / Tower Highway Line",
        "verizon_reliability": "2-3 bars 4G LTE near main county roads",
        "att_reliability": "2-3 bars 4G LTE",
        "tmobile_reliability": "1-2 bars 4G LTE",
        "terrain_obstruction_risk": "Moderate (Dense boreal forest pine canopy blocks signal in low spots)",
        "distance_from_tower_corridor_miles": 6.0,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Primitive Boreal Forest Campsites",
        "Glacial Lake Access",
        "Northern Lights (Aurora Borealis) Stargazing",
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
          "town_name": "Grand Marais, MN",
          "distance_miles": 18.0,
          "services_available": ["Cook County Whole Foods / Supermarket", "Gas Stations", "Public Library", "Outfitters", "Hospital"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "35-52°F, ice-out on lakes, crisp boreal air.",
        "summer": "65-78°F, warm sunny days, cool crisp lake nights.",
        "fall": "42-60°F, vibrant yellow birch foliage, autumn northern lights.",
        "winter": "-10 to 20°F, deep boreal snow, winter snowshoeing and dog sledding."
      },
      "dangers_and_hazards": [
        "Black bears (bear canister or bear hang mandatory for food)",
        "Biting black flies and mosquitoes in June/July",
        "Freezing cold water temperatures in lakes"
      ],
      "acoustic_environment": {
        "quietness_rating": "10/10 - Loon calls, wolf howls, and wind through white pines",
        "common_human_made_sounds": ["Occasional logging truck on distant forest road"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["White Pine", "Red Pine", "Paper Birch", "Balsam Fir", "Wild Blueberry"],
        "common_animals": ["Common Loon", "Moose", "Gray Wolf", "Black Bear", "Lynx", "Walleye"]
      },
      "human_demographics_and_culture": "Canoeists, North Shore wilderness lovers, anglers, winter woodsmen.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Ojibwe (Anishinaabe) ancestral lands rich with legends of Maymaygwaysiwuk (water spirits) and deep forest reverence.",
        "energetic_and_spiritual_features": "Hauntingly beautiful loon calls, pristine glacial lake stillness, dark sky aurora energy."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Superior Hiking Trail (SHT) - Oberg Mountain Loop",
          "length_miles": 4.5,
          "difficulty": "Moderate",
          "features": "Lake Superior views, boreal forest bluffs, autumn foliage"
        }
      ],
      "public_reviews_summary": "Serene Northwoods primitive camping in Superior National Forest. Free dispersed sites near Grand Marais with incredible loon calls and aurora night skies.",
      "other_data": "Free USFS dispersed land outside BWCAW boundary.",
      "last_updated": "2026-09-12"
    }
  ],
  "montana.json": [
    {
      "id": "mt-flathead-nf-hungry-horse-reservoir",
      "name": "Hungry Horse Reservoir Dispersed Primitive Camping",
      "state": "Montana",
      "county": "Flathead County",
      "coordinates": { "latitude": 48.3214, "longitude": -113.9654, "elevation_ft": 3580 },
      "management_agency": {
        "name": "US Forest Service - Flathead National Forest (Hungry Horse Ranger District)",
        "type": "USFS",
        "phone": "(406) 387-3800",
        "website": "https://www.fs.usda.gov/flathead"
      },
      "rules_and_regulations": {
        "cost": "100% Free - Flathead National Forest Dispersed Primitive Land (zero fee)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed camping at designated pullouts along West and East Reservoir Roads (FR 895 / FR 38). Food storage order in effect (grizzly bear country)."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6-8 inches deep in soil 200 feet from reservoir shoreline. Pack out all hygiene paper.",
        "trash_policy": "Strict Pack-In / Pack-Out. Zero trash left unattended (grizzly bear attractant)."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Abundant dead and down pine wood collection permitted.",
        "safety_requirements": "Campfires in established rock fire rings only. Fully douse with water until cold before vacating.",
        "seasonal_fire_bans": "Stage 1 and 2 fire restrictions common July-September."
      },
      "access_and_road_conditions": {
        "road_type": "Paved to gravel/dirt Forest Service Reservoir Road",
        "road_conditions": "Washboard gravel, potholed sections, dusty in summer.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance vehicles to main reservoir pullouts; 4x4 recommended for high spur roads.",
        "scores": { "road_grade": 4, "road_terrain_difficulty": 4, "supply_run_pain": 4 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Fair to Moderate / North End Signal",
        "verizon_reliability": "2-3 bars 4G LTE near dam / north reservoir road",
        "att_reliability": "2-3 bars 4G LTE",
        "tmobile_reliability": "1-2 bars 4G LTE",
        "terrain_obstruction_risk": "High further south down reservoir canyon",
        "distance_from_tower_corridor_miles": 6.5,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Reservoir Waterfront Primitive Campsites",
        "Mountain Glacier Overlooks",
        "Boat Launch Access",
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
          "town_name": "Hungry Horse / Columbia Falls, MT",
          "distance_miles": 10.0,
          "services_available": ["Supermarket", "Gas Stations", "Hardware Store", "Laundromat", "Public Library"]
        },
        {
          "town_name": "Kalispell, MT",
          "distance_miles": 24.0,
          "services_available": ["Costco / Target", "Logan Health Hospital", "24/7 Gyms", "Full Metro Services"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "40-55°F, snowmelt filling reservoir, crisp mountain weather.",
        "summer": "72-88°F, warm sunny days, refreshing mountain reservoir swimming.",
        "fall": "45-65°F, golden larch (tamarack) needle color change, cool nights.",
        "winter": "15-30°F, heavy snowpack, road closed to wheeled vehicles past dam."
      },
      "dangers_and_hazards": [
        "Grizzly and black bears present (certified bear canister or bear hang required)",
        "Cold mountain reservoir water temperatures",
        "Falling rock on reservoir roads"
      ],
      "acoustic_environment": {
        "quietness_rating": "9/10 - Mountain wind and reservoir water lapping",
        "common_human_made_sounds": ["Distant motorboat on reservoir in summer", "Infrequent forest road truck"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Western Larch (Tamarack)", "Douglas Fir", "Lodgepole Pine", "Huckleberry"],
        "common_animals": ["Grizzly Bear", "Black Bear", "Elk", "Osprey", "Bull Trout", "Bald Eagle"]
      },
      "human_demographics_and_culture": "Glacier National Park visitors, Montana boaters, huckleberry pickers, wilderness campers.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Traditional lands of the Blackfeet, Salish, and Kootenai tribes. The surrounding Swan Peak wilderness holds deep reverence.",
        "energetic_and_spiritual_features": "Majestic Rocky Mountain reflection views, serene turquoise reservoir waters."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Columbia Mountain Trail",
          "length_miles": 11.5,
          "difficulty": "Strenuous",
          "features": "Sweeping Flathead Valley and Glacier Park vistas"
        }
      ],
      "public_reviews_summary": "Top free camping spot right outside Glacier National Park. Gorgeous reservoir views, solid cell service near dam end, and free USFS access.",
      "other_data": "Flathead National Forest. Strict Forest Service food storage order enforced for bears.",
      "last_updated": "2026-09-12"
    }
  ],
  "nevada.json": [
    {
      "id": "nv-ruby-mountains-humboldt-toiyabe-nf",
      "name": "Lamoille Canyon / Ruby Mountains Dispersed Primitive Camping",
      "state": "Nevada",
      "county": "Elko County",
      "coordinates": { "latitude": 40.6812, "longitude": -115.4712, "elevation_ft": 6400 },
      "management_agency": {
        "name": "US Forest Service - Humboldt-Toiyabe National Forest (Mountain City-Ruby Mountains-Jarbidge Ranger District)",
        "type": "USFS",
        "phone": "(775) 752-3357",
        "website": "https://www.fs.usda.gov/htnf"
      },
      "rules_and_regulations": {
        "cost": "100% Free - Humboldt-Toiyabe NF Dispersed Primitive Land (zero fee)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed camping at pullouts along Lamoille Canyon Road and lower canyon dirt spurs. Camp 100ft minimum from Lamoille Creek."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6-8 inches deep in soil 200 feet from Lamoille Creek. Pack out all hygiene items.",
        "trash_policy": "Strict Leave No Trace."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down wood gathering permitted.",
        "safety_requirements": "Campfires in established rock fire rings only. Fully extinguish with water.",
        "seasonal_fire_bans": "Summer desert mountain fire bans active July-September."
      },
      "access_and_road_conditions": {
        "road_type": "Paved Scenic Byway (Lamoille Canyon Road) to dirt pullouts",
        "road_conditions": "Paved scenic main road, smooth gravel pullouts.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance vehicles.",
        "scores": { "road_grade": 2, "road_terrain_difficulty": 2, "supply_run_pain": 4 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Moderate / Canyon Mouth Line",
        "verizon_reliability": "3-4 bars 4G LTE at canyon mouth; 1-2 bars up canyon",
        "att_reliability": "3-4 bars 4G LTE",
        "tmobile_reliability": "2-3 bars 4G LTE",
        "terrain_obstruction_risk": "Moderate (Glacial alpine canyon walls reduce signal further up valley)",
        "distance_from_tower_corridor_miles": 4.0,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Alpine Stream Primitive Campsites",
        "Glacial Cirque Valley Views ('Alps of Nevada')",
        "Lamoille Creek Water Source (Filter mandatory)",
        "Paved Scenic Access"
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
          "town_name": "Elko, NV",
          "distance_miles": 20.0,
          "services_available": ["Walmart Supercenter", "Gas Stations", "Elko County Library", "Hospitals", "Gyms", "Restaurants"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "42-60°F, rushing snowmelt cascades, green alpine meadows.",
        "summer": "75-88°F, pleasant high mountain escape from Nevada desert heat.",
        "fall": "48-68°F, world-class golden quaking aspen foliage.",
        "winter": "15-35°F, heavy alpine snowpack, road snowplowed to power plant."
      },
      "dangers_and_hazards": [
        "High elevation altitude sickness risk (up to 8,800ft at road end)",
        "Sudden summer alpine thunderstorms",
        "High mountain summer UV exposure"
      ],
      "acoustic_environment": {
        "quietness_rating": "9/10 - Alpine stream cascades and mountain wind",
        "common_human_made_sounds": ["Occasional scenic drive vehicle on main road"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Quaking Aspen", "Limber Pine", "Mountain Mahogany", "Alpine Wildflowers"],
        "common_animals": ["Himalayan Snowcock", "Mountain Goat", "Bighorn Sheep", "Mule Deer", "Beaver"]
      },
      "human_demographics_and_culture": "Nevada ranchers, alpine hikers, fly anglers, outdoor nomads, winter backcountry skiers.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Western Shoshone ancestral mountains (Newe Sogobia). The Ruby Mountains are held in deep sacred honor for their life-giving waters.",
        "energetic_and_spiritual_features": "Breathtaking glacial alpine energy, towering granite peaks, golden aspen serenity."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Lamoille Canyon to Island Lake Trail",
          "length_miles": 3.6,
          "difficulty": "Moderate",
          "features": "Glacial alpine lake, towering granite cirque bluffs, wildflower basins"
        }
      ],
      "public_reviews_summary": "The 'Alps of Nevada'. Stunning free primitive camping in Lamoille Canyon with smooth paved access, great cell coverage near Elko, and unbelievable alpine views.",
      "other_data": "Humboldt-Toiyabe National Forest. Free dispersed camping.",
      "last_updated": "2026-09-12"
    }
  ],
  "new_mexico.json": [
    {
      "id": "nm-gila-nf-middle-fork-primitive",
      "name": "Gila National Forest / Gila Wilderness Dispersed Camping",
      "state": "New Mexico",
      "county": "Catron / Grant County",
      "coordinates": { "latitude": 33.2214, "longitude": -108.2412, "elevation_ft": 5800 },
      "management_agency": {
        "name": "US Forest Service - Gila National Forest (Wilderness Ranger District)",
        "type": "USFS",
        "phone": "(575) 536-2250",
        "website": "https://www.fs.usda.gov/gila"
      },
      "rules_and_regulations": {
        "cost": "100% Free - Gila National Forest Primitive Dispersed Land (zero fee)",
        "stay_limit": "14 consecutive days limit",
        "guidelines": "Dispersed primitive camping along Forest Road 150 (North Wall) and Gila River access pullouts. Leave No Trace."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6-8 inches deep in soil 200 feet from Gila River and natural springs. Pack out hygiene products.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Abundant dead and down pine and oak firewood gathering permitted.",
        "safety_requirements": "Campfires in established stone rings. Douse thoroughly with water before leaving.",
        "seasonal_fire_bans": "Spring dry windy season fire restrictions common May-June."
      },
      "access_and_road_conditions": {
        "road_type": "Paved NM 15 to unpaved Forest Road gravel/dirt",
        "road_conditions": "Winding mountain pavement, rough gravel dirt roads.",
        "vehicle_recommendation": "High clearance recommended for Forest Road 150; standard 2WD can reach pavement pullouts near Gila Cliff Dwellings.",
        "scores": { "road_grade": 5, "road_terrain_difficulty": 5, "supply_run_pain": 6 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Low to Moderate / Mountain Ridge Dependent",
        "verizon_reliability": "1-2 bars 4G LTE near high highway passes; SOS in deep canyons",
        "att_reliability": "1-2 bars 4G LTE",
        "tmobile_reliability": "No Service in deep canyon",
        "terrain_obstruction_risk": "High (Deep volcanic canyon walls block signals)",
        "distance_from_tower_corridor_miles": 12.0,
        "cellular_internet_dependable": False
      },
      "amenities": [
        "Primitive Canyon Campsites",
        "Nearby Natural Thermal Hot Springs (Lightfeather / Jordan Hot Springs access)",
        "Gila River Access",
        "Ponderosa Pine Forest Shade"
      ],
      "location_scores": {
        "distance_to_groceries_score": 4,
        "distance_to_library_score": 4,
        "distance_to_gym_score": 3,
        "terrain_score": 10,
        "quietness_score": 10
      },
      "nearest_supply_towns": [
        {
          "town_name": "Silver City, NM",
          "distance_miles": 38.0,
          "services_available": ["Food Coop / Supermarkets", "Gas Stations", "Western New Mexico University Library", "Hospital", "Restaurants"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "50-70°F, windy afternoon high mountain breeze, river snowmelt runoff.",
        "summer": "75-88°F, monsoon rain showers in July/August bringing lush green growth.",
        "fall": "55-72°F, sunny crisp days, ideal backpacking weather.",
        "winter": "25-48°F, freezing night temps, dusting of snow in high wilderness peaks."
      },
      "dangers_and_hazards": [
        "Summer afternoon monsoon flash floods in canyon drainages",
        "Narrow winding mountain roads",
        "Black bears and mountain lions (store food securely)"
      ],
      "acoustic_environment": {
        "quietness_rating": "10/10 - Absolute wilderness canyon silence and river breeze",
        "common_human_made_sounds": ["None in wilderness boundary"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Ponderosa Pine", "Alligator Juniper", "Piñon Pine", "Narrowleaf Cottonwood"],
        "common_animals": ["Gila Monster", "Elk", "Mule Deer", "Javelina", "Coati", "Mexican Gray Wolf (rare)"]
      },
      "human_demographics_and_culture": "Chiricahua Apache homeland, Aldo Leopold conservation heritage, desert mountain nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "First Wilderness area in the world designated by Aldo Leopold in 1924. Rich Mogollon Native American archaeological history.",
        "energetic_and_spiritual_features": "Profound high desert wilderness silence, natural hot spring healing energy."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Middle Fork Gila River Trail to Jordan Hot Springs",
          "length_miles": 12.0,
          "difficulty": "Strenuous",
          "features": "Multiple river crossings, towering volcanic canyon walls, thermal soak pools"
        }
      ],
      "public_reviews_summary": "World-class wilderness camping in New Mexico's Gila National Forest. Natural hot springs, majestic ponderosa forests, and complete off-grid solitude.",
      "other_data": "Free Gila National Forest dispersed land. Bring water filter and satellite communicator.",
      "last_updated": "2026-09-12"
    }
  ],
  "north_carolina.json": [
    {
      "id": "nc-pisgah-nf-linville-gorge-wilderness",
      "name": "Linville Gorge Wilderness Dispersed Primitive Camping",
      "state": "North Carolina",
      "county": "Burke County",
      "coordinates": { "latitude": 35.8812, "longitude": -81.8912, "elevation_ft": 3200 },
      "management_agency": {
        "name": "US Forest Service - Pisgah National Forest (Grandfather Ranger District)",
        "type": "USFS",
        "phone": "(828) 652-2144",
        "website": "https://www.fs.usda.gov/nfsnc"
      },
      "rules_and_regulations": {
        "cost": "100% Free - Dispersed Wilderness Primitive Camping (zero cost; free USFS permit required for weekend camping May 1 - Oct 31)",
        "stay_limit": "3 consecutive nights limit in gorge area",
        "guidelines": "Dispersed camping at designated primitive sites along Old NC 105 (Kistler Memorial Highway) and gorge rim. Camp 130ft minimum from water."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6-8 inches deep in organic soil 200 feet from Linville River and springs. Pack out hygiene products.",
        "trash_policy": "Strict Leave No Trace wilderness policy."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down wood gathering permitted on forest land.",
        "safety_requirements": "Campfires in small rock fire rings only. Fully douse with water before vacating.",
        "seasonal_fire_bans": "Fall dry leaf fire warnings enforced."
      },
      "access_and_road_conditions": {
        "road_type": "Unpaved Dirt Mountain Ridge Road (Old NC 105)",
        "road_conditions": "Rough dirt, deep ruts, exposed bedrock, narrow blind curves.",
        "vehicle_recommendation": "High clearance recommended; careful standard 2WD cars can reach northern rim pullouts in dry weather.",
        "scores": { "road_grade": 7, "road_terrain_difficulty": 7, "supply_run_pain": 5 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Moderate / High Rim Line Signal",
        "verizon_reliability": "3-4 bars 4G LTE along Old NC 105 high rim pullouts",
        "att_reliability": "3-4 bars 4G LTE",
        "tmobile_reliability": "2-3 bars 4G LTE",
        "terrain_obstruction_risk": "High inside deep river gorge; low on high gorge rim",
        "distance_from_tower_corridor_miles": 4.5,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Spectacular Gorge Rim Overlook Campsites",
        "Table Rock & Shortoff Mountain Views",
        "Linville River Access (Strenuous Hike)",
        "Stone Fire Rings"
      ],
      "location_scores": {
        "distance_to_groceries_score": 5,
        "distance_to_library_score": 5,
        "distance_to_gym_score": 4,
        "terrain_score": 10,
        "quietness_score": 9
      },
      "nearest_supply_towns": [
        {
          "town_name": "Morganton, NC",
          "distance_miles": 18.0,
          "services_available": ["Food Lion / Publix", "Gas Stations", "Burke County Public Library", "Hospital", "Restaurants"]
        },
        {
          "town_name": "Marion, NC",
          "distance_miles": 20.0,
          "services_available": ["Walmart Supercenter", "Laundromat", "Hardware Stores", "Pharmacies"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "50-68°F, blooming mountain laurel and rhododendron.",
        "summer": "72-85°F, pleasant high mountain breezes compared to humid lowlands.",
        "fall": "48-68°F, world-renowned Blue Ridge fall foliage colors.",
        "winter": "25-45°F, freezing rim winds, ice formation on gorge cliffs."
      },
      "dangers_and_hazards": [
        "Sheer 1,000ft canyon cliff drop-offs",
        "Rough Old NC 105 dirt road conditions",
        "Timber rattlesnakes and copperheads in rocky outcrops"
      ],
      "acoustic_environment": {
        "quietness_rating": "9/10 - Gorge wind and roaring river far below",
        "common_human_made_sounds": ["Occasional 4x4 engine on Old NC 105"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Catawba Rhododendron", "Mountain Laurel", "Table Mountain Pine", "Carolina Hemlock"],
        "common_animals": ["Peregrine Falcon", "Black Bear", "White-tailed Deer", "Timber Rattlesnake"]
      },
      "human_demographics_and_culture": "Cherokee ancestral lands, rock climbers, Blue Ridge hikers, wilderness nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Known as the 'Grand Canyon of the East'. Famous local folklore of the mysterious Brown Mountain Lights visible from gorge overlooks.",
        "energetic_and_spiritual_features": "Electric high mountain rim energy, breathtaking sunrise vistas over Table Rock."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Shortoff Mountain / Linville Gorge Trail",
          "length_miles": 7.4,
          "difficulty": "Strenuous",
          "features": "360-degree Blue Ridge views, cliffside gorges, wildflower mountain balds"
        }
      ],
      "public_reviews_summary": "Unrivaled gorge overlook primitive camping in North Carolina. Fast cell connectivity along the high rim, majestic sunset vistas, and free access.",
      "other_data": "Pisgah National Forest. Free permit required for summer weekend overnight stays.",
      "last_updated": "2026-09-12"
    }
  ],
  "oregon.json": [
    {
      "id": "or-deschutes-nf-three-sisters-wilderness",
      "name": "Three Sisters Wilderness Dispersed Primitive Camping",
      "state": "Oregon",
      "county": "Deschutes County",
      "coordinates": { "latitude": 44.0214, "longitude": -121.6512, "elevation_ft": 4850 },
      "management_agency": {
        "name": "US Forest Service - Deschutes National Forest (Bend-Fort Rock Ranger District)",
        "type": "USFS",
        "phone": "(541) 383-5300",
        "website": "https://www.fs.usda.gov/deschutes"
      },
      "rules_and_regulations": {
        "cost": "100% Free - USFS Dispersed Primitive Camping (zero cost; free wilderness permit self-issue at trailhead outside peak day-use permit zones)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed primitive camping at established forest road sites along Cascade Lakes Highway corridors and Forest Road 46. Camp 100ft from lakes."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6-8 inches deep in soil 200 feet from volcanic lakes and streams. Pack out hygiene items.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down pine wood gathering permitted.",
        "safety_requirements": "Campfires in established rock fire rings only. Fully extinguish with water.",
        "seasonal_fire_bans": "Strict summer wildfire bans enforced July through September."
      },
      "access_and_road_conditions": {
        "road_type": "Paved Cascade Lakes Scenic Byway to dirt/gravel Forest Roads",
        "road_conditions": "Paved main highway, smooth gravel forest spur pullouts.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance vehicles.",
        "scores": { "road_grade": 2, "road_terrain_difficulty": 3, "supply_run_pain": 3 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Good to Strong / Highway Tower Line",
        "verizon_reliability": "3-4 bars 4G LTE (20-45 Mbps download)",
        "att_reliability": "3-4 bars 4G LTE",
        "tmobile_reliability": "2-3 bars 4G LTE",
        "terrain_obstruction_risk": "Low to Moderate on open lava pine flats",
        "distance_from_tower_corridor_miles": 3.0,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Snowcapped Volcanic Peak Views (South Sister / Broken Top)",
        "Ponderosa Pine & Lodgepole Shade",
        "Clear Volcanic Stream Access",
        "Flat Gravel Van Parking Pullouts"
      ],
      "location_scores": {
        "distance_to_groceries_score": 7,
        "distance_to_library_score": 7,
        "distance_to_gym_score": 6,
        "terrain_score": 10,
        "quietness_score": 9
      },
      "nearest_supply_towns": [
        {
          "town_name": "Bend, OR",
          "distance_miles": 18.0,
          "services_available": ["Trader Joe's / Safeway", "REI / Outdoor Gear", "Deschutes County Library", "St. Charles Hospital", "24/7 Gyms"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "40-55°F, snow melt on mountain roads, crisp sunny Central Oregon air.",
        "summer": "72-86°F, warm sunny dry mountain weather, clear blue skies.",
        "fall": "48-68°F, golden aspen colors, crisp chilly starry nights.",
        "winter": "15-32°F, heavy Cascade mountain snowpack, snowshoe and cross-country ski season."
      },
      "dangers_and_hazards": [
        "Summer wildfire smoke risks",
        "Volcanic rock tripping hazards",
        "Mosquitoes around snowmelt lakes in June/July"
      ],
      "acoustic_environment": {
        "quietness_rating": "9/10 - Mountain wind through lodgepole pines",
        "common_human_made_sounds": ["Distant vehicle on Cascade Lakes Byway"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Ponderosa Pine", "Lodgepole Pine", "Manzanita", "Bitterbrush", "Wild Huckleberry"],
        "common_animals": ["Osprey", "Cascades Frog", "Mule Deer", "Black Bear", "Golden-mantled Ground Squirrel"]
      },
      "human_demographics_and_culture": "Bend outdoor athletes, trail runners, paddleboarders, vanlife digital nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Warm Springs and Paiute ancestral lands honoring the sacred Cascade volcanic peaks as majestic guardians.",
        "energetic_and_spiritual_features": "Revitalizing high desert mountain energy, crystalline volcanic lake clarity."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Green Lakes Trail",
          "length_miles": 9.1,
          "difficulty": "Moderate",
          "features": "Obsidian lava flows, rushing mountain waterfalls, South Sister views"
        }
      ],
      "public_reviews_summary": "Top nomad boondocking spot outside Bend, Oregon. Excellent cell internet, flat pine campsites, and quick access to Bend's cafes and gyms.",
      "other_data": "Deschutes National Forest. Free dispersed camping.",
      "last_updated": "2026-09-12"
    }
  ],
  "texas.json": [
    {
      "id": "tx-sam-houston-nf-lone-star-trail",
      "name": "Sam Houston National Forest Dispersed Primitive Camping",
      "state": "Texas",
      "county": "Walker / Montgomery County",
      "coordinates": { "latitude": 30.5214, "longitude": -95.6312, "elevation_ft": 310 },
      "management_agency": {
        "name": "US Forest Service - National Forests and Grasslands in Texas (Sam Houston District)",
        "type": "USFS",
        "phone": "(936) 344-6205",
        "website": "https://www.fs.usda.gov/texas"
      },
      "rules_and_regulations": {
        "cost": "100% Free - USFS Dispersed Primitive Camping (zero fee outside designated fee campgrounds)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed camping permitted throughout Sam Houston National Forest along Lone Star Hiking Trail corridor and forest roads outside deer hunting season."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6 inches deep in soil 200 feet from streams and Lake Conroe drainages. Pack out all paper.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down wood gathering permitted on forest lands.",
        "safety_requirements": "Campfires in established rock rings only. Extinguish fully with water.",
        "seasonal_fire_bans": "Summer East Texas burn bans common July-August."
      },
      "access_and_road_conditions": {
        "road_type": "Paved FM roads to gravel Forest Service roads (FR 208 / FR 213)",
        "road_conditions": "Graded gravel, red clay dirt spur pullouts.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance passenger cars.",
        "scores": { "road_grade": 2, "road_terrain_difficulty": 3, "supply_run_pain": 3 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / Near Metro Cell Towers",
        "verizon_reliability": "4-5 bars 4G/5G LTE (30-65 Mbps download)",
        "att_reliability": "4-5 bars 4G/5G LTE",
        "tmobile_reliability": "3-4 bars 4G/5G LTE",
        "terrain_obstruction_risk": "Low (Gentle piney woods topography)",
        "distance_from_tower_corridor_miles": 2.5,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Shaded Piney Woods Primitive Campsites",
        "Flat Dirt/Gravel RV & Van Pullouts",
        "Lone Star Hiking Trailhead Access",
        "Stone Fire Rings"
      ],
      "location_scores": {
        "distance_to_groceries_score": 8,
        "distance_to_library_score": 8,
        "distance_to_gym_score": 7,
        "terrain_score": 6,
        "quietness_score": 8
      },
      "nearest_supply_towns": [
        {
          "town_name": "Huntsville, TX",
          "distance_miles": 12.0,
          "services_available": ["H-E-B Supermarket", "Target / Walmart", "Sam Houston State Univ Library", "Hospital", "24/7 Gyms"]
        },
        {
          "town_name": "Conroe / Willis, TX",
          "distance_miles": 16.0,
          "services_available": ["Full Houston Metro Services", "Hardware Stores", "Restaurants", "Laundromats"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "62-78°F, blooming wild azaleas, pleasant warm weather.",
        "summer": "85-96°F, hot humid East Texas piney woods summer.",
        "fall": "60-78°F, prime mild camping weather, warm days and cool nights.",
        "winter": "42-62°F, mild short winters, occasional light rain."
      },
      "dangers_and_hazards": [
        "Feral hogs in forested creek bottoms",
        "Copperhead and cottonmouth snakes near water",
        "High summer heat and humidity"
      ],
      "acoustic_environment": {
        "quietness_rating": "8/10 - Pine forest wind and cicadas",
        "common_human_made_sounds": ["Distant highway traffic on I-45 corridor"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Loblolly Pine", "Shortleaf Pine", "Post Oak", "Yaupon Holly", "Spanish Moss"],
        "common_animals": ["White-tailed Deer", "Red-cockaded Woodpecker (endangered)", "Feral Hog", "Armadillo", "Broad-headed Skink"]
      },
      "human_demographics_and_culture": "East Texas piney woods locals, SHSU college students, Houston nomads, long-distance backpackers.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Traditional lands of the Atakapa-Ishak and Caddo nations. Rich frontier lore of Sam Houston and Texas independence.",
        "energetic_and_spiritual_features": "Soothing pine needle forest floor, gentle warm breeze tranquility."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Lone Star Hiking Trail (Section 4)",
          "length_miles": 8.5,
          "difficulty": "Easy to Moderate",
          "features": "Piney woods canopy, creek bridge crossings, lush fern gulches"
        }
      ],
      "public_reviews_summary": "Best free nomad camping close to Houston. Lightning-fast 5G cell internet, flat pine campsites, and easy 15-minute drive to H-E-B and gyms in Huntsville.",
      "other_data": "National Forests in Texas. Free dispersed camping.",
      "last_updated": "2026-09-12"
    }
  ],
  "utah.json": [
    {
      "id": "ut-grand-staircase-escalante-blm-hole-in-the-rock",
      "name": "Hole-in-the-Rock Road BLM Dispersed Primitive Camping",
      "state": "Utah",
      "county": "Garfield County",
      "coordinates": { "latitude": 37.7214, "longitude": -111.5312, "elevation_ft": 5300 },
      "management_agency": {
        "name": "Bureau of Land Management (BLM) - Grand Staircase-Escalante National Monument",
        "type": "Federal BLM",
        "phone": "(435) 826-5400",
        "website": "https://www.blm.gov/grand-staircase-escalante"
      },
      "rules_and_regulations": {
        "cost": "100% Free - Free BLM Dispersed Camping Permit available at Escalante Interagency Visitor Center (zero cost)",
        "stay_limit": "14 consecutive days limit",
        "guidelines": "Dispersed camping at established pullouts along Hole-in-the-Rock Road (BLM 200). Must carry portable toilet system or WAG bags in slot canyon zones."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Portable toilet system or pack-out human waste (WAG bags) mandatory in Escalante canyon country. Digging cat-holes strictly prohibited in narrow desert wash areas.",
        "trash_policy": "Strict Pack-In / Pack-Out. Zero trash left in desert."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Must bring your own firewood. Gathering wood on Grand Staircase-Escalante BLM land is prohibited.",
        "safety_requirements": "Campfires must be contained in metal fire pan. Fully extinguish before leaving.",
        "seasonal_fire_bans": "Summer desert fire restrictions active June through August."
      },
      "access_and_road_conditions": {
        "road_type": "Unpaved Dirt / Washout Desert Road (Hole-in-the-Rock Road / BLM 200)",
        "road_conditions": "Severe washboard dirt, clay mud when wet, flash flood wash crossings.",
        "vehicle_recommendation": "High clearance 2WD or 4x4 recommended; careful standard 2WD cars can reach first 5 miles in dry conditions.",
        "scores": { "road_grade": 6, "road_terrain_difficulty": 6, "supply_run_pain": 5 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Fair near Highway 12 / Weak down road",
        "verizon_reliability": "2-3 bars 4G LTE near highway junction; SOS further down road",
        "att_reliability": "2-3 bars 4G LTE near junction",
        "tmobile_reliability": "1-2 bars 4G LTE",
        "terrain_obstruction_risk": "Moderate (Sandstone slickrock mesas block signals in deep washes)",
        "distance_from_tower_corridor_miles": 5.0,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Red Sandstone Slickrock Primitive Campsites",
        "Slot Canyon Trailhead Access (Peek-A-Boo / Spooky Slot access)",
        "Panoramic Desert Slickrock Views",
        "Dark Sky Stargazing"
      ],
      "location_scores": {
        "distance_to_groceries_score": 5,
        "distance_to_library_score": 5,
        "distance_to_gym_score": 3,
        "terrain_score": 10,
        "quietness_score": 10
      },
      "nearest_supply_towns": [
        {
          "town_name": "Escalante, UT",
          "distance_miles": 7.0,
          "services_available": ["Griffin's Grocery", "Gas Stations", "Escalante Public Library", "Outfitters", "Restaurants"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "55-72°F, prime desert hiking weather, clear sunny skies.",
        "summer": "88-102°F, intense desert heat, afternoon monsoon flash flood risk in slot canyons.",
        "fall": "60-78°F, golden autumn cottonwoods in Escalante river canyon, perfect desert temps.",
        "winter": "25-45°F, freezing desert nights, dustings of snow on red slickrock."
      },
      "dangers_and_hazards": [
        "Monsoon flash floods in slot canyons (check weather forecast at visitor center)",
        "Severe washboard road causing vehicle rattles and damage",
        "Dehydration in dry high desert heat"
      ],
      "acoustic_environment": {
        "quietness_rating": "10/10 - Pure canyon desert silence",
        "common_human_made_sounds": ["Occasional 4x4 passing on dirt road"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Utah Juniper", "Piñon Pine", "Slickrock Paintbrush", "Prickly Pear Cactus", "Fremont Cottonwood"],
        "common_animals": ["Desert Bighorn Sheep", "Raven", "Canyon Wren", "Collared Lizard", "Mule Deer"]
      },
      "human_demographics_and_culture": "Ancestral Puebloan & Fremont lands, slot canyon hikers, desert wanderers, vanlifers.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Grand Staircase slickrock features ancient Fremont rock art and sacred petroglyphs honoring water and desert spirits.",
        "energetic_and_spiritual_features": "Profound red rock desert mana, vast silent horizons, world-class dark night skies."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Peek-A-Boo and Spooky Slot Canyons Loop",
          "length_miles": 5.5,
          "difficulty": "Moderate to Strenuous",
          "features": "Narrow sandstone slot squeezes, arches, slickrock scrambles"
        }
      ],
      "public_reviews_summary": "Unbelievable red rock desert primitive camping outside Escalante. Epic slot canyon hiking, free BLM permit, and solid cell service near the highway entrance.",
      "other_data": "BLM Grand Staircase-Escalante National Monument. Free permit required.",
      "last_updated": "2026-09-12"
    }
  ],
  "virginia.json": [
    {
      "id": "va-george-washington-nf-reddish-knob",
      "name": "Reddish Knob / Flagpole Knob Dispersed Primitive Camping",
      "state": "Virginia",
      "county": "Rockingham / Augusta County",
      "coordinates": { "latitude": 38.4612, "longitude": -79.2412, "elevation_ft": 4350 },
      "management_agency": {
        "name": "US Forest Service - George Washington & Jefferson National Forests (North River Ranger District)",
        "type": "USFS",
        "phone": "(540) 432-0187",
        "website": "https://www.fs.usda.gov/gwj"
      },
      "rules_and_regulations": {
        "cost": "100% Free - GWNF Dispersed Primitive Land (zero fee)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed camping at primitive pullout sites along Briery Branch Road (FR 85) and Flagpole Knob ridge. Camp 100ft minimum from water."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6-8 inches deep in organic mountain soil 200 feet from streams. Pack out all hygiene items.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down wood gathering permitted.",
        "safety_requirements": "Campfires in established rock rings only. Extinguish completely before departing.",
        "seasonal_fire_bans": "Spring and autumn high wind fire restrictions."
      },
      "access_and_road_conditions": {
        "road_type": "Paved mountain road to unpaved dirt/gravel Forest Road (FR 85)",
        "road_conditions": "Winding paved ascent to narrow gravel ridge road with steep turnouts.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance vehicles to Reddish Knob summit pullouts; 4x4 required for Flagpole Knob rough trail.",
        "scores": { "road_grade": 6, "road_terrain_difficulty": 5, "supply_run_pain": 4 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / High Ridge Line Elevation",
        "verizon_reliability": "4-5 bars 4G/5G LTE (25-60 Mbps download)",
        "att_reliability": "4-5 bars 4G/5G LTE",
        "tmobile_reliability": "3-4 bars 4G LTE",
        "terrain_obstruction_risk": "Low along 4,350ft mountain ridge line",
        "distance_from_tower_corridor_miles": 4.0,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Panoramic 360-Degree Shenandoah & Allegheny Mountain Views",
        "High Altitude Summer Breeze",
        "Flat Ridge Vehicle Pullouts",
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
          "town_name": "Harrisonburg, VA",
          "distance_miles": 22.0,
          "services_available": ["Kroger / Martin's", "JMU Metro City", "Rockingham Memorial Hospital", "24/7 Gyms", "Restaurants"]
        },
        {
          "town_name": "Bridgewater / Dayton, VA",
          "distance_miles": 16.0,
          "services_available": ["Farmers Markets", "Gas Stations", "Pharmacies", "Hardware Stores"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "45-62°F, mountain laurel blooms, cool crisp breezes.",
        "summer": "68-80°F, cool high-elevation escape from humid Shenandoah Valley heat.",
        "fall": "45-65°F, world-class Shenandoah Valley autumn color vistas.",
        "winter": "18-35°F, severe freezing mountain winds, snow and ice on ridge roads."
      },
      "dangers_and_hazards": [
        "High cliff edges along Reddish Knob summit",
        "Sudden mountain fog and high wind squalls",
        "Black bears in surrounding George Washington NF"
      ],
      "acoustic_environment": {
        "quietness_rating": "9/10 - High mountain wind and songbird calls",
        "common_human_made_sounds": ["Occasional sightseer vehicle on Reddish Knob summit loop"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Red Spruce", "Mountain Ash", "Chestnut Oak", "Rhododendron", "Highbush Blueberry"],
        "common_animals": ["Black Bear", "Broad-winged Hawk", "White-tailed Deer", "Raven", "Shenandoah Salamander"]
      },
      "human_demographics_and_culture": "JMU students, Shenandoah Valley local outdoorsmen, 4x4 overland nomads, stargazers.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Monongahela and Shenandoah mountain traditions honor these high peaks as sacred lookout crests of the Blue Ridge.",
        "energetic_and_spiritual_features": "Exhilarating 4,300ft mountain ridge line energy, sweeping sunrise and sunset views over two states."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Shenandoah Mountain Crest Trail",
          "length_miles": 8.2,
          "difficulty": "Moderate to Strenuous",
          "features": "State line ridge walking, Virginia & West Virginia mountain panoramas"
        }
      ],
      "public_reviews_summary": "Spectacular 4,350ft summit ridge camping in Virginia. Fast 5G cell internet, cool summer mountain air, and unmatched 360-degree vistas.",
      "other_data": "George Washington National Forest. Free dispersed primitive camping.",
      "last_updated": "2026-09-12"
    }
  ],
  "washington.json": [
    {
      "id": "wa-olympic-nf-skokomish-river-road",
      "name": "South Fork Skokomish River Dispersed Primitive Camping",
      "state": "Washington",
      "county": "Mason County",
      "coordinates": { "latitude": 47.3812, "longitude": -123.3214, "elevation_ft": 750 },
      "management_agency": {
        "name": "US Forest Service - Olympic National Forest (Hood Canal Ranger District)",
        "type": "USFS",
        "phone": "(360) 765-2200",
        "website": "https://www.fs.usda.gov/olympic"
      },
      "rules_and_regulations": {
        "cost": "100% Free - USFS Dispersed Primitive Camping (zero fee)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed camping at designated pullouts along South Fork Skokomish River Road (FR 2353). Camp 100ft minimum from river."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6-8 inches deep in rich rainforest moss soil 200 feet from river. Pack out all hygiene items.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Abundant dead and down hemlock and cedar wood gathering permitted.",
        "safety_requirements": "Campfires in established rock fire rings only. Fully douse with water before vacating.",
        "seasonal_fire_bans": "Late summer Western Washington dry burn bans enforced."
      },
      "access_and_road_conditions": {
        "road_type": "Paved county road to paved/gravel Forest Service Road (FR 2353)",
        "road_conditions": "Paved main access to smooth gravel river pullouts.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance passenger cars.",
        "scores": { "road_grade": 2, "road_terrain_difficulty": 3, "supply_run_pain": 3 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Fair to Moderate / Hood Canal Corridor Signal",
        "verizon_reliability": "2-3 bars 4G LTE near main highway junction",
        "att_reliability": "2-3 bars 4G LTE",
        "tmobile_reliability": "1-2 bars 4G LTE",
        "terrain_obstruction_risk": "Moderate (Dense temperate rainforest canopy and river valley walls)",
        "distance_from_tower_corridor_miles": 5.5,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Pristine Rainforest Riverfront Campsites",
        "Old Growth Cedar & Douglas Fir Canopy",
        "Clear Turquoise Skokomish River Access",
        "Flat Dirt/Gravel Vehicle Pullouts"
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
          "town_name": "Shelton, WA",
          "distance_miles": 18.0,
          "services_available": ["Fred Meyer / Safeway", "Gas Stations", "Mason County Library", "Hospital", "Gyms", "Hardware Stores"]
        },
        {
          "town_name": "Hoodsport, WA",
          "distance_miles": 12.0,
          "services_available": ["Local Market", "Hood Canal Marina", "Gas Station", "Restaurants"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "48-62°F, lush green rainforest moss growth, misty showers.",
        "summer": "70-82°F, prime Olympic Peninsula summer weather, clear blue skies.",
        "fall": "50-65°F, salmon runs in river, golden bigleaf maple leaves.",
        "winter": "38-48°F, heavy rainforest precipitation, rare snow in lower river valley."
      },
      "dangers_and_hazards": [
        "Fast-moving river currents during spring rain runoff",
        "Falling dead cedar/hemlock tree limbs during windstorms",
        "Black bears in Olympic National Forest"
      ],
      "acoustic_environment": {
        "quietness_rating": "9/10 - Rushing river soundscape and forest rain drop taps",
        "common_human_made_sounds": ["Infrequent vehicle on forest road"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Western Red Cedar", "Douglas Fir", "Western Hemlock", "Sword Fern", "Moss-draped Bigleaf Maple"],
        "common_animals": ["Roosevelt Elk", "Chum & Coho Salmon", "Bald Eagle", "Black Bear", "Northern Spotted Owl"]
      },
      "human_demographics_and_culture": "Skokomish Tribal nation lands heritage, Pacific Northwest rainforest hikers, anglers, digital nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Ancestral territory of the Skokomish (Tuwaduq) people who honor the river as the sacred lifeblood of their salmon culture.",
        "energetic_and_spiritual_features": "Enchanting ancient rainforest energy, majestic emerald river pools, soothing mossy tranquility."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "South Fork Skokomish River Trail",
          "length_miles": 10.2,
          "difficulty": "Moderate",
          "features": "Old-growth rainforest trees, river gorge bridges, mossy fern flats"
        }
      ],
      "public_reviews_summary": "Magical Olympic Peninsula rainforest primitive camping. Crystal clear river water, ancient red cedars, and easy 2WD driving outside Shelton.",
      "other_data": "Olympic National Forest. Free dispersed primitive camping.",
      "last_updated": "2026-09-12"
    }
  ],
  "wyoming.json": [
    {
      "id": "wy-bridger-teton-nf-shadow-mountain",
      "name": "Shadow Mountain USFS / BLM Dispersed Primitive Camping",
      "state": "Wyoming",
      "county": "Teton County",
      "coordinates": { "latitude": 43.7012, "longitude": -110.6012, "elevation_ft": 7100 },
      "management_agency": {
        "name": "US Forest Service - Bridger-Teton National Forest (Jackson Ranger District)",
        "type": "USFS",
        "phone": "(307) 739-5500",
        "website": "https://www.fs.usda.gov/btnf"
      },
      "rules_and_regulations": {
        "cost": "100% Free - USFS / BLM Dispersed Primitive Camping (zero fee)",
        "stay_limit": "16 consecutive days stay limit",
        "guidelines": "Dispersed camping at designated pullout sites along Shadow Mountain Loop Road (FR 30340). Strict Forest Service food storage order in effect (grizzly & black bear zone)."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6-8 inches deep in soil 200 feet from natural springs and drainages. Pack out all toilet paper.",
        "trash_policy": "Strict Pack-In / Pack-Out. Mandatory bear safety disposal."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down pine firewood collection permitted.",
        "safety_requirements": "Campfires in established rock fire rings only. Fully douse with water until cold before leaving.",
        "seasonal_fire_bans": "Summer high wind dry mountain fire restrictions common July-August."
      },
      "access_and_road_conditions": {
        "road_type": "Unpaved Dirt / Gravel Mountain Loop Road (FR 30340)",
        "road_conditions": "Washboard dirt, steep switchbacks, deep ruts, muddy after rain.",
        "vehicle_recommendation": "High clearance recommended; standard 2WD vehicles can access lower sites near Antelope Flats Road in dry weather.",
        "scores": { "road_grade": 6, "road_terrain_difficulty": 6, "supply_run_pain": 4 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / Direct Line of Sight to Jackson Hole Towers",
        "verizon_reliability": "4-5 bars 4G/5G LTE (30-80 Mbps download)",
        "att_reliability": "4-5 bars 4G/5G LTE",
        "tmobile_reliability": "3-4 bars 4G LTE",
        "terrain_obstruction_risk": "Low (Unobstructed line of sight across Jackson Hole valley to Teton Range)",
        "distance_from_tower_corridor_miles": 4.5,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Unrivaled Iconic Grand Teton Range Panorama Views",
        "Lodgepole Pine Forest Shade",
        "Flat Dirt Vehicle Pullouts",
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
          "town_name": "Jackson, WY",
          "distance_miles": 16.0,
          "services_available": ["Albertsons / Jackson Whole Grocer", "Gas Stations", "Teton County Library", "St. John's Hospital", "24/7 Gyms", "REI"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "38-55°F, snow melt on mountain loop, crisp sunny mountain air.",
        "summer": "70-84°F, prime mountain camping weather, clear starry nights.",
        "fall": "42-65°F, golden aspen groves in Jackson Hole, crisp chilly nights.",
        "winter": "10-28°F, deep mountain snowpack, road closed to wheeled vehicles."
      },
      "dangers_and_hazards": [
        "Grizzly and black bear country (certified bear spray & bear canister mandatory)",
        "Steep dirt mountain road ruts when wet",
        "High elevation sun exposure (7,100+ ft)"
      ],
      "acoustic_environment": {
        "quietness_rating": "9/10 - High mountain breeze and elk bugles in autumn",
        "common_human_made_sounds": ["Occasional 4x4 vehicle on Shadow Mountain dirt loop"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Lodgepole Pine", "Quaking Aspen", "Sagebrush", "Indian Paintbrush (Wyoming state flower)"],
        "common_animals": ["Grizzly Bear", "Elk", "Bison", "Moose", "Mule Deer", "Bighorn Sheep"]
      },
      "human_demographics_and_culture": "Shoshone, Bannock, & Blackfeet ancestral lands, Grand Teton climbers, Jackson Hole digital nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "The Teton peaks (Teewinot - 'Many Pinnacles') carry profound Native American spiritual history as sacred spires of the Creator.",
        "energetic_and_spiritual_features": "Unrivaled awe-inspiring Teton peak reflections, expansive mountain valley energy, world-class sunsets."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Shadow Mountain Summit Trail",
          "length_miles": 4.5,
          "difficulty": "Moderate",
          "features": "Direct Grand Teton peak overlooks, wildflowers, lodgepole forest"
        }
      ],
      "public_reviews_summary": "The absolute single best free camping site in the United States. Direct front-row views of Grand Teton National Park, blazing 5G cell internet, and 100% free USFS access.",
      "other_data": "Bridger-Teton National Forest. Strict bear food storage order enforced.",
      "last_updated": "2026-09-12"
    }
  ]
}

for filename, sites in dataset_expansion.items():
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
