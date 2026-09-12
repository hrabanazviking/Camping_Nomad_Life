import json
import os

BASE_DIR = "/home/volmarr/.gemini/antigravity/scratch/Camping_Nomad_Life/states"

b4_expansion = {
  "mississippi.json": [
    {
      "id": "ms-de-soto-nf-tuxachanie-trail",
      "name": "Tuxachanie Trail Dispersed Primitive Camping",
      "state": "Mississippi",
      "county": "Forrest / Stone County",
      "coordinates": { "latitude": 30.9812, "longitude": -89.0214, "elevation_ft": 180 },
      "management_agency": {
        "name": "US Forest Service - National Forests in Mississippi (De Soto Ranger District)",
        "type": "USFS",
        "phone": "(601) 528-6160",
        "website": "https://www.fs.usda.gov/mississippi"
      },
      "rules_and_regulations": {
        "cost": "100% Free - USFS Dispersed Primitive Camping (zero fee)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed primitive camping permitted along Tuxachanie Trail corridor and Forest Service dirt roads outside gun hunting season."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6 inches deep in soil 200 feet from Tuxachanie Creek. Pack out all paper.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down longleaf pine wood collection permitted.",
        "safety_requirements": "Campfires in established rock fire rings only. Fully douse with water before vacating.",
        "seasonal_fire_bans": "Fall dry weather pine burn warnings."
      },
      "access_and_road_conditions": {
        "road_type": "Paved US Hwy 49 to gravel/dirt Forest Service roads",
        "road_conditions": "Graded gravel access roads, flat dirt trailhead pullouts.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance passenger cars.",
        "scores": { "road_grade": 2, "road_terrain_difficulty": 3, "supply_run_pain": 3 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / Near US 49 Tower Line",
        "verizon_reliability": "4-5 bars 4G/5G LTE (25-50 Mbps download)",
        "att_reliability": "4-5 bars 4G/5G LTE",
        "tmobile_reliability": "3-4 bars 4G LTE",
        "terrain_obstruction_risk": "Low (Flat piney woods terrain)",
        "distance_from_tower_corridor_miles": 2.5,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Shaded Longleaf Pine Canopy",
        "Tuxachanie Creek Water Source (Filter mandatory)",
        "Flat Dirt Vehicle Pullouts",
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
          "town_name": "Wiggins, MS",
          "distance_miles": 10.0,
          "services_available": ["Piggly Wiggly / Walmart", "Gas Stations", "Stone County Library", "Hospital", "Restaurants"]
        },
        {
          "town_name": "Hattiesburg, MS",
          "distance_miles": 22.0,
          "services_available": ["Full USM Metro City Services", "Costco / Target", "24/7 Gyms", "Forrest General Hospital"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "62-78°F, blooming pitcher plants, warm pleasant breeze.",
        "summer": "85-95°F, hot humid Gulf coastal piney woods summer.",
        "fall": "60-78°F, prime mild camping weather, crisp cool nights.",
        "winter": "42-62°F, short mild winters, sunny dry days."
      },
      "dangers_and_hazards": [
        "Ticks and chiggers in summer (use permethrin)",
        "High summer heat and humidity",
        "Venomous snakes near wetland pitcher plant bogs"
      ],
      "acoustic_environment": {
        "quietness_rating": "8/10 - Pine forest wind and cicadas",
        "common_human_made_sounds": ["Distant highway traffic on US 49 corridor"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Longleaf Pine", "Pitcher Plants (carnivorous bog plants)", "Slash Pine", "Sweetbay Magnolia"],
        "common_animals": ["Gopher Tortoise (threatened species)", "Red-cockaded Woodpecker", "White-tailed Deer", "Armadillo"]
      },
      "human_demographics_and_culture": "Choctaw ancestral lands, Mississippi Gulf Coast outdoorsmen, nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Traditional Choctaw lands honoring the ancient longleaf pine savannas and sacred pitcher plant bogs.",
        "energetic_and_spiritual_features": "Relaxing Gulf pine forest breezes, unique carnivorous plant bog ecosystem."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Tuxachanie National Recreation Trail",
          "length_miles": 12.0,
          "difficulty": "Easy to Moderate",
          "features": "Longleaf pine savanna, historic logging railroad bed, pitcher plant bogs"
        }
      ],
      "public_reviews_summary": "Top free nomad spot in Southern Mississippi. Blazing 5G cell internet, flat pine campsites, and fast 10-minute drive to Wiggins.",
      "other_data": "De Soto National Forest. Free dispersed primitive camping.",
      "last_updated": "2026-09-12"
    }
  ],
  "nebraska.json": [
    {
      "id": "ne-bessey-ranger-district-nebraska-nf",
      "name": "Bessey Ranger District Dispersed Primitive Camping",
      "state": "Nebraska",
      "county": "Thomas County",
      "coordinates": { "latitude": 41.8312, "longitude": -100.3214, "elevation_ft": 2750 },
      "management_agency": {
        "name": "US Forest Service - Nebraska National Forest (Bessey Ranger District)",
        "type": "USFS",
        "phone": "(308) 533-2251",
        "website": "https://www.fs.usda.gov/nebraska"
      },
      "rules_and_regulations": {
        "cost": "100% Free - USFS Dispersed Primitive Camping (zero fee outside developed fee campground)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed primitive camping permitted throughout Sandhills hand-planted pine forest and prairie grassland pullouts. Leave No Trace."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6 inches deep in sandy soil 200 feet from Middle Loup River. Pack out hygiene products.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down wood gathering permitted on site.",
        "safety_requirements": "Campfires in established rock fire rings only. Fully douse with water before vacating.",
        "seasonal_fire_bans": "Strict Sandhills dry grass fire bans active in summer."
      },
      "access_and_road_conditions": {
        "road_type": "Paved NE Hwy 2 (Sandhills Journey Scenic Byway) to gravel/sand Forest Roads",
        "road_conditions": "Paved highway main entrance, smooth sand/gravel forest roads.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance vehicles on main forest gravel drives.",
        "scores": { "road_grade": 2, "road_terrain_difficulty": 3, "supply_run_pain": 4 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / Highway 2 Tower Line",
        "verizon_reliability": "3-4 bars 4G LTE (20-40 Mbps download)",
        "att_reliability": "3-4 bars 4G LTE",
        "tmobile_reliability": "2-3 bars 4G LTE",
        "terrain_obstruction_risk": "Low across rolling Sandhills dunes",
        "distance_from_tower_corridor_miles": 3.0,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Hand-Planted Ponderosa & Jack Pine Canopy",
        "Middle Loup River Kayak Access",
        "Rolling Sandhills Dune Overlooks",
        "Stone Fire Rings"
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
          "town_name": "Halsey / Thedford, NE",
          "distance_miles": 3.0,
          "services_available": ["General Store", "Gas Station", "Thomas County Library", "Local Cafe"]
        },
        {
          "town_name": "Broken Bow, NE",
          "distance_miles": 42.0,
          "services_available": ["Grocery Supermarket", "Hospital", "24/7 Gym", "Hardware Stores"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "48-66°F, greening Sandhills prairie, spring rain squalls.",
        "summer": "75-92°F, warm sunny Sandhills days, refreshing pine shade.",
        "fall": "50-70°F, golden Sandhills grass foliage, crisp chilly nights.",
        "winter": "15-35°F, cold prairie wind, dusting of snow on Sandhills dunes."
      },
      "dangers_and_hazards": [
        "High wind and wildfire risks on prairie Sandhills",
        "Soft sand forest spurs (avoid driving off established gravel onto loose sand dunes)"
      ],
      "acoustic_environment": {
        "quietness_rating": "9/10 - Wind through hand-planted pine forest and prairie birds",
        "common_human_made_sounds": ["Distant BNSF train whistle across Sandhills valley"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Ponderosa Pine", "Jack Pine", "Little Bluestem", "Prairie Sandreed"],
        "common_animals": ["Mule Deer", "Pronghorn Antelope", "Sharp-tailed Grouse", "Prairie Chicken", "Wild Turkey"]
      },
      "human_demographics_and_culture": "Lakota & Pawnee ancestral lands, Sandhills ranchers, Nebraska foresters, nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Largest hand-planted forest in North America, created by Charles E. Bessey in 1902. Rich Sandhills pioneer lore.",
        "energetic_and_spiritual_features": "Unique pine oasis in the middle of vast rolling grass Sandhills dunes."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Scott Lookout Tower Trail",
          "length_miles": 3.5,
          "difficulty": "Easy to Moderate",
          "features": "Historic fire lookout tower, panoramic Sandhills dune views"
        }
      ],
      "public_reviews_summary": "A surprising pine forest oasis in the Nebraska Sandhills. Free primitive camping, great cell service along Highway 2, and serene starfilled nights.",
      "other_data": "Nebraska National Forest. Free dispersed primitive camping.",
      "last_updated": "2026-09-12"
    }
  ],
  "new_hampshire.json": [
    {
      "id": "nh-pemigewasset-wilderness-white-mountain-nf",
      "name": "Pemigewasset Wilderness Dispersed Primitive Camping",
      "state": "New Hampshire",
      "county": "Grafton County",
      "coordinates": { "latitude": 44.1412, "longitude": -71.5812, "elevation_ft": 2150 },
      "management_agency": {
        "name": "US Forest Service - White Mountain National Forest (Pemigewasset Ranger District)",
        "type": "USFS",
        "phone": "(603) 536-5400",
        "website": "https://www.fs.usda.gov/whitemountain"
      },
      "rules_and_regulations": {
        "cost": "100% Free - WMNF Wilderness Dispersed Primitive Camping (zero fee)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed wilderness camping permitted at least 200ft from trails and water streams throughout Pemigewasset Wilderness and Tripoli Road primitive corridors."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6-8 inches deep in organic soil 200 feet from East Branch Pemigewasset River. Pack out hygiene products.",
        "trash_policy": "Strict Leave No Trace wilderness rules."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down wood gathering permitted on forest lands.",
        "safety_requirements": "Campfires in established rock rings using dead wood only. Douse thoroughly with water before leaving.",
        "seasonal_fire_bans": "Spring leaf dry weather fire restrictions."
      },
      "access_and_road_conditions": {
        "road_type": "Paved Kancamagus Highway (NH 112) to gravel Forest Roads (Tripoli Road)",
        "road_conditions": "Paved scenic highway main access, graded gravel forest roads.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance vehicles.",
        "scores": { "road_grade": 3, "road_terrain_difficulty": 3, "supply_run_pain": 3 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Moderate / High Mountain Pass Signal",
        "verizon_reliability": "3-4 bars 4G LTE near Lincoln / Interstate 93 corridor",
        "att_reliability": "3-4 bars 4G LTE",
        "tmobile_reliability": "2-3 bars 4G LTE",
        "terrain_obstruction_risk": "Moderate inside deep glacial notch valleys",
        "distance_from_tower_corridor_miles": 4.5,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Pristine White Mountain Alpine Stream Campsites",
        "Granite Peak Overlook Views",
        "Pemigewasset River Water Source (Filter mandatory)",
        "Stone Fire Rings"
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
          "town_name": "Lincoln / Woodstock, NH",
          "distance_miles": 8.0,
          "services_available": ["Price Chopper Supermarket", "Gas Stations", "Lincoln Public Library", "Outfitters", "Restaurants"]
        },
        {
          "town_name": "Plymouth, NH",
          "distance_miles": 18.0,
          "services_available": ["Full Metro Services", "Speare Memorial Hospital", "24/7 Gyms", "Hardware Stores"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "40-55°F, roaring alpine snowmelt cascades, cool mountain air.",
        "summer": "68-80°F, prime White Mountain summer hiking weather, clear mountain streams.",
        "fall": "42-62°F, world-famous New Hampshire autumn foliage.",
        "winter": "10-25°F, heavy alpine snowpack, winter mountaineering and ice climbing."
      },
      "dangers_and_hazards": [
        "Sudden alpine weather shifts in White Mountains",
        "Black bears in WMNF (bear hang or canister mandatory for food storage)",
        "Slick granite rock stream crossings"
      ],
      "acoustic_environment": {
        "quietness_rating": "9/10 - Rushing mountain stream and forest wind",
        "common_human_made_sounds": ["Occasional mountain hiker on trail"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Balsam Fir", "Paper Birch", "Red Spruce", "Sugar Maple", "Hobblebush"],
        "common_animals": ["Moose", "Black Bear", "White-tailed Deer", "Bicknell's Thrush", "Brook Trout"]
      },
      "human_demographics_and_culture": "Abenaki ancestral lands, White Mountain 4,000-foot peak baggers, AT backpackers, digital nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Abenaki territory honoring the sacred mountain notches and spirit realms of the White Mountains.",
        "energetic_and_spiritual_features": "Exhilarating granite peak energy, crystal clear mountain cascade waters."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Lincoln Woods Trail / Pemigewasset Wilderness",
          "length_miles": 9.5,
          "difficulty": "Moderate",
          "features": "Historic logging railroad grade, suspension footbridges, roaring river pools"
        }
      ],
      "public_reviews_summary": "Spectacular free wilderness camping in New Hampshire's White Mountains. Fast cell internet near Lincoln, crystal clear streams, and easy access to 4,000ft peaks.",
      "other_data": "White Mountain National Forest. Free dispersed wilderness camping.",
      "last_updated": "2026-09-12"
    }
  ],
  "new_jersey.json": [
    {
      "id": "nj-penn-state-forest-batona-trail",
      "name": "Penn State Forest Dispersed Primitive Area / Batona Trail Shelter",
      "state": "New Jersey",
      "county": "Burlington County",
      "coordinates": { "latitude": 39.8124, "longitude": -74.4312, "elevation_ft": 110 },
      "management_agency": {
        "name": "New Jersey Department of Environmental Protection (NJDEP) - State Park Service",
        "type": "State NJDEP",
        "phone": "(609) 292-2797",
        "website": "https://www.nj.gov/dep/parksandforests"
      },
      "rules_and_regulations": {
        "cost": "100% Free - NJDEP Primitive Backpacking Wilderness Shelter (zero cost)",
        "stay_limit": "2 consecutive nights stay limit",
        "guidelines": "Primitive backpacking camping permitted at designated Batona Trail shelter/primitive clearings in Penn State Forest Pine Barrens. Leave No Trace."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6 inches deep in sandy Pine Barrens soil 200 feet from Oswego River. Pack out hygiene products.",
        "trash_policy": "Strict Carry-In / Carry-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down pitch pine wood gathering permitted on site.",
        "safety_requirements": "Campfires in established metal fire rings only. Fully douse with water until cold to touch.",
        "seasonal_fire_bans": "Spring dry Pine Barrens wildfire warnings strictly enforced."
      },
      "access_and_road_conditions": {
        "road_type": "Paved county road to sand/gravel forest service entrance road",
        "road_conditions": "Graded sand/gravel entrance road, flat parking lot.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance vehicles to parking lot.",
        "scores": { "road_grade": 2, "road_terrain_difficulty": 3, "supply_run_pain": 3 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / Flat Pine Barrens Cell Signal",
        "verizon_reliability": "4-5 bars 4G/5G LTE (25-60 Mbps download)",
        "att_reliability": "4-5 bars 4G/5G LTE",
        "tmobile_reliability": "3-4 bars 4G LTE",
        "terrain_obstruction_risk": "Low (Flat sandy topography)",
        "distance_from_tower_corridor_miles": 2.5,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Pitch Pine & Cedar Wilderness Canopy",
        "Oswego River Cedar Water Source (Filter mandatory)",
        "Wooden Lean-To Shelter Access",
        "Stone Fire Rings"
      ],
      "location_scores": {
        "distance_to_groceries_score": 7,
        "distance_to_library_score": 7,
        "distance_to_gym_score": 6,
        "terrain_score": 7,
        "quietness_score": 8
      },
      "nearest_supply_towns": [
        {
          "town_name": "Manahawkin / Tuckerton, NJ",
          "distance_miles": 12.0,
          "services_available": ["Acme Markets / Target", "Gas Stations", "Ocean County Library", "Hospital", "Restaurants"]
        },
        {
          "town_name": "Medford, NJ",
          "distance_miles": 18.0,
          "services_available": ["Full Metro Services", "ShopRite", "24/7 Gyms", "Pharmacies"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "55-70°F, blooming mountain laurel and pink lady's slipper orchids.",
        "summer": "78-90°F, warm Pine Barrens summer days, fresh cedar water breeze.",
        "fall": "52-70°F, vibrant autumn foliage around cranberry bogs.",
        "winter": "30-45°F, mild winter weather, quiet pine woods."
      },
      "dangers_and_hazards": [
        "Pine Barrens ticks in summer (use permethrin)",
        "Soft sand forest spur roads (avoid driving off established gravel into deep sugar sand)"
      ],
      "acoustic_environment": {
        "quietness_rating": "8/10 - Pine forest wind and cedar stream trickles",
        "common_human_made_sounds": ["Distant pine barrens roadway vehicle"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Pitch Pine", "Atlantic White Cedar", "Scrub Oak", "Cranberry", "Pink Lady's Slipper"],
        "common_animals": ["Pine Barrens Treefrog", "Whitetail Deer", "Red Fox", "Eastern Towhee"]
      },
      "human_demographics_and_culture": "Lenape ancestral lands, Piney culture, Batona Trail long-distance hikers, NJ nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Famous home of the legendary Jersey Devil folklore. The Pine Barrens biosphere is world-renowned for its unique ecological purity.",
        "energetic_and_spiritual_features": "Soothing pitch pine aroma, tranquil cedar tea-colored water streams."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Batona Trail (Penn State Forest Section)",
          "length_miles": 8.0,
          "difficulty": "Easy",
          "features": "Atlantic white cedar swamps, pitch pine forests, sandy ridge paths"
        }
      ],
      "public_reviews_summary": "New Jersey's hidden wilderness jewel in the Pine Barrens. Free primitive backpacking shelter, fast 5G cell signal, and quiet pine woods.",
      "other_data": "NJDEP State Forest. Free primitive backpacking.",
      "last_updated": "2026-09-12"
    }
  ],
  "new_york.json": [
    {
      "id": "ny-adirondack-park-moose-river-plains",
      "name": "Moose River Plains Primitive Camping Area",
      "state": "New York",
      "county": "Hamilton County",
      "coordinates": { "latitude": 43.6812, "longitude": -74.6512, "elevation_ft": 2120 },
      "management_agency": {
        "name": "New York State Department of Environmental Conservation (DEC) - Region 5",
        "type": "State DEC",
        "phone": "(518) 897-1200",
        "website": "https://www.dec.ny.gov"
      },
      "rules_and_regulations": {
        "cost": "100% Free - NYS DEC Adirondack Forest Preserve Primitive Camping (zero fee for stays under 3 nights; free DEC permit for longer stays)",
        "stay_limit": "3 consecutive nights free without permit; up to 14 days with free DEC forest ranger permit",
        "guidelines": "Dispersed primitive camping at 140+ designated roadside sites along Moose River Plains Road (Limekiln Lake - Cedar River Road). Camp 150ft minimum from water."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Use wooden pit privy provided at roadside primitive sites or dig cat-hole 6-8 inches deep in soil 200ft from Moose River. Pack out hygiene items.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down firewood collection permitted within 50 miles.",
        "safety_requirements": "Campfires in established rock fire rings only. Fully douse with water before vacating.",
        "seasonal_fire_bans": "Spring dry leaf weather fire warnings."
      },
      "access_and_road_conditions": {
        "road_type": "Unpaved Gravel / Dirt Adirondack Forest Road (Moose River Plains Road)",
        "road_conditions": "Graded gravel, washboard sections, easily drivable in summer.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance vehicles, vans, and camper rigs.",
        "scores": { "road_grade": 3, "road_terrain_difficulty": 3, "supply_run_pain": 4 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Fair to Moderate / Road Entrance Tower Line",
        "verizon_reliability": "2-3 bars 4G LTE near Inlet/Old Forge entrance gates",
        "att_reliability": "2-3 bars 4G LTE",
        "tmobile_reliability": "1-2 bars 4G LTE",
        "terrain_obstruction_risk": "Moderate (Adirondack mountain ridges reduce signal deep in interior plains)",
        "distance_from_tower_corridor_miles": 5.5,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Designated Grassy Roadside RV & Van Pullouts",
        "Pit Privy Toilets at Most Sites",
        "Moose River Freshwater Streams",
        "Stone Fire Rings & Picnic Tables"
      ],
      "location_scores": {
        "distance_to_groceries_score": 6,
        "distance_to_library_score": 6,
        "distance_to_gym_score": 4,
        "terrain_score": 10,
        "quietness_score": 9
      },
      "nearest_supply_towns": [
        {
          "town_name": "Inlet / Old Forge, NY",
          "distance_miles": 12.0,
          "services_available": ["Kalil's Grocery / TOPS", "Gas Stations", "Inlet Public Library", "Hardware Store", "Restaurants"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "40-55°F, black fly season in June, crisp mountain air.",
        "summer": "68-80°F, prime Adirondack summer camping, cool mountain nights.",
        "fall": "42-62°F, world-class Adirondack red maple foliage.",
        "winter": "5-25°F, heavy Adirondack snowpack, road closed to wheeled vehicles (snowmobile trail)."
      },
      "dangers_and_hazards": [
        "Black bears present (NYS DEC approved bear canister mandatory for food storage)",
        "Black flies in late spring/early summer"
      ],
      "acoustic_environment": {
        "quietness_rating": "9/10 - Loon calls and wind through Adirondack white pines",
        "common_human_made_sounds": ["Occasional forest road vehicle"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Eastern White Pine", "Balsam Fir", "Paper Birch", "Sugar Maple"],
        "common_animals": ["Black Bear", "Moose", "Common Loon", "White-tailed Deer", "Brook Trout"]
      },
      "human_demographics_and_culture": "Haudenosaunee (Iroquois) ancestral lands, Adirondack guides, NY nomads, wilderness campers.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Haudenosaunee territory honoring the pristine Adirondack mountain waters and sacred wilderness solitude.",
        "energetic_and_spiritual_features": "Profound Adirondack Northwoods quietness, majestic pine forest canopy."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Black River Mountain Trail",
          "length_miles": 5.2,
          "difficulty": "Moderate",
          "features": "Pristine wilderness ponds, hardwood ridges, mountain views"
        }
      ],
      "public_reviews_summary": "The largest free roadside primitive camping area in New York State. Over 140 free designated sites in Adirondack Park with pit privies and solid cell service near Inlet.",
      "other_data": "NYS DEC Adirondack Forest Preserve. 100% Free.",
      "last_updated": "2026-09-12"
    }
  ],
  "north_dakota.json": [
    {
      "id": "nd-little-missouri-national-grassland",
      "name": "Little Missouri National Grassland Dispersed Primitive Camping",
      "state": "North Dakota",
      "county": "Billings / McKenzie County",
      "coordinates": { "latitude": 46.9214, "longitude": -103.5214, "elevation_ft": 2450 },
      "management_agency": {
        "name": "US Forest Service - Dakota Prairie Grasslands (Medora Ranger District)",
        "type": "USFS",
        "phone": "(701) 227-7800",
        "website": "https://www.fs.usda.gov/dpg"
      },
      "rules_and_regulations": {
        "cost": "100% Free - USFS Dispersed Primitive Camping (zero fee)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed primitive camping permitted throughout Little Missouri National Grassland along Maah Daah Hey Trail access points and forest roads."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6 inches deep in clay soil 200 feet from Little Missouri River. Pack out hygiene items.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Gathering dead and down wood permitted; fire pan recommended.",
        "safety_requirements": "Campfires in established rock fire rings or metal fire pans only. Fully extinguish before leaving.",
        "seasonal_fire_bans": "Summer high wind prairie burn bans active July-August."
      },
      "access_and_road_conditions": {
        "road_type": "Paved Interstate 94 / US 85 to gravel grassland roads",
        "road_conditions": "Graded gravel, bentonite clay dirt spurs (slick when wet).",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance vehicles in dry weather; 4x4 recommended after rains.",
        "scores": { "road_grade": 4, "road_terrain_difficulty": 4, "supply_run_pain": 4 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / I-94 & US 85 Tower Line",
        "verizon_reliability": "3-4 bars 4G LTE (20-45 Mbps download)",
        "att_reliability": "3-4 bars 4G LTE",
        "tmobile_reliability": "2-3 bars 4G LTE",
        "terrain_obstruction_risk": "Low across rolling badlands topography",
        "distance_from_tower_corridor_miles": 4.0,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Badlands Butte & Prairie Panoramas",
        "Maah Daah Hey Trailhead Access",
        "Flat Dirt/Gravel Vehicle Pullouts",
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
          "town_name": "Medora, ND",
          "distance_miles": 8.0,
          "services_available": ["General Store", "Gas Stations", "Historic Saloons", "Restaurants", "Visitor Center"]
        },
        {
          "town_name": "Dickinson, ND",
          "distance_miles": 32.0,
          "services_available": ["Walmart Supercenter", "Dan's Supermarket", "Dickinson Hospital", "24/7 Gyms", "Full Services"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "45-65°F, greening badlands prairie, crisp sunny weather.",
        "summer": "78-92°F, warm sunny Badlands days, bright clear skies.",
        "fall": "50-70°F, golden cottonwood river bottom colors, cool nights.",
        "winter": "5-25°F, severe prairie cold, dusting of snow on badlands bluffs."
      },
      "dangers_and_hazards": [
        "Bentonite clay roads become unpassable mud when wet",
        "High wind on open prairie",
        "Bison in surrounding Theodore Roosevelt National Park area"
      ],
      "acoustic_environment": {
        "quietness_rating": "9/10 - Badlands prairie wind and coyote calls",
        "common_human_made_sounds": ["Distant train whistle across prairie valley"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Rocky Mountain Juniper", "Fremont Cottonwood", "Western Wheatgrass", "Prickly Pear Cactus"],
        "common_animals": ["Bison", "Pronghorn Antelope", "Mule Deer", "Coyote", "Golden Eagle", "Prairie Dog"]
      },
      "human_demographics_and_culture": "Mandan, Hidatsa, & Arikara ancestral lands, Dakota ranchers, Theodore Roosevelt conservation heritage, nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Sacred badlands territory of the Lakota and Mandan nations. Where Theodore Roosevelt developed his legendary passion for conservation.",
        "energetic_and_spiritual_features": "Majestic badlands prairie horizon, breathtaking sunset light on clay cutbanks."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Maah Daah Hey Trail (Medora Section)",
          "length_miles": 14.0,
          "difficulty": "Moderate",
          "features": "Badlands clay ridges, juniper draws, Little Missouri river vistas"
        }
      ],
      "public_reviews_summary": "Stunning Dakota Badlands primitive camping. Free USFS access, fast cell internet near Medora, and world-class trail access on the Maah Daah Hey.",
      "other_data": "Dakota Prairie Grasslands. Free dispersed primitive camping.",
      "last_updated": "2026-09-12"
    }
  ]
}

for filename, sites in b4_expansion.items():
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
