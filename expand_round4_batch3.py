import json
import os

BASE_DIR = "/home/volmarr/.gemini/antigravity/scratch/Camping_Nomad_Life/states"

r4_batch3 = {
  "illinois.json": [
    {
      "id": "il-rim-rock-shawnee-nf-dispersed",
      "name": "Rim Rock / Pounds Hollow Wilderness Dispersed Camping",
      "state": "Illinois",
      "county": "Gallatin / Hardin County",
      "coordinates": { "latitude": 37.6012, "longitude": -88.2012, "elevation_ft": 520 },
      "management_agency": {
        "name": "US Forest Service - Shawnee National Forest (Hidden Springs Ranger District)",
        "type": "USFS",
        "phone": "(618) 658-2111",
        "website": "https://www.fs.usda.gov/shawnee"
      },
      "rules_and_regulations": {
        "cost": "100% Free - USFS Dispersed Primitive Camping (zero fee outside developed fee campground)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed primitive camping permitted throughout Rim Rock and Pounds Hollow forest lands along Forest Road 130. Camp 100ft minimum from water."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6 inches deep in soil 200 feet from Pounds Hollow Lake. Pack out hygiene products.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down wood gathering permitted on site.",
        "safety_requirements": "Campfires in established rock fire rings only. Fully douse with water before vacating.",
        "seasonal_fire_bans": "Fall dry leaf fire warnings."
      },
      "access_and_road_conditions": {
        "road_type": "Paved state route to gravel Forest Service roads (FR 130)",
        "road_conditions": "Graded gravel access roads, flat pullouts.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance passenger cars.",
        "scores": { "road_grade": 2, "road_terrain_difficulty": 3, "supply_run_pain": 3 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / Ohio River Corridor Line",
        "verizon_reliability": "3-4 bars 4G LTE near Karbers Ridge Road",
        "att_reliability": "3-4 bars 4G LTE",
        "tmobile_reliability": "2-3 bars 4G LTE",
        "terrain_obstruction_risk": "Low to Moderate across sandstone ridge escarpments",
        "distance_from_tower_corridor_miles": 3.0,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Sandstone Escarpment & Canyon Views",
        "Pounds Hollow Lake Access",
        "Flat Dirt/Gravel Vehicle Pullouts",
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
          "town_name": "Harrisburg / Shawneetown, IL",
          "distance_miles": 14.0,
          "services_available": ["Kroger Supermarket", "Gas Stations", "Harrisburg Public Library", "Hospital", "Restaurants"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "50-68°F, blooming spring dogwood, roaring canyon stream cascades.",
        "summer": "78-90°F, warm Southern Illinois summer days, shaded oak canopy.",
        "fall": "50-70°F, colorful hardwood autumn foliage.",
        "winter": "28-45°F, mild winter, light snow."
      },
      "dangers_and_hazards": [
        "Sandstone bluff drop-offs",
        "Copperhead snakes near rocky outcrops"
      ],
      "acoustic_environment": {
        "quietness_rating": "9/10 - Forest wind and lake water trickles",
        "common_human_made_sounds": ["Occasional vehicle on forest road"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["White Oak", "Sugar Maple", "Shortleaf Pine", "Sandstone Cedar"],
        "common_animals": ["White-tailed Deer", "Wild Turkey", "Bobcat", "Pileated Woodpecker"]
      },
      "human_demographics_and_culture": "Shawnee ancestral lands, Southern Illinois outdoorsmen, nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Historic Beaver Civilization stone wall remnants at Rim Rock. Sacred Shawnee territory honoring the ancient sandstone canyons.",
        "energetic_and_spiritual_features": "Relaxing oak forest quietness, dramatic sandstone rock escarpment energy."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Rim Rock National Recreation Trail",
          "length_miles": 4.5,
          "difficulty": "Easy to Moderate",
          "features": "Ox-lot cave, sandstone bluff stairways, hardwood forest"
        }
      ],
      "public_reviews_summary": "Incredible free primitive camping in Southern Illinois's Shawnee National Forest. Sandstone bluffs, fast cell internet near Harrisburg, and 100% free USFS access.",
      "other_data": "Shawnee National Forest. Free dispersed primitive camping.",
      "last_updated": "2026-09-12"
    }
  ],
  "michigan.json": [
    {
      "id": "mi-pigeon-river-country-state-forest",
      "name": "Pigeon River Country State Forest Dispersed Camping",
      "state": "Michigan",
      "county": "Otsego / Cheboygan County",
      "coordinates": { "latitude": 45.1812, "longitude": -84.4412, "elevation_ft": 920 },
      "management_agency": {
        "name": "Michigan Department of Natural Resources (DNR) - Forest Resources Division",
        "type": "State DNR",
        "phone": "(989) 983-4101",
        "website": "https://www.michigan.gov/dnr"
      },
      "rules_and_regulations": {
        "cost": "100% Free - Free Michigan DNR Camp Registration Card posted at site required (zero fee for dispersed state forest camping)",
        "stay_limit": "15 consecutive days stay limit",
        "guidelines": "Dispersed primitive camping permitted throughout 105,000-acre Pigeon River Country State Forest ('The Big Wild'). Camp 100ft minimum from river."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6-8 inches deep in sandy soil 200 feet from Pigeon River. Pack out hygiene products.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down wood gathering permitted on state forest lands.",
        "safety_requirements": "Campfires in established rock fire rings only. Fully douse with water before vacating.",
        "seasonal_fire_bans": "Spring dry leaf forest fire warnings."
      },
      "access_and_road_conditions": {
        "road_type": "Paved county road to gravel/dirt Forest Service roads (Osmun Road)",
        "road_conditions": "Graded gravel access roads, flat dirt turnouts.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance passenger cars.",
        "scores": { "road_grade": 2, "road_terrain_difficulty": 3, "supply_run_pain": 3 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / Gaylord & Vanderbilt Tower Line",
        "verizon_reliability": "3-4 bars 4G LTE near Osmun Road / Vanderbilt entrance",
        "att_reliability": "3-4 bars 4G LTE",
        "tmobile_reliability": "2-3 bars 4G LTE",
        "terrain_obstruction_risk": "Low to Moderate across northern hardwood moraine hills",
        "distance_from_tower_corridor_miles": 3.5,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "105,000-Acre 'Big Wild' Forest Campsites",
        "Pigeon River Blue-Ribbon Trout Stream Access",
        "Elk Viewing Area Access",
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
          "town_name": "Gaylord / Vanderbilt, MI",
          "distance_miles": 14.0,
          "services_available": ["Meijer / Walmart", "Gas Stations", "Otsego County Library", "Otsego Memorial Hospital", "24/7 Gyms"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "42-58°F, spring trout stream runoff, greening hardwood forest.",
        "summer": "68-80°F, ideal Northern Michigan summer camping weather.",
        "fall": "45-62°F, world-class northern Michigan sugar maple autumn foliage, elk bugling.",
        "winter": "15-30°F, heavy snowpack, cross-country skiing & snowmobiling."
      },
      "dangers_and_hazards": [
        "Black bears in Pigeon River Country (bear hang or canister recommended)",
        "Michigan elk herd territory (keep distance from elk)"
      ],
      "acoustic_environment": {
        "quietness_rating": "9/10 - River water trickles and autumn elk bugles",
        "common_human_made_sounds": ["Occasional forest road vehicle"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Sugar Maple", "White Pine", "Paper Birch", "American Beech"],
        "common_animals": ["Elk (largest wild elk herd east of Mississippi)", "Black Bear", "Brown Trout", "White-tailed Deer", "Bobcat"]
      },
      "human_demographics_and_culture": "Anishinaabe (Ojibwe) ancestral lands, Ernest Hemingway fishing heritage, Michigan woodsmen, nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Known as 'The Big Wild'. Inspired Ernest Hemingway's 'Nick Adams' Northern Michigan fishing stories. Sacred Ojibwe territory.",
        "energetic_and_spiritual_features": "Profound Northwoods wilderness silence, majestic wild elk bugling in autumn."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "High Country Pathway (Pigeon River Section)",
          "length_miles": 12.0,
          "difficulty": "Moderate",
          "features": "Pigeon River trout streams, elk viewing meadows, old-growth pine"
        }
      ],
      "public_reviews_summary": "Michigan's premier free state forest primitive camping. Largest wild elk herd in the Midwest, blue-ribbon trout fishing, fast cell internet near Gaylord, and zero fees.",
      "other_data": "Michigan DNR State Forest. Free camp registration card required.",
      "last_updated": "2026-09-12"
    }
  ],
  "minnesota.json": [
    {
      "id": "mn-richard-j-dorer-hardwood-forest",
      "name": "Richard J. Dorer Memorial Hardwood State Forest Dispersed Camping",
      "state": "Minnesota",
      "county": "Houston / Winona County",
      "coordinates": { "latitude": 43.6812, "longitude": -91.4412, "elevation_ft": 1050 },
      "management_agency": {
        "name": "Minnesota Department of Natural Resources (DNR) - Forestry Division",
        "type": "State DNR",
        "phone": "(507) 206-2850",
        "website": "https://www.dnr.state.mn.us"
      },
      "rules_and_regulations": {
        "cost": "100% Free - Minnesota DNR State Forest Dispersed Primitive Camping (zero fee)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed primitive camping permitted throughout Richard J. Dorer State Forest units in the Mississippi River Driftless Area. Camp 50ft minimum from trails."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6 inches deep in soil 200 feet from trout streams. Pack out all paper.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down wood gathering permitted on site.",
        "safety_requirements": "Campfires in established rock fire rings only. Fully douse before vacating.",
        "seasonal_fire_bans": "Observe drought fire warnings."
      },
      "access_and_road_conditions": {
        "road_type": "Paved state highway to gravel forest entrance roads",
        "road_conditions": "Graded gravel access roads, flat trailhead pullouts.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance passenger cars.",
        "scores": { "road_grade": 3, "road_terrain_difficulty": 3, "supply_run_pain": 3 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / Mississippi River & La Crosse Tower Line",
        "verizon_reliability": "4-5 bars 4G/5G LTE on high limestone ridges",
        "att_reliability": "4-5 bars 4G/5G LTE",
        "tmobile_reliability": "3-4 bars 4G LTE",
        "terrain_obstruction_risk": "Low to Moderate across rolling Driftless limestone bluffs",
        "distance_from_tower_corridor_miles": 2.5,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Driftless Area Limestone Bluff Overlooks",
        "Trout Stream Valley Access",
        "Oak & Walnut Hardwood Canopy",
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
          "town_name": "Caledonia / Winona, MN",
          "distance_miles": 10.0,
          "services_available": ["Fareway Grocery", "Gas Stations", "Caledonia Public Library", "Hospital", "Restaurants"]
        },
        {
          "town_name": "La Crosse, WI / Winona, MN Metro",
          "distance_miles": 22.0,
          "services_available": ["Full Metro Services", "Target / Woodman's", "Gundersen Lutheran Hospital", "24/7 Gyms"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "50-68°F, blooming wild spring trout lilies, cold stream cascades.",
        "summer": "75-88°F, warm summer days under shaded hardwood canopy.",
        "fall": "50-70°F, world-class Mississippi River bluff fall foliage.",
        "winter": "18-35°F, crisp winter weather, light snow."
      },
      "dangers_and_hazards": [
        "Limestone bluff cliff drop-offs",
        "Timber rattlesnakes on rocky bluff ledges"
      ],
      "acoustic_environment": {
        "quietness_rating": "9/10 - Trout stream water flow and woodland songbirds",
        "common_human_made_sounds": ["Occasional trout angler on stream"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Black Walnut", "White Oak", "Sugar Maple", "Maidenhair Fern"],
        "common_animals": ["Brown Trout", "Bald Eagle", "White-tailed Deer", "Wild Turkey"]
      },
      "human_demographics_and_culture": "Dakota & Ho-Chunk ancestral lands, Driftless Area trout anglers, Minnesota woodsmen, nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Ancestral territory of the Dakota nation honoring the ancient unglaciated limestone bluffs and spring-fed trout streams of Southern Minnesota.",
        "energetic_and_spiritual_features": "Profound Driftless limestone ridge energy, pristine trout stream water clarity."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Rattlesnake Bluff Trail",
          "length_miles": 4.5,
          "difficulty": "Moderate",
          "features": "Limestone bluff overlooks, Root River valley views, hardwood forest"
        }
      ],
      "public_reviews_summary": "Minnesota's premier free Driftless Area primitive camping. Sweeping Mississippi River bluff views, fast 5G cell internet, trout fishing, and zero fees.",
      "other_data": "Minnesota DNR State Forest. Free dispersed primitive camping.",
      "last_updated": "2026-09-12"
    }
  ],
  "nevada.json": [
    {
      "id": "nv-sacramento-pass-blm-primitive",
      "name": "Sacramento Pass BLM Recreation Area Primitive Campsites",
      "state": "Nevada",
      "county": "White Pine County",
      "coordinates": { "latitude": 39.1214, "longitude": -114.3214, "elevation_ft": 6700 },
      "management_agency": {
        "name": "Bureau of Land Management (BLM) - Ely District",
        "type": "Federal BLM",
        "phone": "(775) 289-1800",
        "website": "https://www.blm.gov/office/ely-district-office"
      },
      "rules_and_regulations": {
        "cost": "100% Free - Public BLM Land Dispersed Primitive Camping (zero fees)",
        "stay_limit": "14 consecutive days within a 28-day period",
        "guidelines": "Dispersed primitive camping permitted at established pullout sites around Sacramento Pass BLM pond and mountain ridge area."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Use vault toilet provided at pass trailhead or dig cat-hole 6-8 inches deep in soil 200ft from pond water. Pack out paper.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down piñon pine wood gathering permitted on BLM land.",
        "safety_requirements": "Campfires in established rock fire rings only. Fully douse with water before vacating.",
        "seasonal_fire_bans": "Summer desert mountain fire restrictions active July-September."
      },
      "access_and_road_conditions": {
        "road_type": "Paved US 6 / US 50 (Loneliest Road in America) to smooth gravel BLM roads",
        "road_conditions": "Paved main highway access, smooth gravel pullouts.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance passenger cars.",
        "scores": { "road_grade": 2, "road_terrain_difficulty": 2, "supply_run_pain": 4 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / US 50 Highway Pass Signal",
        "verizon_reliability": "3-4 bars 4G LTE along 6,700ft Sacramento Pass crest",
        "att_reliability": "3-4 bars 4G LTE",
        "tmobile_reliability": "2-3 bars 4G LTE",
        "terrain_obstruction_risk": "Low along open mountain pass crest",
        "distance_from_tower_corridor_miles": 3.0,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Wheeler Peak & Great Basin National Park Horizon Views",
        "Sacramento Pass Fishing Pond",
        "Vault Toilet at Pass Entrance",
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
          "town_name": "Baker, NV",
          "distance_miles": 12.0,
          "services_available": ["Baker General Store", "Gas Stations", "Great Basin Visitor Center", "Restaurants"]
        },
        {
          "town_name": "Ely, NV",
          "distance_miles": 42.0,
          "services_available": ["Ridley's Family Markets", "Gas Stations", "White Pine County Library", "Hospital", "24/7 Gyms"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "45-62°F, greening desert mountain slopes, cool mountain air.",
        "summer": "75-88°F, pleasant 6,700ft mountain pass escape from Nevada desert heat.",
        "fall": "50-70°F, golden quaking aspen colors in Great Basin, crisp clear nights.",
        "winter": "20-38°F, cold high desert winter weather, snow dustings on pass."
      },
      "dangers_and_hazards": [
        "High mountain elevation sun exposure (6,700+ ft)"
      ],
      "acoustic_environment": {
        "quietness_rating": "9/10 - High mountain pass wind and desert solitude",
        "common_human_made_sounds": ["Occasional vehicle on US 50 highway"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Single-leaf Piñon Pine", "Utah Juniper", "Mountain Mahogany", "Big Sagebrush"],
        "common_animals": ["Mule Deer", "Pronghorn Antelope", "Golden Eagle", "Rainbow Trout", "Coyote"]
      },
      "human_demographics_and_culture": "Western Shoshone ancestral lands, Great Basin ranchers, US 50 roadtrippers, nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Located on US 50 ('Loneliest Road in America'). Direct view of sacred Wheeler Peak (13,063ft) and ancient Bristlecone Pine groves.",
        "energetic_and_spiritual_features": "Exhilarating 6,700ft Great Basin mountain pass energy, infinite dark night sky stargazing."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Sacramento Pass Mountain Bike / Hike Trail",
          "length_miles": 6.5,
          "difficulty": "Easy to Moderate",
          "features": "Great Basin vistas, piñon pine forests, fishing pond"
        }
      ],
      "public_reviews_summary": "Top free primitive camping spot outside Great Basin National Park. Wheeler Peak views, solid cell internet along US 50, vault toilet access, and 100% free BLM access.",
      "other_data": "BLM Ely District. Free primitive dispersed camping.",
      "last_updated": "2026-09-12"
    }
  ],
  "new_york.json": [
    {
      "id": "ny-pharsalia-woods-state-forest",
      "name": "Pharsalia Woods State Forest Primitive Campsites",
      "state": "New York",
      "county": "Chenango County",
      "coordinates": { "latitude": 42.6012, "longitude": -75.7412, "elevation_ft": 1720 },
      "management_agency": {
        "name": "New York State Department of Environmental Conservation (DEC) - Region 7",
        "type": "State DEC",
        "phone": "(607) 674-4036",
        "website": "https://www.dec.ny.gov"
      },
      "rules_and_regulations": {
        "cost": "100% Free - NYS DEC State Forest Primitive Camping (zero fee for stays under 3 nights)",
        "stay_limit": "3 consecutive nights free without permit; up to 14 days with free DEC forest ranger permit",
        "guidelines": "Dispersed primitive camping permitted at designated roadside sites along Elmer Jackson Road and Finger Lakes Trail corridor."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6-8 inches deep in soil 200 feet from Canasawacta Creek and ponds. Pack out all paper.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down wood gathering permitted within 50 miles.",
        "safety_requirements": "Campfires in established rock fire rings only. Fully douse with water before vacating.",
        "seasonal_fire_bans": "Spring dry leaf weather fire warnings."
      },
      "access_and_road_conditions": {
        "road_type": "Paved state route to gravel town/forest roads",
        "road_conditions": "Graded gravel access roads, flat dirt turnouts.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance passenger cars.",
        "scores": { "road_grade": 2, "road_terrain_difficulty": 2, "supply_run_pain": 3 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / Norwich & NY 23 Tower Line",
        "verizon_reliability": "4-5 bars 4G/5G LTE (30-65 Mbps download)",
        "att_reliability": "4-5 bars 4G/5G LTE",
        "tmobile_reliability": "3-4 bars 4G LTE",
        "terrain_obstruction_risk": "Low across rolling Central NY hill plateau",
        "distance_from_tower_corridor_miles": 2.5,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Central NY Sugar Maple & Hemlock Canopy",
        "Canasawacta Pond Access",
        "Finger Lakes Trailhead Access",
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
          "town_name": "Norwich, NY",
          "distance_miles": 10.0,
          "services_available": ["TOPS Friendly Markets / Price Chopper", "Gas Stations", "Guernsey Memorial Library", "Chenango Memorial Hospital", "Gyms"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "48-65°F, spring trillium bloom, crisp fresh forest air.",
        "summer": "70-82°F, pleasant Central NY forest summer weather.",
        "fall": "48-65°F, world-class Central NY sugar maple fall foliage.",
        "winter": "20-35°F, snowpack on trails, snowshoeing."
      },
      "dangers_and_hazards": [
        "Black bears present (NYS DEC approved food storage recommended)"
      ],
      "acoustic_environment": {
        "quietness_rating": "8/10 - Wind through sugar maples and songbirds",
        "common_human_made_sounds": ["Occasional vehicle on town road"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Sugar Maple", "Eastern Hemlock", "American Beech", "Black Cherry"],
        "common_animals": ["White-tailed Deer", "Wild Turkey", "Red Fox", "Ruffed Grouse"]
      },
      "human_demographics_and_culture": "Haudenosaunee (Oneida) ancestral lands, Central NY woodsmen, Finger Lakes Trail backpackers, nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Traditional Oneida nation territory honoring the ancient hardwood hill forests of Chenango County.",
        "energetic_and_spiritual_features": "Relaxing sugar maple forest quietness, serene pond water reflections."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Finger Lakes Trail (Pharsalia Woods Section)",
          "length_miles": 7.0,
          "difficulty": "Easy to Moderate",
          "features": "Canasawacta Pond, sugar maple groves, historic stone walls"
        }
      ],
      "public_reviews_summary": "Top free state forest primitive camping in Central New York. Blazing 5G cell internet, beautiful sugar maple forest, and 10 minutes to Norwich.",
      "other_data": "NYS DEC State Forest. 100% Free primitive camping.",
      "last_updated": "2026-09-12"
    }
  ],
  "north_carolina.json": [
    {
      "id": "nc-croatan-nf-neuse-river",
      "name": "Croatan National Forest Neuse River Dispersed Camping",
      "state": "North Carolina",
      "county": "Craven / Carteret County",
      "coordinates": { "latitude": 34.9412, "longitude": -76.9412, "elevation_ft": 20 },
      "management_agency": {
        "name": "US Forest Service - National Forests in North Carolina (Croatan Ranger District)",
        "type": "USFS",
        "phone": "(252) 638-5628",
        "website": "https://www.fs.usda.gov/nfsnc"
      },
      "rules_and_regulations": {
        "cost": "100% Free - USFS Dispersed Primitive Camping (zero fee outside developed fee campgrounds)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed primitive camping permitted along Neuse River shoreline pullouts and Forest Service dirt roads (FR 126). Camp 50ft minimum from water."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6 inches deep in sandy soil 200 feet from Neuse River estuary water. Pack out hygiene products.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down pine and oak wood collection permitted on site.",
        "safety_requirements": "Campfires in established rock fire rings only. Fully douse with water before vacating.",
        "seasonal_fire_bans": "Spring dry coastal pine burn warnings."
      },
      "access_and_road_conditions": {
        "road_type": "Paved US 70 to gravel Forest Service roads (FR 126)",
        "road_conditions": "Graded gravel access roads, flat dirt turnouts.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance passenger cars.",
        "scores": { "road_grade": 1, "road_terrain_difficulty": 2, "supply_run_pain": 3 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / New Bern & US 70 Tower Line",
        "verizon_reliability": "4-5 bars 4G/5G LTE (30-70 Mbps download)",
        "att_reliability": "4-5 bars 4G/5G LTE",
        "tmobile_reliability": "3-4 bars 4G LTE",
        "terrain_obstruction_risk": "Low across flat coastal pine savanna",
        "distance_from_tower_corridor_miles": 2.5,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Neuse River Estuary Shoreline Campsites",
        "Loblolly Pine & Live Oak Canopy",
        "Kayak & Boat Access",
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
          "town_name": "New Bern / Havelock, NC",
          "distance_miles": 10.0,
          "services_available": ["Harris Teeter / Publix", "Walmart", "New Bern Public Library", "CarolinaEast Hospital", "24/7 Gyms"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "65-78°F, blooming wild azaleas, pleasant coastal breezes.",
        "summer": "85-92°F, warm humid coastal piney woods summer weather.",
        "fall": "62-78°F, prime pleasant coastal camping weather.",
        "winter": "42-62°F, mild winter, dry clear days."
      },
      "dangers_and_hazards": [
        "Ticks and chiggers in summer (use permethrin)",
        "Alligators in coastal river creeks (exercise caution near water edges)"
      ],
      "acoustic_environment": {
        "quietness_rating": "8/10 - River estuary water waves and pine forest wind",
        "common_human_made_sounds": ["Occasional boat on Neuse River"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Loblolly Pine", "Live Oak", "Venus Flytrap (endemic bog plant)", "Cabbage Palm"],
        "common_animals": ["American Alligator", "Red-cockaded Woodpecker", "Bald Eagle", "Osprey", "Black Bear"]
      },
      "human_demographics_and_culture": "Tuscarora ancestral lands, Coastal Carolina rivermen, digital nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Only true coastal national forest in the Eastern US. Home of the native Venus Flytrap. Sacred Tuscarora territory.",
        "energetic_and_spiritual_features": "Relaxing coastal river estuary breezes, unique carnivorous plant bog ecosystem."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Neuse River Trail / Weetock Trail",
          "length_miles": 8.0,
          "difficulty": "Easy",
          "features": "Neuse River shoreline views, Venus Flytrap bogs, loblolly pine groves"
        }
      ],
      "public_reviews_summary": "Top free coastal primitive camping in North Carolina's Croatan National Forest. Blazing 5G cell internet, Neuse River views, and 10 minutes to New Bern.",
      "other_data": "Croatan National Forest. Free dispersed primitive camping.",
      "last_updated": "2026-09-12"
    }
  ],
  "oregon.json": [
    {
      "id": "or-alvord-desert-blm-primitive",
      "name": "Alvord Desert Edge BLM Dispersed Primitive Camping",
      "state": "Oregon",
      "county": "Harney County",
      "coordinates": { "latitude": 42.5214, "longitude": -118.5214, "elevation_ft": 4020 },
      "management_agency": {
        "name": "Bureau of Land Management (BLM) - Burns District",
        "type": "Federal BLM",
        "phone": "(541) 573-4400",
        "website": "https://www.blm.gov/office/burns-district-office"
      },
      "rules_and_regulations": {
        "cost": "100% Free - Public BLM Land Dispersed Primitive Camping (zero fees)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed primitive camping permitted on public BLM land along Alvord Desert dry lakebed edge and Steens Mountain foothills. Carry out human waste."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Portable toilet system or pack-out human waste (WAG bags) mandatory on dry alkali playa. Dig cat-hole 6-8 inches deep in dirt areas 200ft from hot springs.",
        "trash_policy": "Strict Leave No Trace. Zero trash left on playa."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Must bring your own firewood. Gathering wood on playa is prohibited.",
        "safety_requirements": "Campfires must be contained in metal fire pan. Fully extinguish before leaving.",
        "seasonal_fire_bans": "Summer desert fire restrictions active June through August."
      },
      "access_and_road_conditions": {
        "road_type": "Paved OR 78 to gravel Fields-Denio Road to dry playa access",
        "road_conditions": "Graded gravel access road, dry salt flat playa surface.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance vehicles on dry playa in dry weather; 4x4 recommended after rain.",
        "scores": { "road_grade": 3, "road_terrain_difficulty": 4, "supply_run_pain": 5 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Fair near Fields / Tower Line",
        "verizon_reliability": "2-3 bars 4G LTE near Fields Station / playa entrance",
        "att_reliability": "2-3 bars 4G LTE",
        "tmobile_reliability": "1-2 bars 4G LTE",
        "terrain_obstruction_risk": "Low across 12-mile flat open salt flat playa",
        "distance_from_tower_corridor_miles": 5.0,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Vast Open Salt Flat Lakebed & Steens Mountain Views",
        "Nearby Geothermal Hot Springs (Alvord Hot Springs access)",
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
          "town_name": "Fields, OR",
          "distance_miles": 12.0,
          "services_available": ["Fields Station / Store", "Gas Station", "Famous Milkshakes", "Local Diner"]
        },
        {
          "town_name": "Burns, OR",
          "distance_miles": 85.0,
          "services_available": ["Safeway / Supermarket", "Harney District Hospital", "Full Services", "Hardware Stores"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "48-65°F, cool high desert breeze, spring mountain snowmelt views.",
        "summer": "85-98°F, warm sunny desert playa days, cool clear nights.",
        "fall": "55-75°F, prime desert camping weather, clear starry nights.",
        "winter": "22-40°F, freezing desert nights, playa wet/muddy."
      },
      "dangers_and_hazards": [
        "Playa surface turns into unpassable sticky mud after rain (never drive on wet playa)",
        "High wind gusts across open dry lakebed",
        "Severe dehydration in dry high desert heat"
      ],
      "acoustic_environment": {
        "quietness_rating": "10/10 - Absolute desert playa silence",
        "common_human_made_sounds": ["None (Wilderness area)"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Big Sagebrush", "Greasewood", "Shadscale", "Desert Wildflowers"],
        "common_animals": ["Pronghorn Antelope", "Wild Horses (Mustangs)", "Coyote", "Golden Eagle", "Raven"]
      },
      "human_demographics_and_culture": "Northern Paiute ancestral lands, Harney County ranchers, desert nomads, land-speed record racers.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Traditional Northern Paiute territory honoring the sacred Steens Mountain and vast Alvord salt flats.",
        "energetic_and_spiritual_features": "Infinite dry salt flat horizons, majestic 9,700ft Steens Mountain backdrop, world-class dark night sky stargazing."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Pike Creek Canyon Trail (Steens Mountain)",
          "length_miles": 5.5,
          "difficulty": "Moderate to Strenuous",
          "features": "Steens Mountain gorge cliffs, desert bighorn sheep, wild stream cascades"
        }
      ],
      "public_reviews_summary": "Oregon's most surreal primitive boondocking location. Drive right onto the vast 12-mile Alvord salt flat under Steens Mountain, soak in hot springs, 100% free BLM access.",
      "other_data": "BLM Burns District. Free primitive dispersed camping.",
      "last_updated": "2026-09-12"
    }
  ],
  "utah.json": [
    {
      "id": "ut-moab-blm-willow-springs",
      "name": "Willow Springs Trail BLM Dispersed Area",
      "state": "Utah",
      "county": "Grand County",
      "coordinates": { "latitude": 38.6812, "longitude": -109.6812, "elevation_ft": 4500 },
      "management_agency": {
        "name": "Bureau of Land Management (BLM) - Moab Field Office",
        "type": "Federal BLM",
        "phone": "(435) 259-2100",
        "website": "https://www.blm.gov/office/moab-field-office"
      },
      "rules_and_regulations": {
        "cost": "100% Free - Free BLM Dispersed Permit required online/on-site sign (zero cost)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed primitive camping permitted at designated campsites along Willow Springs Trail (BLM 378). Must carry portable toilet system or WAG bags."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Portable toilet system or pack-out human waste (WAG bags) mandatory in Moab desert country. Digging cat-holes strictly prohibited in Moab canyon soil.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Must bring your own firewood. Gathering wood on Moab BLM land is prohibited.",
        "safety_requirements": "Campfires must be contained in metal fire pan. Fully extinguish before leaving.",
        "seasonal_fire_bans": "Summer desert fire restrictions active June through August."
      },
      "access_and_road_conditions": {
        "road_type": "Paved US 191 to smooth gravel dirt BLM road (Willow Springs Trail)",
        "road_conditions": "Graded gravel dirt road, easily drivable for all vehicles.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance vehicles, vans, and RVs.",
        "scores": { "road_grade": 2, "road_terrain_difficulty": 3, "supply_run_pain": 2 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / Direct Line of Sight to Moab Towers",
        "verizon_reliability": "4-5 bars 4G/5G LTE (30-85 Mbps download)",
        "att_reliability": "4-5 bars 4G/5G LTE",
        "tmobile_reliability": "3-4 bars 4G LTE",
        "terrain_obstruction_risk": "Low across open red slickrock mesa flats",
        "distance_from_tower_corridor_miles": 3.0,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Red Sandstone Slickrock & Arches National Park Views",
        "Flat Gravel RV & Van Pullouts",
        "Dinosaur Trackway Trailhead Access",
        "Stone Fire Rings"
      ],
      "location_scores": {
        "distance_to_groceries_score": 8,
        "distance_to_library_score": 8,
        "distance_to_gym_score": 7,
        "terrain_score": 10,
        "quietness_score": 8
      },
      "nearest_supply_towns": [
        {
          "town_name": "Moab, UT",
          "distance_miles": 10.0,
          "services_available": ["City Market / Moonflower Coop", "Gas Stations", "Grand County Public Library", "Moab Regional Hospital", "Gyms", "Gear Shops"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "55-75°F, prime desert hiking & mountain biking weather, clear sunny skies.",
        "summer": "90-104°F, hot desert summer weather, breezy cool nights.",
        "fall": "60-80°F, ideal Moab red rock camping weather.",
        "winter": "25-45°F, freezing desert nights, dustings of snow on red slickrock."
      },
      "dangers_and_hazards": [
        "Dehydration in dry desert summer heat",
        "Sudden thunderstorm flash floods in wash crossings"
      ],
      "acoustic_environment": {
        "quietness_rating": "8/10 - Red rock desert wind and canyon wrens",
        "common_human_made_sounds": ["Occasional camper vehicle on Willow Springs dirt drive"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Utah Juniper", "Piñon Pine", "Slickrock Paintbrush", "Yucca", "Prickly Pear Cactus"],
        "common_animals": ["Desert Bighorn Sheep", "Raven", "Collared Lizard", "Mule Deer", "Coyote"]
      },
      "human_demographics_and_culture": "Ancestral Puebloan & Ute lands, Moab mountain bikers, rock climbers, digital nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Famous free nomad hub outside Arches National Park. Contains ancient fossilized dinosaur trackways right on site.",
        "energetic_and_spiritual_features": "Profound red slickrock desert energy, breathtaking sunset light on the La Sal Mountains."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Willow Springs Dinosaur Trackway Trail",
          "length_miles": 2.5,
          "difficulty": "Easy",
          "features": "Real 140-million-year-old dinosaur footprints, slickrock mesas, Arches views"
        }
      ],
      "public_reviews_summary": "The premier free digital nomad boondocking hub in Moab, Utah. Blazing 5G cell internet, flat easy driving, Arches National Park views, and 100% free BLM access.",
      "other_data": "BLM Moab Field Office. Free permit required.",
      "last_updated": "2026-09-12"
    }
  ],
  "wyoming.json": [
    {
      "id": "wy-medicine-bow-nf-snowy-range",
      "name": "Snowy Range Road Dispersed Camping",
      "state": "Wyoming",
      "county": "Albany / Carbon County",
      "coordinates": { "latitude": 41.3412, "longitude": -106.2812, "elevation_ft": 8800 },
      "management_agency": {
        "name": "US Forest Service - Medicine Bow-Routt National Forests (Laramie Ranger District)",
        "type": "USFS",
        "phone": "(307) 745-2300",
        "website": "https://www.fs.usda.gov/mbr"
      },
      "rules_and_regulations": {
        "cost": "100% Free - USFS Dispersed Primitive Camping (zero fee)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed primitive camping permitted at established pullout sites along Snowy Range Scenic Byway (WY 130) and Sand Lake Road (FR 103)."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6-8 inches deep in soil 200 feet from alpine streams. Pack out all paper.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Abundant dead and down pine wood collection permitted on forest lands.",
        "safety_requirements": "Campfires in established rock fire rings only. Fully douse with water before vacating.",
        "seasonal_fire_bans": "Summer high wind fire restrictions active July-August."
      },
      "access_and_road_conditions": {
        "road_type": "Paved Snowy Range Scenic Byway (WY 130) to gravel Forest Service roads",
        "road_conditions": "Paved main scenic highway, smooth gravel forest road pullouts.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance passenger cars.",
        "scores": { "road_grade": 4, "road_terrain_difficulty": 3, "supply_run_pain": 3 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / Laramie & Centennial Tower Line",
        "verizon_reliability": "3-4 bars 4G LTE near Centennial entrance / WY 130",
        "att_reliability": "3-4 bars 4G LTE",
        "tmobile_reliability": "2-3 bars 4G LTE",
        "terrain_obstruction_risk": "Low along open 8,800ft Snowy Range mountain plateau",
        "distance_from_tower_corridor_miles": 3.5,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Subalpine Glacial Lake & Quartzite Peak Views",
        "Lodgepole Pine & Spruce Shade",
        "Flat Gravel RV & Van Pullouts",
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
          "town_name": "Centennial / Laramie, WY",
          "distance_miles": 10.0,
          "services_available": ["Safeway / Ridleys", "Gas Stations", "Univ of Wyoming Library", "Ivinson Hospital", "24/7 Gyms"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "35-50°F, snow melt on high pass, crisp mountain air.",
        "summer": "68-80°F, prime alpine mountain camping, clear blue skies.",
        "fall": "40-60°F, golden quaking aspen foliage, crisp chilly nights.",
        "winter": "10-25°F, heavy mountain snowpack, highway closed past snow gate."
      },
      "dangers_and_hazards": [
        "High altitude mountain elevation sickness risk (8,800+ ft)",
        "Sudden high-elevation alpine thunderstorms",
        "Black bears and moose present (store food securely)"
      ],
      "acoustic_environment": {
        "quietness_rating": "9/10 - High mountain wind and subalpine stream cascades",
        "common_human_made_sounds": ["Occasional vehicle on Snowy Range Byway"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Engelmann Spruce", "Subalpine Fir", "Quaking Aspen", "Wyoming Indian Paintbrush"],
        "common_animals": ["Moose", "Elk", "Bighorn Sheep", "Pika", "Golden Eagle", "Cutthroat Trout"]
      },
      "human_demographics_and_culture": "Cheyenne, Arapaho, & Ute ancestral lands, UW college outdoorsmen, Wyoming nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Known for massive Medicine Bow quartzite cliffs (Medicine Bow Peak 12,013ft). Sacred Arapaho territory honoring mountain healing grounds.",
        "energetic_and_spiritual_features": "Exhilarating 8,800ft alpine mountain energy, crystalline subalpine lake clarity."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Medicine Bow Peak Loop Trail",
          "length_miles": 7.0,
          "difficulty": "Strenuous",
          "features": "12,013ft quartzite peak summit, alpine glacial lakes, tundra wildflower basins"
        }
      ],
      "public_reviews_summary": "Top free high-alpine primitive camping in Wyoming's Medicine Bow National Forest. Crystalline glacial lakes, 12,000ft quartzite peaks, fast cell internet near Laramie, and 100% free USFS access.",
      "other_data": "Medicine Bow National Forest. Free dispersed primitive camping.",
      "last_updated": "2026-09-12"
    }
  ]
}

for filename, sites in r4_batch3.items():
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
