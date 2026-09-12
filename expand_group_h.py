import json
import os

BASE_DIR = "/home/volmarr/.gemini/antigravity/scratch/Camping_Nomad_Life/states"

group_h = {
  "new_jersey.json": [
    {
      "id": "nj-worthington-state-forest-appalachian-trail",
      "name": "Worthington State Forest Appalachian Trail Primitive Campsites",
      "state": "New Jersey",
      "county": "Warren County",
      "coordinates": { "latitude": 41.0214, "longitude": -75.1214, "elevation_ft": 1420 },
      "management_agency": {
        "name": "New Jersey Department of Environmental Protection (NJDEP) - State Park Service",
        "type": "State NJDEP",
        "phone": "(908) 841-9575",
        "website": "https://www.nj.gov/dep/parksandforests"
      },
      "rules_and_regulations": {
        "cost": "100% Free - NJDEP Primitive Backpacking Camping (zero cost along AT corridor)",
        "stay_limit": "1 night stay limit per shelter/campsite area",
        "guidelines": "Primitive backpacking camping permitted at designated Sunfish Pond / Appalachian Trail shelter sites along Kittatinny Ridge in Worthington State Forest."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Use wilderness pit privy at shelter site or dig cat-hole 6 inches deep in soil 200 feet from Sunfish Pond. Pack out hygiene products.",
        "trash_policy": "Strict Carry-In / Carry-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down wood gathering permitted on site.",
        "safety_requirements": "Campfires in established stone fire rings only. Fully douse with water until cold to touch.",
        "seasonal_fire_bans": "Spring dry leaf weather fire restrictions."
      },
      "access_and_road_conditions": {
        "road_type": "Paved Interstate 80 to gravel state forest parking lot",
        "road_conditions": "Smooth paved parking lot access, 1.5 mile hike-in on trail.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance passenger cars.",
        "scores": { "road_grade": 2, "road_terrain_difficulty": 3, "supply_run_pain": 3 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / Delaware Water Gap Tower Line",
        "verizon_reliability": "4-5 bars 4G/5G LTE (25-60 Mbps download)",
        "att_reliability": "4-5 bars 4G/5G LTE",
        "tmobile_reliability": "3-4 bars 4G LTE",
        "terrain_obstruction_risk": "Low along 1,420ft Kittatinny Mountain Ridge",
        "distance_from_tower_corridor_miles": 2.5,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Glacial Sunfish Pond Lake Vistas",
        "Kittatinny Ridge Appalachian Mountain Overlooks",
        "Pit Privy Toilet",
        "Stone Fire Ring"
      ],
      "location_scores": {
        "distance_to_groceries_score": 7,
        "distance_to_library_score": 7,
        "distance_to_gym_score": 6,
        "terrain_score": 9,
        "quietness_score": 8
      },
      "nearest_supply_towns": [
        {
          "town_name": "Delaware Water Gap / Stroudsburg, PA",
          "distance_miles": 6.0,
          "services_available": ["ShopRite / Weis", "Gas Stations", "Stroudsburg Library", "Hospital", "Restaurants"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "50-68°F, spring mountain laurel bloom, fresh mountain breeze.",
        "summer": "75-88°F, pleasant high ridge escape from NYC metro summer heat.",
        "fall": "50-70°F, spectacular Delaware Water Gap autumn foliage.",
        "winter": "25-40°F, mountain snowpack, crisp clear days."
      },
      "dangers_and_hazards": [
        "Black bears in Kittatinny Ridge (bear hang for food mandatory)",
        "Rocky Appalachian Trail footing"
      ],
      "acoustic_environment": {
        "quietness_rating": "8/10 - Ridge mountain wind and songbirds",
        "common_human_made_sounds": ["Distant highway traffic in Delaware Water Gap valley"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Chestnut Oak", "Pitch Pine", "Mountain Laurel", "Rhododendron"],
        "common_animals": ["Black Bear", "White-tailed Deer", "Timber Rattlesnake", "Broad-winged Hawk"]
      },
      "human_demographics_and_culture": "Lenape ancestral lands, Delaware Water Gap outdoorsmen, AT backpackers, digital nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "National Natural Landmark (Sunfish Pond glacial lake). Traditional Lenape territory honoring the sacred Kittatinny ridge.",
        "energetic_and_spiritual_features": "Exhilarating Kittatinny Ridge mountain energy, pristine glacial pond stillness."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Appalachian Trail (Sunfish Pond Loop)",
          "length_miles": 7.5,
          "difficulty": "Moderate to Strenuous",
          "features": "Glacial Sunfish Pond, Delaware Water Gap overlooks, rocky ridge walking"
        }
      ],
      "public_reviews_summary": "Spectacular free primitive shelter camping along New Jersey's Appalachian Trail. Glacial lake views, fast 5G cell internet, and easy 10-minute drive to Stroudsburg.",
      "other_data": "NJDEP State Forest. Free primitive backpacking camping.",
      "last_updated": "2026-09-12"
    }
  ],
  "new_york.json": [
    {
      "id": "ny-catskill-park-slide-mountain-wilderness",
      "name": "Slide Mountain Wilderness Primitive Campsites",
      "state": "New York",
      "county": "Ulster County",
      "coordinates": { "latitude": 41.9812, "longitude": -74.3812, "elevation_ft": 2450 },
      "management_agency": {
        "name": "New York State Department of Environmental Conservation (DEC) - Region 3",
        "type": "State DEC",
        "phone": "(845) 256-3000",
        "website": "https://www.dec.ny.gov"
      },
      "rules_and_regulations": {
        "cost": "100% Free - NYS DEC Catskill Forest Preserve Primitive Camping (zero fee for stays under 3 nights)",
        "stay_limit": "3 consecutive nights free without permit; up to 14 days with free DEC forest ranger permit",
        "guidelines": "Dispersed primitive camping permitted at least 150ft from trails and water streams throughout Slide Mountain Wilderness. Camp below 3,500ft elevation."
      },
      "waste_disposal_rules": {
        "poop_disposal": "Dig cat-hole 6-8 inches deep in organic soil 200 feet from Esopus Creek. Pack out all hygiene items.",
        "trash_policy": "Strict Pack-In / Pack-Out."
      },
      "campfire_rules": {
        "permitted": True,
        "firewood_policy": "Dead and down firewood collection permitted within 50 miles.",
        "safety_requirements": "Campfires in established rock fire rings only. Fully douse with water before vacating.",
        "seasonal_fire_bans": "Spring dry leaf weather fire warnings."
      },
      "access_and_road_conditions": {
        "road_type": "Paved NY Route 28 to paved/gravel county road (Oliveria Road)",
        "road_conditions": "Paved main access roads, smooth trailhead parking lot.",
        "vehicle_recommendation": "Accessible by standard 2WD low clearance passenger cars.",
        "scores": { "road_grade": 3, "road_terrain_difficulty": 3, "supply_run_pain": 3 }
      },
      "nomad_connectivity_rating": {
        "overall_rating": "Strong / Route 28 Corridor Signal",
        "verizon_reliability": "3-4 bars 4G LTE near Phoenicia / Route 28 entrance",
        "att_reliability": "3-4 bars 4G LTE",
        "tmobile_reliability": "2-3 bars 4G LTE",
        "terrain_obstruction_risk": "Moderate inside deep mountain hollows",
        "distance_from_tower_corridor_miles": 4.0,
        "cellular_internet_dependable": True
      },
      "amenities": [
        "Catskill Mountain Wilderness Campsites",
        "Esopus Creek Trout Stream Access",
        "Hardwood & Hemlock Forest Shade",
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
          "town_name": "Phoenicia / Boiceville, NY",
          "distance_miles": 10.0,
          "services_available": ["Supermarket", "Gas Stations", "Phoenicia Library", "Pharmacy", "Restaurants"]
        },
        {
          "town_name": "Kingston, NY",
          "distance_miles": 26.0,
          "services_available": ["Full Metro Services", "Target / Walmart", "HealthAlliance Hospital", "24/7 Gyms"]
        }
      ],
      "seasonal_weather_effects": {
        "spring": "45-62°F, blooming wild trillium, roaring trout streams.",
        "summer": "70-82°F, cool Catskill mountain escape from NYC summer heat.",
        "fall": "48-65°F, world-class Catskill red sugar maple foliage.",
        "winter": "18-35°F, heavy mountain snowpack, snowshoeing & ice climbing."
      },
      "dangers_and_hazards": [
        "Black bears in Catskills (NYS DEC approved bear canister mandatory for food storage)",
        "Slick stream rock crossings"
      ],
      "acoustic_environment": {
        "quietness_rating": "9/10 - Rushing trout stream and mountain forest wind",
        "common_human_made_sounds": ["Occasional backpacker on trail"]
      },
      "flora_and_fauna": {
        "common_plants_and_trees": ["Sugar Maple", "Yellow Birch", "Eastern Hemlock", "Balsam Fir"],
        "common_animals": ["Black Bear", "White-tailed Deer", "Brown Trout", "Bicknell's Thrush", "Fisher"]
      },
      "human_demographics_and_culture": "Munsee Lenape ancestral lands, Catskill guides, John Burroughs conservation heritage, NYC nomads.",
      "spiritual_and_folklore_data": {
        "nature_spirits_and_mythological_lore": "Famous home of Rip Van Winkle folklore. Where John Burroughs wrote his legendary nature essays.",
        "energetic_and_spiritual_features": "Profound Catskill mountain silence, pristine trout stream water."
      },
      "nearby_hiking_trails": [
        {
          "trail_name": "Slide Mountain Summit Trail",
          "length_miles": 5.6,
          "difficulty": "Moderate to Strenuous",
          "features": "Highest peak in Catskills (4,180ft), balsam fir forest, panoramic Catskill vistas"
        }
      ],
      "public_reviews_summary": "Top free primitive wilderness camping in New York's Catskill Park. Majestic hardwood forests, crystal clear trout streams, fast cell internet near Phoenicia.",
      "other_data": "NYS DEC Catskill Forest Preserve. 100% Free.",
      "last_updated": "2026-09-12"
    }
  ]
}

for filename, sites in group_h.items():
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
