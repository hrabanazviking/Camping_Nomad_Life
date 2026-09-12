import json

def load_state(name):
    path = f'/home/volmarr/.gemini/antigravity/scratch/Camping_Nomad_Life/states/{name}.json'
    with open(path, 'r') as f:
        return json.load(f), path

def save_state(data, path):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

# Arizona (+5 sites -> 10 total)
az, az_path = load_state('arizona')
az.extend([
  {
    "id": "arizona-006",
    "name": "Plomosa Road BLM Dispersed Camping Area",
    "state": "Arizona",
    "county": "La Paz",
    "coordinates": {"latitude": 33.7842, "longitude": -114.1852, "elevation_ft": 1150.0},
    "management_agency": {"name": "Bureau of Land Management (BLM) - Yuma Field Office", "type": "Federal", "phone": "(928) 317-3200", "website": "https://www.blm.gov/arizona"},
    "rules_and_regulations": {"cost": "Free ($0/night primitive BLM dispersed camping)", "stay_limit": "14 days maximum stay within a 28-day window", "guidelines": "Dispersed camping allowed along Plomosa Road dirt pullouts north of Quartzsite. Leave No Trace."},
    "waste_disposal_rules": {"poop_disposal": "Pack out human waste or bury in 6-8 inch cat-holes 200 ft from washes. RVs use Quartzsite dump station.", "trash_policy": "Strict Pack-It-In Pack-It-Out policy."},
    "campfire_rules": {"permitted": True, "firewood_policy": "Bring firewood or collect dead palo verde/mesquite down wood.", "safety_requirements": "Campfires permitted in cleared metal or stone rings. Extinguish cold.", "seasonal_fire_bans": "Subject to BLM Stage 1 & 2 fire restrictions in May/June."},
    "access_and_road_conditions": {"road_type": "Paved Plomosa Road to hard-packed gravel pullouts", "road_conditions": "Smooth paved main road; gravel pullouts accessible by all rigs.", "vehicle_recommendation": "Any vehicle including low-clearance FWD sedans and large motorhomes.", "scores": {"road_grade": 1, "road_terrain_difficulty": 1, "supply_run_pain": 2}},
    "nomad_connectivity_rating": {"overall_rating": "Great (4.5/5 Stars)", "verizon_reliability": "4-5 bars 5G/4G LTE", "att_reliability": "4 bars 5G", "tmobile_reliability": "4 bars 5G", "terrain_obstruction_risk": "Low - open desert plain surrounded by distant Plomosa mountains", "distance_from_tower_corridor_miles": 2.5, "cellular_internet_dependable": True},
    "amenities": ["Hard-packed RV Pullouts", "Plomosa Mountain Views", "Sunset Vistas"],
    "location_scores": {"distance_to_groceries_score": 8, "distance_to_library_score": 7, "distance_to_gym_score": 5, "terrain_score": 7, "quietness_score": 8},
    "nearest_supply_towns": [{"town_name": "Quartzsite, AZ", "distance_miles": 8.5, "services_available": ["Propane", "Water Refill", "Dump Station", "Grocery Store", "Hardware Store"]}],
    "seasonal_weather_effects": {"spring": "Pleasant spring weather (75-85°F) with desert wildflower blooms.", "summer": "Extremely hot (105-115°F); dangerous heat.", "fall": "Warm sunny days and cool desert nights.", "winter": "Ideal winter desert climate (65-75°F); popular nomad snowbird hub."},
    "dangers_and_hazards": ["Extreme Summer Heat", "Rattlesnakes", "Flash Floods in Wash Beds"],
    "acoustic_environment": {"quietness_rating": "Peaceful Desert Plain (Quietness Score: 8/10)", "common_human_made_sounds": ["Distant Plomosa Road traffic", "Occasional generator hum"]},
    "flora_and_fauna": {"common_plants_and_trees": ["Saguaro Cactus", "Creosote Bush", "Palo Verde", "Ocotillo"], "common_animals": ["Desert Tortoise", "Coyote", "Gambel's Quail", "Jackrabbit"]},
    "human_demographics_and_culture": "Quartzsite snowbird nomad culture and winter rockhounding hub.",
    "spiritual_and_folklore_data": {"nature_spirits_and_mythological_lore": "Indigenous Mojave legends honor the Plomosa Mountains as spirit sentinels of the Sonoran desert.", "energetic_and_spiritual_features": "Wide open desert plains offering vast 360-degree sunset vistas."},
    "nearby_hiking_trails": [{"trail_name": "Plomosa Mountains Crest Trail", "length_miles": 4.5, "difficulty": "Moderate", "features": "Desert mountain ridge walk, quartz veins, panoramic valley views"}],
    "public_reviews_summary": "Top choice for nomads needing lightning fast 5G cell service and easy flat access near Quartzsite.",
    "other_data": "Water and dump stations available in nearby Quartzsite for small fee.",
    "last_updated": "2026-09-12"
  },
  {
    "id": "arizona-007",
    "name": "Indian Bread Rocks BLM Primitive Camping Area",
    "state": "Arizona",
    "county": "Cochise",
    "coordinates": {"latitude": 32.2412, "longitude": -109.4125, "elevation_ft": 4200.0},
    "management_agency": {"name": "Bureau of Land Management (BLM) - Safford Field Office", "type": "Federal", "phone": "(928) 348-4400", "website": "https://www.blm.gov/arizona"},
    "rules_and_regulations": {"cost": "Free ($0/night primitive BLM dispersed camping)", "stay_limit": "14 days maximum stay limit", "guidelines": "Dispersed primitive camping allowed among granite boulder formations at Dos Cabezas mountain base. Leave No Trace."},
    "waste_disposal_rules": {"poop_disposal": "Utilize BLM pit toilet at day-use area or bury 6-8 inches deep 200 ft from washes.", "trash_policy": "Strict Pack-It-In Pack-It-Out policy."},
    "campfire_rules": {"permitted": True, "firewood_policy": "Gather dead and down wood locally.", "safety_requirements": "Campfires permitted in cleared metal or stone rings. Extinguish cold.", "seasonal_fire_bans": "Subject to BLM dry season burn bans."},
    "access_and_road_conditions": {"road_type": "Gravel dirt access road", "road_conditions": "Graded gravel road with flat pullouts among granite boulders.", "vehicle_recommendation": "Accessible by standard FWD passenger car and camper vans.", "scores": {"road_grade": 2, "road_terrain_difficulty": 3, "supply_run_pain": 3}},
    "nomad_connectivity_rating": {"overall_rating": "Great (4/5 Stars)", "verizon_reliability": "4 bars 4G LTE", "att_reliability": "3-4 bars 4G LTE", "tmobile_reliability": "3 bars 4G LTE", "terrain_obstruction_risk": "Low - open high desert plain framed by granite formations", "distance_from_tower_corridor_miles": 3.1, "cellular_internet_dependable": True},
    "amenities": ["Granite Boulder Formations", "Vault Toilet nearby", "Metal Picnic Tables at Day Use", "Dark Sky Astronomy"],
    "location_scores": {"distance_to_groceries_score": 7, "distance_to_library_score": 7, "distance_to_gym_score": 6, "terrain_score": 9, "quietness_score": 9},
    "nearest_supply_towns": [{"town_name": "Bowie, AZ", "distance_miles": 6.2, "services_available": ["Gas Station", "Post Office", "Local Diner"]}, {"town_name": "Willcox, AZ", "distance_miles": 18.5, "services_available": ["Supermarket", "Hospital", "Public Library", "Hardware Store", "Gym"]}],
    "seasonal_weather_effects": {"spring": "Mild high desert spring weather (70-80°F).", "summer": "Warm to hot (90-98°F) with afternoon monsoons.", "fall": "Crisp dry autumn days with glowing granite boulders.", "winter": "Cool winter (45-60°F) with brisk night temps."},
    "dangers_and_hazards": ["Rattlesnakes", "High Desert Sun Exposure", "Bee Hives in Boulder Crevices"],
    "acoustic_environment": {"quietness_rating": "Granite Boulder Quiet (Quietness Score: 9/10)", "common_human_made_sounds": ["Distant I-10 train horn in valley"]},
    "flora_and_fauna": {"common_plants_and_trees": ["Scrub Oak", "Mesquite", "Yucca", "Prickly Pear"], "common_animals": ["Javelina", "Coati", "Mule Deer", "Great Horned Owl"]},
    "human_demographics_and_culture": "Cochise County historic Apache pass and high desert ranching heritage.",
    "spiritual_and_folklore_data": {"nature_spirits_and_mythological_lore": "Chiricahua Apache traditions honor the Dos Cabezas peak as sacred ancestral land.", "energetic_and_spiritual_features": "Giant 1.5-billion-year-old weathered granite boulders generate a peaceful grounding energy."},
    "nearby_hiking_trails": [{"trail_name": "Dos Cabezas Foothills Trail", "length_miles": 3.8, "difficulty": "Moderate", "features": "Granite bouldering outcrops, desert basin vistas"}],
    "public_reviews_summary": "Incredible bouldering landscape, clean vault toilet, and strong cell service make this a hidden nomad paradise.",
    "other_data": "Bring fresh drinking water.",
    "last_updated": "2026-09-12"
  },
  {
    "id": "arizona-008",
    "name": "Coconino National Forest FR 525 Dispersed Camping Zone",
    "state": "Arizona",
    "county": "Yavapai",
    "coordinates": {"latitude": 34.8412, "longitude": -111.9125, "elevation_ft": 4450.0},
    "management_agency": {"name": "U.S. Forest Service - Coconino National Forest (Red Rock Ranger District)", "type": "Federal", "phone": "(928) 203-2900", "website": "https://www.fs.usda.gov/coconino"},
    "rules_and_regulations": {"cost": "Free ($0/night primitive dispersed forest camping in designated FR 525 sites)", "stay_limit": "14 days maximum stay within a 30-day window", "guidelines": "Camping allowed ONLY at designated numbered sites along Forest Road 525 outside Sedona red rock fee boundary. Leave No Trace."},
    "waste_disposal_rules": {"poop_disposal": "Bury waste 6-8 inches deep 200 ft from washes. Pack out toilet paper.", "trash_policy": "Strict Pack-It-In Pack-It-Out policy."},
    "campfire_rules": {"permitted": True, "firewood_policy": "Gather dead and down wood locally.", "safety_requirements": "Campfires permitted in cleared metal or stone fire rings at designated sites. Extinguish cold.", "seasonal_fire_bans": "Subject to USFS Stage 1 & 2 fire bans during dry spring/summer."},
    "access_and_road_conditions": {"road_type": "Gravel forest service road (FR 525)", "road_conditions": "Graded gravel road with occasional washboards; accessible by most vehicles.", "vehicle_recommendation": "Accessible by standard FWD passenger car, camper vans, and small trailers.", "scores": {"road_grade": 2, "road_terrain_difficulty": 3, "supply_run_pain": 3}},
    "nomad_connectivity_rating": {"overall_rating": "Great (4/5 Stars)", "verizon_reliability": "4 bars 5G/4G LTE", "att_reliability": "4 bars 4G LTE", "tmobile_reliability": "3-4 bars 4G LTE", "terrain_obstruction_risk": "Low to Moderate - high red rock plateau overview", "distance_from_tower_corridor_miles": 2.8, "cellular_internet_dependable": True},
    "amenities": ["Red Rock Butte Views", "Designated Numbered Sites", "Dark Sky Star Observation"],
    "location_scores": {"distance_to_groceries_score": 7, "distance_to_library_score": 7, "distance_to_gym_score": 6, "terrain_score": 10, "quietness_score": 8},
    "nearest_supply_towns": [{"town_name": "Cottonwood, AZ", "distance_miles": 10.5, "services_available": ["Supercenter", "Hospital", "Public Library", "Gym & Fitness Center", "Hardware Store"]}, {"town_name": "Sedona, AZ", "distance_miles": 12.0, "services_available": ["Grocery Stores", "Arts & Culture", "Outfitters", "Restaurants"]}],
    "seasonal_weather_effects": {"spring": "Lush high desert spring weather (70-80°F).", "summer": "Warm to hot (90-98°F); cool night air.", "fall": "Stunning autumn foliage reflections on red rocks.", "winter": "Cool winter (45-60°F) with light snow on red rock rims."},
    "dangers_and_hazards": ["Rattlesnakes", "High Summer Heat", "Flash Floods in Washes"],
    "acoustic_environment": {"quietness_rating": "Red Rock Valley Quiet (Quietness Score: 8/10)", "common_human_made_sounds": ["Occasional passing OHV tour", "Distant highway US-89A hum"]},
    "flora_and_fauna": {
      "common_plants_and_trees": ["Pinyon Pine", "Utah Juniper", "Red Rock Scrub Oak", "Prickly Pear"],
      "common_animals": ["Mule Deer", "Javelina", "Coyote", "Red-tailed Hawk"]
    },
    "human_demographics_and_culture": "Sedona red rock wilderness, vortex tourism, and high desert conservation culture.",
    "spiritual_and_folklore_data": {
      "nature_spirits_and_mythological_lore": "Yavapai-Apache sacred tradition honors the red rock country of Sedona as ancestral heartland.",
      "energetic_and_spiritual_features": "Panoramic views of Mingus Mountain and Sedona red rock bluffs radiate intense creative energy."
    },
    "nearby_hiking_trails": [{"trail_name": "Loy Canyon Trail & Robbers Roost", "length_miles": 5.2, "difficulty": "Moderate", "features": "Red rock canyons, ancestral cliff alcoves, pine groves"}],
    "public_reviews_summary": "Unbelievable views of Sedona's red rocks with blazing fast 5G cell service and zero cost.",
    "other_data": "Camp ONLY in designated numbered sites along FR 525.",
    "last_updated": "2026-09-12"
  },
  {
    "id": "arizona-009",
    "name": "Prescott National Forest Thumb Butte Dispersed Zone",
    "state": "Arizona",
    "county": "Yavapai",
    "coordinates": {"latitude": 34.5412, "longitude": -112.5214, "elevation_ft": 5820.0},
    "management_agency": {"name": "U.S. Forest Service - Prescott National Forest (Bradshaw Ranger District)", "type": "Federal", "phone": "(928) 443-8000", "website": "https://www.fs.usda.gov/prescott"},
    "rules_and_regulations": {"cost": "Free ($0/night primitive dispersed camping)", "stay_limit": "14 days maximum stay limit", "guidelines": "Dispersed primitive camping allowed along Copper Basin Road (FR 53) outside Prescott city basin limit. Camp 100 ft from streams. Leave No Trace."},
    "waste_disposal_rules": {"poop_disposal": "Bury waste 6-8 inches deep 200 ft from streams. Pack out toilet paper.", "trash_policy": "Strict Pack-It-In Pack-It-Out policy."},
    "campfire_rules": {"permitted": True, "firewood_policy": "Gather dead and down pine wood locally.", "safety_requirements": "Campfires permitted in cleared stone rings. Extinguish cold.", "seasonal_fire_bans": "Subject to USFS Stage 1 & 2 fire bans during dry spring/summer."},
    "access_and_road_conditions": {"road_type": "Gravel forest service roads", "road_conditions": "Graded gravel roads with flat ponderosa pine pullouts.", "vehicle_recommendation": "Accessible by standard FWD passenger car.", "scores": {"road_grade": 3, "road_terrain_difficulty": 3, "supply_run_pain": 3}},
    "nomad_connectivity_rating": {"overall_rating": "Great (4/5 Stars)", "verizon_reliability": "4 bars 5G/4G LTE", "att_reliability": "4 bars 4G LTE", "tmobile_reliability": "3-4 bars 5G", "terrain_obstruction_risk": "Low - high ponderosa pine ridge looking towards Prescott", "distance_from_tower_corridor_miles": 2.2, "cellular_internet_dependable": True},
    "amenities": ["Ponderosa Pine Shade", "Prescott Valley Views", "Primitive Fire Rings"],
    "location_scores": {"distance_to_groceries_score": 8, "distance_to_library_score": 8, "distance_to_gym_score": 7, "terrain_score": 8, "quietness_score": 8},
    "nearest_supply_towns": [{"town_name": "Prescott, AZ", "distance_miles": 6.8, "services_available": ["Supermarket", "Hospital", "Public Library", "Gym & Fitness Center", "Hardware Store", "Historic Downtown"]}],
    "seasonal_weather_effects": {"spring": "Mild mountain spring (65-75°F).", "summer": "Pleasant summer weather (80-86°F) escaping Phoenix heat.", "fall": "Crisp mountain autumn foliage.", "winter": "Cool to cold (30-48°F) with light snow."},
    "dangers_and_hazards": ["High Wildfire Hazard in Summer", "Javelina", "Freezing Winter Night Temps"],
    "acoustic_environment": {"quietness_rating": "Mountain Forest Quiet (Quietness Score: 8/10)", "common_human_made_sounds": ["Distant Prescott valley hum", "Occasional forest road car"]},
    "flora_and_fauna": {
      "common_plants_and_trees": ["Ponderosa Pine", "Gamble Oak", "Alligator Juniper", "Manzanita"],
      "common_animals": ["Mule Deer", "Javelina", "Abert's Squirrel", "Mountain Lion"]
    },
    "human_demographics_and_culture": "Prescott mile-high mountain pine forest, historic territorial capital, and outdoor mountain biking culture.",
    "spiritual_and_folklore_data": {
      "nature_spirits_and_mythological_lore": "Yavapai tradition honors Thumb Butte (Thumb Peak) as a sacred landmark sentinel.",
      "energetic_and_spiritual_features": "High ponderosa pine ridges overlooking granite dells provide an invigorating mountain air."
    },
    "nearby_hiking_trails": [{"trail_name": "Thumb Butte Loop Trail #33", "length_miles": 2.5, "difficulty": "Moderate", "features": "Granite pinnacle views, ponderosa pine canopy, birdwatching"}],
    "public_reviews_summary": "Cool mile-high pine forest camping just minutes from downtown Prescott with fast 5G cell internet.",
    "other_data": "Bring fresh drinking water.",
    "last_updated": "2026-09-12"
  },
  {
    "id": "arizona-010",
    "name": "Gardner Canyon Upper Dispersed Zone - Coronado National Forest",
    "state": "Arizona",
    "county": "Santa Cruz",
    "coordinates": {"latitude": 31.7125, "longitude": -110.7412, "elevation_ft": 5120.0},
    "management_agency": {"name": "U.S. Forest Service - Coronado National Forest (Nogales Ranger District)", "type": "Federal", "phone": "(520) 281-2296", "website": "https://www.fs.usda.gov/coronado"},
    "rules_and_regulations": {"cost": "Free ($0/night primitive dispersed forest camping)", "stay_limit": "14 days maximum stay limit", "guidelines": "Dispersed primitive camping allowed along Gardner Canyon Road (FR 92) pullouts at Santa Rita mountain base. Leave No Trace."},
    "waste_disposal_rules": {"poop_disposal": "Bury waste 6-8 inches deep 200 ft from Gardner Creek wash. Pack out paper.", "trash_policy": "Strict Pack-It-In Pack-It-Out policy."},
    "campfire_rules": {"permitted": True, "firewood_policy": "Gather dead and down wood locally.", "safety_requirements": "Campfires permitted in cleared stone rings. Extinguish cold.", "seasonal_fire_bans": "Subject to USFS dry season burn bans."},
    "access_and_road_conditions": {"road_type": "Gravel forest service road", "road_conditions": "Graded gravel road; high clearance recommended for upper canyon pullouts.", "vehicle_recommendation": "CUV, SUV, or standard FWD car driven carefully.", "scores": {"road_grade": 3, "road_terrain_difficulty": 3, "supply_run_pain": 4}},
    "nomad_connectivity_rating": {"overall_rating": "Good (3.5/5 Stars)", "verizon_reliability": "3-4 bars 4G LTE", "att_reliability": "3 bars 4G LTE", "tmobile_reliability": "2-3 bars 4G LTE", "terrain_obstruction_risk": "Moderate - Santa Rita mountain canyon slope", "distance_from_tower_corridor_miles": 4.5, "cellular_internet_dependable": True},
    "amenities": ["Oak-Pine Canopy", "Santa Rita Mountain Views", "Primitive Stone Fire Rings"],
    "location_scores": {"distance_to_groceries_score": 6, "distance_to_library_score": 6, "distance_to_gym_score": 5, "terrain_score": 9, "quietness_score": 9},
    "nearest_supply_towns": [{"town_name": "Sonoita, AZ", "distance_miles": 9.5, "services_available": ["Grocery Store", "Gas Station", "Hardware Store", "Local Wineries & Dining"]}, {"town_name": "Tucson, AZ", "distance_miles": 42.0, "services_available": ["International Airport", "Major Hospitals", "Full Urban Amenities"]}],
    "seasonal_weather_effects": {"spring": "Lush high desert mountain spring (70-78°F).", "summer": "Warm (85-92°F) with cooling summer monsoons in July/August.", "fall": "Crisp autumn weather with golden oak leaves.", "winter": "Cool winter (48-60°F) with light mountain snow on Mount Wrightson peaks."},
    "dangers_and_hazards": ["Border Region Remote Travel Caution", "Rattlesnakes", "Flash Floods in Wash Beds"],
    "acoustic_environment": {"quietness_rating": "Mountain Canyon Quiet (Quietness Score: 9/10)", "common_human_made_sounds": ["Occasional passing forest road car", "High altitude commercial flights"]},
    "flora_and_fauna": {
      "common_plants_and_trees": ["Emory Oak", "Arizona White Oak", "Pinyon Pine", "Agave"],
      "common_animals": ["Coues White-tailed Deer", "Coatimundi", "Javelina", "Elegant Trogon"]
    },
    "human_demographics_and_culture": "Southern Arizona sky island conservation, Sonoita wine country, and borderlands mountain heritage.",
    "spiritual_and_folklore_data": {
      "nature_spirits_and_mythological_lore": "Tohono O'odham traditions honor the Santa Rita Mountains as sacred high sky island peaks.",
      "energetic_and_spiritual_features": "High elevation oak woodland beneath 9,400-foot Mount Wrightson offers a tranquil sky island sanctuary."
    },
    "nearby_hiking_trails": [{"trail_name": "Gardner Canyon Trail & Mount Wrightson Wilderness Access", "length_miles": 6.8, "difficulty": "Moderate to Strenuous", "features": "Sky island oak-pine forest, mountain ridge overlooks, rare birdwatching"}],
    "public_reviews_summary": "Gorgeous sky island mountain camping near Sonoita wine country with reliable cell signal and cool mountain air.",
    "other_data": "Bring fresh drinking water.",
    "last_updated": "2026-09-12"
  }
])
save_state(az, az_path)

# California (+5 sites -> 10 total)
ca, ca_path = load_state('california')
ca.extend([
  {
    "id": "california-006",
    "name": "Alabama Hills BLM Dispersed Buffer Zone",
    "state": "California",
    "county": "Inyo",
    "coordinates": {"latitude": 36.6125, "longitude": -118.1214, "elevation_ft": 4680.0},
    "management_agency": {"name": "Bureau of Land Management (BLM) - Bishop Field Office", "type": "Federal", "phone": "(760) 872-5000", "website": "https://www.blm.gov/california"},
    "rules_and_regulations": {"cost": "Free ($0/night primitive BLM dispersed camping in designated open zones; free online BLM fire permit required for stoves)", "stay_limit": "14 days maximum stay within a 28-day window", "guidelines": "Dispersed primitive camping allowed ONLY in designated open zones outside central movie rocks fee area. Camp on durable surfaces. Leave No Trace."},
    "waste_disposal_rules": {"poop_disposal": "Pack out all human waste using WAG bags / Portable Toilet due to high usage and fragile granite soils. Dump stations in Lone Pine.", "trash_policy": "Strict Pack-It-In Pack-It-Out policy."},
    "campfire_rules": {"permitted": True, "firewood_policy": "Bring firewood; no collecting down wood in fragile desert area.", "safety_requirements": "Campfire permit required. Campfires permitted in existing stone fire rings in open zones. Extinguish cold.", "seasonal_fire_bans": "Subject to BLM Stage 1 & 2 fire bans during summer/fall."},
    "access_and_road_conditions": {"road_type": "Gravel and dirt wash roads", "road_conditions": "Graded gravel access roads; accessible by standard passenger cars.", "vehicle_recommendation": "Accessible by standard FWD passenger car, camper vans, and rigs.", "scores": {"road_grade": 2, "road_terrain_difficulty": 3, "supply_run_pain": 2}},
    "nomad_connectivity_rating": {"overall_rating": "Great (4.5/5 Stars)", "verizon_reliability": "4-5 bars 5G", "att_reliability": "4 bars 5G", "tmobile_reliability": "4 bars 5G", "terrain_obstruction_risk": "Low - open Owens Valley floor looking towards Sierra Nevada wall", "distance_from_tower_corridor_miles": 2.1, "cellular_internet_dependable": True},
    "amenities": ["14,505-ft Mount Whitney Views", "Rounded Granite Rock Formations", "Dark Sky Astronomy"],
    "location_scores": {"distance_to_groceries_score": 8, "distance_to_library_score": 8, "distance_to_gym_score": 6, "terrain_score": 10, "quietness_score": 9},
    "nearest_supply_towns": [{"town_name": "Lone Pine, CA", "distance_miles": 4.5, "services_available": ["Grocery Store", "Gas Station", "Hardware Store", "Outfitters", "Restaurants", "Dump Station"]}],
    "seasonal_weather_effects": {"spring": "Ideal spring weather (70-80°F) with snowcapped Sierra peaks.", "summer": "Hot high desert summer (95-104°F).", "fall": "Crisp dry autumn weather with glowing golden granite rocks.", "winter": "Cool winter (45-60°F) with cold night temps (28°F)."},
    "dangers_and_hazards": ["High Desert Sun & Heat", "Rattlesnakes", "High Sierra Wind Gusts"],
    "acoustic_environment": {"quietness_rating": "Sierra Valley Quiet (Quietness Score: 9/10)", "common_human_made_sounds": ["Distant US-395 traffic hum", "Occasional jet contrail"]},
    "flora_and_fauna": {
      "common_plants_and_trees": ["Creosote Bush", "Desert Sagebrush", "Single-leaf Pinyon Pine", "Joshua Tree (scattered)"],
      "common_animals": ["Tule Elk", "Mule Deer", "Desert Kit Fox", "Golden Eagle"]
    },
    "human_demographics_and_culture": "Owens Valley Paiute-Shoshone, Hollywood Western film history (over 400 movies filmed here), and Mount Whitney mountaineering culture.",
    "spiritual_and_folklore_data": {
      "nature_spirits_and_mythological_lore": "Paiute traditions honor the eastern Sierra crest as sacred guardian peaks of spirit waters.",
      "energetic_and_spiritual_features": "Rounded golden granite arch formations framing 14,505-foot Mount Whitney generate world-class majestic energy."
    },
    "nearby_hiking_trails": [{"trail_name": "Mobius Arch Loop Trail", "length_miles": 1.2, "difficulty": "Easy", "features": "Natural granite arch framing Mount Whitney, movie location spots"}],
    "public_reviews_summary": "World-class views of Mount Whitney, super fast 5G cell internet, and 5 minutes to Lone Pine.",
    "other_data": "Pack out ALL human waste using WAG bags.",
    "last_updated": "2026-09-12"
  },
  {
    "id": "california-007",
    "name": "Carrizo Plain National Monument BLM Dispersed Zone",
    "state": "California",
    "county": "San Luis Obispo",
    "coordinates": {"latitude": 35.1812, "longitude": -119.6812, "elevation_ft": 2240.0},
    "management_agency": {"name": "Bureau of Land Management (BLM) - Bakersfield Field Office", "type": "Federal", "phone": "(661) 391-6000", "website": "https://www.blm.gov/california"},
    "rules_and_regulations": {"cost": "Free ($0/night primitive BLM dispersed camping in designated open ridge zones)", "stay_limit": "14 days maximum stay limit", "guidelines": "Dispersed primitive camping allowed along Elkhorn Grade and Caliente Ridge roads outside Soda Lake preserve zone. Leave No Trace."},
    "waste_disposal_rules": {"poop_disposal": "Utilize vault toilets at KCL/Selby campgrounds or pack out using WAG bags / bury 6-8 inches deep 200 ft from washes.", "trash_policy": "Strict Pack-It-In Pack-It-Out policy."},
    "campfire_rules": {"permitted": True, "firewood_policy": "Bring firewood; no wood collecting on grasslands.", "safety_requirements": "Campfire permit required. Campfires permitted in cleared metal rings in open zones. Extinguish cold.", "seasonal_fire_bans": "Subject to BLM Stage 1 & 2 fire bans during dry season."},
    "access_and_road_conditions": {"road_type": "Gravel and dirt grassland roads", "road_conditions": "Graded gravel main road; dirt roads become impassable clay mud when wet.", "vehicle_recommendation": "Accessible by standard FWD car in dry weather; 4WD required when wet.", "scores": {"road_grade": 3, "road_terrain_difficulty": 4, "supply_run_pain": 6}},
    "nomad_connectivity_rating": {"overall_rating": "Fair (2.5/5 Stars)", "verizon_reliability": "2 bars 4G LTE on Caliente Ridge", "att_reliability": "1-2 bars 4G LTE", "tmobile_reliability": "1 bar 4G LTE", "terrain_obstruction_risk": "Moderate - Caliente Mountain range and San Andreas fault scarps", "distance_from_tower_corridor_miles": 14.0, "cellular_internet_dependable": False},
    "amenities": ["Superbloom Flower Fields (Spring)", "Soda Lake Soda Crust Views", "San Andreas Fault Scarp Views"],
    "location_scores": {"distance_to_groceries_score": 4, "distance_to_library_score": 4, "distance_to_gym_score": 3, "terrain_score": 9, "quietness_score": 10},
    "nearest_supply_towns": [{"town_name": "Taft, CA", "distance_miles": 28.5, "services_available": ["Supermarket", "Gas Station", "Hardware Store", "Hospital", "Restaurants"]}, {"town_name": "Atascadero, CA", "distance_miles": 48.0, "services_available": ["Full Urban Amenities"]}],
    "seasonal_weather_effects": {"spring": "World-famous wildflower superbloom (March/April) across yellow and purple valley floors.", "summer": "Hot dry valley heat (95-104°F).", "fall": "Mild dry autumn weather.", "winter": "Cool winter (45-60°F) with rains turning clay roads to sticky mud."},
    "dangers_and_hazards": ["Clay Roads Impassable when Wet", "Extreme Remote Isolation", "Rattlesnakes"],
    "acoustic_environment": {"quietness_rating": "Vast Grassland Silence (Quietness Score: 10/10)", "common_human_made_sounds": ["High altitude commercial flights"]},
    "flora_and_fauna": {
      "common_plants_and_trees": ["California Poppy", "Goldfields", "Valley Oak", "Ephedra", "Saltbush"],
      "common_animals": ["Pronghorn Antelope", "Tule Elk", "San Joaquin Kit Fox", "Blunt-nosed Leopard Lizard", "Giant Kangaroo Rat"]
    },
    "human_demographics_and_culture": "San Joaquin Valley grassland conservation, Native Chumash rock art, and San Andreas fault geology culture.",
    "spiritual_and_folklore_data": {
      "nature_spirits_and_mythological_lore": "Chumash traditions honor Painted Rock as a sacred ceremonial temple of earth spirits.",
      "energetic_and_spiritual_features": "Vast carpet of spring wildflowers stretching across the San Andreas fault plain generates profound awe."
    },
    "nearby_hiking_trails": [{"trail_name": "Caliente Mountain Ridge Trail", "length_miles": 8.0, "difficulty": "Moderate to Strenuous", "features": "5,106-ft county high point, views of Soda Lake and Temblor range"}],
    "public_reviews_summary": "Unreal spring wildflower superblooms and complete quietness on California's last vast valley grassland.",
    "other_data": "Do not drive on dirt roads during or immediately after rain.",
    "last_updated": "2026-09-12"
  },
  {
    "id": "california-008",
    "name": "Inyo National Forest Volcanic Tablelands BLM Dispersed Zone",
    "state": "California",
    "county": "Mono / Inyo",
    "coordinates": {"latitude": 37.4125, "longitude": -118.4125, "elevation_ft": 4520.0},
    "management_agency": {"name": "Bureau of Land Management (BLM) - Bishop Field Office", "type": "Federal", "phone": "(760) 872-5000", "website": "https://www.blm.gov/california"},
    "rules_and_regulations": {"cost": "Free ($0/night primitive BLM dispersed camping; free online CA fire permit required for stoves)", "stay_limit": "14 days maximum stay within a 28-day window", "guidelines": "Dispersed primitive camping allowed along Fish Slough Road and Tablelands dirt roads. Camp on durable surfaces. Leave No Trace."},
    "waste_disposal_rules": {"poop_disposal": "Bury waste 6-8 inches deep 200 ft from Fish Slough wetlands or pack out using WAG bags. Dump station in Bishop.", "trash_policy": "Strict Pack-It-In Pack-It-Out policy."},
    "campfire_rules": {"permitted": True, "firewood_policy": "Bring firewood; no collecting down wood on tablelands.", "safety_requirements": "CA Fire Permit required. Campfires permitted in cleared metal or stone rings. Extinguish cold.", "seasonal_fire_bans": "Subject to BLM Stage 1 & 2 fire bans during dry season."},
    "access_and_road_conditions": {"road_type": "Gravel and dirt volcanic tuff roads", "road_conditions": "Graded gravel access roads; smooth sandy dirt pullouts among volcanic rocks.", "vehicle_recommendation": "Accessible by standard FWD passenger car, camper vans, and rigs.", "scores": {"road_grade": 2, "road_terrain_difficulty": 3, "supply_run_pain": 2}},
    "nomad_connectivity_rating": {"overall_rating": "Great (4.5/5 Stars)", "verizon_reliability": "4-5 bars 5G", "att_reliability": "4 bars 5G", "tmobile_reliability": "4 bars 5G", "terrain_obstruction_risk": "Low - elevated volcanic tuff plateau overlooking Owens Valley", "distance_from_tower_corridor_miles": 2.5, "cellular_internet_dependable": True},
    "amenities": ["Sierra Nevada & White Mountain Vistas", "Volcanic Tuff Bouldering", "Dark Sky Astronomy"],
    "location_scores": {"distance_to_groceries_score": 8, "distance_to_library_score": 8, "distance_to_gym_score": 7, "terrain_score": 9, "quietness_score": 9},
    "nearest_supply_towns": [{"town_name": "Bishop, CA", "distance_miles": 6.2, "services_available": ["Supermarkets", "Hospital", "Public Library", "Gym & Fitness Center", "Outfitters", "Bakery & Dining"]}],
    "seasonal_weather_effects": {"spring": "Ideal spring weather (68-78°F) with snowcapped Sierra peaks.", "summer": "Hot high desert summer (92-100°F).", "fall": "Crisp autumn weather with golden bishop tufa reflections.", "winter": "Cool winter (42-55°F) with cold night temps (25°F)."},
    "dangers_and_hazards": ["High Desert Sun & Heat", "Rattlesnakes", "Sudden Windstorms"],
    "acoustic_environment": {"quietness_rating": "Volcanic Plateau Quiet (Quietness Score: 9/10)", "common_human_made_sounds": ["Distant US-395 traffic hum", "Occasional boulderer car"]},
    "flora_and_fauna": {
      "common_plants_and_trees": ["Big Sagebrush", "Bitterbrush", "Single-leaf Pinyon Pine", "Desert Peach"],
      "common_animals": ["Owens Valley Tule Elk", "Mule Deer", "Chukar", "Golden Eagle"]
    },
    "human_demographics_and_culture": "Eastern Sierra Bishop climbing, bouldering, Owens Valley Paiute petroglyph, and outdoor recreation culture.",
    "spiritual_and_folklore_data": {
      "nature_spirits_and_mythological_lore": "Paiute history honors the Volcanic Tablelands and Fish Slough petroglyphs as sacred ceremonial rock art sites.",
      "energetic_and_spiritual_features": "360-degree views bounded by 14,000-foot Sierra Nevada and White Mountain ranges generate sublime clarity."
    },
    "nearby_hiking_trails": [{"trail_name": "Happy Boulders & Fish Slough Petroglyph Trail", "length_miles": 3.5, "difficulty": "Easy to Moderate", "features": "Volcanic tuff bouldering canyons, ancient Native petroglyphs, wetland birdwatching"}],
    "public_reviews_summary": "Incredible volcanic climbing landscape, blazing fast 5G cell internet, and 10 minutes to Bishop's famous bakery.",
    "other_data": "Respect protected petroglyph rock art sites (do not touch rock art).",
    "last_updated": "2026-09-12"
  },
  {
    "id": "california-009",
    "name": "Sierra National Forest Black Rock Primitive Dispersed Zone",
    "state": "California",
    "county": "Fresno",
    "coordinates": {"latitude": 36.9125, "longitude": -119.0142, "elevation_ft": 4120.0},
    "management_agency": {"name": "U.S. Forest Service - Sierra National Forest (High Sierra Ranger District)", "type": "Federal", "phone": "(559) 855-5355", "website": "https://www.fs.usda.gov/sierra"},
    "rules_and_regulations": {"cost": "Free ($0/night primitive dispersed forest camping; free CA fire permit required for stoves)", "stay_limit": "14 days maximum stay within a 30-day window", "guidelines": "Dispersed primitive camping allowed along Black Rock Road (FR 11S12) outside developed fee sites. Camp 100 ft from Kings River. Leave No Trace."},
    "waste_disposal_rules": {"poop_disposal": "Bury waste 6-8 inches deep 200 ft from Kings River. Pack out toilet paper.", "trash_policy": "Strict Pack-It-In Pack-It-Out policy."},
    "campfire_rules": {"permitted": True, "firewood_policy": "Gather dead and down wood locally.", "safety_requirements": "CA Fire Permit required. Campfires permitted in cleared stone rings. Extinguish cold.", "seasonal_fire_bans": "Subject to USFS dry season burn bans."},
    "access_and_road_conditions": {"road_type": "Paved mountain road to gravel forest service roads", "road_conditions": "Paved scenic access road to gravel forest turnouts.", "vehicle_recommendation": "Accessible by standard FWD passenger car in dry weather.", "scores": {"road_grade": 4, "road_terrain_difficulty": 3, "supply_run_pain": 4}},
    "nomad_connectivity_rating": {"overall_rating": "Fair (2.5/5 Stars)", "verizon_reliability": "2 bars 4G LTE on high granite ridge points", "att_reliability": "2 bars 4G LTE", "tmobile_reliability": "1 bar 4G LTE", "terrain_obstruction_risk": "High - Kings River canyon walls and massive ponderosa pine canopy", "distance_from_tower_corridor_miles": 8.5, "cellular_internet_dependable": False},
    "amenities": ["Kings River Whitewater Access", "Giant Pine Canopy", "Primitive Stone Fire Rings"],
    "location_scores": {"distance_to_groceries_score": 6, "distance_to_library_score": 6, "distance_to_gym_score": 5, "terrain_score": 9, "quietness_score": 9},
    "nearest_supply_towns": [{"town_name": "Prather, CA", "distance_miles": 18.5, "services_available": ["Grocery Store", "Gas Station", "Hardware Store", "Restaurants"]}, {"town_name": "Fresno, CA", "distance_miles": 48.0, "services_available": ["International Airport", "Major Supercenters", "Hospitals", "Full Urban Amenities"]}],
    "seasonal_weather_effects": {"spring": "Lush Sierra greening with roaring Kings River whitewater.", "summer": "Warm mountain summer (82-90°F); river swimming and pine shade.", "fall": "Crisp autumn weather with golden black oak leaves.", "winter": "Cold mountain winter (30-45°F) with light snow pack."},
    "dangers_and_hazards": ["Black Bears (Bear food storage required)", "Rushing Kings River Currents", "Rattlesnakes"],
    "acoustic_environment": {"quietness_rating": "Sierra River Canyon Audio (Quietness Score: 9/10)", "common_human_made_sounds": ["Occasional forest road car", "High altitude aircraft"]},
    "flora_and_fauna": {
      "common_plants_and_trees": ["Ponderosa Pine", "Incense Cedar", "California Black Oak", "White Fir"],
      "common_animals": ["Black Bear", "Mule Deer", "Mountain Lion", "California Quail"]
    },
    "human_demographics_and_culture": "Western Sierra Nevada mountain logging, Kings Canyon national park gateway, and whitewater kayaking culture.",
    "spiritual_and_folklore_data": {
      "nature_spirits_and_mythological_lore": "Western Mono (Monache) traditions honor the Kings River canyon as sacred spirit river grounds.",
      "energetic_and_spiritual_features": "Giant incense cedar trees and rushing mountain waters produce a restorative pine-scented sanctuary."
    },
    "nearby_hiking_trails": [{"trail_name": "Kings River National Recreation Trail", "length_miles": 6.0, "difficulty": "Moderate", "features": "Whitewater canyon views, oak woodlands, spring wildflower blooms"}],
    "public_reviews_summary": "Peaceful pine forest camping near Kings Canyon with cool river swims and zero cost.",
    "other_data": "Store food in bear canisters or vehicle trunks.",
    "last_updated": "2026-09-12"
  },
  {
    "id": "california-010",
    "name": "Shasta-Trinity National Forest McCloud River Primitive Zone",
    "state": "California",
    "county": "Siskiyou",
    "coordinates": {"latitude": 41.2148, "longitude": -122.1214, "elevation_ft": 3120.0},
    "management_agency": {"name": "U.S. Forest Service - Shasta-Trinity National Forest (McCloud Ranger District)", "type": "Federal", "phone": "(530) 964-2184", "website": "https://www.fs.usda.gov/stnf"},
    "rules_and_regulations": {"cost": "Free ($0/night primitive dispersed forest camping)", "stay_limit": "14 days maximum stay within a 30-day window", "guidelines": "Dispersed primitive camping allowed along McCloud River Loop forest service roads outside developed day-use waterfall loops. Leave No Trace."},
    "waste_disposal_rules": {"poop_disposal": "Bury waste 6-8 inches deep 200 ft from McCloud River. Pack out toilet paper.", "trash_policy": "Strict Pack-It-In Pack-It-Out policy."},
    "campfire_rules": {"permitted": True, "firewood_policy": "Gather dead and down wood locally.", "safety_requirements": "CA Fire Permit required. Campfires permitted in cleared stone rings. Extinguish cold.", "seasonal_fire_bans": "Subject to USFS dry summer fire bans."},
    "access_and_road_conditions": {"road_type": "Paved state highway to gravel forest service roads", "road_conditions": "Paved access roads to smooth gravel river turnouts.", "vehicle_recommendation": "Accessible by standard FWD passenger car.", "scores": {"road_grade": 2, "road_terrain_difficulty": 3, "supply_run_pain": 3}},
    "nomad_connectivity_rating": {"overall_rating": "Good (3/5 Stars)", "verizon_reliability": "3 bars 4G LTE", "att_reliability": "2-3 bars 4G LTE", "tmobile_reliability": "2 bars 4G LTE", "terrain_obstruction_risk": "Moderate - Mount Shasta volcanic foothills and tall fir forest", "distance_from_tower_corridor_miles": 5.2, "cellular_internet_dependable": True},
    "amenities": ["14,179-ft Mount Shasta Views", "Turquoise River Falls Access", "Douglas Fir Canopy"],
    "location_scores": {"distance_to_groceries_score": 7, "distance_to_library_score": 7, "distance_to_gym_score": 6, "terrain_score": 10, "quietness_score": 9},
    "nearest_supply_towns": [{"town_name": "McCloud, CA", "distance_miles": 7.5, "services_available": ["Grocery Store", "Gas Station", "Hardware Store", "Restaurants"]}, {"town_name": "Mount Shasta, CA", "distance_miles": 18.0, "services_available": ["Supermarket", "Hospital", "Public Library", "Gym & Fitness Center", "Outfitters"]}],
    "seasonal_weather_effects": {"spring": "Rushing glacial river melt and blooming mountain dogwood.", "summer": "Pleasant summer weather (78-86°F) with cool river swimming.", "fall": "Vibrant autumn foliage reflections on river pools.", "winter": "Cold mountain winter (25-40°F) with snowpack; Mount Shasta ski area nearby."},
    "dangers_and_hazards": ["Black Bears", "Cold Glacial River Whitewater", "High Wildfire Risk in Late Summer"],
    "acoustic_environment": {"quietness_rating": "Turquoise River Audio (Quietness Score: 9/10)", "common_human_made_sounds": ["Occasional forest road car", "High altitude aircraft"]},
    "flora_and_fauna": {
      "common_plants_and_trees": ["Douglas Fir", "Ponderosa Pine", "Incense Cedar", "Pacific Dogwood"],
      "common_animals": ["Black Bear", "Mule Deer", "Redband Trout", "Bald Eagle"]
    },
    "human_demographics_and_culture": "Northern California Shasta mountain timber, trout fishing, and Mount Shasta spiritual tourism culture.",
    "spiritual_and_folklore_data": {
      "nature_spirits_and_mythological_lore": "Wintu and Pit River traditions honor Mount Shasta and the McCloud River as sacred sources of life water.",
      "energetic_and_spiritual_features": "Turquoise river pools under 14,179-foot Mount Shasta generate world-class uplifting spiritual energy."
    },
    "nearby_hiking_trails": [{"trail_name": "McCloud River Falls Trail", "length_miles": 3.8, "difficulty": "Easy to Moderate", "features": "Lower, Middle, and Upper McCloud waterfalls, volcanic basalt canyon, turquoise pools"}],
    "public_reviews_summary": "Gorgeous turquoise waterfall river camping under Mount Shasta with easy access and decent cell service.",
    "other_data": "Filter river water and store food in bear canisters.",
    "last_updated": "2026-09-12"
  }
])
save_state(ca, ca_path)

print("Arizona and California expanded to 10 campsites each!")
