import json
import os

BASE_DIR = "/home/volmarr/.gemini/antigravity/scratch/Camping_Nomad_Life/states"

group_k = {
  "oklahoma.json": [
    {
      "id": "ok-mcgee-creek-natural-scenic-area",
      "name": "McGee Creek Natural Scenic Area Primitive Backpack Campsites",
      "state": "Oklahoma",
      "county": "Atoka County",
      "coordinates": { "latitude": 34.3812, "longitude": -95.8812, "elevation_ft": 650 },
      "management_agency": {
        "name": "Oklahoma Department of Wildlife Conservation (ODWC) / State Parks",
        "type": "State ODWC",
        "phone": "(580) 889-3750",
        "website": "https://www.wildlifedepartment.com"
      },
      "rules_and_regulations": {
        "cost": "100% Free - Free ODWC Primitive Backpacking Permit required at trailhead (zero cost)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed primitive backpacking camping permitted along 25+ miles of trails in McGee Creek Natural Scenic Area. No motorized vehicles allowed."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6 inches deep in soil 200 feet from McGee Creek and reservoirs. Pack out all paper.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down wood gathering permitted on site.",
        "safety_requirements": "Campfires in established rock fire rings only. Fully douse with water before vacating.",
        "seasonal_fire_bans": "Fall dry weather burn warnings."
      },
      "access_and_road_conditions": {
        "road_type": "Paved state highway to gravel entrance road to trailhead parking lot",
        "road_conditions": "Smooth gravel trailhead parking access.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance passenger cars.",
        "scores": { "road_grade": 2, "road_terrain_difficulty": 3, "supply_run_pain": 3 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / Atoka US 69 Tower Line",
        "verizon_reliability": "3-4 bars 4G LTE on ridge trails",
        "att_reliability": "3-4 bars 4G LTE",
        "tmobile_reliability": "2-3 bars 4G LTE",
        "terrain_obstruction_risk": "Low to Moderate across Ouachita foothill ridges",
        "distance_from_tower_corridor_miles": 3.5,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Ouachita Pine & Oak Forest Campsites",
        "McGee Creek Water Source (Filter mandatory)",
        "Trailhead Parking Lot",
        "Stone Fire Rings"
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
          "town_name": "Atoka / Antlers, OK",
          "distance_miles": 12.0,
          "services_available": ["Supermarket", "Gas Stations", "Atoka County Library", "Hospital", "Restaurants"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "55-72°F, blooming wild azaleas, spring creek flows.",
        "summer": "78-90°F, warm Southern Oklahoma summer days under oak canopy.",
        "fall": "55-75°F, colorful Ouachita foothill autumn foliage.",
        "winter": "32-52°F, mild winter, dry sunny days."
      },
      "dangers_and_hazards": [
        "Ticks in summer months (use permethrin)"
      ],
      "acoustic_environment": {
        "quietness_rating": "9/10 - Creek water trickles and pine forest wind",
        "common_human_made_sounds": ["Occasional backpacker on trail"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Shortleaf Pine", "Post Oak", "Flowering Dogwood", "French Mulberry"],
        "common_animals": ["White-tailed Deer", "Wild Turkey", "Bobcat", "Smallmouth Bass"]
      },
      "human_demographics_and_culture": "Choctaw Nation ancestral territory, Oklahoma outdoorsmen, backpackers, nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Traditional Choctaw Nation territory honoring the pristine pine hills and clear waters of Atoka County.",
        "energetic_and_spiritual_features": "Relaxing pine ridge quietness, pristine creek water solitude."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "McGee Creek Natural Scenic Trail System",
          "length_miles": 10.5,
          "difficulty": "Moderate",
          "features": "Shortleaf pine forest, rocky creek ravines, wildlife watching"
        }
      ],
      "public_reviews_summary": "Oklahoma's hidden wilderness gem. Free primitive backpacking camping, quiet pine ridges, fast cell internet near Atoka, and zero fees.",
      "other_data": "Oklahoma ODWC Natural Scenic Area. Free permit required at trailhead.",
      "last_updated": "2026-09-12"
    }
  ],
  "rhode_island.json": [
    {
      "id": "ri-casimir-pulaski-memorial-state-park-shelter",
      "name": "Casimir Pulaski Primitive Shelter Site",
      "state": "Rhode Island",
      "county": "Providence County",
      "coordinates": { "latitude": 41.9412, "longitude": -71.7812, "elevation_ft": 620 },
      "management_agency": {
        "name": "Rhode Island Department of Environmental Management (DEM)",
        "type": "State DEM",
        "phone": "(401) 568-2013",
        "website": "https://dem.ri.gov"
      },
      "rules_and_regulations": {
        "cost": "100% Free - Free RI DEM Primitive Backpacking Permit required online (zero cost)",
        "stay_limit": "2 consecutive nights stay limit",
        "guidelines": "Primitive backpacking camping permitted at designated shelter/primitive site in Pulaski State Park / George Washington Management Area."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Use wooden pit privy at shelter site or dig cat-hole 6 inches deep in soil 200 feet from Peck Pond. Pack out all paper.",
        "trash_policy": "Strict Carry-In / Carry-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down wood gathering permitted on site.",
        "safety_requirements": "Campfires in established stone fire pit only. Fully douse with water before leaving.",
        "seasonal_fire_bans": "Spring dry leaf weather fire restrictions."
      },
      "access_and_road_conditions": {
        "road_type": "Paved state route to gravel forest entrance road",
        "road_conditions": "Smooth gravel parking area access, 0.5 mile hike-in.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance passenger cars.",
        "scores": { "road_grade": 2, "road_terrain_difficulty": 2, "supply_run_pain": 3 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / Providence Metro Cell Signal",
        "verizon_reliability": "4-5 bars 4G/5G LTE (30-70 Mbps download)",
        "att_reliability": "4-5 bars 4G/5G LTE",
        "tmobile_reliability": "3-4 bars 4G LTE",
        "terrain_obstruction_risk": "Low (Rolling piney forest topography)",
        "distance_from_tower_corridor_miles": 2.0,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Wooden Lean-To Shelter",
        "Pit Privy Toilet",
        "Peck Pond Water Source (Filter mandatory)",
        "Stone Fire Ring"
      ],
      "location_scores": {
        "distance_to_groceries_score": 8,
        "distance_to_library_score": 8,
        "distance_to_gym_score": 7,
        "terrain_score": 7,
        "quietness_score": 8
      },
      "nearest_supply_towns": [
        {
          "town_name": "Chepachet / Pascoag, RI",
          "distance_miles": 4.0,
          "services_available": ["Supermarket", "Gas Stations", "Glocester Manton Free Public Library", "Restaurants"]
        },
        {
          "town_name": "Providence, RI",
          "distance_miles": 22.0,
          "services_available": ["Full Capital Metro Services", "Costco / Target", "Rhode Island Hospital", "24/7 Gyms"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "48-65°F, blooming wild mountain laurel, crisp fresh pine air.",
        "summer": "72-84°F, pleasant New England forest summer weather.",
        "fall": "50-68°F, vibrant colorful hardwood foliage.",
        "winter": "25-40°F, mild winter, light snow."
      },
      "dangers_and_hazards": [
        "Ticks in summer months (use permethrin)"
      ],
      "acoustic_environment": {
        "quietness_rating": "8/10 - Wind through white pines and woodland songbirds",
        "common_human_made_sounds": ["Occasional distant vehicle on state route"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["White Pine", "Red Oak", "Hemlock", "Mountain Laurel"],
        "common_animals": ["White-tailed Deer", "Wild Turkey", "Red Fox", "Osprey"]
      },
      "human_demographics_and_culture": "Nipmuc ancestral lands, Rhode Island outdoorsmen, digital nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Traditional Nipmuc nation territory honoring the ancient pine forests and clear ponds of Northwest Rhode Island.",
        "energetic_and_spiritual_features": "Relaxing pine forest quietness, serene pond water reflections."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Walkill / Pulaski Loop Trail",
          "length_miles": 4.5,
          "difficulty": "Easy",
          "features": "Peck Pond shoreline, white pine groves, historic stone walls"
        }
      ],
      "public_reviews_summary": "Great free primitive shelter camping in Northwest Rhode Island. Blazing 5G cell internet, clean wooden lean-to, and just 5 minutes to Chepachet.",
      "other_data": "Rhode Island DEM. Free permit required online.",
      "last_updated": "2026-09-12"
    }
  ],
  "south_carolina.json": [
    {
      "id": "sc-francis-marion-nf-swamp-fox",
      "name": "Swamp Fox Passage Dispersed Campsites",
      "state": "South Carolina",
      "county": "Berkeley / Charleston County",
      "coordinates": { "latitude": 33.1412, "longitude": -79.7812, "elevation_ft": 40 },
      "management_agency": {
        "name": "US Forest Service - Francis Marion National Forest (Francis Marion Ranger District)",
        "type": "USFS",
        "phone": "(843) 336-3248",
        "website": "https://www.fs.usda.gov/scnfs"
      },
      "rules_and_regulations": {
        "cost": "100% Free - USFS Dispersed Primitive Camping (zero fee)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed primitive camping permitted along Swamp Fox Passage of Palmetto Trail and Forest Service dirt roads outside developed fee campgrounds."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6 inches deep in soil 200 feet from water drainages. Pack out all paper.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down wood gathering permitted on site.",
        "safety_requirements": "Campfires in established rock fire rings only. Fully douse with water before vacating.",
        "seasonal_fire_bans": "Observe dry weather pine burn warnings."
      },
      "access_and_road_conditions": {
        "road_type": "Paved US 17 / SC 45 to gravel Forest Service roads",
        "road_conditions": "Graded gravel access roads, flat dirt turnouts.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance passenger cars.",
        "scores": { "road_grade": 1, "road_terrain_difficulty": 2, "supply_run_pain": 3 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / Charleston Coastal Tower Line",
        "verizon_reliability": "4-5 bars 4G/5G LTE (30-65 Mbps download)",
        "att_reliability": "4-5 bars 4G/5G LTE",
        "tmobile_reliability": "3-4 bars 4G LTE",
        "terrain_obstruction_risk": "Low across flat coastal pine savanna",
        "distance_from_tower_corridor_miles": 2.5,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Longleaf Pine Savanna & Live Oak Campsites",
        "Palmetto Trailhead Access",
        "Flat Dirt/Gravel Pullouts",
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
          "town_name": "Moncks Corner / Mount Pleasant, SC",
          "distance_miles": 14.0,
          "services_available": ["Publix / Walmart", "Gas Stations", "Berkeley County Library", "Hospital", "Restaurants"]
        },
        {
          "town_name": "Charleston, SC",
          "distance_miles": 28.0,
          "services_available": ["Full Metro City Services", "Costco / Target", "24/7 Gyms", "Hardware Stores"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "65-80°F, blooming wild azaleas, pleasant coastal pine breezes.",
        "summer": "85-94°F, hot humid Lowcountry summer weather under pine canopy.",
        "fall": "62-80°F, prime mild coastal camping weather.",
        "winter": "42-65°F, mild winter, dry clear days."
      },
      "dangers_and_hazards": [
        "Ticks and chiggers in summer (use permethrin)",
        "American alligators in coastal swamp channels"
      ],
      "acoustic_environment": {
        "quietness_rating": "8/10 - Pine forest wind and coastal bird calls",
        "common_human_made_sounds": ["Distant highway traffic on US 17 corridor"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Longleaf Pine", "Loblolly Pine", "Live Oak", "Spanish Moss", "Cabbage Palm"],
        "common_animals": ["Red-cockaded Woodpecker", "White-tailed Deer", "Wild Turkey", "Alligator", "Bobcat"]
      },
      "human_demographics_and_culture": "Sewee & Santee ancestral lands, Lowcountry Gullah Geechee culture, South Carolina nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Revolutionary War history of General Francis Marion ('The Swamp Fox'). Deeply sacred ancestral Lowcountry territory.",
        "energetic_and_spiritual_features": "Relaxing coastal longleaf pine savanna energy, soothing Spanish moss oak canopy."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Palmetto Trail (Swamp Fox Passage)",
          "length_miles": 14.0,
          "difficulty": "Easy to Moderate",
          "features": "Longleaf pine savanna, boardwalk swamp crossings, historic causeways"
        }
      ],
      "public_reviews_summary": "Best free nomad camping outside Charleston, South Carolina. Blazing 5G cell internet, flat pine campsites, and 15 minutes to Moncks Corner.",
      "other_data": "Francis Marion National Forest. Free dispersed primitive camping.",
      "last_updated": "2026-09-12"
    }
  ],
  "south_dakota.json": [
    {
      "id": "sd-buffalo-gap-national-grassland",
      "name": "Buffalo Gap National Grassland Dispersed Camping",
      "state": "South Dakota",
      "county": "Pennington / Custer County",
      "coordinates": { "latitude": 43.7812, "longitude": -102.3214, "elevation_ft": 2850 },
      "management_agency": {
        "name": "US Forest Service - Nebraska National Forests & Grasslands (Wall Ranger District)",
        "type": "USFS",
        "phone": "(605) 279-2125",
        "website": "https://www.fs.usda.gov/nebraska"
      },
      "rules_and_regulations": {
        "cost": "100% Free - USFS Dispersed Primitive Camping (zero fee)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed primitive camping permitted throughout Buffalo Gap National Grassland along Badlands overlook rim roads. Leave No Trace."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6 inches deep in soil 200 feet from canyon washes. Pack out all paper.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Must bring your own firewood. Gathering wood on grassland is prohibited.",
        "safety_requirements": "Campfires in established rock fire rings or metal fire pans only. Fully douse before vacating.",
        "seasonal_fire_bans": "Summer high wind prairie burn bans active July-August."
      },
      "access_and_road_conditions": {
        "road_type": "Paved Interstate 90 / SD 240 to gravel/dirt grassland roads (Nomad View Rim Road)",
        "road_conditions": "Graded gravel main access, clay dirt rim pullouts (slick when wet).",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance vehicles in dry weather.",
        "scores": { "road_grade": 3, "road_terrain_difficulty": 3, "supply_run_pain": 3 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / Wall & I-90 Tower Line",
        "verizon_reliability": "4-5 bars 4G/5G LTE (30-80 Mbps download on Nomad View rim)",
        "att_reliability": "4-5 bars 4G/5G LTE",
        "tmobile_reliability": "3-4 bars 4G LTE",
        "terrain_obstruction_risk": "Low along high open Badlands wall rim",
        "distance_from_tower_corridor_miles": 2.5,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Spectacular Badlands National Park Wall Rim Panorama Views",
        "Flat Dirt/Gravel RV & Van Pullouts",
        "Dark Sky Stargazing",
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
          "town_name": "Wall, SD",
          "distance_miles": 8.0,
          "services_available": ["Wall Drug / Supermarket", "Gas Stations", "Wall Public Library", "Clinic", "Restaurants"]
        },
        {
          "town_name": "Rapid City, SD",
          "distance_miles": 52.0,
          "services_available": ["Full Metro Services", "Costco / Target", "Hospitals", "24/7 Gyms"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "50-68°F, greening prairie grass, cool wind.",
        "summer": "82-95°F, warm sunny Badlands days, bright clear skies.",
        "fall": "55-72°F, golden prairie foliage, crisp chilly nights.",
        "winter": "15-35°F, severe prairie cold, dusting of snow on Badlands bluffs."
      },
      "dangers_and_hazards": [
        "Sheer 300ft Badlands cliff rim drop-offs (watch footing near edge)",
        "High wind gusts on open prairie wall",
        "Clay dirt roads become slick mud when wet"
      ],
      "acoustic_environment": {
        "quietness_rating": "9/10 - Badlands prairie wind and coyote choruses",
        "common_human_made_sounds": ["Distant vehicle on SD 240 in Badlands park"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Western Wheatgrass", "Prickly Pear Cactus", "Yucca", "Yellow Sweetclover"],
        "common_animals": ["Bison", "Bighorn Sheep", "Pronghorn Antelope", "Prairie Dog", "Black-footed Ferret", "Coyote"]
      },
      "human_demographics_and_culture": "Oglala Lakota sacred ancestral lands, South Dakota ranchers, Badlands travelers, digital nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Famous 'Nomad View' rim location. Sacred Oglala Lakota territory honoring the majestic Badlands wall and vast Dakota prairie.",
        "energetic_and_spiritual_features": "Unrivaled 300ft Badlands rim panorama energy, cosmic dark night sky stargazing."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Badlands Wall Rim Trail",
          "length_miles": 5.0,
          "difficulty": "Easy to Moderate",
          "features": "Badlands clay hoodoos, prairie grass overlooks, bison viewing"
        }
      ],
      "public_reviews_summary": "World-famous 'Nomad View' primitive camping rim outside Badlands National Park. Blazing 5G cell internet, front-row Badlands sunsets, and 100% free USFS access.",
      "other_data": "Buffalo Gap National Grassland. Free dispersed primitive camping.",
      "last_updated": "2026-09-12"
    }
  ],
  "tennessee.json": [
    {
      "id": "tn-big-south-fork-nra-backcountry",
      "name": "Big South Fork National River & Recreation Area Backcountry Camping",
      "state": "Tennessee",
      "county": "Scott / Fentress County",
      "coordinates": { "latitude": 36.4812, "longitude": -84.6812, "elevation_ft": 1450 },
      "management_agency": {
        "name": "National Park Service (NPS) - Big South Fork NRA",
        "type": "Federal NPS",
        "phone": "(423) 569-9778",
        "website": "https://www.nps.gov/biso"
      },
      "rules_and_regulations": {
        "cost": "100% Free - Free NPS Backcountry Camping Permit required online (zero cost)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed backcountry primitive camping permitted throughout Big South Fork NRA along river and cliff trail networks. Camp 100ft minimum from trails."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6-8 inches deep in organic soil 200 feet from Big South Fork River. Pack out hygiene products.",
        "trash_policy": "Strict Leave No Trace."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down wood gathering permitted on site.",
        "safety_requirements": "Campfires in established rock fire rings only. Fully douse with water before vacating.",
        "seasonal_fire_bans": "Fall leaf dry weather fire warnings."
      },
      "access_and_road_conditions": {
        "road_type": "Paved state highway to gravel NPS park roads (Divide Road)",
        "road_conditions": "Graded gravel access roads, flat trailhead parking.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance passenger cars.",
        "scores": { "road_grade": 3, "road_terrain_difficulty": 3, "supply_run_pain": 3 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / Oneida & Hwy 27 Tower Line",
        "verizon_reliability": "3-4 bars 4G LTE near Divide Road ridge trailheads",
        "att_reliability": "3-4 bars 4G LTE",
        "tmobile_reliability": "2-3 bars 4G LTE",
        "terrain_obstruction_risk": "Moderate inside deep sandstone river gorge",
        "distance_from_tower_corridor_miles": 4.0,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Sandstone Bluff & Arch Overlook Campsites",
        "Big South Fork River Water Source (Filter mandatory)",
        "Hardwood Canopy Shade",
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
          "town_name": "Oneida / Jamestown, TN",
          "distance_miles": 12.0,
          "services_available": ["Walmart Supercenter / Kroger", "Gas Stations", "Scott County Library", "Hospital", "Restaurants"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "55-72°F, blooming wild azaleas, roaring river rapids.",
        "summer": "75-88°F, pleasant river gorge swimming weather.",
        "fall": "52-72°F, spectacular Cumberland Plateau autumn foliage.",
        "winter": "30-48°F, mild winter, crisp mountain air."
      },
      "dangers_and_hazards": [
        "Sandstone cliff drop-offs",
        "Black bears in Big South Fork NRA (bear hang or canister recommended)"
      ],
      "acoustic_environment": {
        "quietness_rating": "9/10 - River rapids thunder and mountain breeze",
        "common_human_made_sounds": ["Occasional backpacker on trail"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Shortleaf Pine", "White Oak", "Hemlock", "Rhododendron"],
        "common_animals": ["Black Bear", "White-tailed Deer", "Smallmouth Bass", "Pileated Woodpecker"]
      },
      "human_demographics_and_culture": "Cherokee ancestral lands, Cumberland Plateau outdoorsmen, NPS river guides, nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Famous for massive sandstone natural arches (Twin Arches). Sacred Cherokee territory honoring the gorge waters.",
        "energetic_and_spiritual_features": "Exhilarating sandstone arch mountain energy, pristine river gorge solitude."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Twin Arches Loop Trail",
          "length_miles": 4.6,
          "difficulty": "Moderate",
          "features": "Massive 100ft sandstone natural arches, rock shelters, hardwood forest"
        }
      ],
      "public_reviews_summary": "Top free backcountry camping in Tennessee's Big South Fork NPS area. Massive natural rock arches, fast cell internet near Oneida, and free NPS access.",
      "other_data": "NPS Big South Fork NRA. Free permit required online.",
      "last_updated": "2026-09-12"
    }
  ],
  "texas.json": [
    {
      "id": "tx-sabine-nf-trail-between-the-lakes",
      "name": "Trail Between the Lakes Primitive Campsites",
      "state": "Texas",
      "county": "Sabine / San Augustine County",
      "coordinates": { "latitude": 31.3812, "longitude": -93.8812, "elevation_ft": 280 },
      "management_agency": {
        "name": "US Forest Service - National Forests and Grasslands in Texas (Sabine District)",
        "type": "USFS",
        "phone": "(409) 625-1940",
        "website": "https://www.fs.usda.gov/texas"
      },
      "rules_and_regulations": {
        "cost": "100% Free - USFS Dispersed Primitive Camping (zero fee)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed primitive camping permitted along 28-mile Trail Between the Lakes corridor connecting Toledo Bend and Sam Rayburn Reservoirs."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6 inches deep in soil 200 feet from Toledo Bend / Sam Rayburn lake drainages. Pack out all paper.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down wood gathering permitted on site.",
        "safety_requirements": "Campfires in established rock fire rings only. Fully douse with water before vacating.",
        "seasonal_fire_bans": "Summer East Texas burn bans active July-August."
      },
      "access_and_road_conditions": {
        "road_type": "Paved state highway to gravel Forest Service roads (FR 111)",
        "road_conditions": "Graded gravel access roads, flat dirt turnouts.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance passenger cars.",
        "scores": { "road_grade": 2, "road_terrain_difficulty": 3, "supply_run_pain": 3 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / Hemphill & Lake Toledo Tower Line",
        "verizon_reliability": "4-5 bars 4G/5G LTE (25-50 Mbps download)",
        "att_reliability": "4-5 bars 4G/5G LTE",
        "tmobile_reliability": "3-4 bars 4G LTE",
        "terrain_obstruction_risk": "Low (Gentle rolling piney woods topography)",
        "distance_from_tower_corridor_miles": 2.5,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Piney Woods & Toledo Bend Lake Campsites",
        "Flat Dirt/Gravel RV & Van Pullouts",
        "Trailhead Access",
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
          "town_name": "Hemphill / San Augustine, TX",
          "distance_miles": 10.0,
          "services_available": ["Supermarket", "Gas Stations", "Sabine County Library", "Hospital", "Restaurants"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "62-78°F, blooming wild dogwood, warm lake breezes.",
        "summer": "85-95°F, hot humid East Texas piney woods summer.",
        "fall": "60-78°F, prime mild camping weather.",
        "winter": "42-62°F, mild winter, dry clear days."
      },
      "dangers_and_hazards": [
        "Feral hogs in forest bottoms",
        "Ticks and chiggers in summer (use permethrin)"
      ],
      "acoustic_environment": {
        "quietness_rating": "8/10 - Pine forest wind and lake water lapping",
        "common_human_made_sounds": ["Occasional fishing boat on Toledo Bend reservoir"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Loblolly Pine", "Shortleaf Pine", "Post Oak", "Dogwood"],
        "common_animals": ["White-tailed Deer", "Feral Hog", "Bald Eagle", "Large-mouth Bass", "Armadillo"]
      },
      "human_demographics_and_culture": "Caddo ancestral lands, East Texas piney woods outdoorsmen, lake anglers, nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Traditional Caddo nation territory honoring the ancient piney woods connecting the major East Texas river valleys.",
        "energetic_and_spiritual_features": "Relaxing East Texas pine needle aroma, peaceful lake reflection views."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Trail Between the Lakes",
          "length_miles": 12.0,
          "difficulty": "Moderate",
          "features": "Piney woods canopy, creek bridge crossings, lake vistas"
        }
      ],
      "public_reviews_summary": "Top free primitive camping in Sabine National Forest. Fast 5G cell internet, flat pine campsites, and 10 minutes to Hemphill.",
      "other_data": "Sabine National Forest. Free dispersed primitive camping.",
      "last_updated": "2026-09-12"
    }
  ],
  "vermont.json": [
    {
      "id": "vt-green-mountain-nf-breadloaf-wilderness",
      "name": "Breadloaf Wilderness Primitive Campsites",
      "state": "Vermont",
      "county": "Addison County",
      "coordinates": { "latitude": 43.9812, "longitude": -72.9812, "elevation_ft": 2250 },
      "management_agency": {
        "name": "US Forest Service - Green Mountain National Forest (Middlebury Ranger District)",
        "type": "USFS",
        "phone": "(802) 388-4362",
        "website": "https://www.fs.usda.gov/greenmountain"
      },
      "rules_and_regulations": {
        "cost": "100% Free - GMNF Wilderness Dispersed Primitive Camping (zero fee)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed primitive camping permitted at least 200ft from Long Trail / Appalachian Trail and water streams throughout Breadloaf Wilderness."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6-8 inches deep in organic soil 200 feet from streams. Pack out hygiene products.",
        "trash_policy": "Strict Leave No Trace wilderness policy."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down wood gathering permitted on forest lands.",
        "safety_requirements": "Campfires in established rock fire rings only. Fully douse with water before vacating.",
        "seasonal_fire_bans": "Spring dry leaf weather fire warnings."
      },
      "access_and_road_conditions": {
        "road_type": "Paved VT Route 125 to gravel Forest Service roads (FR 59)",
        "road_conditions": "Graded gravel access roads, flat trailhead parking.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance passenger cars.",
        "scores": { "road_grade": 3, "road_terrain_difficulty": 3, "supply_run_pain": 3 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / Middlebury & Route 125 Tower Line",
        "verizon_reliability": "3-4 bars 4G LTE near Middlebury Gap / Route 125",
        "att_reliability": "3-4 bars 4G LTE",
        "tmobile_reliability": "2-3 bars 4G LTE",
        "terrain_obstruction_risk": "Moderate inside deep mountain hollows",
        "distance_from_tower_corridor_miles": 4.0,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Green Mountain Ridge Wilderness Campsites",
        "Long Trail Access",
        "Sugar Maple Canopy Shade",
        "Stone Fire Rings"
      ],
      "location_scores": {
        "distance_to_groceries_score": 7,
        "distance_to_library_score": 7,
        "distance_to_gym_score": 6,
        "terrain_score": 9,
        "quietness_score": 9
      },
      "nearest_supply_towns": [
        {
          "town_name": "Middlebury, VT",
          "distance_miles": 12.0,
          "services_available": ["Hannaford / Shaw's", "Gas Stations", "Ilsley Public Library", "Porter Hospital", "Restaurants"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "40-55°F, mud season in Vermont, spring trout streams.",
        "summer": "68-80°F, ideal Vermont mountain summer hiking weather.",
        "fall": "42-62°F, world-famous Vermont sugar maple autumn foliage.",
        "winter": "10-25°F, heavy mountain snowpack, snowshoeing & skiing."
      },
      "dangers_and_hazards": [
        "Black bears in Green Mountain NF (store food securely)",
        "Spring mud season road conditions"
      ],
      "acoustic_environment": {
        "quietness_rating": "9/10 - Mountain stream flow and wind through maple trees",
        "common_human_made_sounds": ["Occasional Long Trail backpacker"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Sugar Maple", "Yellow Birch", "Red Spruce", "Balsam Fir"],
        "common_animals": ["Moose", "Black Bear", "White-tailed Deer", "Bicknell's Thrush"]
      },
      "human_demographics_and_culture": "Abenaki ancestral lands, Middlebury College culture, Vermont woodsmen, Long Trail hikers, nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Traditional Abenaki territory honoring the sacred Green Mountain crest line and sugar maple forests of Addison County.",
        "energetic_and_spiritual_features": "Profound Vermont mountain quietness, majestic sugar maple autumn foliage."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Long Trail (Breadloaf Section)",
          "length_miles": 7.5,
          "difficulty": "Moderate to Strenuous",
          "features": "Mount Ellen summit views, sugar maple ridges, pristine mountain brooks"
        }
      ],
      "public_reviews_summary": "Vermont's finest free wilderness primitive camping in Green Mountain National Forest. Fast cell internet near Middlebury, sugar maple shade, and 100% free USFS access.",
      "other_data": "Green Mountain National Forest. Free dispersed wilderness camping.",
      "last_updated": "2026-09-12"
    }
  ],
  "virginia.json": [
    {
      "id": "va-jefferson-nf-mount-rogers-nra",
      "name": "Mount Rogers National Recreation Area High Country Primitive Camping",
      "state": "Virginia",
      "county": "Grayson / Smyth County",
      "coordinates": { "latitude": 36.6812, "longitude": -81.5214, "elevation_ft": 4850 },
      "management_agency": {
        "name": "US Forest Service - George Washington & Jefferson National Forests (Mount Rogers NRA)",
        "type": "USFS",
        "phone": "(276) 783-5196",
        "website": "https://www.fs.usda.gov/gwj"
      },
      "rules_and_regulations": {
        "cost": "100% Free - GWJ National Forests Dispersed Primitive Camping (zero fee outside developed campgrounds)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed primitive camping permitted throughout Mount Rogers High Country along Scales Road (FR 613) and Appalachian Trail corridor. Camp 100ft minimum from water."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6-8 inches deep in organic mountain soil 200 feet from mountain springs. Pack out hygiene products.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down wood gathering permitted on forest lands.",
        "safety_requirements": "Campfires in established rock fire rings only. Fully douse with water before vacating.",
        "seasonal_fire_bans": "Spring and fall dry weather high wind fire warnings."
      },
      "access_and_road_conditions": {
        "road_type": "Paved US 58 to gravel/dirt Forest Service roads (FR 613 / Scales Road)",
        "road_conditions": "Winding paved access to narrow mountain gravel ridge road.",
        "vehicle_recommendation": "High clearance recommended for Scales Road; standard 2WD vehicles can access US 58 pullouts near Whitetop Mountain.",
        "scores": { "road_grade": 5, "road_terrain_difficulty": 5, "supply_run_pain": 4 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / High Ridge Line Elevation",
        "verizon_reliability": "4-5 bars 4G/5G LTE along 4,850ft Whitetop & Mount Rogers crests",
        "att_reliability": "4-5 bars 4G/5G LTE",
        "tmobile_reliability": "3-4 bars 4G LTE",
        "terrain_obstruction_risk": "Low along exposed 4,850ft high mountain balds",
        "distance_from_tower_corridor_miles": 4.0,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "360-Degree Blue Ridge High Country Bald Views",
        "Wild Pony Grazing Area Access",
        "Flat Ridge Dirt/Gravel Pullouts",
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
          "town_name": "Marion / Damascus, VA",
          "distance_miles": 14.0,
          "services_available": ["Food City Supermarket", "Gas Stations", "Marion Public Library", "Smyth County Hospital", "Restaurants"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "45-62°F, blooming wild rhododendron, cool high mountain breezes.",
        "summer": "65-78°F, cool high-elevation escape from humid Virginia lowlands.",
        "fall": "45-65°F, world-class Virginia High Country autumn foliage.",
        "winter": "18-35°F, freezing mountain winds, heavy snowpack on Whitetop."
      },
      "dangers_and_hazards": [
        "High wind and sudden mountain fog squalls along exposed mountain balds",
        "Do not feed or pet the wild ponies (strictly enforced rule for pony safety)"
      ],
      "acoustic_environment": {
        "quietness_rating": "9/10 - High mountain bald wind and raven calls",
        "common_human_made_sounds": ["Occasional AT backpacker on trail"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Fraser Fir", "Red Spruce", "Catawba Rhododendron", "Highland Grass Balds"],
        "common_animals": ["Wild Ponies (famous Grayson Highlands herd)", "Black Bear", "White-tailed Deer", "Raven"]
      },
      "human_demographics_and_culture": "Cherokee ancestral lands, Virginia High Country mountain locals, AT hikers, overland nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Highest mountain peak in Virginia (Mount Rogers 5,729ft). Famous for its wild high-country roaming ponies and open mountain balds.",
        "energetic_and_spiritual_features": "Exhilarating 4,800+ ft high bald mountain energy, sweeping 360-degree vistas over three states."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Appalachian Trail (Mount Rogers Crest Section)",
          "length_miles": 8.5,
          "difficulty": "Moderate to Strenuous",
          "features": "Wild pony balds, Fraser fir spruce-fir summit forest, rock outcrops"
        }
      ],
      "public_reviews_summary": "Unrivaled high-country primitive camping in Virginia's Mount Rogers NRA. Wild roaming ponies, 360-degree mountain views, fast 5G cell internet, and free USFS access.",
      "other_data": "George Washington & Jefferson National Forests. Free dispersed primitive camping.",
      "last_updated": "2026-09-12"
    }
  ],
  "washington.json": [
    {
      "id": "wa-mt-baker-snoqualmie-nf-middle-fork",
      "name": "Middle Fork Snoqualmie River Road Dispersed Camping",
      "state": "Washington",
      "county": "King County",
      "coordinates": { "latitude": 47.5214, "longitude": -121.5412, "elevation_ft": 1050 },
      "management_agency": {
        "name": "US Forest Service - Mt. Baker-Snoqualmie National Forest (Snoqualmie Ranger District)",
        "type": "USFS",
        "phone": "(425) 888-1421",
        "website": "https://www.fs.usda.gov/mbs"
      },
      "rules_and_regulations": {
        "cost": "100% Free - USFS Dispersed Primitive Camping (zero fee outside developed fee campgrounds)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed primitive camping permitted at designated pullouts along Middle Fork Snoqualmie River Road (FR 56). Camp 100ft minimum from river."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6-8 inches deep in rich rainforest soil 200 feet from Snoqualmie River. Pack out hygiene products.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Abundant dead and down cedar and hemlock wood collection permitted.",
        "safety_requirements": "Campfires in established rock fire rings only. Fully douse with water before vacating.",
        "seasonal_fire_bans": "Late summer Western Washington dry burn bans enforced."
      },
      "access_and_road_conditions": {
        "road_type": "Paved I-90 to paved Middle Fork Road (FR 56) to gravel pullouts",
        "road_conditions": "Paved main access road, smooth gravel turnouts.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance passenger cars.",
        "scores": { "road_grade": 2, "road_terrain_difficulty": 2, "supply_run_pain": 2 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / Seattle Metro Tower Corridor",
        "verizon_reliability": "4-5 bars 4G/5G LTE near North Bend entrance",
        "att_reliability": "4-5 bars 4G/5G LTE",
        "tmobile_reliability": "3-4 bars 4G LTE",
        "terrain_obstruction_risk": "Low to Moderate inside Cascade river valley",
        "distance_from_tower_corridor_miles": 3.0,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Cascade Rainforest Riverfront Campsites",
        "Old-Growth Douglas Fir & Red Cedar Shade",
        "Clear Turquoise Snoqualmie River Access",
        "Stone Fire Rings"
      ],
      "location_scores": {
        "distance_to_groceries_score": 8,
        "distance_to_library_score": 8,
        "distance_to_gym_score": 7,
        "terrain_score": 10,
        "quietness_score": 9
      },
      "nearest_supply_towns": [
        {
          "town_name": "North Bend / Snoqualmie, WA",
          "distance_miles": 10.0,
          "services_available": ["Safeway / QFC", "Gas Stations", "Snoqualmie Public Library", "Hospital", "REI Outlet", "24/7 Gyms"]
        },
        {
          "town_name": "Seattle Metro, WA",
          "distance_miles": 35.0,
          "services_available": ["Full Major Metro Services", "Trader Joe's / Costco", "Hospitals"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "48-62°F, green rainforest moss growth, misty mountain showers.",
        "summer": "72-85°F, prime Pacific Northwest summer weather, clear blue skies.",
        "fall": "50-65°F, golden bigleaf maple foliage, crisp nights.",
        "winter": "38-48°F, heavy rainforest precipitation, dusting of snow on peaks."
      },
      "dangers_and_hazards": [
        "Fast river currents during spring snow melt",
        "Black bears in Cascade mountains (store food securely)"
      ],
      "acoustic_environment": {
        "quietness_rating": "9/10 - Rushing river soundscape and rainforest breeze",
        "common_human_made_sounds": ["Occasional forest road vehicle"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Douglas Fir", "Western Red Cedar", "Western Hemlock", "Sword Fern", "Bigleaf Maple"],
        "common_animals": ["Roosevelt Elk", "Black Bear", "Bald Eagle", "Coho Salmon", "Cascade Frog"]
      },
      "human_demographics_and_culture": "Snoqualmie Tribal nation ancestral lands, Seattle outdoor athletes, trail runners, digital nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Ancestral territory of the Snoqualmie Tribe who honor Snoqualmie Falls and the mountain river valley as the sacred place of creation.",
        "energetic_and_spiritual_features": "Enchanting Cascade rainforest energy, roaring turquoise river water clarity."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Middle Fork Snoqualmie River Trail",
          "length_miles": 12.0,
          "difficulty": "Moderate",
          "features": "Suspension footbridge, old-growth red cedars, river gorge views"
        }
      ],
      "public_reviews_summary": "The single best free nomad camping spot close to Seattle. Blazing 5G cell internet, crystal clear Cascade river water, and 15 minutes to North Bend's Safeway and cafes.",
      "other_data": "Mt. Baker-Snoqualmie National Forest. Free dispersed primitive camping.",
      "last_updated": "2026-09-12"
    }
  ],
  "west_virginia.json": [
    {
      "id": "wv-monongahela-nf-cranberry-backcountry",
      "name": "Cranberry Backcountry Dispersed Primitive Camping",
      "state": "West Virginia",
      "county": "Pocahontas / Nicholas County",
      "coordinates": { "latitude": 38.2214, "longitude": -80.3214, "elevation_ft": 3450 },
      "management_agency": {
        "name": "US Forest Service - Monongahela National Forest (Gauley Ranger District)",
        "type": "USFS",
        "phone": "(304) 846-2695",
        "website": "https://www.fs.usda.gov/mnf"
      },
      "rules_and_regulations": {
        "cost": "100% Free - Monongahela NF Wilderness Dispersed Primitive Camping (zero fee)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed primitive camping permitted along Cranberry River Road (FR 76) pullouts and Cranberry Wilderness boundary. Camp 100ft minimum from river."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6-8 inches deep in peaty soil 200 feet from Cranberry River. Pack out hygiene products.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down wood gathering permitted on site.",
        "safety_requirements": "Campfires in established rock fire rings only. Fully douse with water before vacating.",
        "seasonal_fire_bans": "Fall dry leaf fire warnings."
      },
      "access_and_road_conditions": {
        "road_type": "Paved WV 150 (Highland Scenic Highway) to gravel Forest Service roads",
        "road_conditions": "Paved scenic highway main access, graded gravel river roads.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance passenger cars.",
        "scores": { "road_grade": 3, "road_terrain_difficulty": 3, "supply_run_pain": 4 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / Highland Highway Pass Signal",
        "verizon_reliability": "3-4 bars 4G LTE along Highland Scenic Highway 3,400ft pullouts",
        "att_reliability": "3-4 bars 4G LTE",
        "tmobile_reliability": "2-3 bars 4G LTE",
        "terrain_obstruction_risk": "Low along high mountain scenic highway crest",
        "distance_from_tower_corridor_miles": 4.0,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Pristine Appalachian Mountain River Campsites",
        "Highland Scenic Highway Ridge Overlooks",
        "Cranberry River Trout Stream Access",
        "Stone Fire Rings"
      ],
      "location_scores": {
        "distance_to_groceries_score": 6,
        "distance_to_library_score": 6,
        "distance_to_gym_score": 5,
        "terrain_score": 10,
        "quietness_score": 10
      },
      "nearest_supply_towns": [
        {
          "town_name": "Richwood / Marlinton, WV",
          "distance_miles": 14.0,
          "services_available": ["Supermarket", "Gas Stations", "Richwood Public Library", "Hospital", "Restaurants"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "45-62°F, blooming wild orchids in Cranberry Glades, crisp trout stream air.",
        "summer": "68-80°F, cool West Virginia high mountain escape from summer heat.",
        "fall": "48-65°F, world-class Highland Scenic Highway autumn foliage.",
        "winter": "18-35°F, heavy mountain snowpack, snowshoeing & cross-country skiing."
      },
      "dangers_and_hazards": [
        "Black bears in Monongahela NF (bear hang or canister recommended)",
        "High mountain fog on Highland Scenic Highway"
      ],
      "acoustic_environment": {
        "quietness_rating": "10/10 - Cranberry River rapids and mountain forest wind",
        "common_human_made_sounds": ["Occasional fly angler on river"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Red Spruce", "Hemlock", "Yellow Birch", "Sugar Maple", "Cranberry"],
        "common_animals": ["Black Bear", "Native Brook Trout", "White-tailed Deer", "Wild Turkey"]
      },
      "human_demographics_and_culture": "Monongahela ancestral lands, West Virginia mountain outdoorsmen, trout anglers, nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Cranberry Glades Botanical Area (arctic-tundra bog ecology in West Virginia). Rich Allegheny mountain folklore.",
        "energetic_and_spiritual_features": "Profound high mountain bog quietness, pristine trout river water."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Cranberry River Trail",
          "length_miles": 16.0,
          "difficulty": "Moderate",
          "features": "Non-motorized river valley, hemlock groves, trout pools"
        }
      ],
      "public_reviews_summary": "West Virginia's premier trout river primitive camping. Fast cell internet on Highland Scenic Highway, crystal clear Cranberry River pools, and 100% free USFS access.",
      "other_data": "Monongahela National Forest. Free dispersed primitive camping.",
      "last_updated": "2026-09-12"
    }
  ],
  "wisconsin.json": [
    {
      "id": "wi-black-river-state-forest-backpack",
      "name": "Black River State Forest Backpack Primitive Campsites",
      "state": "Wisconsin",
      "county": "Jackson County",
      "coordinates": { "latitude": 44.2812, "longitude": -90.7812, "elevation_ft": 950 },
      "management_agency": {
        "name": "Wisconsin Department of Natural Resources (DNR) - Division of Forestry",
        "type": "State DNR",
        "phone": "(715) 284-4103",
        "website": "https://dnr.wisconsin.gov"
      },
      "rules_and_regulations": {
        "cost": "100% Free - Free WI DNR State Forest Backpacking Permit required online/forest office (zero cost)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed primitive camping permitted at designated backpack sites along Black River State Forest trail system."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Use wooden pit privy at trail campsite or dig cat-hole 6 inches deep in soil 200 feet from Black River. Pack out paper.",
        "trash_policy": "Strict Carry-In / Carry-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down wood gathering permitted on site.",
        "safety_requirements": "Campfires in established rock fire rings only. Fully douse with water before vacating.",
        "seasonal_fire_bans": "Spring dry leaf forest fire warnings."
      },
      "access_and_road_conditions": {
        "road_type": "Paved state highway to gravel forest entrance road",
        "road_conditions": "Graded gravel access roads, flat trailhead parking.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance passenger cars.",
        "scores": { "road_grade": 2, "road_terrain_difficulty": 2, "supply_run_pain": 3 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / I-94 Corridor Tower Line",
        "verizon_reliability": "4-5 bars 4G/5G LTE (25-55 Mbps download)",
        "att_reliability": "4-5 bars 4G/5G LTE",
        "tmobile_reliability": "3-4 bars 4G LTE",
        "terrain_obstruction_risk": "Low across sandstone mound topography",
        "distance_from_tower_corridor_miles": 2.5,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Sandstone Mound Bluff Overlook Campsites",
        "Jack Pine & Oak Canopy Shade",
        "Pit Privy Toilet",
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
          "town_name": "Black River Falls, WI",
          "distance_miles": 8.0,
          "services_available": ["SuperOne Foods / Walmart", "Gas Stations", "Black River Falls Public Library", "Hospital", "Restaurants"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "48-65°F, blooming wild lupine, fresh pine air.",
        "summer": "72-84°F, pleasant Wisconsin forest summer weather.",
        "fall": "48-68°F, vibrant oak and maple autumn foliage.",
        "winter": "18-35°F, snowpack on trails, cross-country skiing."
      },
      "dangers_and_hazards": [
        "Ticks in summer months (use permethrin)"
      ],
      "acoustic_environment": {
        "quietness_rating": "8/10 - Wind through jack pines and woodland birds",
        "common_human_made_sounds": ["Occasional distant highway traffic on I-94"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Jack Pine", "Red Oak", "Wild Lupine (Karner Blue Butterfly habitat)", "Pitcher Plant"],
        "common_animals": ["Karner Blue Butterfly (endangered)", "Elk", "White-tailed Deer", "Wild Turkey"]
      },
      "human_demographics_and_culture": "Ho-Chunk (Winnebago) ancestral lands, Wisconsin woodsmen, digital nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Ancestral territory of the Ho-Chunk Nation honoring Castle Mound sandstone bluffs and pine plains of Jackson County.",
        "energetic_and_spiritual_features": "Relaxing jack pine forest aroma, unique sandstone mound bluff energy."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Castle Mound Pine Trail",
          "length_miles": 4.5,
          "difficulty": "Easy to Moderate",
          "features": "Sandstone bluff overlooks, jack pine plains, wildflower meadows"
        }
      ],
      "public_reviews_summary": "Great free primitive camping in Wisconsin's Black River State Forest. Blazing 5G cell internet, sandstone mound overlooks, and 10 minutes to Black River Falls.",
      "other_data": "Wisconsin DNR State Forest. Free permit required online.",
      "last_updated": "2026-09-12"
    }
  ]
}

for filename, sites in group_k.items():
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
