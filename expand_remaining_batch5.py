import json
import os

BASE_DIR = "/home/volmarr/.gemini/antigravity/scratch/Camping_Nomad_Life/states"

b5_expansion = {
  "ohio.json": [
    {
      "id": "oh-wayne-nf-covered-bridge-trail",
      "name": "Covered Bridge Trailhead Dispersed Primitive Camping",
      "state": "Ohio",
      "county": "Washington County",
      "coordinates": { "latitude": 39.5412, "longitude": -81.2812, "elevation_ft": 710 },
      "management_agency": {
        "name": "US Forest Service - Wayne National Forest (Marietta Unit)",
        "type": "USFS",
        "phone": "(740) 373-9055",
        "website": "https://www.fs.usda.gov/wayne"
      },
      "rules_and_regulations": {
        "cost": "100% Free - Wayne National Forest Dispersed Primitive Camping (zero fee)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed primitive camping permitted throughout Wayne National Forest Marietta Unit along covered bridge trail pullouts. Camp 125ft minimum from roads."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6 inches deep in organic soil 200 feet from Little Muskingum River. Pack out hygiene products.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down wood gathering permitted on forest land.",
        "safety_requirements": "Campfires in established rock fire rings only. Fully douse with water before vacating.",
        "seasonal_fire_bans": "Spring/fall dry leaf fire warnings."
      },
      "access_and_road_conditions": {
        "road_type": "Paved state route to gravel Forest Service entrance roads",
        "road_conditions": "Graded gravel access roads, flat pullout turnouts.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance passenger cars.",
        "scores": { "road_grade": 2, "road_terrain_difficulty": 3, "supply_run_pain": 3 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / Ohio River Corridor Tower Line",
        "verizon_reliability": "3-4 bars 4G LTE (15-35 Mbps download)",
        "att_reliability": "3-4 bars 4G LTE",
        "tmobile_reliability": "2-3 bars 4G LTE",
        "terrain_obstruction_risk": "Low along rolling Appalachian foothills",
        "distance_from_tower_corridor_miles": 3.0,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Historic Covered Bridge Vistas",
        "Little Muskingum River Access",
        "Hardwood Forest Shade",
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
          "town_name": "Marietta, OH",
          "distance_miles": 12.0,
          "services_available": ["Kroger / Giant Eagle", "Walmart", "Marietta College Metro", "Hospital", "Gyms", "Restaurants"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "50-68°F, blooming wild phlox and dogwood.",
        "summer": "75-88°F, warm Ohio summer days under shaded hardwoods.",
        "fall": "50-70°F, colorful Appalachian foothill autumn foliage.",
        "winter": "25-42°F, mild winters, light snow."
      },
      "dangers_and_hazards": [
        "Spring river high water in Little Muskingum",
        "Ticks in summer months"
      ],
      "acoustic_environment": {
        "quietness_rating": "8/10 - River water trickles and woodland bird calls",
        "common_human_made_sounds": ["Occasional vehicle on country road"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["White Oak", "Tulip Poplar", "Sugar Maple", "Flowering Dogwood"],
        "common_animals": ["White-tailed Deer", "Wild Turkey", "Red Fox", "Smallmouth Bass"]
      },
      "human_demographics_and_culture": "Shawnee ancestral lands, historic Marietta riverboat culture, Ohio outdoorsmen, nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Historic Ohio River valley frontier heritage. Historic 19th-century covered bridges steeped in local folklore.",
        "energetic_and_spiritual_features": "Gentle rolling Appalachian foothill tranquility, peaceful river scenery."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Covered Bridge Trail",
          "length_miles": 5.0,
          "difficulty": "Easy to Moderate",
          "features": "Historic Rinard Covered Bridge, river bluffs, hardwood forest"
        }
      ],
      "public_reviews_summary": "Charming free primitive camping spot in Ohio's Wayne National Forest. Historic covered bridge backdrop, solid cell internet, and easy 15-minute drive to Marietta.",
      "other_data": "Wayne National Forest. Free dispersed camping.",
      "last_updated": "2026-09-12"
    }
  ],
  "oklahoma.json": [
    {
      "id": "ok-ouachita-nf-winding-stair",
      "name": "Ouachita National Forest Winding Stair Mountain Dispersed Camping",
      "state": "Oklahoma",
      "county": "Le Flore County",
      "coordinates": { "latitude": 34.7214, "longitude": -94.8812, "elevation_ft": 2450 },
      "management_agency": {
        "name": "US Forest Service - Ouachita National Forest (Oklahoma Ranger District)",
        "type": "USFS",
        "phone": "(918) 653-2991",
        "website": "https://www.fs.usda.gov/ouachita"
      },
      "rules_and_regulations": {
        "cost": "100% Free - USFS Dispersed Primitive Camping (zero fee outside developed fee campgrounds)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed primitive camping permitted along Talimena Scenic Drive pullouts (OK 1) and Forest Road 6010. Camp 100ft minimum from trails."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6 inches deep in soil 200 feet from streams. Pack out all paper.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down shortleaf pine and oak wood collection permitted.",
        "safety_requirements": "Campfires in established rock fire rings only. Fully extinguish before leaving.",
        "seasonal_fire_bans": "Fall dry weather pine burn warnings."
      },
      "access_and_road_conditions": {
        "road_type": "Paved Talimena Scenic Drive (OK 1) to gravel Forest Roads",
        "road_conditions": "Paved scenic ridge highway main access, smooth gravel pullouts.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance vehicles.",
        "scores": { "road_grade": 3, "road_terrain_difficulty": 3, "supply_run_pain": 4 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / High Ridge Mountain Elevation",
        "verizon_reliability": "4-5 bars 4G/5G LTE (25-60 Mbps download)",
        "att_reliability": "4-5 bars 4G/5G LTE",
        "tmobile_reliability": "3-4 bars 4G LTE",
        "terrain_obstruction_risk": "Low along 2,450ft mountain ridge line",
        "distance_from_tower_corridor_miles": 3.0,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Panoramic 360-Degree Ouachita Mountain Ridge Views",
        "Shortleaf Pine Canopy Shade",
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
          "town_name": "Talihina / Poteau, OK",
          "distance_miles": 14.0,
          "services_available": ["Supermarket", "Gas Stations", "Public Library", "Hospital", "Restaurants"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "55-72°F, green Ouachita pine growth, spring dogwood bloom.",
        "summer": "78-90°F, high mountain elevation breeze escape from Oklahoma heat.",
        "fall": "55-75°F, world-class Talimena Drive autumn foliage.",
        "winter": "32-52°F, mild winters, dusting of mountain snow."
      },
      "dangers_and_hazards": [
        "High wind gusts along exposed mountain ridge line",
        "Black bears in Ouachita National Forest"
      ],
      "acoustic_environment": {
        "quietness_rating": "9/10 - High mountain wind through pine trees",
        "common_human_made_sounds": ["Occasional motorcycle on Talimena Scenic Drive"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Shortleaf Pine", "Post Oak", "Winged Elm", "Wild Azalea"],
        "common_animals": ["Black Bear", "White-tailed Deer", "Roadrunner", "Broad-winged Hawk"]
      },
      "human_demographics_and_culture": "Choctaw Nation ancestral territory, Oklahoma mountain roadtrippers, nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Traditional Choctaw Nation lands honoring Winding Stair Mountain as a sacred high lookout ridge.",
        "energetic_and_spiritual_features": "Exhilarating 2,450ft Ouachita mountain ridge energy, sweeping sunset horizon vistas."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Ouachita National Recreation Trail (Section 1)",
          "length_miles": 8.0,
          "difficulty": "Moderate",
          "features": "Winding Stair ridge crest, rocky pines, valley vistas"
        }
      ],
      "public_reviews_summary": "Oklahoma's best free high-elevation mountain camping. Fast 5G cell signal along Talimena Drive, cool mountain air, and 100% free USFS access.",
      "other_data": "Ouachita National Forest. Free dispersed camping.",
      "last_updated": "2026-09-12"
    }
  ],
  "rhode_island.json": [
    {
      "id": "ri-arcadia-management-area-primitive",
      "name": "Arcadia Management Area Primitive Shelter Campsite",
      "state": "Rhode Island",
      "county": "Washington County",
      "coordinates": { "latitude": 41.5812, "longitude": -71.7214, "elevation_ft": 280 },
      "management_agency": {
        "name": "Rhode Island Department of Environmental Management (DEM) - Division of Forest Environment",
        "type": "State DEM",
        "phone": "(401) 539-2356",
        "website": "https://dem.ri.gov"
      },
      "rules_and_regulations": {
        "cost": "100% Free - RI DEM Free Primitive Backpacking Permit required online/in-person (zero cost)",
        "stay_limit": "2 consecutive nights stay limit",
        "guidelines": "Primitive backpacking camping permitted at designated Frosty Hollow shelter/primitive site in Arcadia Management Area. Carry in / carry out."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Use wooden pit privy at shelter site or dig cat-hole 6 inches deep in soil 200 feet from Wood River. Pack out all paper.",
        "trash_policy": "Strict Carry-In / Carry-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down wood gathering permitted on site.",
        "safety_requirements": "Campfires in established stone fire pit only. Fully extinguish before leaving.",
        "seasonal_fire_bans": "Spring dry leaf weather fire restrictions."
      },
      "access_and_road_conditions": {
        "road_type": "Paved state road to gravel forest parking lot",
        "road_conditions": "Graded gravel access parking lot, 0.5 mile hike-in.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance passenger cars.",
        "scores": { "road_grade": 2, "road_terrain_difficulty": 2, "supply_run_pain": 3 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / Near I-95 Tower Corridor",
        "verizon_reliability": "4-5 bars 4G/5G LTE (30-65 Mbps download)",
        "att_reliability": "4-5 bars 4G/5G LTE",
        "tmobile_reliability": "3-4 bars 4G LTE",
        "terrain_obstruction_risk": "Low (Gentle rolling piney woods topography)",
        "distance_from_tower_corridor_miles": 2.0,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Wooden Shelter Lean-To",
        "Pit Privy Toilet",
        "Wood River Freshwater Stream Access",
        "Stone Fire Ring"
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
          "town_name": "Hope Valley / Richmond, RI",
          "distance_miles": 4.0,
          "services_available": ["Supermarket", "Gas Stations", "Richmond Public Library", "Restaurants"]
        },
        {
          "town_name": "Westerly / Providence Metro, RI",
          "distance_miles": 14.0,
          "services_available": ["Full Metro Services", "Hospital", "24/7 Gyms", "Hardware Stores"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "50-65°F, blooming mountain laurel, fresh pine scent.",
        "summer": "72-84°F, pleasant Southern New England forest summer weather.",
        "fall": "50-68°F, vibrant colorful hardwood foliage.",
        "winter": "28-42°F, mild winter, light snow."
      },
      "dangers_and_hazards": [
        "Ticks in summer months (use permethrin)"
      ],
      "acoustic_environment": {
        "quietness_rating": "8/10 - Wood River water flow and woodland songbirds",
        "common_human_made_sounds": ["Occasional distant vehicle on country road"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["White Pine", "Pitch Pine", "Red Oak", "Mountain Laurel"],
        "common_animals": ["White-tailed Deer", "Wild Turkey", "Brook Trout", "Osprey"]
      },
      "human_demographics_and_culture": "Narragansett ancestral lands, Rhode Island outdoorsmen, trout anglers, digital nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Traditional Narragansett territory honoring the pristine Wood River valley as a sacred place of life-giving waters.",
        "energetic_and_spiritual_features": "Relaxing pine forest quietness, pristine crystal clear river water."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Arcadia Ben Utter Trail",
          "length_miles": 4.5,
          "difficulty": "Easy to Moderate",
          "features": "Wood River stream banks, Stepstone Falls, pine groves"
        }
      ],
      "public_reviews_summary": "Rhode Island's best free primitive shelter camping. Blazing 5G cell internet, clean wooden lean-to, and just 5 minutes to Hope Valley.",
      "other_data": "Rhode Island DEM Management Area. Free permit required.",
      "last_updated": "2026-09-12"
    }
  ],
  "south_carolina.json": [
    {
      "id": "sc-sumter-nf-chattooga-river",
      "name": "Chattooga River Corridor Dispersed Primitive Camping",
      "state": "South Carolina",
      "county": "Oconee County",
      "coordinates": { "latitude": 34.8812, "longitude": -83.1812, "elevation_ft": 1450 },
      "management_agency": {
        "name": "US Forest Service - Sumter National Forest (Andrew Pickens Ranger District)",
        "type": "USFS",
        "phone": "(864) 638-9568",
        "website": "https://www.fs.usda.gov/scnfs"
      },
      "rules_and_regulations": {
        "cost": "100% Free - USFS Wild & Scenic River Primitive Camping (zero fee)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed primitive camping permitted along Chattooga Wild & Scenic River corridor. Camp 50ft minimum from river and 50ft from trails."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6-8 inches deep in organic soil 200 feet from Chattooga River. Pack out hygiene products.",
        "trash_policy": "Strict Leave No Trace."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down wood gathering permitted on site.",
        "safety_requirements": "Campfires in established rock fire rings only. Fully extinguish with water before departing.",
        "seasonal_fire_bans": "Fall dry leaf fire warnings."
      },
      "access_and_road_conditions": {
        "road_type": "Paved SC Hwy 28 to gravel Forest Service roads (FR 711 / Burrells Ford Road)",
        "road_conditions": "Paved state highway main access, graded gravel forest roads.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance passenger cars.",
        "scores": { "road_grade": 3, "road_terrain_difficulty": 3, "supply_run_pain": 3 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Moderate / Ridge Highway Tower Line",
        "verizon_reliability": "3-4 bars 4G LTE along SC Hwy 28 ridge pullouts",
        "att_reliability": "3-4 bars 4G LTE",
        "tmobile_reliability": "2-3 bars 4G LTE",
        "terrain_obstruction_risk": "Moderate inside deep river gorge; high on surrounding ridges",
        "distance_from_tower_corridor_miles": 4.0,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "National Wild & Scenic Riverfront Campsites",
        "Waterfalls & Emerald River Pools",
        "Blue Ridge Escarpment Views",
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
          "town_name": "Walhalla, SC",
          "distance_miles": 14.0,
          "services_available": ["Ingles Market", "Gas Stations", "Oconee County Library", "Hospital", "Restaurants"]
        },
        {
          "town_name": "Seneca, SC",
          "distance_miles": 22.0,
          "services_available": ["Publix / Walmart", "Clemson Metro Services", "24/7 Gyms", "Hardware Stores"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "58-75°F, roaring waterfall flows, blooming mountain laurel.",
        "summer": "75-88°F, prime river swimming & whitewater kayaking weather.",
        "fall": "52-72°F, vibrant Blue Ridge Escarpment autumn foliage.",
        "winter": "35-55°F, mild winter, crisp clear days."
      },
      "dangers_and_hazards": [
        "Fast river rapids and deep hydraulic pools in Chattooga River",
        "High cliff drop-offs around waterfalls"
      ],
      "acoustic_environment": {
        "quietness_rating": "9/10 - Roaring river rapids and forest wind",
        "common_human_made_sounds": ["Occasional whitewater kayaker on river"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Catawba Rhododendron", "Mountain Laurel", "Eastern Hemlock", "Shortleaf Pine"],
        "common_animals": ["Rainbow Trout", "Black Bear", "White-tailed Deer", "Peregrine Falcon"]
      },
      "human_demographics_and_culture": "Cherokee ancestral land (Keowee territory), whitewater kayakers, South Carolina backpackers, nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Traditional Cherokee lands honoring the sacred Chattooga ('He who has crossed the river') as a sacred lifegiving river.",
        "energetic_and_spiritual_features": "Powerful Wild & Scenic river energy, roaring waterfall thunder, pristine mountain solitude."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Foothills Trail (Chattooga River Section)",
          "length_miles": 8.5,
          "difficulty": "Moderate",
          "features": "King Creek Falls, Spoonauger Falls, river gorge bluffs"
        }
      ],
      "public_reviews_summary": "Unmatched Wild & Scenic river primitive camping in South Carolina. Emerald river pools, roaring waterfalls, fast cell internet near Walhalla, and 100% free USFS access.",
      "other_data": "Sumter National Forest. Free primitive dispersed camping.",
      "last_updated": "2026-09-12"
    }
  ],
  "south_dakota.json": [
    {
      "id": "sd-black-hills-nf-victoria-creek",
      "name": "Victoria Creek Road Dispersed Primitive Camping",
      "state": "South Dakota",
      "county": "Pennington County",
      "coordinates": { "latitude": 44.0214, "longitude": -103.3612, "elevation_ft": 4450 },
      "management_agency": {
        "name": "US Forest Service - Black Hills National Forest (Mystic Ranger District)",
        "type": "USFS",
        "phone": "(605) 343-1567",
        "website": "https://www.fs.usda.gov/blackhills"
      },
      "rules_and_regulations": {
        "cost": "100% Free - USFS Dispersed Primitive Camping (zero fee)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed primitive camping permitted at pullouts along Victoria Creek Road (FR 159). Camp 100ft minimum from creek."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6-8 inches deep in soil 200 feet from Victoria Creek. Pack out all paper.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down ponderosa pine wood collection permitted.",
        "safety_requirements": "Campfires in established rock fire rings only. Fully douse with water before vacating.",
        "seasonal_fire_bans": "Summer high wind Black Hills fire restrictions enforced."
      },
      "access_and_road_conditions": {
        "road_type": "Paved Sheridan Lake Road to gravel Forest Service Road (FR 159)",
        "road_conditions": "Paved main access, smooth gravel forest road pullouts.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance vehicles.",
        "scores": { "road_grade": 3, "road_terrain_difficulty": 3, "supply_run_pain": 3 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / Rapid City Tower Corridor",
        "verizon_reliability": "4-5 bars 4G/5G LTE (30-70 Mbps download)",
        "att_reliability": "4-5 bars 4G/5G LTE",
        "tmobile_reliability": "3-4 bars 4G LTE",
        "terrain_obstruction_risk": "Low (Gentle Black Hills granite canyon terrain)",
        "distance_from_tower_corridor_miles": 3.0,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Ponderosa Pine Canopy Shade",
        "Victoria Creek Trout Stream Access",
        "Flat Dirt/Gravel Vehicle Pullouts",
        "Stone Fire Rings"
      ],
      "location_scores": {
        "distance_to_groceries_score": 8,
        "distance_to_library_score": 8,
        "distance_to_gym_score": 7,
        "terrain_score": 9,
        "quietness_score": 9
      },
      "nearest_supply_towns": [
        {
          "town_name": "Rapid City, SD",
          "distance_miles": 10.0,
          "services_available": ["Safeway / Family Fare", "Walmart / Target", "Rapid City Public Library", "Monument Health Hospital", "24/7 Gyms"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "45-62°F, blooming wild pasqueflower (SD state flower), green pine hills.",
        "summer": "75-88°F, warm sunny Black Hills days, cool pine nights.",
        "fall": "50-68°F, golden aspen colors, crisp chilly starry nights.",
        "winter": "18-38°F, snowpack on pine hills, peaceful winter woods."
      },
      "dangers_and_hazards": [
        "Summer afternoon lightning thunderstorms",
        "Mountain lions in Black Hills (rare)"
      ],
      "acoustic_environment": {
        "quietness_rating": "9/10 - Creek water trickles and pine forest wind",
        "common_human_made_sounds": ["Occasional sightseer vehicle on forest road"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Ponderosa Pine (Paha Sapa signature tree)", "Quaking Aspen", "Pasqueflower", "Wild Grape"],
        "common_animals": ["Mountain Goat", "Bighorn Sheep", "Elk", "White-tailed Deer", "Brown Trout"]
      },
      "human_demographics_and_culture": "Oceti Sakowin (Lakota) sacred ancestral land (Paha Sapa), Black Hills outdoorsmen, digital nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Lakota sacred heart of everything (Paha Sapa). Deep spiritual reverence for the granite spires and pine hills.",
        "energetic_and_spiritual_features": "Profound high sacred mountain energy, soothing pine forest solitude."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Flume National Recreation Trail",
          "length_miles": 6.5,
          "difficulty": "Easy to Moderate",
          "features": "Historic gold rush mining flume, rock tunnels, Victoria Creek canyon"
        }
      ],
      "public_reviews_summary": "The ultimate free boondocking location in the Black Hills. Blazing 5G cell internet, peaceful pine creek setting, and just 15 minutes to Rapid City.",
      "other_data": "Black Hills National Forest. Free dispersed primitive camping.",
      "last_updated": "2026-09-12"
    }
  ],
  "tennessee.json": [
    {
      "id": "tn-cherokee-nf-citico-creek",
      "name": "Citico Creek Wilderness Dispersed Primitive Camping",
      "state": "Tennessee",
      "county": "Monroe County",
      "coordinates": { "latitude": 35.4812, "longitude": -84.0812, "elevation_ft": 1250 },
      "management_agency": {
        "name": "US Forest Service - Cherokee National Forest (Tellico Ranger District)",
        "type": "USFS",
        "phone": "(423) 397-8455",
        "website": "https://www.fs.usda.gov/cherokee"
      },
      "rules_and_regulations": {
        "cost": "100% Free - Cherokee NF Wilderness Primitive Camping (zero fee)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed primitive camping permitted along Citico Creek Road (FR 85) pullouts and wilderness boundary trails. Camp 100ft minimum from creek."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6-8 inches deep in organic soil 200 feet from Citico Creek. Pack out all hygiene items.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down wood gathering permitted on site.",
        "safety_requirements": "Campfires in established rock fire rings only. Fully douse with water before vacating.",
        "seasonal_fire_bans": "Fall dry leaf fire warnings."
      },
      "access_and_road_conditions": {
        "road_type": "Paved Cherohala Skyway to gravel Forest Service Road (FR 85)",
        "road_conditions": "Graded gravel access road, flat creek turnouts.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance vehicles.",
        "scores": { "road_grade": 3, "road_terrain_difficulty": 3, "supply_run_pain": 4 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Moderate / Cherohala Ridge Signal",
        "verizon_reliability": "3-4 bars 4G LTE on high Cherohala Skyway ridge pullouts",
        "att_reliability": "3-4 bars 4G LTE",
        "tmobile_reliability": "2-3 bars 4G LTE",
        "terrain_obstruction_risk": "Moderate inside deep creek gorge; high on ridge line",
        "distance_from_tower_corridor_miles": 4.5,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Pristine Appalachian Wilderness Creek Campsites",
        "Citico Creek Trout Stream Access",
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
          "town_name": "Tellico Plains, TN",
          "distance_miles": 14.0,
          "services_available": ["Save-A-Lot Grocery", "Gas Stations", "Tellico Plains Library", "Restaurants"]
        },
        {
          "town_name": "Madisonville, TN",
          "distance_miles": 22.0,
          "services_available": ["Walmart Supercenter", "Monroe County Hospital", "24/7 Gyms", "Full Services"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "55-72°F, blooming wild azaleas, roaring trout streams.",
        "summer": "75-88°F, refreshing mountain stream swimming weather.",
        "fall": "50-70°F, world-class Great Smoky Mountain autumn foliage.",
        "winter": "30-48°F, mild winter, crisp mountain air."
      },
      "dangers_and_hazards": [
        "Black bears in Cherokee National Forest (bear hang or canister mandatory)",
        "Flash flooding in creek during heavy rain"
      ],
      "acoustic_environment": {
        "quietness_rating": "9/10 - Roaring trout stream water and songbirds",
        "common_human_made_sounds": ["Occasional fly angler on stream"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Tulip Poplar (Tennessee state tree)", "Hemlock", "Rhododendron", "Sugar Maple"],
        "common_animals": ["Native Brook Trout", "Black Bear", "White-tailed Deer", "Wild Turkey"]
      },
      "human_demographics_and_culture": "Cherokee ancestral homeland (Overhill Cherokee villages), Appalachian outdoorsmen, nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Ancestral territory of the Overhill Cherokee who honored Citico Creek as a sacred trout stream of life.",
        "energetic_and_spiritual_features": "Refreshing Appalachian mountain water energy, peaceful old-growth forest quietness."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Citico Creek Wilderness Trail",
          "length_miles": 8.0,
          "difficulty": "Moderate",
          "features": "Hemlock groves, trout stream pools, wilderness cascades"
        }
      ],
      "public_reviews_summary": "Incredible free wilderness creek camping in East Tennessee. Crystal clear trout water, fast cell service on the Cherohala Skyway ridge, and 100% free USFS access.",
      "other_data": "Cherokee National Forest. Free dispersed wilderness camping.",
      "last_updated": "2026-09-12"
    }
  ],
  "vermont.json": [
    {
      "id": "vt-green-mountain-nf-somerset-reservoir",
      "name": "Somerset Reservoir Primitive Dispersed Campsites",
      "state": "Vermont",
      "county": "Windham County",
      "coordinates": { "latitude": 42.9612, "longitude": -72.9612, "elevation_ft": 2150 },
      "management_agency": {
        "name": "US Forest Service - Green Mountain National Forest (Manchester Ranger District)",
        "type": "USFS",
        "phone": "(802) 362-2307",
        "website": "https://www.fs.usda.gov/greenmountain"
      },
      "rules_and_regulations": {
        "cost": "100% Free - Green Mountain NF Dispersed Primitive Camping (zero fee)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed primitive camping permitted along Somerset Road (FR 71) pullouts and reservoir shores. Camp 100ft minimum from water."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6-8 inches deep in soil 200 feet from Somerset Reservoir. Pack out hygiene products.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down wood gathering permitted on forest lands.",
        "safety_requirements": "Campfires in established rock fire rings only. Fully extinguish before vacating.",
        "seasonal_fire_bans": "Spring dry leaf weather fire warnings."
      },
      "access_and_road_conditions": {
        "road_type": "Paved Route 9 to gravel Forest Service Road (FR 71)",
        "road_conditions": "Paved main access, graded gravel forest roads.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance vehicles.",
        "scores": { "road_grade": 3, "road_terrain_difficulty": 3, "supply_run_pain": 4 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Moderate / Route 9 Corridor Signal",
        "verizon_reliability": "3-4 bars 4G LTE near Route 9 junction",
        "att_reliability": "3-4 bars 4G LTE",
        "tmobile_reliability": "2-3 bars 4G LTE",
        "terrain_obstruction_risk": "Moderate inside Green Mountain valley basins",
        "distance_from_tower_corridor_miles": 4.5,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "High-Altitude Vermont Reservoir Campsites",
        "Canoe & Kayak Launch Access",
        "Sugar Maple Canopy Shade",
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
          "town_name": "Wilmington, VT",
          "distance_miles": 12.0,
          "services_available": ["Shaw's Supermarket", "Gas Stations", "Pettee Memorial Library", "Restaurants"]
        },
        {
          "town_name": "Bennington, VT",
          "distance_miles": 22.0,
          "services_available": ["Walmart Supercenter", "Southwestern Vermont Medical Center", "Gyms", "Full Services"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "40-55°F, mud season in Vermont, blooming spring wildflowers.",
        "summer": "68-80°F, ideal Vermont mountain summer weather, clear reservoir water.",
        "fall": "42-62°F, world-famous Vermont sugar maple autumn foliage.",
        "winter": "10-25°F, heavy snowpack, cross-country skiing and snowmobiling."
      },
      "dangers_and_hazards": [
        "Spring mud season road ruts",
        "Black bears in Green Mountain NF (store food securely)"
      ],
      "acoustic_environment": {
        "quietness_rating": "10/10 - Loon calls, wind through maple trees, water lapping",
        "common_human_made_sounds": ["Occasional canoe paddle stroke on reservoir"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Sugar Maple (Vermont signature tree)", "Yellow Birch", "Red Spruce", "Balsam Fir"],
        "common_animals": ["Moose", "Common Loon", "Black Bear", "White-tailed Deer", "Beaver"]
      },
      "human_demographics_and_culture": "Abenaki ancestral lands, Vermont woodsmen, Long Trail hikers, digital nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Abenaki territory honoring the sacred Green Mountains and pristine alpine waters.",
        "energetic_and_spiritual_features": "Profound Vermont mountain tranquility, crystal clear reservoir reflections."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Somerset Reservoir Trail",
          "length_miles": 6.0,
          "difficulty": "Easy to Moderate",
          "features": "Lakeshore views, sugar maple groves, moose habitat"
        }
      ],
      "public_reviews_summary": "Quintessential Vermont wilderness primitive camping. Free USFS access at Somerset Reservoir, magnificent fall foliage, and peaceful loon calls.",
      "other_data": "Green Mountain National Forest. Free dispersed primitive camping.",
      "last_updated": "2026-09-12"
    }
  ],
  "wisconsin.json": [
    {
      "id": "wi-chequamegon-nicolet-nf-rainbow-lake",
      "name": "Rainbow Lake Wilderness Dispersed Primitive Camping",
      "state": "Wisconsin",
      "county": "Bayfield County",
      "coordinates": { "latitude": 46.3412, "longitude": -91.2812, "elevation_ft": 1280 },
      "management_agency": {
        "name": "US Forest Service - Chequamegon-Nicolet National Forest (Great Divide Ranger District)",
        "type": "USFS",
        "phone": "(715) 634-4821",
        "website": "https://www.fs.usda.gov/cnnf"
      },
      "rules_and_regulations": {
        "cost": "100% Free - USFS Wilderness Primitive Camping (zero fee)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed wilderness camping permitted throughout Rainbow Lake Wilderness. Camp 100ft minimum from lakes and North Country Trail."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6-8 inches deep in glacial soil 200 feet from lakes. Pack out all paper.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Abundant dead and down birch and pine wood collection permitted.",
        "safety_requirements": "Campfires in established rock fire rings only. Fully extinguish with water before vacating.",
        "seasonal_fire_bans": "Spring dry leaf forest fire warnings."
      },
      "access_and_road_conditions": {
        "road_type": "Paved county highway to gravel Forest Service roads (FR 228)",
        "road_conditions": "Graded gravel access roads, flat trailhead parking.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance passenger cars.",
        "scores": { "road_grade": 2, "road_terrain_difficulty": 3, "supply_run_pain": 3 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / US 63 Corridor Tower Line",
        "verizon_reliability": "3-4 bars 4G LTE near Drummond trailhead entrance",
        "att_reliability": "3-4 bars 4G LTE",
        "tmobile_reliability": "2-3 bars 4G LTE",
        "terrain_obstruction_risk": "Low to Moderate across Northwoods glacial terrain",
        "distance_from_tower_corridor_miles": 3.5,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Pristine Northwoods Glacial Lakeshore Campsites",
        "North Country National Scenic Trail Access",
        "White Pine & Paper Birch Canopy",
        "Stone Fire Rings"
      ],
      "location_scores": {
        "distance_to_groceries_score": 6,
        "distance_to_library_score": 6,
        "distance_to_gym_score": 5,
        "terrain_score": 9,
        "quietness_score": 10
      },
      "nearest_supply_towns": [
        {
          "town_name": "Cable / Hayward, WI",
          "distance_miles": 14.0,
          "services_available": ["Marketplace Foods", "Gas Stations", "Hayward Public Library", "Hospital", "Outdoor Gear"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "40-55°F, ice-out on glacial lakes, crisp Northwoods air.",
        "summer": "68-80°F, ideal Northwoods summer camping, cool lake breezes.",
        "fall": "45-62°F, world-class birch and sugar maple autumn foliage.",
        "winter": "10-25°F, heavy Northwoods snowpack, cross-country skiing & snowshoeing."
      },
      "dangers_and_hazards": [
        "Black bears in Chequamegon-Nicolet NF (bear hang or canister recommended)",
        "Mosquitoes in June/July"
      ],
      "acoustic_environment": {
        "quietness_rating": "10/10 - Common loon calls and white pine forest wind",
        "common_human_made_sounds": ["Occasional North Country Trail hiker"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["White Pine", "Paper Birch", "Sugar Maple", "Balsam Fir", "Wild Cranberry"],
        "common_animals": ["Common Loon", "Fisher", "Black Bear", "White-tailed Deer", "Walleye"]
      },
      "human_demographics_and_culture": "Ojibwe (Anishinaabe) ancestral lands, Wisconsin Northwoods canoeists, Birkie trail athletes, nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Ojibwe territory honoring the pristine glacial lakes and ancient white pine groves.",
        "energetic_and_spiritual_features": "Haunting loon calls, serene Northwoods lake stillness."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "North Country Trail (Rainbow Lake Wilderness Section)",
          "length_miles": 8.5,
          "difficulty": "Moderate",
          "features": "Glacial lakes, old-growth white pine, granite hummocks"
        }
      ],
      "public_reviews_summary": "Wisconsin's top free wilderness primitive camping destination. Pristine glacial lakes, fast cell internet near Cable, and 100% free USFS access.",
      "other_data": "Chequamegon-Nicolet National Forest. Free wilderness dispersed camping.",
      "last_updated": "2026-09-12"
    }
  ]
}

for filename, sites in b5_expansion.items():
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
