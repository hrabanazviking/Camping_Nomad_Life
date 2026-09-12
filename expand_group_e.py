import json
import os

BASE_DIR = "/home/volmarr/.gemini/antigravity/scratch/Camping_Nomad_Life/states"

group_e = {
  "kentucky.json": [
    {
      "id": "ky-beaver-creek-wilderness-dispersed",
      "name": "Beaver Creek Wilderness Backpacking Primitive Camping",
      "state": "Kentucky",
      "county": "McCreary County",
      "coordinates": { "latitude": 36.8812, "longitude": -84.4412, "elevation_ft": 1120 },
      "management_agency": {
        "name": "US Forest Service - Daniel Boone National Forest (Stearns Ranger District)",
        "type": "USFS",
        "phone": "(606) 376-5323",
        "website": "https://www.fs.usda.gov/dbnf"
      },
      "rules_and_regulations": {
        "cost": "100% Free - USFS Wilderness Dispersed Primitive Camping (zero fee)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed wilderness camping permitted throughout Beaver Creek Wilderness. Camp 100ft minimum from trails and streams."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6-8 inches deep in organic soil 200 feet from Beaver Creek. Pack out all paper.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down wood gathering permitted on forest lands.",
        "safety_requirements": "Campfires in established rock fire rings only. Fully douse with water before vacating.",
        "seasonal_fire_bans": "Autumn dry leaf fire warnings."
      },
      "access_and_road_conditions": {
        "road_type": "Paved US 27 to gravel Forest Service roads (FR 411)",
        "road_conditions": "Graded gravel access roads, flat trailhead parking.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance passenger cars.",
        "scores": { "road_grade": 3, "road_terrain_difficulty": 3, "supply_run_pain": 4 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Moderate / US 27 Corridor Signal",
        "verizon_reliability": "3-4 bars 4G LTE near Whitley City / US 27",
        "att_reliability": "3-4 bars 4G LTE",
        "tmobile_reliability": "2-3 bars 4G LTE",
        "terrain_obstruction_risk": "Moderate inside sandstone cliff gorge",
        "distance_from_tower_corridor_miles": 4.0,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Sandstone Cliff Overlook Campsites",
        "Beaver Creek Trout Water Source (Filter mandatory)",
        "Hardwood Canopy Shade",
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
          "town_name": "Whitley City / Somerset, KY",
          "distance_miles": 12.0,
          "services_available": ["Kroger / Save-A-Lot", "Gas Stations", "McCreary County Library", "Hospital", "Restaurants"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "52-70°F, blooming wild azaleas, spring stream cascades.",
        "summer": "78-90°F, warm summer days under shaded hardwoods.",
        "fall": "52-72°F, colorful Appalachian cliff autumn foliage.",
        "winter": "28-45°F, mild winter, light snow."
      },
      "dangers_and_hazards": [
        "Sandstone cliff drop-offs",
        "Copperhead snakes in rocky talus"
      ],
      "acoustic_environment": {
        "quietness_rating": "9/10 - Creek water cascades and mountain wind",
        "common_human_made_sounds": ["Occasional backpacker on trail"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Shortleaf Pine", "White Oak", "Hemlock", "Rhododendron"],
        "common_animals": ["White-tailed Deer", "Wild Turkey", "Bobcat", "Pileated Woodpecker"]
      },
      "human_demographics_and_culture": "Cherokee ancestral lands, Cumberland Plateau outdoorsmen, Daniel Boone NF backpackers, nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Traditional Cherokee territory honoring the sandstone bluffs and pristine creek waters of the Cumberland Plateau.",
        "energetic_and_spiritual_features": "Peaceful sandstone gorge quietness, pristine stream water clarity."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Beaver Creek Wilderness Trail",
          "length_miles": 7.5,
          "difficulty": "Moderate",
          "features": "Sandstone rock arches, coal seam historic sites, hemlock gorges"
        }
      ],
      "public_reviews_summary": "Incredible free wilderness backpacking in Kentucky's Daniel Boone National Forest. Sandstone arches, fast cell internet near Whitley City, and 100% free USFS access.",
      "other_data": "Daniel Boone National Forest. Free wilderness dispersed camping.",
      "last_updated": "2026-09-12"
    }
  ],
  "louisiana.json": [
    {
      "id": "la-sherburne-wma-primitive-campground",
      "name": "Sherburne Wildlife Management Area Primitive Campground",
      "state": "Louisiana",
      "county": "Pointe Coupee Parish",
      "coordinates": { "latitude": 30.4812, "longitude": -91.6812, "elevation_ft": 30 },
      "management_agency": {
        "name": "Louisiana Department of Wildlife and Fisheries (LDWF)",
        "type": "State LDWF",
        "phone": "(337) 948-0255",
        "website": "https://www.wlf.louisiana.gov"
      },
      "rules_and_regulations": {
        "cost": "100% Free - Free LDWF WMA Camping Permit required online (zero cost)",
        "stay_limit": "14 consecutive days stay limit",
        "guidelines": "Dispersed primitive camping permitted at designated camping areas throughout Sherburne WMA in Atchafalaya Basin."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Use portable toilet or dig cat-hole 6 inches deep in soil 200 feet from bayou water. Pack out all paper.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down cypress and oak wood collection permitted on site.",
        "safety_requirements": "Campfires in established rock fire rings only. Fully douse before vacating.",
        "seasonal_fire_bans": "Observe dry weather burn warnings."
      },
      "access_and_road_conditions": {
        "road_type": "Paved parish road to gravel WMA access roads",
        "road_conditions": "Graded gravel access roads, flat dirt turnouts.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance vehicles.",
        "scores": { "road_grade": 1, "road_terrain_difficulty": 3, "supply_run_pain": 3 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / I-10 Atchafalaya Corridor Signal",
        "verizon_reliability": "3-4 bars 4G LTE (20-40 Mbps download)",
        "att_reliability": "3-4 bars 4G LTE",
        "tmobile_reliability": "2-3 bars 4G LTE",
        "terrain_obstruction_risk": "Low across flat cypress swamp basin",
        "distance_from_tower_corridor_miles": 3.5,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Atchafalaya Swamp & Bayou Primitive Campsites",
        "Bald Cypress & Live Oak Canopy",
        "Boat & Kayak Launching",
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
          "town_name": "Krotz Springs / Opelousas, LA",
          "distance_miles": 10.0,
          "services_available": ["Supermarket", "Gas Stations", "Public Library", "Hospital", "Cajun Restaurants"]
        },
        {
          "town_name": "Baton Rouge, LA",
          "distance_miles": 34.0,
          "services_available": ["Full State Capital Metro", "Costco / Target", "Hospitals", "24/7 Gyms"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "65-80°F, lush green swamp spring growth, mild bayou breezes.",
        "summer": "85-95°F, hot humid Cajun swamp summer weather.",
        "fall": "62-80°F, prime mild camping weather.",
        "winter": "42-65°F, mild winter, dry clear days."
      },
      "dangers_and_hazards": [
        "American Alligators in bayou waters (do not swim near banks)",
        "Mosquitoes in summer months (use permethrin)"
      ],
      "acoustic_environment": {
        "quietness_rating": "9/10 - Bayou frog choruses and barred owl calls",
        "common_human_made_sounds": ["Occasional fishing boat on bayou"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Bald Cypress", "Water Tupelo", "Spanish Moss", "Live Oak"],
        "common_animals": ["American Alligator", "Louisiana Black Bear", "Barred Owl", "Prothonotary Warbler", "Crappie"]
      },
      "human_demographics_and_culture": "Atakapa & Chitimacha ancestral lands, Cajun swamp culture, Louisiana outdoorsmen, nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Heart of the Atchafalaya National Heritage Area. Rich Cajun swamp folklore of Rougarou and sacred bayou spirits.",
        "energetic_and_spiritual_features": "Enchanting mossy cypress swamp energy, serene bayou water reflections."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Sherburne Nature Trail",
          "length_miles": 3.5,
          "difficulty": "Easy",
          "features": "Bald cypress swamps, bayou boardwalks, bird watching"
        }
      ],
      "public_reviews_summary": "Authentic Louisiana Atchafalaya basin primitive camping. Bald cypress shade, fast cell internet, and free LDWF WMA access near Krotz Springs.",
      "other_data": "LDWF Wildlife Management Area. Free WMA permit required.",
      "last_updated": "2026-09-12"
    }
  ],
  "maryland.json": [
    {
      "id": "md-janes-island-water-trail",
      "name": "Janes Island State Park Backcountry Water Trail Campsites",
      "state": "Maryland",
      "county": "Somerset County",
      "coordinates": { "latitude": 37.9812, "longitude": -75.8612, "elevation_ft": 10 },
      "management_agency": {
        "name": "Maryland Department of Natural Resources (DNR) - Park Service",
        "type": "State DNR",
        "phone": "(410) 968-1565",
        "website": "https://dnr.maryland.gov/publiclands"
      },
      "rules_and_regulations": {
        "cost": "100% Free - Free DNR Backcountry Water Trail Camping Permit required online (zero cost)",
        "stay_limit": "3 consecutive nights stay limit",
        "guidelines": "Primitive paddle-in coastal camping permitted at designated backcountry sites on Janes Island along Chesapeake Bay water trails."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Use backcountry pit privy at site or pack out human waste (WAG bags) on fragile salt marsh island. Pack out hygiene products.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Gathering dead driftwood below high tide mark permitted.",
        "safety_requirements": "Campfires permitted only on open sandy beach zone below high tide mark or established fire rings.",
        "seasonal_fire_bans": "Observe dry weather high wind fire warnings."
      },
      "access_and_road_conditions": {
        "road_type": "Paved state highway to boat ramp parking lot",
        "road_conditions": "Smooth paved boat ramp parking, 1.5 to 3 mile paddle-in access.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance vehicles to parking lot.",
        "scores": { "road_grade": 1, "road_terrain_difficulty": 3, "supply_run_pain": 4 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / Chesapeake Bay Open Water Tower Line",
        "verizon_reliability": "4-5 bars 4G/5G LTE across open water campsites",
        "att_reliability": "4-5 bars 4G/5G LTE",
        "tmobile_reliability": "3-4 bars 4G LTE",
        "terrain_obstruction_risk": "Low across flat open salt marsh bay island",
        "distance_from_tower_corridor_miles": 2.0,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Chesapeake Bay Pristine Island Salt Marsh Campsites",
        "Private Sandy Beach Access",
        "Pit Privy Toilet",
        "World-Class Sunset Views"
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
          "town_name": "Crisfield, MD",
          "distance_miles": 3.0,
          "services_available": ["Food Lion Supermarket", "Gas Stations", "Crisfield Public Library", "Seafood Markets", "Restaurants"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "55-70°F, spring ospreys return, pleasant sea breeze.",
        "summer": "78-88°F, warm sunny Chesapeake Bay summer days, warm water.",
        "fall": "55-72°F, prime pleasant coastal weather, clear nights.",
        "winter": "35-48°F, crisp coastal winter, waterfowl migrations."
      },
      "dangers_and_hazards": [
        "High tides and wind waves in open Chesapeake Bay waters (paddle close to marsh channels)",
        "Biting greenhead flies and mosquitoes in summer (use permethrin)"
      ],
      "acoustic_environment": {
        "quietness_rating": "9/10 - Chesapeake Bay wave surf and sea bird calls",
        "common_human_made_sounds": ["Distant waterman crab boat horn on bay"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Saltmarsh Cordgrass", "Loblolly Pine", "Glasswort", "Seaside Goldenrod"],
        "common_animals": ["Osprey", "Blue Crab", "Brown Pelican", "Diamondback Terrapin", "Great Blue Heron"]
      },
      "human_demographics_and_culture": "Pocomoke & Accawmack ancestral lands, Chesapeake watermen culture, kayakers, digital nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Traditional Pocomoke nation lands honoring the pristine salt marshes and blue crab waters of the Eastern Shore.",
        "energetic_and_spiritual_features": "Exhilarating open bay ocean horizon energy, majestic golden sunset views."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Janes Island Backcountry Water Trail",
          "length_miles": 12.0,
          "difficulty": "Moderate Kayak",
          "features": "Salt marsh channels, secluded sandy beaches, island wildlife"
        }
      ],
      "public_reviews_summary": "Maryland's premier paddle-in primitive camping on Chesapeake Bay. Blazing 5G cell internet, private sandy beaches, and 5 minutes to Crisfield seafood.",
      "other_data": "Maryland DNR State Park. Free backcountry permit required.",
      "last_updated": "2026-09-12"
    }
  ]
}

for filename, sites in group_e.items():
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
