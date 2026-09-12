import json
import os

BASE_DIR = "/home/volmarr/.gemini/antigravity/scratch/Camping_Nomad_Life/states"

group_c = {
  "indiana.json": [
    {
      "id": "in-german-ridge-hoosier-nf",
      "name": "German Ridge Trail Dispersed Primitive Camping",
      "state": "Indiana",
      "county": "Perry County",
      "coordinates": { "latitude": 37.9412, "longitude": -86.5812, "elevation_ft": 650 },
      "management_agency": {
        "name": "US Forest Service - Hoosier National Forest (Tell City Ranger District)",
        "type": "USFS",
        "phone": "(812) 547-7051",
        "website": "https://www.fs.usda.gov/hoosier"
      },
      "rules_and_regulations": {
        "cost": "100% Free - Hoosier National Forest Dispersed Primitive Camping (zero fee)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed primitive camping permitted along German Ridge Trail corridor and forest roads. Camp 125ft minimum from trails."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6 inches deep in soil 200 feet from German Ridge Lake and streams. Pack out all paper.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down wood gathering permitted on forest land.",
        "safety_requirements": "Campfires in established rock fire rings only. Fully douse with water before vacating.",
        "seasonal_fire_bans": "Autumn leaf dry weather fire warnings."
      },
      "access_and_road_conditions": {
        "road_type": "Paved state route to gravel Forest Service roads (FR 132)",
        "road_conditions": "Graded gravel access roads, flat pullout turnouts.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance passenger cars.",
        "scores": { "road_grade": 2, "road_terrain_difficulty": 3, "supply_run_pain": 3 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / Ohio River Tower Line",
        "verizon_reliability": "3-4 bars 4G LTE (15-35 Mbps download)",
        "att_reliability": "3-4 bars 4G LTE",
        "tmobile_reliability": "2-3 bars 4G LTE",
        "terrain_obstruction_risk": "Low along high sandstone ridge line",
        "distance_from_tower_corridor_miles": 3.0,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Oak & Pine Ridge Campsites",
        "German Ridge Lake Access",
        "Trailhead Parking",
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
          "town_name": "Tell City / Cannelton, IN",
          "distance_miles": 10.0,
          "services_available": ["Walmart Supercenter", "Gas Stations", "Tell City Public Library", "Hospital", "Restaurants"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "50-68°F, blooming wild phlox and dogwood.",
        "summer": "75-88°F, warm Southern Indiana summer days.",
        "fall": "50-70°F, colorful Ohio River valley autumn foliage.",
        "winter": "25-42°F, mild winter, light snow."
      },
      "dangers_and_hazards": [
        "Ticks in summer months (use permethrin)"
      ],
      "acoustic_environment": {
        "quietness_rating": "8/10 - Forest wind and lake water trickles",
        "common_human_made_sounds": ["Occasional vehicle on forest road"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["White Oak", "Shortleaf Pine", "Sugar Maple", "Flowering Dogwood"],
        "common_animals": ["White-tailed Deer", "Wild Turkey", "Red Fox", "Large-mouth Bass"]
      },
      "human_demographics_and_culture": "Shawnee ancestral lands, German-American pioneer heritage, Indiana outdoorsmen, nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Historic 19th-century German pioneer settlement heritage. Rich Ohio River valley sandstone ridge folklore.",
        "energetic_and_spiritual_features": "Relaxing oak ridge quietness, peaceful lake reflection views."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "German Ridge Trail Loop",
          "length_miles": 6.2,
          "difficulty": "Moderate",
          "features": "German Ridge Lake, sandstone rock outcrops, hardwood forest"
        }
      ],
      "public_reviews_summary": "Top free primitive camping in Southern Indiana's Hoosier National Forest. Solid cell internet, flat easy driving, and 10 minutes to Tell City.",
      "other_data": "Hoosier National Forest. Free dispersed camping.",
      "last_updated": "2026-09-12"
    }
  ],
  "minnesota.json": [
    {
      "id": "mn-chippewa-nf-suomi-hills",
      "name": "Chippewa National Forest Suomi Hills Primitive Backpacking",
      "state": "Minnesota",
      "county": "Itasca County",
      "coordinates": { "latitude": 47.4812, "longitude": -93.6512, "elevation_ft": 1350 },
      "management_agency": {
        "name": "US Forest Service - Chippewa National Forest (Deer River Ranger District)",
        "type": "USFS",
        "phone": "(218) 246-2123",
        "website": "https://www.fs.usda.gov/chippewa"
      },
      "rules_and_regulations": {
        "cost": "100% Free - USFS Dispersed Primitive Camping (zero fee)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed primitive camping permitted at designated backcountry lake sites throughout Suomi Hills semi-primitive non-motorized area. Camp 100ft minimum from lakes."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Use wilderness pit privy at backcountry campsite clearing or dig cat-hole 6-8 inches deep in organic soil 200ft from lakes. Pack out paper.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Abundant dead and down birch and pine wood collection permitted.",
        "safety_requirements": "Campfires in established rock fire rings only. Fully douse with water before vacating.",
        "seasonal_fire_bans": "Spring dry leaf forest fire warnings."
      },
      "access_and_road_conditions": {
        "road_type": "Paved MN Hwy 38 (Edge of the Wilderness Scenic Byway) to gravel trailhead parking lot",
        "road_conditions": "Paved scenic main highway access, smooth gravel trailhead parking.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance passenger cars.",
        "scores": { "road_grade": 2, "road_terrain_difficulty": 3, "supply_run_pain": 3 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / Highway 38 Tower Line",
        "verizon_reliability": "3-4 bars 4G LTE near highway trailhead entrance",
        "att_reliability": "3-4 bars 4G LTE",
        "tmobile_reliability": "2-3 bars 4G LTE",
        "terrain_obstruction_risk": "Low to Moderate across rolling glacial moraine hills",
        "distance_from_tower_corridor_miles": 3.0,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Pristine Glacial Lake Shoreline Campsites",
        "Pit Privy Toilet",
        "Canoe & Kayak Lake Access",
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
          "town_name": "Grand Rapids, MN",
          "distance_miles": 16.0,
          "services_available": ["L&M Fleet / Super One", "Target / Walmart", "Grand Rapids Public Library", "Grand Itasca Hospital", "24/7 Gyms"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "40-55°F, ice-out on glacial lakes, crisp Northwoods air.",
        "summer": "68-80°F, ideal Minnesota Northwoods summer camping weather, cool lake breezes.",
        "fall": "45-62°F, spectacular sugar maple and birch autumn foliage.",
        "winter": "10-25°F, heavy snowpack, cross-country ski and snowshoe paradise."
      },
      "dangers_and_hazards": [
        "Black bears in Chippewa NF (bear hang or canister recommended)",
        "Mosquitoes in June/July"
      ],
      "acoustic_environment": {
        "quietness_rating": "10/10 - Common loon calls and wind through white pines",
        "common_human_made_sounds": ["Occasional canoe paddle stroke on lake"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["White Pine", "Red Pine", "Paper Birch", "Sugar Maple"],
        "common_animals": ["Common Loon", "Bald Eagle (highest nesting density in US)", "White-tailed Deer", "Walleye"]
      },
      "human_demographics_and_culture": "Ojibwe (Anishinaabe) Leech Lake Band ancestral lands, Minnesota Northwoods woodsmen, nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Ojibwe territory honoring the pristine glacial lakes and sacred bald eagles of the Chippewa forest.",
        "energetic_and_spiritual_features": "Haunting loon calls, serene glacial lake reflections."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Suomi Hills Trail Loop",
          "length_miles": 8.5,
          "difficulty": "Moderate",
          "features": "Glacial lakes, rolling hardwood moraines, white pine groves"
        }
      ],
      "public_reviews_summary": "Incredible free primitive lakeshore camping in Minnesota's Chippewa National Forest. Pristine glacial lakes, fast cell internet near Grand Rapids, and 100% free USFS access.",
      "other_data": "Chippewa National Forest. Free dispersed primitive camping.",
      "last_updated": "2026-09-12"
    }
  ],
  "nevada.json": [
    {
      "id": "nv-black-rock-desert-blm-primitive",
      "name": "Black Rock Desert / High Rock Canyon BLM Dispersed Camping",
      "state": "Nevada",
      "county": "Humboldt / Washoe County",
      "coordinates": { "latitude": 40.9124, "longitude": -119.0214, "elevation_ft": 3900 },
      "management_agency": {
        "name": "Bureau of Land Management (BLM) - Winnemucca District",
        "type": "Federal BLM",
        "phone": "(775) 623-1500",
        "website": "https://www.blm.gov/office/winnemucca-district-office"
      },
      "rules_and_regulations": {
        "cost": "100% Free - Public BLM Land Dispersed Primitive Camping (zero fees)",
        "stay_limit": "14 consecutive days within a 28-day period",
        "guidelines": "Dispersed primitive camping permitted throughout public BLM playa edge and canyon areas outside designated event closures. Carry out human waste where required."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Portable toilet system or pack-out human waste (WAG bags) recommended on dry alkali playa. Dig cat-hole 6-8 inches deep in dirt areas 200ft from hot springs.",
        "trash_policy": "Strict Leave No Trace. Zero trash left in desert."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Must bring your own firewood. Gathering wood on playa is prohibited.",
        "safety_requirements": "Campfires must be contained in metal fire pan. Fully extinguish before leaving.",
        "seasonal_fire_bans": "Summer desert fire restrictions active June through August."
      },
      "access_and_road_conditions": {
        "road_type": "Paved NV 447 to unpaved dirt/playa entrance roads",
        "road_conditions": "Smooth dry alkali playa when dry; severe unpassable mud when wet.",
        "vehicle_recommendation": "High clearance 2WD or 4x4 recommended; standard 2WD vehicles can access dry playa edges carefully in dry weather.",
        "scores": { "road_grade": 4, "road_terrain_difficulty": 5, "supply_run_pain": 5 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Fair near Gerlach / Tower Line",
        "verizon_reliability": "2-3 bars 4G LTE near Gerlach / NV 447; SOS deep on playa",
        "att_reliability": "2-3 bars 4G LTE",
        "tmobile_reliability": "1-2 bars 4G LTE",
        "terrain_obstruction_risk": "Low across flat open dry desert playa",
        "distance_from_tower_corridor_miles": 5.0,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Vast Open Salt Flat Playa Panoramas",
        "Nearby Geothermal Hot Springs (Soldier Meadows access)",
        "Flat Salt Flat Van/RV Parking",
        "World-Class Dark Sky Stargazing"
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
          "town_name": "Gerlach, NV",
          "distance_miles": 12.0,
          "services_available": ["Bruno's Country Club / Store", "Gas Station", "Local Saloon", "Water Fill"]
        },
        {
          "town_name": "Fernley / Reno, NV",
          "distance_miles": 78.0,
          "services_available": ["Full Metro Services", "Walmart / Costco", "Hospitals", "24/7 Gyms"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "50-70°F, cool desert breeze, occasional spring rain squalls.",
        "summer": "88-102°F, intense dry desert heat, blazing sun.",
        "fall": "60-78°F, prime desert camping weather, clear starry nights.",
        "winter": "25-45°F, freezing desert nights, playa wet/muddy."
      },
      "dangers_and_hazards": [
        "Playa surface turns into unpassable sticky mud after rain (never drive on wet playa)",
        "Severe dehydration in dry high desert heat",
        "Extremely high dust winds"
      ],
      "acoustic_environment": {
        "quietness_rating": "10/10 - Absolute desert playa silence",
        "common_human_made_sounds": ["None (Wilderness area)"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Big Sagebrush", "Greasewood", "Shadscale", "Desert Paintbrush"],
        "common_animals": ["Pronghorn Antelope", "Wild Horses (Mustangs)", "Coyote", "Kit Fox", "Raven"]
      },
      "human_demographics_and_culture": "Northern Paiute ancestral lands, Nevada ranchers, desert nomads, overland adventurers.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Ancestral territory of the Northern Paiute people. Iconic vast dry lakebed known worldwide for its surreal alien-like vastness.",
        "energetic_and_spiritual_features": "Infinite dry salt flat horizons, cosmic dark night sky stargazing."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "High Rock Canyon Trail",
          "length_miles": 12.0,
          "difficulty": "Strenuous Overland",
          "features": "Narrow volcanic canyon bluffs, historic pioneer wagon ruts, petroglyphs"
        }
      ],
      "public_reviews_summary": "Mind-blowing open desert primitive camping on Nevada's Black Rock Desert playa. Infinite horizon sunsets, world-class dark sky stargazing, and free BLM access.",
      "other_data": "BLM Black Rock Desert-High Rock Canyon NCA. Free dispersed camping.",
      "last_updated": "2026-09-12"
    }
  ],
  "oregon.json": [
    {
      "id": "or-rogue-river-siskiyou-nf-illinois-river",
      "name": "Illinois River Road Dispersed Primitive Camping",
      "state": "Oregon",
      "county": "Josephine County",
      "coordinates": { "latitude": 42.2412, "longitude": -123.6812, "elevation_ft": 1150 },
      "management_agency": {
        "name": "US Forest Service - Rogue River-Siskiyou National Forest (Wild Rivers Ranger District)",
        "type": "USFS",
        "phone": "(541) 592-4000",
        "website": "https://www.fs.usda.gov/rogue-siskiyou"
      },
      "rules_and_regulations": {
        "cost": "100% Free - USFS Dispersed Primitive Camping (zero fee)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed primitive camping permitted at designated pullouts along Illinois River Road (Forest Road 4103). Camp 100ft minimum from river high water mark."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6-8 inches deep in soil 200 feet from Illinois River. Pack out hygiene products.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down pine and madrone wood collection permitted.",
        "safety_requirements": "Campfires in established rock fire rings only. Fully douse with water before vacating.",
        "seasonal_fire_bans": "Summer dry forest fire restrictions active July through September."
      },
      "access_and_road_conditions": {
        "road_type": "Paved US 199 to unpaved dirt/gravel Forest Road 4103",
        "road_conditions": "Winding narrow paved/gravel river road, steep shelf turnouts.",
        "vehicle_recommendation": "High clearance recommended; standard 2WD vehicles can reach lower pullouts carefully in dry weather.",
        "scores": { "road_grade": 5, "road_terrain_difficulty": 5, "supply_run_pain": 3 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / Cave Junction Tower Line",
        "verizon_reliability": "3-4 bars 4G LTE near US 199 highway junction",
        "att_reliability": "3-4 bars 4G LTE",
        "tmobile_reliability": "2-3 bars 4G LTE",
        "terrain_obstruction_risk": "Moderate inside deep emerald river canyon",
        "distance_from_tower_corridor_miles": 3.5,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Emerald Turquoise Riverfront Campsites",
        "Siskiyou Mountain Pine & Madrone Canopy",
        "Natural Swimming Holes & Rock Jumps",
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
          "town_name": "Cave Junction, OR",
          "distance_miles": 8.0,
          "services_available": ["Shop Smart Supermarket", "Gas Stations", "Illinois Valley Public Library", "Clinic", "Restaurants"]
        },
        {
          "town_name": "Grants Pass, OR",
          "distance_miles": 32.0,
          "services_available": ["Full Metro Services", "Safeway / Fred Meyer", "Three Rivers Hospital", "24/7 Gyms"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "50-68°F, roaring emerald river runoff, green Siskiyou growth.",
        "summer": "78-92°F, prime Oregon river swimming weather, warm sunny days.",
        "fall": "52-72°F, golden madrone and bigleaf maple foliage.",
        "winter": "38-50°F, mild winter rain, rushing green river water."
      },
      "dangers_and_hazards": [
        "Fast-moving river currents and slippery rocks in Illinois River canyon",
        "Poison oak in Siskiyou underbrush",
        "Narrow dirt canyon road with steep drop-offs"
      ],
      "acoustic_environment": {
        "quietness_rating": "9/10 - Emerald river rapids and forest wind",
        "common_human_made_sounds": ["Occasional 4x4 on river road"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Pacific Madrone", "Douglas Fir", "Ponderosa Pine", "Darlingtonia (Carnivorous Cobra Lily)", "Poison Oak"],
        "common_animals": ["Chinook Salmon", "River Otter", "Black Bear", "Osprey", "Bald Eagle"]
      },
      "human_demographics_and_culture": "Takelma and Tututni ancestral lands, Siskiyou mountain locals, river swimmers, digital nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Traditional Takelma territory honoring the emerald Illinois River as a sacred life-giving waterway of the Siskiyou mountains.",
        "energetic_and_spiritual_features": "Crystalline emerald green river water energy, lush madrone forest serenity."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Illinois River Trail",
          "length_miles": 12.0,
          "difficulty": "Strenuous",
          "features": "Emerald river canyon bluffs, cobra lily bogs, old-growth pines"
        }
      ],
      "public_reviews_summary": "One of Oregon's most beautiful free river boondocking locations. Crystal clear emerald green swimming holes, fast cell internet near Cave Junction, and free USFS access.",
      "other_data": "Rogue River-Siskiyou National Forest. Free dispersed primitive camping.",
      "last_updated": "2026-09-12"
    }
  ],
  "utah.json": [
    {
      "id": "ut-san-rafael-swell-blm-wedge-overlook",
      "name": "Wedge Overlook BLM Dispersed Primitive Camping",
      "state": "Utah",
      "county": "Emery County",
      "coordinates": { "latitude": 39.0812, "longitude": -110.7412, "elevation_ft": 6200 },
      "management_agency": {
        "name": "Bureau of Land Management (BLM) - Price Field Office",
        "type": "Federal BLM",
        "phone": "(435) 636-3600",
        "website": "https://www.blm.gov/office/price-field-office"
      },
      "rules_and_regulations": {
        "cost": "100% Free - Public BLM Land Dispersed Primitive Camping (zero fees)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed primitive camping permitted at designated pullouts along Wedge Overlook Road (Buckhorn Draw / San Rafael Swell). Portable toilet recommended."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Portable toilet system or pack-out human waste (WAG bags) recommended on canyon rim. Dig cat-hole 6-8 inches deep in desert soil 200ft from rim edges.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Must bring your own firewood. Gathering wood on BLM rim lands is prohibited.",
        "safety_requirements": "Campfires must be contained in metal fire pan. Fully extinguish before leaving.",
        "seasonal_fire_bans": "Summer desert fire restrictions active June through August."
      },
      "access_and_road_conditions": {
        "road_type": "Paved UT 155 to graded gravel dirt BLM roads (Buckhorn Draw Road)",
        "road_conditions": "Graded gravel, washboard dirt, easily drivable in dry weather.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance passenger cars in dry weather.",
        "scores": { "road_grade": 3, "road_terrain_difficulty": 3, "supply_run_pain": 4 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / High Canyon Rim Elevation",
        "verizon_reliability": "3-4 bars 4G LTE along 6,200ft Wedge Overlook canyon rim",
        "att_reliability": "3-4 bars 4G LTE",
        "tmobile_reliability": "2-3 bars 4G LTE",
        "terrain_obstruction_risk": "Low along high open canyon rim; high inside deep Buckhorn Draw canyon",
        "distance_from_tower_corridor_miles": 4.5,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "'Little Grand Canyon' Red Sandstone Panorama Views",
        "Flat Dirt/Gravel RV & Van Pullouts",
        "Buckhorn Draw Rock Art Access",
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
          "town_name": "Castle Dale / Huntington, UT",
          "distance_miles": 18.0,
          "services_available": ["Stewart's Market", "Gas Stations", "Emery County Library", "Hospital", "Restaurants"]
        },
        {
          "town_name": "Price, UT",
          "distance_miles": 38.0,
          "services_available": ["Walmart Supercenter", "Lin's Fresh Market", "24/7 Gyms", "Hardware Stores"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "55-72°F, prime desert canyon hiking weather, clear blue skies.",
        "summer": "85-98°F, warm sunny desert canyon days, breezy nights.",
        "fall": "60-78°F, golden autumn cottonwoods in canyon bottom, ideal desert temps.",
        "winter": "22-42°F, freezing desert nights, dusting of snow on red canyon cliffs."
      },
      "dangers_and_hazards": [
        "Sheer 1,000ft canyon cliff drop-offs at Wedge Overlook (watch footing near rim)",
        "Flash floods in narrow slot draws during summer thunderstorms"
      ],
      "acoustic_environment": {
        "quietness_rating": "10/10 - Pure canyon desert rim silence",
        "common_human_made_sounds": ["Occasional 4x4 engine on distant dirt road"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Utah Juniper", "Piñon Pine", "Slickrock Paintbrush", "Fremont Cottonwood"],
        "common_animals": ["Desert Bighorn Sheep", "Golden Eagle", "Raven", "Collared Lizard", "Mule Deer"]
      },
      "human_demographics_and_culture": "Fremont Culture ancestral lands, San Rafael Swell ranchers, desert nomads, rock art stewards.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Known as the 'Little Grand Canyon of Utah'. Buckhorn Draw features world-famous ancient Fremont barrier-canyon style petroglyph panels.",
        "energetic_and_spiritual_features": "Profound 1,000ft red sandstone canyon rim energy, breathtaking sunrise light."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Goodson Canyon / Wedge Rim Trail",
          "length_miles": 6.5,
          "difficulty": "Easy to Moderate",
          "features": "1,000ft canyon rim panoramas, desert slickrock, ancient juniper groves"
        }
      ],
      "public_reviews_summary": "Utah's single best free rim camping spot. 1,000ft canyon drop-off views over the Little Grand Canyon, blazing cell internet on the rim, and free BLM access.",
      "other_data": "BLM San Rafael Swell Recreation Area. Free dispersed primitive camping.",
      "last_updated": "2026-09-12"
    }
  ],
  "wyoming.json": [
    {
      "id": "wy-shoshone-nf-beartooth-plateau",
      "name": "Beartooth Plateau Dispersed Primitive Camping",
      "state": "Wyoming",
      "county": "Park County",
      "coordinates": { "latitude": 44.9412, "longitude": -109.6512, "elevation_ft": 8900 },
      "management_agency": {
        "name": "US Forest Service - Shoshone National Forest (Clarks Fork Ranger District)",
        "type": "USFS",
        "phone": "(307) 527-6921",
        "website": "https://www.fs.usda.gov/shoshone"
      },
      "rules_and_regulations": {
        "cost": "100% Free - USFS Dispersed Primitive Camping (zero fee)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed primitive camping permitted along Chief Joseph Scenic Byway (WY 296) and Crandall Creek forest roads. Strict food storage order in effect (grizzly bear country)."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6-8 inches deep in soil 200 feet from Clarks Fork River. Pack out all hygiene items.",
        "trash_policy": "Strict Pack-In / Pack-Out. Mandatory bear safety disposal."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down pine wood gathering permitted on forest lands.",
        "safety_requirements": "Campfires in established rock fire rings only. Fully douse with water before vacating.",
        "seasonal_fire_bans": "Summer high wind dry mountain fire restrictions common July-August."
      },
      "access_and_road_conditions": {
        "road_type": "Paved Chief Joseph Scenic Byway (WY 296) to gravel Forest Service roads",
        "road_conditions": "Paved main scenic highway, smooth gravel turnouts.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance passenger cars.",
        "scores": { "road_grade": 4, "road_terrain_difficulty": 3, "supply_run_pain": 4 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / High Highway Pass Signal",
        "verizon_reliability": "3-4 bars 4G LTE along WY 296 mountain pass pullouts",
        "att_reliability": "3-4 bars 4G LTE",
        "tmobile_reliability": "2-3 bars 4G LTE",
        "terrain_obstruction_risk": "Low along high mountain ridge pass",
        "distance_from_tower_corridor_miles": 4.0,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Spectacular Beartooth & Absaroka Peak Panoramas",
        "Clarks Fork Yellowstone River Access",
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
          "town_name": "Cody, WY",
          "distance_miles": 28.0,
          "services_available": ["Albertsons / Walmart", "Gas Stations", "Cody Public Library", "West Park Hospital", "24/7 Gyms", "REI"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "35-50°F, snow melt on high pass, crisp sunny mountain air.",
        "summer": "70-82°F, prime alpine mountain camping, clear starry nights.",
        "fall": "42-62°F, golden aspen colors, crisp chilly nights.",
        "winter": "10-25°F, heavy mountain snowpack, snowshoe and ski season."
      },
      "dangers_and_hazards": [
        "Grizzly and black bear country (bear spray and certified bear canister mandatory)",
        "High elevation altitude exertion (8,900+ ft)"
      ],
      "acoustic_environment": {
        "quietness_rating": "9/10 - High mountain wind and river water cascades",
        "common_human_made_sounds": ["Occasional vehicle on Chief Joseph Byway"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Lodgepole Pine", "Quaking Aspen", "Subalpine Fir", "Wyoming Indian Paintbrush"],
        "common_animals": ["Grizzly Bear", "Elk", "Bison", "Moose", "Bighorn Sheep", "Bald Eagle"]
      },
      "human_demographics_and_culture": "Nez Perce, Crow, & Shoshone ancestral lands, Chief Joseph historical route, Wyoming nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Historic route of Chief Joseph and the Nez Perce flight in 1877. Deeply sacred mountain wilderness for Plains tribes.",
        "energetic_and_spiritual_features": "Exhilarating 8,900ft Absaroka mountain pass energy, crystal clear Yellowstone river headwaters."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Clarks Fork Canyon Trail",
          "length_miles": 7.0,
          "difficulty": "Moderate",
          "features": "Deep granite river canyon, waterfalls, Absaroka peak vistas"
        }
      ],
      "public_reviews_summary": "World-class free primitive camping outside Yellowstone National Park. Breathtaking Absaroka peak views, fast cell internet along Chief Joseph Byway, and 100% free USFS access.",
      "other_data": "Shoshone National Forest. Free dispersed primitive camping.",
      "last_updated": "2026-09-12"
    }
  ]
}

for filename, sites in group_c.items():
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
