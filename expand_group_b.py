import json
import os

BASE_DIR = "/home/volmarr/.gemini/antigravity/scratch/Camping_Nomad_Life/states"

group_b = {
  "maine.json": [
    {
      "id": "me-cutler-coast-public-reserved-land",
      "name": "Cutler Coast Public Reserved Land Primitive Coastal Campsites",
      "state": "Maine",
      "county": "Washington County",
      "coordinates": { "latitude": 44.6812, "longitude": -67.2012, "elevation_ft": 80 },
      "management_agency": {
        "name": "Maine Department of Agriculture, Conservation and Forestry - Bureau of Parks and Lands",
        "type": "State BPL",
        "phone": "(207) 941-4412",
        "website": "https://www.maine.gov/dacf/parks"
      },
      "rules_and_regulations": {
        "cost": "100% Free - Maine BPL Public Reserved Land Primitive Camping (zero fee)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Primitive hike-in coastal camping permitted at designated sites at Black Cut and Fairy Point along the Bold Coast Trail network. First-come, first-served."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Use wilderness pit privy at campsite clearing or dig cat-hole 6-8 inches deep in soil 200ft from ocean line. Pack out hygiene products.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Gathering fallen beach driftwood permitted below high tide mark.",
        "safety_requirements": "Campfires permitted only on open cobble/rock beach zone below high tide mark or established fire rings.",
        "seasonal_fire_bans": "Observe Maine Forest Service dry weather fire warnings."
      },
      "access_and_road_conditions": {
        "road_type": "Paved ME Route 191 to gravel trailhead parking lot",
        "road_conditions": "Smooth gravel trailhead access lot, 3.5 to 5 mile hike-in on trail.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance vehicles.",
        "scores": { "road_grade": 2, "road_terrain_difficulty": 4, "supply_run_pain": 5 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Fair to Moderate / High Ocean Bluff Signal",
        "verizon_reliability": "2-3 bars 4G LTE on ocean bluff crests",
        "att_reliability": "2-3 bars 4G LTE",
        "tmobile_reliability": "1-2 bars 4G LTE",
        "terrain_obstruction_risk": "Moderate in deep spruce ravines; low along open ocean bluffs",
        "distance_from_tower_corridor_miles": 6.0,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Sweeping 100ft Ocean Cliff Overlook Campsites",
        "Wild Atlantic Ocean Surf & Tidal Pool Views",
        "Pit Privy Toilet",
        "Freshwater Stream Source (Filter mandatory)"
      ],
      "location_scores": {
        "distance_to_groceries_score": 4,
        "distance_to_library_score": 4,
        "distance_to_gym_score": 2,
        "terrain_score": 10,
        "quietness_score": 10
      },
      "nearest_supply_towns": [
        {
          "town_name": "Machias, ME",
          "distance_miles": 18.0,
          "services_available": ["Hannaford Supermarket", "Gas Stations", "Porter Memorial Library", "Hospital", "Restaurants"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "38-52°F, ocean fog, crisp Maine sea breeze.",
        "summer": "60-72°F, pleasant cool ocean coastal escape from summer heat.",
        "fall": "42-58°F, spectacular coastal birch and cranberry autumn colors.",
        "winter": "15-32°F, freezing ocean gales, dusting of coastal snow."
      },
      "dangers_and_hazards": [
        "Sheer 100ft ocean cliff drop-offs (watch footing near edges)",
        "Sudden thick ocean fog rolls",
        "Slick wet coastal rocks"
      ],
      "acoustic_environment": {
        "quietness_rating": "10/10 - Crashing Atlantic ocean waves and sea bird calls",
        "common_human_made_sounds": ["Distant lobster boat diesel engine on ocean horizon"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["White Spruce", "Balsam Fir", "Mountain Ash", "Crowberry", "Peat Moss"],
        "common_animals": ["Harbor Seal", "Bald Eagle", "Osprey", "Common Eider", "Whales (offshore)"]
      },
      "human_demographics_and_culture": "Passamaquoddy ancestral lands, Maine lobstermen, coastal backpackers, nature photographers.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Known as the 'Bold Coast of Maine'. Passamaquoddy territory steeped in sacred coastal legends of spirit fog and ocean guardians.",
        "energetic_and_spiritual_features": "Exhilarating 100ft Atlantic cliff energy, wild ocean surf horizon."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Bold Coast Trail Loop",
          "length_miles": 9.2,
          "difficulty": "Moderate to Strenuous",
          "features": "Ocean cliff overlooks, cobble beaches, coastal spruce-fir forest"
        }
      ],
      "public_reviews_summary": "One of the most spectacular coastal primitive camping locations in North America. Pitch a tent atop 100ft cliffs over crashing Atlantic waves, free Maine BPL access.",
      "other_data": "Maine Bureau of Parks & Lands Public Reserved Land. Free primitive camping.",
      "last_updated": "2026-09-12"
    }
  ],
  "new_mexico.json": [
    {
      "id": "nm-carson-nf-valle-vidal",
      "name": "Valle Vidal Dispersed Primitive Camping",
      "state": "New Mexico",
      "county": "Taos / Colfax County",
      "coordinates": { "latitude": 36.7812, "longitude": -105.1812, "elevation_ft": 9400 },
      "management_agency": {
        "name": "US Forest Service - Carson National Forest (Questa Ranger District)",
        "type": "USFS",
        "phone": "(575) 586-0520",
        "website": "https://www.fs.usda.gov/carson"
      },
      "rules_and_regulations": {
        "cost": "100% Free - Carson National Forest Dispersed Primitive Camping (zero fee)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed primitive camping permitted at designated pullout clearings along Forest Road 1950 outside seasonal elk calving closure areas (closed April 1 - June 30)."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6-8 inches deep in mountain soil 200 feet from Comanche Creek. Pack out all paper.",
        "trash_policy": "Strict Leave No Trace."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Abundant dead and down pine wood collection permitted.",
        "safety_requirements": "Campfires in established rock fire rings only. Fully douse with water before vacating.",
        "seasonal_fire_bans": "Spring dry mountain fire restrictions enforced."
      },
      "access_and_road_conditions": {
        "road_type": "Unpaved Dirt / Gravel Mountain Road (Forest Road 1950)",
        "road_conditions": "Graded gravel, washboard dirt, steep mountain grade switchbacks.",
        "vehicle_recommendation": "High clearance recommended; standard 2WD vehicles can access with slow careful driving in dry weather.",
        "scores": { "road_grade": 5, "road_terrain_difficulty": 5, "supply_run_pain": 5 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Fair / High Ridge Signal",
        "verizon_reliability": "2-3 bars 4G LTE on high meadow ridges",
        "att_reliability": "2-3 bars 4G LTE",
        "tmobile_reliability": "1-2 bars 4G LTE",
        "terrain_obstruction_risk": "Moderate across 9,400ft alpine valley basin",
        "distance_from_tower_corridor_miles": 7.0,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "High Alpine Meadow Prairie Panoramas ('Yellowstone of the Southwest')",
        "Ponderosa & Aspen Grove Canopy",
        "Comanche Creek Trout Water Source (Filter mandatory)",
        "Stone Fire Rings"
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
          "town_name": "Questa / Red River, NM",
          "distance_miles": 22.0,
          "services_available": ["Supermarket", "Gas Stations", "Questa Public Library", "Restaurants"]
        },
        {
          "town_name": "Taos, NM",
          "distance_miles": 44.0,
          "services_available": ["Cid's Food Market / Smith's", "Full Metro Services", "Holy Cross Hospital", "24/7 Gyms"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "40-58°F, spring snow melt, blooming mountain wildflowers.",
        "summer": "68-80°F, cool high-elevation summer climate, afternoon monsoon showers.",
        "fall": "45-65°F, world-class golden quaking aspen foliage, elk bugling season.",
        "winter": "10-30°F, heavy mountain snowpack, road snow-covered."
      },
      "dangers_and_hazards": [
        "High altitude mountain elevation sickness risk (9,400+ ft)",
        "Summer afternoon lightning strikes in open alpine meadows",
        "Black bears in Carson NF"
      ],
      "acoustic_environment": {
        "quietness_rating": "10/10 - High mountain wind and autumn elk bugles",
        "common_human_made_sounds": ["None inside wilderness basin"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Quaking Aspen", "Ponderosa Pine", "Engelmann Spruce", "Arizona Fescue Prairie Grass"],
        "common_animals": ["Elk (massive herd area)", "Black Bear", "Rio Grande Cutthroat Trout", "Mule Deer", "Golden Eagle"]
      },
      "human_demographics_and_culture": "Jicarilla Apache & Taos Pueblo ancestral lands, New Mexico ranchers, elk hunters, nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Known as the 'Yellowstone of the Southwest'. Sacred ancestral territory of the Taos Pueblo people.",
        "energetic_and_spiritual_features": "Profound high alpine meadow stillness, majestic 9,400ft mountain sky horizons."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Little Costilla Peak Trail",
          "length_miles": 7.5,
          "difficulty": "Strenuous",
          "features": "12,500ft peak summit, alpine tundra, sweeping New Mexico mountain views"
        }
      ],
      "public_reviews_summary": "Unbelievable high-alpine primitive camping in New Mexico's Carson National Forest. Massive wild elk herds, golden aspen groves, and 100% free USFS access.",
      "other_data": "Carson National Forest Valle Vidal Unit. Free dispersed camping.",
      "last_updated": "2026-09-12"
    }
  ]
}

for filename, sites in group_b.items():
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
