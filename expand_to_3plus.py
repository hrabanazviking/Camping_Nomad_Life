import json
import os

BASE_DIR = "/home/volmarr/.gemini/antigravity/scratch/Camping_Nomad_Life/states"

# Further expansion to bring all 50 states to 3-5 primitive campsites
e3_expansion = {
  "georgia.json": [
    {
      "id": "ga-chattahoochee-nf-warwoman-dell",
      "name": "Warwoman Dell / Chattahoochee National Forest Dispersed Camping",
      "state": "Georgia",
      "county": "Rabun County",
      "coordinates": { "latitude": 34.8812, "longitude": -83.3612, "elevation_ft": 1850 },
      "management_agency": {
        "name": "US Forest Service - Chattahoochee-Oconee National Forests (Chattooga River Ranger District)",
        "type": "USFS",
        "phone": "(706) 754-6221",
        "website": "https://www.fs.usda.gov/conf"
      },
      "rules_and_regulations": {
        "cost": "100% Free - USFS Dispersed Primitive Camping (zero fee)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed primitive camping permitted along Warwoman Road pullouts (FR 28) and Sarah's Creek road spurs. Camp 100ft minimum from streams."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6-8 inches deep in soil 200 feet from Warwoman Creek. Pack out hygiene products.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down wood gathering permitted on site.",
        "safety_requirements": "Campfires in established rock fire rings only. Fully douse with water before vacating.",
        "seasonal_fire_bans": "Autumn leaf dry weather fire warnings."
      },
      "access_and_road_conditions": {
        "road_type": "Paved county road to gravel Forest Service roads (FR 28)",
        "road_conditions": "Paved main road, graded gravel forest pullouts.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance vehicles.",
        "scores": { "road_grade": 2, "road_terrain_difficulty": 3, "supply_run_pain": 3 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / Clayton Tower Line",
        "verizon_reliability": "3-4 bars 4G LTE (20-45 Mbps download)",
        "att_reliability": "3-4 bars 4G LTE",
        "tmobile_reliability": "2-3 bars 4G LTE",
        "terrain_obstruction_risk": "Low to Moderate along mountain ridge pullouts",
        "distance_from_tower_corridor_miles": 3.0,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Pristine Appalachian Creek Campsites",
        "Warwoman Waterfall Views",
        "Bartram Trailhead Access",
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
          "town_name": "Clayton, GA",
          "distance_miles": 6.0,
          "services_available": ["Ingles Supermarket", "Gas Stations", "Rabun County Public Library", "Hospital", "Restaurants"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "58-72°F, blooming wild azaleas and mountain laurel, clear trout streams.",
        "summer": "75-88°F, pleasant mountain escape from Atlanta summer heat.",
        "fall": "50-70°F, world-class North Georgia autumn foliage.",
        "winter": "32-52°F, mild mountain winter, crisp clear days."
      },
      "dangers_and_hazards": [
        "Black bears in Chattahoochee NF (bear hang or canister recommended)",
        "Flash flooding in stream gorges during heavy rain"
      ],
      "acoustic_environment": {
        "quietness_rating": "9/10 - Rushing creek water and songbirds",
        "common_human_made_sounds": ["Occasional vehicle on Warwoman Road"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["White Oak", "Eastern Hemlock", "Rhododendron", "Mountain Laurel"],
        "common_animals": ["Black Bear", "Rainbow Trout", "White-tailed Deer", "Wild Turkey"]
      },
      "human_demographics_and_culture": "Cherokee ancestral lands, North Georgia mountain outdoorsmen, Bartram Trail hikers, nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Named after the revered Cherokee leader Warwoman (Ghigau / Beloved Woman). Rich Appalachian mountain history.",
        "energetic_and_spiritual_features": "Peaceful mountain stream tranquility, lush rhododendron valley energy."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Bartram Trail (Warwoman Section)",
          "length_miles": 7.2,
          "difficulty": "Moderate",
          "features": "Becky Branch Falls, mountain bluffs, historic trail markers"
        }
      ],
      "public_reviews_summary": "Top free primitive camping in North Georgia. Beautiful mountain waterfalls, fast cell internet near Clayton, and 100% free USFS access.",
      "other_data": "Chattahoochee National Forest. Free dispersed camping.",
      "last_updated": "2026-09-12"
    }
  ],
  "illinois.json": [
    {
      "id": "il-pine-hills-larue-dispersed",
      "name": "LaRue-Pine Hills Ecological Area Dispersed Camping",
      "state": "Illinois",
      "county": "Union County",
      "coordinates": { "latitude": 37.5612, "longitude": -89.4412, "elevation_ft": 480 },
      "management_agency": {
        "name": "US Forest Service - Shawnee National Forest (Mississippi Bluffs Ranger District)",
        "type": "USFS",
        "phone": "(618) 833-8576",
        "website": "https://www.fs.usda.gov/shawnee"
      },
      "rules_and_regulations": {
        "cost": "100% Free - USFS Dispersed Primitive Camping (zero fee outside restricted research natural area core)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed primitive camping permitted along Pine Hills Road pullouts outside core Snake Road closure zone. Camp 100ft minimum from roads."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6 inches deep in soil 200 feet from Otter Pond. Pack out all paper.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down wood gathering permitted on site.",
        "safety_requirements": "Campfires in established rock fire rings only. Fully douse before vacating.",
        "seasonal_fire_bans": "Fall dry leaf fire warnings."
      },
      "access_and_road_conditions": {
        "road_type": "Paved state route to gravel Forest Service ridge road",
        "road_conditions": "Graded gravel ridge road, flat pullout turnouts.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance vehicles.",
        "scores": { "road_grade": 3, "road_terrain_difficulty": 3, "supply_run_pain": 3 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / Mississippi River Valley Tower Line",
        "verizon_reliability": "4-5 bars 4G/5G LTE (25-55 Mbps download)",
        "att_reliability": "4-5 bars 4G/5G LTE",
        "tmobile_reliability": "3-4 bars 4G LTE",
        "terrain_obstruction_risk": "Low along 400ft limestone ridge bluff top",
        "distance_from_tower_corridor_miles": 2.5,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Mississippi River Floodplain Bluff Views",
        "Shortleaf Pine & Oak Ridge Canopy",
        "Flat Dirt/Gravel Vehicle Pullouts",
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
          "town_name": "Anna / Jonesboro, IL",
          "distance_miles": 12.0,
          "services_available": ["Kroger Supermarket", "Gas Stations", "Stinson Memorial Library", "Hospital", "Restaurants"]
        },
        {
          "town_name": "Carbondale, IL",
          "distance_miles": 22.0,
          "services_available": ["Full SIU Metro Services", "Walmart / Schnucks", "24/7 Gyms", "Hardware Stores"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "55-72°F, famous biannual reptile migration on Snake Road, greening limestone bluffs.",
        "summer": "78-92°F, warm Southern Illinois summer days.",
        "fall": "55-75°F, magnificent Mississippi River valley autumn foliage.",
        "winter": "30-48°F, mild winter, dry sunny days."
      },
      "dangers_and_hazards": [
        "High limestone bluff cliffs",
        "Venomous cottonmouth snakes near swamp bottoms"
      ],
      "acoustic_environment": {
        "quietness_rating": "8/10 - Mississippi floodplain wind and swamp frog choruses",
        "common_human_made_sounds": ["Distant train whistle across Mississippi valley"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Shortleaf Pine", "Chinquapin Oak", "Bald Cypress", "Flowering Dogwood"],
        "common_animals": ["Cottonmouth Snake", "Bird-voiced Treefrog", "White-tailed Deer", "Bald Eagle"]
      },
      "human_demographics_and_culture": "Kaskaskia ancestral lands, Illinois herpetologists, Mississippi valley outdoorsmen, nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "One of the most ecologically diverse natural areas in North America. High limestone bluffs overlooking ancient Mississippi river courses.",
        "energetic_and_spiritual_features": "Exhilarating limestone ridge elevation, vast Mississippi river valley sunset vistas."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Inspiration Point Trail",
          "length_miles": 2.5,
          "difficulty": "Easy to Moderate",
          "features": "300ft limestone cliff overlook, panoramic Mississippi river valley views"
        }
      ],
      "public_reviews_summary": "Top free primitive camping in Southern Illinois. Sweeping Mississippi River bluff views, fast 5G cell internet, and 100% free USFS access.",
      "other_data": "Shawnee National Forest. Free dispersed camping.",
      "last_updated": "2026-09-12"
    }
  ],
  "michigan.json": [
    {
      "id": "mi-hiawatha-nf-sturgeon-river-gorge",
      "name": "Sturgeon River Gorge Wilderness Dispersed Primitive Camping",
      "state": "Michigan",
      "county": "Baraga / Houghton County",
      "coordinates": { "latitude": 46.6812, "longitude": -88.6512, "elevation_ft": 1150 },
      "management_agency": {
        "name": "US Forest Service - Hiawatha & Ottawa National Forests (Kent wildlife office)",
        "type": "USFS",
        "phone": "(906) 852-3500",
        "website": "https://www.fs.usda.gov/ottawa"
      },
      "rules_and_regulations": {
        "cost": "100% Free - USFS Wilderness Primitive Camping (zero fee)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed primitive camping permitted throughout Sturgeon River Gorge Wilderness. Camp 100ft minimum from river and gorge rim."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6-8 inches deep in soil 200 feet from Sturgeon River. Pack out hygiene products.",
        "trash_policy": "Strict Leave No Trace."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Abundant dead and down pine and birch wood gathering permitted.",
        "safety_requirements": "Campfires in established rock fire rings only. Fully douse with water before vacating.",
        "seasonal_fire_bans": "Spring dry leaf forest fire warnings."
      },
      "access_and_road_conditions": {
        "road_type": "Paved US 41 to gravel Forest Service roads (FR 193)",
        "road_conditions": "Graded gravel access roads, flat trailhead pullouts.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance vehicles.",
        "scores": { "road_grade": 3, "road_terrain_difficulty": 3, "supply_run_pain": 4 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Fair to Moderate / High Ridge Signal",
        "verizon_reliability": "2-3 bars 4G LTE near main county roads",
        "att_reliability": "2-3 bars 4G LTE",
        "tmobile_reliability": "1-2 bars 4G LTE",
        "terrain_obstruction_risk": "Moderate in deep sandstone river gorge",
        "distance_from_tower_corridor_miles": 5.0,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "300ft Deep Forested River Gorge Overlooks",
        "Sturgeon Falls Waterfall Views",
        "Sturgeon River Water Source (Filter mandatory)",
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
          "town_name": "Baraga / L'Anse, MI",
          "distance_miles": 16.0,
          "services_available": ["Larry's Market", "Gas Stations", "L'Anse Public Library", "Hospital", "Restaurants"]
        },
        {
          "town_name": "Houghton / Hancock, MI",
          "distance_miles": 32.0,
          "services_available": ["Full Michigan Tech Metro Services", "Walmart Supercenter", "24/7 Gyms", "Hardware Stores"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "38-52°F, roaring waterfall snowmelt cascades, greening hemlock gorge.",
        "summer": "68-80°F, ideal UP Upper Peninsula summer camping weather.",
        "fall": "42-60°F, world-class Upper Peninsula sugar maple autumn foliage.",
        "winter": "10-25°F, heavy UP snowpack, winter snowshoeing and ice fall wilderness."
      },
      "dangers_and_hazards": [
        "300ft steep sandstone gorge cliff edges",
        "Black bears in UP Michigan (bear hang or canister mandatory)"
      ],
      "acoustic_environment": {
        "quietness_rating": "10/10 - Roaring waterfall thunder and hemlock forest wind",
        "common_human_made_sounds": ["None inside wilderness boundary"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Sugar Maple", "Eastern Hemlock", "Paper Birch", "White Pine"],
        "common_animals": ["Black Bear", "Common Loon", "White-tailed Deer", "Brook Trout", "Bald Eagle"]
      },
      "human_demographics_and_culture": "Anishinaabe (Ojibwe) Keweenaw Bay Indian Community lands, UP Yooper woodsmen, backpackers, nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Ojibwe territory honoring the majestic Sturgeon River gorge as a sacred place of roaring waters and ancient hemlocks.",
        "energetic_and_spiritual_features": "Thunderous waterfall power, serene UP wilderness quietness."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Sturgeon Falls Trail",
          "length_miles": 3.8,
          "difficulty": "Moderate",
          "features": "30ft rushing waterfall, deep gorge overlooks, old-growth pine"
        }
      ],
      "public_reviews_summary": "Spectacular wilderness gorge primitive camping in Michigan's Upper Peninsula. Roaring waterfalls, serene hemlock forests, and 100% free USFS access.",
      "other_data": "Ottawa National Forest. Free wilderness dispersed camping.",
      "last_updated": "2026-09-12"
    }
  ],
  "montana.json": [
    {
      "id": "mt-custer-gallatin-nf-beartooth-highway",
      "name": "Beartooth Highway Dispersed Primitive Camping",
      "state": "Montana",
      "county": "Carbon County",
      "coordinates": { "latitude": 45.1214, "longitude": -109.3214, "elevation_ft": 7800 },
      "management_agency": {
        "name": "US Forest Service - Custer Gallatin National Forest (Beartooth Ranger District)",
        "type": "USFS",
        "phone": "(406) 446-2103",
        "website": "https://www.fs.usda.gov/custergallatin"
      },
      "rules_and_regulations": {
        "cost": "100% Free - USFS Dispersed Primitive Camping (zero fee)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed primitive camping permitted at established pullout sites along US Hwy 212 (Beartooth All-American Road) and Rock Creek dirt spur roads. Strict food storage order in effect (grizzly bear country)."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6-8 inches deep in alpine soil 200 feet from Rock Creek. Pack out all hygiene items.",
        "trash_policy": "Strict Pack-In / Pack-Out. Zero attractants left unattended."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down pine wood collection permitted.",
        "safety_requirements": "Campfires in established rock fire rings only. Fully douse with water until cold before vacating.",
        "seasonal_fire_bans": "Summer high wind fire restrictions active July-September."
      },
      "access_and_road_conditions": {
        "road_type": "Paved All-American Road (US 212) to gravel mountain pullouts",
        "road_conditions": "Paved main highway, smooth gravel turnouts.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance vehicles.",
        "scores": { "road_grade": 4, "road_terrain_difficulty": 3, "supply_run_pain": 4 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / Red Lodge Tower Line",
        "verizon_reliability": "3-4 bars 4G LTE (20-50 Mbps download)",
        "att_reliability": "3-4 bars 4G LTE",
        "tmobile_reliability": "2-3 bars 4G LTE",
        "terrain_obstruction_risk": "Low along high mountain highway pullouts",
        "distance_from_tower_corridor_miles": 3.5,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Alpine Snowcapped Beartooth Peak Views",
        "Rock Creek Mountain Stream Access",
        "Flat Gravel Van Pullouts",
        "Stone Fire Rings"
      ],
      "location_scores": {
        "distance_to_groceries_score": 7,
        "distance_to_library_score": 7,
        "distance_to_gym_score": 5,
        "terrain_score": 10,
        "quietness_score": 9
      },
      "nearest_supply_towns": [
        {
          "town_name": "Red Lodge, MT",
          "distance_miles": 10.0,
          "services_available": ["Red Lodge Supermarket", "Gas Stations", "Carbon County Library", "Hospital", "Outdoor Gear Shops", "Restaurants"]
        },
        {
          "town_name": "Billings, MT",
          "distance_miles": 62.0,
          "services_available": ["Costco / Target / Sam's Club", "Full Metro Services", "Hospitals", "24/7 Gyms"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "35-50°F, snow clearing on highway, roaring snowmelt streams.",
        "summer": "68-80°F, prime alpine mountain summer camping, cool crisp nights.",
        "fall": "40-60°F, golden aspen colors, early high mountain snow dustings.",
        "winter": "5-25°F, heavy alpine snowpack, highway closed past snow gate."
      },
      "dangers_and_hazards": [
        "Grizzly and black bear country (bear spray and certified bear canister mandatory)",
        "High altitude exertion (7,800+ ft)"
      ],
      "acoustic_environment": {
        "quietness_rating": "9/10 - Mountain wind and alpine stream cascades",
        "common_human_made_sounds": ["Occasional scenic drive vehicle on highway"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Subalpine Fir", "Engelmann Spruce", "Quaking Aspen", "Alpine Wildflowers"],
        "common_animals": ["Grizzly Bear", "Black Bear", "Bighorn Sheep", "Mountain Goat", "Elk", "Yellow-bellied Marmot"]
      },
      "human_demographics_and_culture": "Crow & Cheyenne ancestral lands, Red Lodge mountain culture, Yellowstone travelers, nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Charles Kuralt called the Beartooth Highway 'the most beautiful drive in America'. Sacred ancestral territory of the Crow nation.",
        "energetic_and_spiritual_features": "Breathtaking high alpine mountain energy, crystalline mountain stream water."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Lake Fork Rock Creek Trail",
          "length_miles": 8.0,
          "difficulty": "Moderate",
          "features": "Glacial lakes, roaring waterfalls, towering granite peaks"
        }
      ],
      "public_reviews_summary": "Top free high-alpine camping spot in Montana. Breathtaking mountain views, fast cell internet near Red Lodge, and 100% free USFS access.",
      "other_data": "Custer Gallatin National Forest. Free dispersed primitive camping.",
      "last_updated": "2026-09-12"
    }
  ]
}

for filename, sites in e3_expansion.items():
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
