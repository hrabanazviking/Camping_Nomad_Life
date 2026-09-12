import json
import os

BASE_DIR = "/home/volmarr/.gemini/antigravity/scratch/Camping_Nomad_Life/states"

group_i = {
  "north_carolina.json": [
    {
      "id": "nc-nantahala-nf-panthertown-valley",
      "name": "Panthertown Valley Dispersed Primitive Campsites",
      "state": "North Carolina",
      "county": "Jackson / Transylvania County",
      "coordinates": { "latitude": 35.1612, "longitude": -83.0214, "elevation_ft": 3600 },
      "management_agency": {
        "name": "US Forest Service - Nantahala National Forest (Nantahala Ranger District)",
        "type": "USFS",
        "phone": "(828) 524-6441",
        "website": "https://www.fs.usda.gov/nfsnc"
      },
      "rules_and_regulations": {
        "cost": "100% Free - USFS Dispersed Primitive Camping (zero fee)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed primitive camping permitted at designated sites throughout Panthertown Valley ('Yosemite of the East'). Bear canister required."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6-8 inches deep in soil 200 feet from Tuckasegee River headwaters and waterfalls. Pack out hygiene products.",
        "trash_policy": "Strict Leave No Trace wilderness policy."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down wood gathering permitted on site.",
        "safety_requirements": "Campfires in established rock fire rings only. Fully douse with water before vacating.",
        "seasonal_fire_bans": "Fall leaf dry weather fire warnings."
      },
      "access_and_road_conditions": {
        "road_type": "Paved state road to gravel Forest Service parking lot",
        "road_conditions": "Graded gravel access parking lot, 0.8 mile hike-in.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance passenger cars.",
        "scores": { "road_grade": 2, "road_terrain_difficulty": 3, "supply_run_pain": 3 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / Cashiers-Highlands Tower Line",
        "verizon_reliability": "3-4 bars 4G LTE near Salt Rock gap / high trail ridges",
        "att_reliability": "3-4 bars 4G LTE",
        "tmobile_reliability": "2-3 bars 4G LTE",
        "terrain_obstruction_risk": "Moderate inside deep granite gorge basins",
        "distance_from_tower_corridor_miles": 3.5,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Granite Cliff Gorges & Waterfall Campsites",
        "Schoolhouse Falls & Granny Burrell Falls Views",
        "Tuckasegee Headwaters Water Source (Filter mandatory)",
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
          "town_name": "Cashiers / Brevard, NC",
          "distance_miles": 8.0,
          "services_available": ["Ingles Supermarket", "Gas Stations", "Albert Carlton Cashiers Library", "Restaurants", "Outfitters"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "52-68°F, blooming rhododendron and mountain laurel, roaring waterfalls.",
        "summer": "72-84°F, pleasant high mountain escape from Southern heat.",
        "fall": "50-70°F, world-class Blue Ridge autumn foliage.",
        "winter": "28-45°F, crisp mountain snow, frozen waterfall cliffs."
      },
      "dangers_and_hazards": [
        "Black bears in Panthertown (bear canister mandatory for food storage)",
        "Slick granite rocks around waterfalls"
      ],
      "acoustic_environment": {
        "quietness_rating": "9/10 - Waterfall thunder and mountain breeze",
        "common_human_made_sounds": ["Occasional mountain hiker on trail"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Catawba Rhododendron", "Mountain Laurel", "Pitch Pine", "Hemlock"],
        "common_animals": ["Black Bear", "Peregrine Falcon", "Native Brook Trout", "White-tailed Deer"]
      },
      "human_demographics_and_culture": "Cherokee ancestral lands, Blue Ridge mountain outdoorsmen, backpackers, nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Known as the 'Yosemite of the East'. Sacred Cherokee territory honoring the ancient granite domes and roaring waterfall gorges.",
        "energetic_and_spiritual_features": "Exhilarating granite dome mountain energy, thunderous waterfall spray."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Panthertown Valley Waterfall Trail",
          "length_miles": 6.5,
          "difficulty": "Moderate",
          "features": "Schoolhouse Falls, Blackrock Mountain granite dome, sand beaches"
        }
      ],
      "public_reviews_summary": "North Carolina's hidden paradise in Nantahala National Forest. Granite domes, majestic waterfalls, fast cell internet near Cashiers, and 100% free USFS access.",
      "other_data": "Nantahala National Forest. Free primitive dispersed camping.",
      "last_updated": "2026-09-12"
    }
  ],
  "ohio.json": [
    {
      "id": "oh-shawnee-state-forest-backpack",
      "name": "Shawnee State Forest Backpack Primitive Campsites",
      "state": "Ohio",
      "county": "Scioto County",
      "coordinates": { "latitude": 38.7412, "longitude": -83.1812, "elevation_ft": 920 },
      "management_agency": {
        "name": "Ohio Department of Natural Resources (ODNR) - Division of Forestry",
        "type": "State ODNR",
        "phone": "(740) 858-6685",
        "website": "https://forestry.ohiodnr.gov"
      },
      "rules_and_regulations": {
        "cost": "100% Free - Free ODNR Backpacking Permit required online/at forest office (zero cost)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed primitive camping permitted at 7 designated backpack trail camps along Shawnee State Forest Day Hike & Backpack Trail."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Use wooden pit privy provided at backpack camps or dig cat-hole 6 inches deep in soil 200ft from streams. Pack out paper.",
        "trash_policy": "Strict Carry-In / Carry-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down wood gathering permitted on site.",
        "safety_requirements": "Campfires in established stone fire rings only. Fully douse with water before vacating.",
        "seasonal_fire_bans": "Spring and fall forest fire warnings."
      },
      "access_and_road_conditions": {
        "road_type": "Paved state route to gravel forest entrance road",
        "road_conditions": "Graded gravel parking area access.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance passenger cars.",
        "scores": { "road_grade": 2, "road_terrain_difficulty": 3, "supply_run_pain": 3 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / Portsmouth & US 52 Tower Line",
        "verizon_reliability": "3-4 bars 4G LTE on high forest ridges",
        "att_reliability": "3-4 bars 4G LTE",
        "tmobile_reliability": "2-3 bars 4G LTE",
        "terrain_obstruction_risk": "Low to Moderate across 'Little Smokies' Appalachian hills",
        "distance_from_tower_corridor_miles": 3.5,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Appalachian Foothill Ridge Campsites",
        "Pit Privy Toilet at Camp Clearings",
        "Water Cistern (Treatment mandatory)",
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
          "town_name": "Portsmouth, OH",
          "distance_miles": 12.0,
          "services_available": ["Kroger Supermarket", "Walmart", "Portsmouth Public Library", "SOMC Hospital", "24/7 Gyms"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "50-68°F, blooming wild phlox and dogwood.",
        "summer": "75-88°F, warm Ohio summer days under shaded hardwoods.",
        "fall": "50-70°F, world-class 'Little Smokies' autumn foliage.",
        "winter": "25-42°F, mild winter, light snow."
      },
      "dangers_and_hazards": [
        "Ticks in summer months (use permethrin)"
      ],
      "acoustic_environment": {
        "quietness_rating": "9/10 - Forest wind and woodland bird calls",
        "common_human_made_sounds": ["Occasional backpacker on trail"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["White Oak", "Chestnut Oak", "Tulip Poplar", "Flowering Dogwood"],
        "common_animals": ["White-tailed Deer", "Wild Turkey", "Bobcat", "Pileated Woodpecker"]
      },
      "human_demographics_and_culture": "Shawnee ancestral lands ('Little Smokies of Ohio'), Appalachian woodsmen, backpackers, nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Known as the 'Little Smokies of Ohio'. Ancient Shawnee nation homeland honors the rugged ridge forests.",
        "energetic_and_spiritual_features": "Peaceful Appalachian ridge quietness, breathtaking autumn hill colors."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Shawnee Backpack Trail Loop",
          "length_miles": 14.0,
          "difficulty": "Moderate to Strenuous",
          "features": "Rugged Appalachian ridges, hollows, pine and oak forests"
        }
      ],
      "public_reviews_summary": "Ohio's premier backpacking destination in the 'Little Smokies'. Free primitive campsite trail clearings with pit privies, solid cell internet, and 15 minutes to Portsmouth.",
      "other_data": "Ohio ODNR Division of Forestry. Free permit required.",
      "last_updated": "2026-09-12"
    }
  ]
}

for filename, sites in group_i.items():
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
