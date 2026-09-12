import json
import os

STATES_DIR = "/home/volmarr/.gemini/antigravity/scratch/Camping_Nomad_Life/states"

new_sites_by_state = {
    "New Mexico": [
        {
            "campsite_name": "Box Canyon Dispersed Camping (BLM Socorro)",
            "state": "New Mexico",
            "managing_agency": "Bureau of Land Management (Socorro Field Office)",
            "gps_coordinates": "34.0289, -107.0142",
            "is_100_percent_free": True,
            "total_cost_or_fees": "$0 - 100% Free Public Land",
            "maximum_stay_length": "14 days within a 28-day period",
            "rules_and_regulations": "Free dispersed camping on open BLM lands. Pack in all supplies and pack out all waste. No trash service. Respect private property boundaries nearby.",
            "poop_disposal_rules": "Bury human waste at least 6 to 8 inches deep in a cathole dug 200 feet away from water sources, trails, and campsites, or pack out via human waste bag system.",
            "campfire_rules": "Campfires permitted subject to seasonal fire restrictions. Use established fire rings where available. Must be extinguished cold to touch with water and soil before departure.",
            "ranger_agency_contact": "BLM Socorro Field Office: (575) 835-0412",
            "access_and_road_conditions": {
                "recommended_vehicle": "Standard low-clearance 2WD accessible for lower pullouts; high-clearance suggested for upper canyon tracks",
                "road_type_and_condition": "Gravel and hard-packed dirt road. Smooth near main access, slightly rougher with dip crossings inside the canyon area.",
                "scores": {
                    "front_wheel_drive_clearance": 7,
                    "high_clearance_necessary": 4,
                    "four_wheel_drive_necessary": 2,
                    "seasonal_impassability_risk": 4
                }
            },
            "nearest_supply_towns": [
                {
                    "town_name": "Socorro, NM",
                    "distance_miles": 9,
                    "amenities_available": "Grocery stores, gas stations, hardware stores, restaurants, pharmacy, mechanic"
                }
            ],
            "seasonal_weather_and_best_times": "Best in spring and autumn with mild sunny days (65°F to 80°F). Summers are hot (>95°F). Winters bring freezing night temperatures.",
            "dangers_and_hazards": "Flash flooding risk during summer monsoon rains (July-August). Rattlesnakes, scorpions, and sharp desert vegetation.",
            "nomad_connectivity_rating": {
                "t_mobile_signal": "3-4 bars 5G/4G LTE",
                "verizon_signal": "4 bars 5G/4G LTE",
                "att_signal": "3-4 bars 5G/4G LTE",
                "terrain_obstruction_risk": "Low to Moderate inside canyon walls",
                "distance_to_nearest_tower_miles": 6.5,
                "is_cellular_internet_dependable": True,
                "recommendation_for_remote_workers": "Excellent site for remote work due to close proximity to Socorro cell towers and low obstruction on upper canyon rim."
            },
            "amenities_and_features": [
                "Dispersed Campsites",
                "Rock Climbing Crags",
                "Scenic Canyon Views",
                "Dark Night Skies",
                "Pet Friendly"
            ],
            "location_scores": {
                "scenery": 8,
                "privacy": 7,
                "accessibility": 8,
                "shade_coverage": 4,
                "water_proximity": 2,
                "safety": 8
            },
            "flora_fauna_and_ecosystem": "Chihuahuan desert grassland transition. Creosote bush, ocotillo, yucca, prickly pear cactus. Roadrunners, red-tailed hawks, coyotes, mule deer.",
            "spiritual_cultural_and_folklore": "Historic Puebloan trade routes and 19th-century mining history surrounding the Magdalena Mountains.",
            "hiking_trails_and_outdoor_recreation": "Box Canyon Recreation Area rock climbing routes, Box Canyon trail loop, mountain biking on nearby dirt roads.",
            "nearest_hospital_and_emergency": "Socorro General Hospital, 1202 Hwy 60 W, Socorro, NM (Approx 10 miles)",
            "trash_and_waste_policy": "Strict Pack-In/Pack-Out policy. All trash and food scraps must be hauled to Socorro disposal points.",
            "last_updated": "2026-09-12"
        },
        {
            "campsite_name": "Mills Canyon Dispersed Camping (Kiowa National Grassland)",
            "state": "New Mexico",
            "managing_agency": "US Forest Service - Cibola National Forest & Kiowa National Grassland",
            "gps_coordinates": "36.0456, -104.3618",
            "is_100_percent_free": True,
            "total_cost_or_fees": "$0 - 100% Free Public Land",
            "maximum_stay_length": "14 days",
            "rules_and_regulations": "Dispersed camping allowed throughout Kiowa National Grassland public rim and canyon areas. Leave No Trace. No garbage collection.",
            "poop_disposal_rules": "Dig cathole 6-8 inches deep at least 200 feet away from Canadian River and rim drainages. Pack out all hygiene items.",
            "campfire_rules": "Fire permitted in designated rings or existing cleared fire spots unless USFS stage restrictions apply. Ensure 100% cold before leaving.",
            "ranger_agency_contact": "Kiowa National Grassland District Office (Roy, NM): (575) 485-2270",
            "access_and_road_conditions": {
                "recommended_vehicle": "2WD suitable for canyon rim campsites; high-clearance 4WD required for descent into Mills Canyon floor",
                "road_type_and_condition": "Steep, narrow gravel/dirt switchback canyon descent. Extremely slick and dangerous when wet.",
                "scores": {
                    "front_wheel_drive_clearance": 5,
                    "high_clearance_necessary": 8,
                    "four_wheel_drive_necessary": 7,
                    "seasonal_impassability_risk": 8
                }
            },
            "nearest_supply_towns": [
                {
                    "town_name": "Roy, NM",
                    "distance_miles": 14,
                    "amenities_available": "Limited gas station, small market, post office"
                },
                {
                    "town_name": "Springer, NM",
                    "distance_miles": 38,
                    "amenities_available": "Full grocery, hardware, gas, restaurants"
                }
            ],
            "seasonal_weather_and_best_times": "Spring and autumn are optimal (60°F-78°F). High winds common in spring. Summer can be hot in canyon bottom (90°F+).",
            "dangers_and_hazards": "Steep rim cliffs, flash floods along Canadian River, extreme mud making canyon road impassable, rattlesnakes.",
            "nomad_connectivity_rating": {
                "t_mobile_signal": "1-2 bars 4G LTE on Rim / 0-1 bar Canyon Bottom",
                "verizon_signal": "2-3 bars 4G LTE on Rim / 1 bar Canyon Bottom",
                "att_signal": "2 bars 4G LTE on Rim / 0-1 bar Canyon Bottom",
                "terrain_obstruction_risk": "High inside Canadian River Canyon / Low on Grassland Rim",
                "distance_to_nearest_tower_miles": 14.0,
                "is_cellular_internet_dependable": False,
                "recommendation_for_remote_workers": "Cellular internet is usable only on the canyon rim. Workers should set up camps near the rim edge for stable speeds."
            },
            "amenities_and_features": [
                "Canyon Rim Overlooks",
                "Canadian River Access",
                "Historic Orchard Ruins",
                "Wilderness Solitude",
                "Stargazing"
            ],
            "location_scores": {
                "scenery": 9,
                "privacy": 9,
                "accessibility": 4,
                "shade_coverage": 5,
                "water_proximity": 4,
                "safety": 6
            },
            "flora_fauna_and_ecosystem": "Shortgrass prairie rim transitioning to Ponderosa pine and cottonwood canyon bottom. Barbary sheep, elk, mule deer, wild turkey, cougars.",
            "spiritual_cultural_and_folklore": "Historic Melvin Mills 1880s fruit orchard ruins destroyed by catastrophic 1904 Canadian River flood.",
            "hiking_trails_and_outdoor_recreation": "Mills Canyon Rim Trail, Canadian River canyon hiking, historic ruin exploration, bird watching.",
            "nearest_hospital_and_emergency": "Miners' Colfax Medical Center, 2035 S 2nd St, Raton, NM (Approx 70 miles)",
            "trash_and_waste_policy": "Strict Pack-In/Pack-Out. No dumpsters anywhere on the grassland.",
            "last_updated": "2026-09-12"
        },
        {
            "campsite_name": "Datil Well Dispersed Area (BLM / Cibola NF Border)",
            "state": "New Mexico",
            "managing_agency": "Bureau of Land Management (Socorro) / USFS Cibola National Forest",
            "gps_coordinates": "34.1481, -107.8483",
            "is_100_percent_free": True,
            "total_cost_or_fees": "$0 - 100% Free Public Land",
            "maximum_stay_length": "14 days",
            "rules_and_regulations": "Free dispersed camping on surrounding BLM and National Forest lands. Keep vehicles on established tracks. Pack out all waste.",
            "poop_disposal_rules": "Standard 6-8 inch catholes dug 200 feet from drainage areas and campsites.",
            "campfire_rules": "Follow seasonal fire restrictions. Extinguish completely with water and dirt until cool to touch.",
            "ranger_agency_contact": "BLM Socorro Field Office: (575) 835-0412",
            "access_and_road_conditions": {
                "recommended_vehicle": "Low-clearance 2WD easily accessible along US-60 dirt spur roads",
                "road_type_and_condition": "Well-maintained gravel roads with minimal rutting.",
                "scores": {
                    "front_wheel_drive_clearance": 9,
                    "high_clearance_necessary": 2,
                    "four_wheel_drive_necessary": 1,
                    "seasonal_impassability_risk": 3
                }
            },
            "nearest_supply_towns": [
                {
                    "town_name": "Pie Town, NM",
                    "distance_miles": 21,
                    "amenities_available": "Famous pie cafes, small general store, gas station"
                },
                {
                    "town_name": "Magdalena, NM",
                    "distance_miles": 36,
                    "amenities_available": "Gas, groceries, hardware, cafes"
                }
            ],
            "seasonal_weather_and_best_times": "Late spring through early autumn (elevation ~7,400 ft provides cooler summer temperatures around 80°F-85°F). Winter brings snow.",
            "dangers_and_hazards": "High elevation sun exposure, rapid nighttime temperature drops, summer afternoon lightning storms.",
            "nomad_connectivity_rating": {
                "t_mobile_signal": "2-3 bars 4G LTE",
                "verizon_signal": "3 bars 4G LTE",
                "att_signal": "2-3 bars 4G LTE",
                "terrain_obstruction_risk": "Low",
                "distance_to_nearest_tower_miles": 4.2,
                "is_cellular_internet_dependable": True,
                "recommendation_for_remote_workers": "Dependable signal for remote work along US-60 corridor near Datil village tower."
            },
            "amenities_and_features": [
                "Ponderosa & Piñon Pine Shade",
                "Continental Divide Trail Access",
                "Easy Highway Access",
                "Dark Sky Stargazing"
            ],
            "location_scores": {
                "scenery": 7,
                "privacy": 8,
                "accessibility": 9,
                "shade_coverage": 7,
                "water_proximity": 1,
                "safety": 9
            },
            "flora_fauna_and_ecosystem": "Piñon-juniper savanna transitioning to Ponderosa pine forest. Pronghorn antelope, mule deer, elk, gray foxes, golden eagles.",
            "spiritual_cultural_and_folklore": "Historic trail head for the 19th century Magdalena Livestock Driveway, known as the 'Hoof Highway'.",
            "hiking_trails_and_outdoor_recreation": "Continental Divide National Scenic Trail hiking, Datil Mountain trail system, wildlife watching.",
            "nearest_hospital_and_emergency": "Socorro General Hospital, 1202 Hwy 60 W, Socorro, NM (Approx 60 miles)",
            "trash_and_waste_policy": "Pack-In/Pack-Out mandatory. Keep camp pristine.",
            "last_updated": "2026-09-12"
        },
        {
            "campsite_name": "Cosmic Campground Dispersed Area (Gila National Forest)",
            "state": "New Mexico",
            "managing_agency": "US Forest Service - Gila National Forest (Glenwood Ranger District)",
            "gps_coordinates": "33.4797, -108.9228",
            "is_100_percent_free": True,
            "total_cost_or_fees": "$0 - 100% Free Public Land",
            "maximum_stay_length": "14 days",
            "rules_and_regulations": "International Dark Sky Sanctuary area. No unshielded white lights allowed after dark (red lights only for night vision preservation). Pack out all trash.",
            "poop_disposal_rules": "Bury waste 6-8 inches deep 200 feet from drainage channels and campsites.",
            "campfire_rules": "Campfires in designated rings or established fire spots only. No fires during high wind conditions or stage restrictions.",
            "ranger_agency_contact": "Glenwood Ranger District: (575) 539-2481",
            "access_and_road_conditions": {
                "recommended_vehicle": "Standard 2WD car accessible via paved US-180 and short smooth gravel entrance",
                "road_type_and_condition": "Paved highway leads directly to gravel entry loop.",
                "scores": {
                    "front_wheel_drive_clearance": 9,
                    "high_clearance_necessary": 1,
                    "four_wheel_drive_necessary": 1,
                    "seasonal_impassability_risk": 2
                }
            },
            "nearest_supply_towns": [
                {
                    "town_name": "Glenwood, NM",
                    "distance_miles": 12,
                    "amenities_available": "Gas station, small store, cafe, post office"
                },
                {
                    "town_name": "Reserve, NM",
                    "distance_miles": 26,
                    "amenities_available": "Groceries, gas, hardware, diner"
                }
            ],
            "seasonal_weather_and_best_times": "Spring, summer, and autumn (elevation 5,400 ft). Pleasant summer days (~85°F) with cool clear nights.",
            "dangers_and_hazards": "Monsoon lightning storms in July/August, extreme nighttime dark requires flashlight caution near rock edges.",
            "nomad_connectivity_rating": {
                "t_mobile_signal": "0-1 bar (Very Weak/No Data)",
                "verizon_signal": "1-2 bars 4G LTE (Intermittent)",
                "att_signal": "1 bar 4G LTE",
                "terrain_obstruction_risk": "Moderate due to surrounding Gila mountains",
                "distance_to_nearest_tower_miles": 13.5,
                "is_cellular_internet_dependable": False,
                "recommendation_for_remote_workers": "Cellular signal is unreliable for heavy remote work. Starlink satellite internet is highly effective due to unobstructed sky view."
            },
            "amenities_and_features": [
                "International Dark Sky Sanctuary",
                "Telescope Observation Pads",
                "Smooth Road Access",
                "Panoramic Mountain Views"
            ],
            "location_scores": {
                "scenery": 10,
                "privacy": 8,
                "accessibility": 9,
                "shade_coverage": 3,
                "water_proximity": 1,
                "safety": 9
            },
            "flora_fauna_and_ecosystem": "High desert grassland surrounded by oak woodland and piñon-juniper. Coatimundi, black bears, javelina, mountain lions, owls.",
            "spiritual_cultural_and_folklore": "The Mogollon culture inhabited this region 1,000 years ago; exceptional visibility makes it an ancient astronomical observation ground.",
            "hiking_trails_and_outdoor_recreation": "Gila Wilderness hiking trails nearby, Catwalk Recreation Area trail (15 miles south), night astronomy.",
            "nearest_hospital_and_emergency": "Gila Regional Medical Center, 1313 E 32nd St, Silver City, NM (Approx 70 miles)",
            "trash_and_waste_policy": "Strict Pack-In/Pack-Out policy. Leave no trace of food or waste.",
            "last_updated": "2026-09-12"
        },
        {
            "campsite_name": "Wild Rivers Dispersed Area (Rio Grande del Norte)",
            "state": "New Mexico",
            "managing_agency": "Bureau of Land Management (Taos Field Office)",
            "gps_coordinates": "36.7389, -105.6881",
            "is_100_percent_free": True,
            "total_cost_or_fees": "$0 - 100% Free Public Land (Dispersed spots outside fee loops)",
            "maximum_stay_length": "14 days",
            "rules_and_regulations": "Dispersed primitive camping permitted on designated BLM lands along the Wild Rivers Backcountry Byway outside developed fee loops.",
            "poop_disposal_rules": "Pack out human waste or dig cathole 6-8 inches deep 200 feet away from gorge rim and drainage gullies.",
            "campfire_rules": "Use existing fire rings where present. Observe BLM Taos fire bans during dry spring months. Extinguish completely.",
            "ranger_agency_contact": "BLM Taos Field Office: (575) 758-8851",
            "access_and_road_conditions": {
                "recommended_vehicle": "Low-clearance 2WD accessible via paved NM-515 Backcountry Byway",
                "road_type_and_condition": "Paved primary roads with smooth dirt pullouts for primitive campsites.",
                "scores": {
                    "front_wheel_drive_clearance": 9,
                    "high_clearance_necessary": 2,
                    "four_wheel_drive_necessary": 1,
                    "seasonal_impassability_risk": 3
                }
            },
            "nearest_supply_towns": [
                {
                    "town_name": "Questa, NM",
                    "distance_miles": 10,
                    "amenities_available": "Grocery store, gas station, hardware, restaurants"
                },
                {
                    "town_name": "Taos, NM",
                    "distance_miles": 34,
                    "amenities_available": "Full urban services, outdoor gear, hospital, auto repair"
                }
            ],
            "seasonal_weather_and_best_times": "Late spring through autumn (elevation 7,600 ft). High summer temperatures (~82°F) tempered by canyon breezes. Snow in winter.",
            "dangers_and_hazards": "800-foot sheer vertical cliffs into Rio Grande Gorge. Keep children and pets leashed. High altitude sun.",
            "nomad_connectivity_rating": {
                "t_mobile_signal": "3 bars 5G/4G LTE",
                "verizon_signal": "3-4 bars 5G/4G LTE",
                "att_signal": "3 bars 4G LTE",
                "terrain_obstruction_risk": "Low on high plateau rim",
                "distance_to_nearest_tower_miles": 7.5,
                "is_cellular_internet_dependable": True,
                "recommendation_for_remote_workers": "Excellent cell coverage along plateau rim for remote work with stunning gorge backdrops."
            },
            "amenities_and_features": [
                "Rio Grande Gorge Views",
                "Paved Byway Access",
                "Hiking Trails into Canyon",
                "Mountain Views",
                "Pet Friendly"
            ],
            "location_scores": {
                "scenery": 10,
                "privacy": 7,
                "accessibility": 9,
                "shade_coverage": 5,
                "water_proximity": 3,
                "safety": 9
            },
            "flora_fauna_and_ecosystem": "Sagebrush plateau with piñon pine and juniper. Bighorn sheep along canyon walls, golden eagles, prairie dogs, mule deer.",
            "spiritual_cultural_and_folklore": "Confluence of Rio Grande and Red River, sacred water site for Taos Pueblo and Ancestral Puebloan peoples for millennia.",
            "hiking_trails_and_outdoor_recreation": "La Junta Trail (descends into gorge confluence), Rinconada Loop Trail, Rio Grande Gorge Overlook trail.",
            "nearest_hospital_and_emergency": "Holy Cross Hospital, 1397 Weimer Rd, Taos, NM (Approx 35 miles)",
            "trash_and_waste_policy": "Pack-In/Pack-Out mandatory. Pack out all trash.",
            "last_updated": "2026-09-12"
        }
    ],
    "Oregon": [
        {
            "campsite_name": "Alvord Desert Dispersed Area (BLM Burns)",
            "state": "Oregon",
            "managing_agency": "Bureau of Land Management (Burns District)",
            "gps_coordinates": "42.5321, -118.4608",
            "is_100_percent_free": True,
            "total_cost_or_fees": "$0 - 100% Free Public Land",
            "maximum_stay_length": "14 days within a 28-day period",
            "rules_and_regulations": "Free dispersed camping on public BLM playa and desert edges. Do not drive on wet playa (creates severe ruts). Pack out all human waste and trash.",
            "poop_disposal_rules": "Pack out all human waste using portable toilet or wag-bag system due to hard-baked playa surface lacking soil depth.",
            "campfire_rules": "Campfires must be contained in portable fire pits or pans to protect playa surface. Do not leave ash on playa. Extinguish fully.",
            "ranger_agency_contact": "BLM Burns District Office: (541) 573-4400",
            "access_and_road_conditions": {
                "recommended_vehicle": "Low-clearance 2WD accessible to dry playa edge; 4WD recommended during mud season",
                "road_type_and_condition": "Gravel Fields-Denio Road. Extremely flat, dry playa surface when dry, impassable mud when wet.",
                "scores": {
                    "front_wheel_drive_clearance": 7,
                    "high_clearance_necessary": 4,
                    "four_wheel_drive_necessary": 3,
                    "seasonal_impassability_risk": 9
                }
            },
            "nearest_supply_towns": [
                {
                    "town_name": "Fields, OR",
                    "distance_miles": 22,
                    "amenities_available": "Gas station, famous diner/milkshakes, small store"
                },
                {
                    "town_name": "Burns, OR",
                    "distance_miles": 105,
                    "amenities_available": "Full grocery, hardware, hospital, mechanical services"
                }
            ],
            "seasonal_weather_and_best_times": "Summer and autumn (June-October). Summers are warm (85°F-95°F) with cool nights. Spring brings rain turning playa into deep mud.",
            "dangers_and_hazards": "Dust storms with zero visibility, extreme mud trapping vehicles on wet playa, sudden high desert temperature drops, remote location.",
            "nomad_connectivity_rating": {
                "t_mobile_signal": "0-1 bar (No Data)",
                "verizon_signal": "1-2 bars 4G LTE (Near Fields-Denio road)",
                "att_signal": "1 bar 4G LTE",
                "terrain_obstruction_risk": "Low (Flat open playa, but mountain shadow from Steens Peak)",
                "distance_to_nearest_tower_miles": 22.0,
                "is_cellular_internet_dependable": False,
                "recommendation_for_remote_workers": "Cellular coverage is poor. High performance Starlink is required for remote work on the playa."
            },
            "amenities_and_features": [
                "Flat Alkali Dry Lake Bed",
                "Steens Mountain View Wall",
                "Stargazing Heaven",
                "Land-Sailing / Kite Boarding Area"
            ],
            "location_scores": {
                "scenery": 10,
                "privacy": 9,
                "accessibility": 6,
                "shade_coverage": 1,
                "water_proximity": 1,
                "safety": 7
            },
            "flora_fauna_and_ecosystem": "High desert salt-playa surrounded by big sagebrush and greasewood. Wild horses (mustangs), pronghorn antelope, coyotes, golden eagles.",
            "spiritual_cultural_and_folklore": "Ancestral lands of the Northern Paiute people. Renowned world-record land speed trial site.",
            "hiking_trails_and_outdoor_recreation": "Pike Creek Canyon trail (east side of Steens), desert walking, hot springs bathing (nearby commercial or public pools), land sailing.",
            "nearest_hospital_and_emergency": "Harney District Hospital, 557 W Washington St, Burns, OR (Approx 105 miles)",
            "trash_and_waste_policy": "Strict Pack-In/Pack-Out. Absolute zero trash left behind policy.",
            "last_updated": "2026-09-12"
        },
        {
            "campsite_name": "Leslie Gulch Dispersed Camping (BLM Vale District)",
            "state": "Oregon",
            "managing_agency": "Bureau of Land Management (Vale District / Malheur Field Office)",
            "gps_coordinates": "43.3189, -117.3214",
            "is_100_percent_free": True,
            "total_cost_or_fees": "$0 - 100% Free Public Land",
            "maximum_stay_length": "14 days",
            "rules_and_regulations": "Free primitive dispersed camping allowed in designated pullouts along Leslie Gulch Road outside delicate ACEC botanical zones.",
            "poop_disposal_rules": "Pack out human waste or bury in cathole 6-8 inches deep at least 200 feet from Owyhee Reservoir high water mark.",
            "campfire_rules": "Observe BLM fire restrictions. Bring your own firewood (no wood gathering in canyon). Ensure fires are fully cold.",
            "ranger_agency_contact": "BLM Vale District Office: (541) 473-3144",
            "access_and_road_conditions": {
                "recommended_vehicle": "Standard 2WD suitable during dry weather; high-clearance advised for dirt side tracks",
                "road_type_and_condition": "52 miles south of Jordan Valley, 15 miles of gravel/dirt canyon road. High washboard and rock hazards.",
                "scores": {
                    "front_wheel_drive_clearance": 7,
                    "high_clearance_necessary": 5,
                    "four_wheel_drive_necessary": 3,
                    "seasonal_impassability_risk": 7
                }
            },
            "nearest_supply_towns": [
                {
                    "town_name": "Jordan Valley, OR",
                    "distance_miles": 35,
                    "amenities_available": "Gas station, small grocery, diner, motel"
                },
                {
                    "town_name": "Nysa / Ontario, OR",
                    "distance_miles": 65,
                    "amenities_available": "Full urban amenities, Walmart, medical, hardware"
                }
            ],
            "seasonal_weather_and_best_times": "Spring and autumn (April-June, September-October). High summer heat often exceeds 100°F inside volcanic canyon.",
            "dangers_and_hazards": "Flash flooding in narrow canyons during thunderstorms, extreme heat, rattlesnakes, slick bentonite clay roads when wet.",
            "nomad_connectivity_rating": {
                "t_mobile_signal": "0 bars (No Service)",
                "verizon_signal": "0-1 bar (Extremely weak/No Data)",
                "att_signal": "0 bars (No Service)",
                "terrain_obstruction_risk": "Extreme inside steep volcanic tuff canyon walls",
                "distance_to_nearest_tower_miles": 28.0,
                "is_cellular_internet_dependable": False,
                "recommendation_for_remote_workers": "Cellular internet does not function inside canyon. Work requires satellite setup or driving to higher rim plateau."
            },
            "amenities_and_features": [
                "Towering Volcanic Ash Formations",
                "Owyhee Reservoir Access",
                "Boat Ramp Nearby",
                "Wild Bighorn Sheep Habitat"
            ],
            "location_scores": {
                "scenery": 10,
                "privacy": 8,
                "accessibility": 6,
                "shade_coverage": 3,
                "water_proximity": 4,
                "safety": 7
            },
            "flora_fauna_and_ecosystem": "Volcanic ash tuff ecosystem. Rare endemic plants (Packard's milkvetch, Ertter's senecio). California bighorn sheep, golden eagles, chukar.",
            "spiritual_cultural_and_folklore": "Dramatic natural cathedral-like rock formations carved into Owyhee volcanic field over 15 million years.",
            "hiking_trails_and_outdoor_recreation": "Juniper Gulch trail, Dago Gulch trail, Timber Gulch hiking, kayaking Owyhee Reservoir.",
            "nearest_hospital_and_emergency": "Holy Rosary Medical Center, 351 SW 9th St, Ontario, OR (Approx 65 miles)",
            "trash_and_waste_policy": "Strict Pack-In/Pack-Out. Do not discard food scraps that attract wildlife.",
            "last_updated": "2026-09-12"
        },
        {
            "campsite_name": "Skull Hollow Dispersed Camping (Ochoco National Grassland)",
            "state": "Oregon",
            "managing_agency": "US Forest Service - Ochoco National Forest & Crooked River National Grassland",
            "gps_coordinates": "44.4753, -120.8261",
            "is_100_percent_free": True,
            "total_cost_or_fees": "$0 - 100% Free Public Land (Dispersed pullouts surrounding campground)",
            "maximum_stay_length": "14 days",
            "rules_and_regulations": "Dispersed camping permitted on adjacent National Grassland dirt spur tracks outside developed trailhead area. Keep vehicles within 30 ft of roads.",
            "poop_disposal_rules": "Dig 6-8 inch catholes at least 200 feet from dry creek beds. Pack out all paper products.",
            "campfire_rules": "Check USFS stage fire restrictions (very strict in summer/fall). Campfires must be drowning-cold before departure.",
            "ranger_agency_contact": "Crooked River National Grassland Office (Prineville): (541) 416-6500",
            "access_and_road_conditions": {
                "recommended_vehicle": "Low-clearance 2WD accessible via paved Lone Pine Rd and hard-packed gravel access spur",
                "road_type_and_condition": "Paved secondary road leading to well-graded gravel forest spur roads.",
                "scores": {
                    "front_wheel_drive_clearance": 9,
                    "high_clearance_necessary": 2,
                    "four_wheel_drive_necessary": 1,
                    "seasonal_impassability_risk": 3
                }
            },
            "nearest_supply_towns": [
                {
                    "town_name": "Redmond, OR",
                    "distance_miles": 14,
                    "amenities_available": "Full city amenities, Home Depot, Fred Meyer, restaurants, urgent care"
                },
                {
                    "town_name": "Prineville, OR",
                    "distance_miles": 18,
                    "amenities_available": "Groceries, hardware, gas, outdoor supplies"
                }
            ],
            "seasonal_weather_and_best_times": "Spring, summer, and autumn (elevation 3,100 ft). High summer temperatures (~85°F), cool fall nights.",
            "dangers_and_hazards": "Rattlesnakes, ticks in spring brush, high summer wildfire danger.",
            "nomad_connectivity_rating": {
                "t_mobile_signal": "3-4 bars 5G/4G LTE",
                "verizon_signal": "4 bars 5G/4G LTE",
                "att_signal": "3-4 bars 5G/4G LTE",
                "terrain_obstruction_risk": "Low",
                "distance_to_nearest_tower_miles": 6.8,
                "is_cellular_internet_dependable": True,
                "recommendation_for_remote_workers": "Highly dependable cell signal for remote workers wanting proximity to Smith Rock State Park."
            },
            "amenities_and_features": [
                "Proximity to Smith Rock State Park",
                "Juniper & Sagebrush Views",
                "Trailhead Access",
                "Pet Friendly"
            ],
            "location_scores": {
                "scenery": 8,
                "privacy": 7,
                "accessibility": 9,
                "shade_coverage": 4,
                "water_proximity": 1,
                "safety": 9
            },
            "flora_fauna_and_ecosystem": "High desert juniper savanna. Western juniper, sagebrush, bitterbrush. Mule deer, coyotes, golden eagles, red-tailed hawks.",
            "spiritual_cultural_and_folklore": "Historic sheep grazing corridor of Central Oregon dating back to the late 19th century.",
            "hiking_trails_and_outdoor_recreation": "Gray Butte Trail, Cole Loop Trail, mountain biking, climbing at nearby Smith Rock (3 miles away).",
            "nearest_hospital_and_emergency": "St. Charles Medical Center - Redmond, 1253 NW Canal Blvd, Redmond, OR (Approx 15 miles)",
            "trash_and_waste_policy": "Pack-In/Pack-Out mandatory. Keep grassland clean.",
            "last_updated": "2026-09-12"
        },
        {
            "campsite_name": "Steens Mountain Loop Dispersed (BLM Burns)",
            "state": "Oregon",
            "managing_agency": "Bureau of Land Management (Burns District / Andrews Resource Area)",
            "gps_coordinates": "42.6375, -118.5789",
            "is_100_percent_free": True,
            "total_cost_or_fees": "$0 - 100% Free Public Land",
            "maximum_stay_length": "14 days",
            "rules_and_regulations": "Dispersed camping allowed along Steens Mountain Loop Road outside designated fee campgrounds. Camp only in previously impacted sites.",
            "poop_disposal_rules": "Bury waste 6-8 inches deep 200 feet from streams and lakes, or pack out waste in alpine sub-zones.",
            "campfire_rules": "Extinguish campfires cold with water. Avoid campfires during high wind conditions on mountain ridges.",
            "ranger_agency_contact": "BLM Burns District: (541) 573-4400",
            "access_and_road_conditions": {
                "recommended_vehicle": "High-clearance 2WD/4WD required due to steep gravel grades and rocky washboard sections",
                "road_type_and_condition": "Steens Loop is a gravel mountain road reaching nearly 10,000 ft elevation. Closed by snow late autumn to July.",
                "scores": {
                    "front_wheel_drive_clearance": 4,
                    "high_clearance_necessary": 8,
                    "four_wheel_drive_necessary": 5,
                    "seasonal_impassability_risk": 9
                }
            },
            "nearest_supply_towns": [
                {
                    "town_name": "Frenchglen, OR",
                    "distance_miles": 18,
                    "amenities_available": "Historic hotel, small store, gas pump, post office"
                },
                {
                    "town_name": "Burns, OR",
                    "distance_miles": 78,
                    "amenities_available": "Full grocery, hardware, hospital, mechanical repair"
                }
            ],
            "seasonal_weather_and_best_times": "Late summer (July-September). High elevation (~7,500-9,000 ft) provides cool summer temperatures (65°F-75°F). Early snowfall risk.",
            "dangers_and_hazards": "Sudden alpine blizzards, thunderstorm lightning strikes, 2,000-foot glacial gorge drops, vehicle brake overheating.",
            "nomad_connectivity_rating": {
                "t_mobile_signal": "1-2 bars 4G LTE on high ridges / 0 bars in gorges",
                "verizon_signal": "2-3 bars 4G LTE on high ridges",
                "att_signal": "1-2 bars 4G LTE on high ridges",
                "terrain_obstruction_risk": "High inside Kiger/Little Blitzen Gorges / Low on open subalpine crests",
                "distance_to_nearest_tower_miles": 18.0,
                "is_cellular_internet_dependable": False,
                "recommendation_for_remote_workers": "Cell signal is spotty. Ridge top sites offer usable Verizon data, but mountain storms cause signal fluctuation."
            },
            "amenities_and_features": [
                "Glacial U-Shaped Gorges View",
                "Subalpine Lakes",
                "Wild Mustang Herds",
                "Panoramic 100-Mile Views"
            ],
            "location_scores": {
                "scenery": 10,
                "privacy": 9,
                "accessibility": 5,
                "shade_coverage": 2,
                "water_proximity": 4,
                "safety": 7
            },
            "flora_fauna_and_ecosystem": "Subalpine sagebrush steppe and quaking aspen groves. Wild horses, bighorn sheep, mule deer, elk, redband trout.",
            "spiritual_cultural_and_folklore": "30-mile long fault-block mountain structure rising dramatically over 5,000 feet above the Alvord Desert floor.",
            "hiking_trails_and_outdoor_recreation": "Kiger Gorge Overlook trail, Little Blitzen Gorge trail, Steens Summit walk, Wildhorse Lake trail.",
            "nearest_hospital_and_emergency": "Harney District Hospital, 557 W Washington St, Burns, OR (Approx 78 miles)",
            "trash_and_waste_policy": "Strict Pack-In/Pack-Out policy. High subalpine terrain preserves waste indefinitely if left behind.",
            "last_updated": "2026-09-12"
        },
        {
            "campsite_name": "Lake Owyhee Overlook Dispersed (BLM Vale District)",
            "state": "Oregon",
            "managing_agency": "Bureau of Land Management (Vale District)",
            "gps_coordinates": "43.6412, -117.2348",
            "is_100_percent_free": True,
            "total_cost_or_fees": "$0 - 100% Free Public Land",
            "maximum_stay_length": "14 days",
            "rules_and_regulations": "Free primitive dispersed camping on BLM ridge overlooks above Lake Owyhee. Pack out all garbage.",
            "poop_disposal_rules": "Bury waste 6-8 inches deep 200 feet from drainage channels and lake high water line.",
            "campfire_rules": "Campfires permitted in cleared dirt areas. Douse cold with water before leaving camp unattended.",
            "ranger_agency_contact": "BLM Vale District: (541) 473-3144",
            "access_and_road_conditions": {
                "recommended_vehicle": "High-clearance vehicle recommended due to rocky gravel ridge tracks",
                "road_type_and_condition": "Gravel and dirt plateau roads. Steep grades and loose rock near overlook points.",
                "scores": {
                    "front_wheel_drive_clearance": 6,
                    "high_clearance_necessary": 7,
                    "four_wheel_drive_necessary": 4,
                    "seasonal_impassability_risk": 6
                }
            },
            "nearest_supply_towns": [
                {
                    "town_name": "Adrian, OR",
                    "distance_miles": 24,
                    "amenities_available": "Gas station, small store, diner"
                },
                {
                    "town_name": "Nyssa, OR",
                    "distance_miles": 36,
                    "amenities_available": "Groceries, hardware, gas, restaurants"
                }
            ],
            "seasonal_weather_and_best_times": "Spring and autumn (April-May, September-October). High summer heat (95°F-100°F) with strong canyon winds.",
            "dangers_and_hazards": "Sheer cliff drop-offs into reservoir canyon, high winds, summer rattlesnakes, lack of shade.",
            "nomad_connectivity_rating": {
                "t_mobile_signal": "2-3 bars 4G LTE on ridge top",
                "verizon_signal": "3 bars 4G LTE on ridge top",
                "att_signal": "2-3 bars 4G LTE on ridge top",
                "terrain_obstruction_risk": "Moderate",
                "distance_to_nearest_tower_miles": 16.0,
                "is_cellular_internet_dependable": True,
                "recommendation_for_remote_workers": "Ridge top sites provide surprising line-of-sight cell coverage across the Snake River plain."
            },
            "amenities_and_features": [
                "Canyon Reservoir Panoramic Views",
                "Volcanic Cliff Formations",
                "Boating Access Nearby",
                "Quiet Primitive Solitude"
            ],
            "location_scores": {
                "scenery": 9,
                "privacy": 9,
                "accessibility": 6,
                "shade_coverage": 2,
                "water_proximity": 3,
                "safety": 8
            },
            "flora_fauna_and_ecosystem": "Sagebrush desert steppe. Big sagebrush, rabbitbrush. Chukar, bighorn sheep, coyotes, golden eagles, bass and crappie in reservoir.",
            "spiritual_cultural_and_folklore": "Owyhee River named after 19th-century Hawaiian fur trappers hired by the North West Company who vanished in the canyon in 1819.",
            "hiking_trails_and_outdoor_recreation": "Owyhee Dam trail, canyon rim hiking, bass fishing, kayaking reservoir arms.",
            "nearest_hospital_and_emergency": "Holy Rosary Medical Center, 351 SW 9th St, Ontario, OR (Approx 45 miles)",
            "trash_and_waste_policy": "Pack-In/Pack-Out mandatory.",
            "last_updated": "2026-09-12"
        }
    ],
    "Utah": [
        {
            "campsite_name": "Valley of the Gods Dispersed Camping (BLM Monticello)",
            "state": "Utah",
            "managing_agency": "Bureau of Land Management (Monticello Field Office / Bears Ears NM)",
            "gps_coordinates": "37.2418, -109.8164",
            "is_100_percent_free": True,
            "total_cost_or_fees": "$0 - 100% Free Public Land",
            "maximum_stay_length": "14 days",
            "rules_and_regulations": "Free primitive dispersed camping along 17-mile dirt loop road. Camp ONLY in designated pullout sites with fire rings to protect fragile desert soils.",
            "poop_disposal_rules": "Pack out all human waste using wag-bag or portable toilet system (mandatory in high-use Bears Ears BLM zones).",
            "campfire_rules": "Fires permitted in established metal or stone rings. Must bring own firewood. Extinguish 100% cold with water.",
            "ranger_agency_contact": "BLM Monticello Field Office: (435) 587-1500",
            "access_and_road_conditions": {
                "recommended_vehicle": "High-clearance 2WD suitable during dry weather; 4WD necessary after rain events",
                "road_type_and_condition": "17-mile unpaved dirt and gravel loop. Features sandy dry-wash crossings that rut deeply after rain.",
                "scores": {
                    "front_wheel_drive_clearance": 6,
                    "high_clearance_necessary": 7,
                    "four_wheel_drive_necessary": 5,
                    "seasonal_impassability_risk": 8
                }
            },
            "nearest_supply_towns": [
                {
                    "town_name": "Mexican Hat, UT",
                    "distance_miles": 10,
                    "amenities_available": "Gas stations, small market, diner, lodge"
                },
                {
                    "town_name": "Bluff, UT",
                    "distance_miles": 22,
                    "amenities_available": "Groceries, cafes, gas, outdoor outfitters"
                }
            ],
            "seasonal_weather_and_best_times": "Spring and autumn (March-May, September-November). High summer heat (95°F-105°F). Cold winter freezes.",
            "dangers_and_hazards": "Flash flooding in dry washes during summer monsoons, extreme summer heat, lack of shade, deep sand.",
            "nomad_connectivity_rating": {
                "t_mobile_signal": "1-2 bars 4G LTE",
                "verizon_signal": "2-3 bars 4G LTE",
                "att_signal": "2 bars 4G LTE",
                "terrain_obstruction_risk": "Moderate near massive sandstone monoliths",
                "distance_to_nearest_tower_miles": 11.0,
                "is_cellular_internet_dependable": True,
                "recommendation_for_remote_workers": "Dependable Verizon/AT&T cellular data on open elevated pullouts along the loop road."
            },
            "amenities_and_features": [
                "Iconic Sandstone Butte Scenery",
                "17-Mile Scenic Dirt Loop",
                "Dark Sky Stargazing",
                "Photographer Paradise"
            ],
            "location_scores": {
                "scenery": 10,
                "privacy": 9,
                "accessibility": 7,
                "shade_coverage": 1,
                "water_proximity": 1,
                "safety": 9
            },
            "flora_fauna_and_ecosystem": "Colorado Plateau red rock desert. Blackbrush, Mormon tea, prickly pear, yucca. Desert bighorn sheep, kit foxes, ravens, lizards.",
            "spiritual_cultural_and_folklore": "Sacred landscape to Diné (Navajo) nation; red sandstone monuments represent ancient warriors frozen in stone.",
            "hiking_trails_and_outdoor_recreation": "Dirt road hiking around towering monoliths (Battleship Butte, Rooster Butte), photography, stargazing.",
            "nearest_hospital_and_emergency": "San Juan Hospital, 380 W 100 N, Monticello, UT (Approx 50 miles)",
            "trash_and_waste_policy": "Strict Pack-In/Pack-Out policy. Pack out all trash and waste.",
            "last_updated": "2026-09-12"
        },
        {
            "campsite_name": "San Rafael Swell - Wedge Overlook Dispersed (BLM Price)",
            "state": "Utah",
            "managing_agency": "Bureau of Land Management (Price Field Office)",
            "gps_coordinates": "39.0933, -110.7589",
            "is_100_percent_free": True,
            "total_cost_or_fees": "$0 - 100% Free Public Land",
            "maximum_stay_length": "14 days",
            "rules_and_regulations": "Dispersed camping allowed along canyon rim pullouts. Camp in existing disturbed sites. Leave No Trace.",
            "poop_disposal_rules": "Pack out all human waste using portable waste bags or toilet system, mandatory along canyon rim zone.",
            "campfire_rules": "Fire in existing steel rings or rock rings. Do not cut live wood. Douse with water until cold.",
            "ranger_agency_contact": "BLM Price Field Office: (435) 636-3600",
            "access_and_road_conditions": {
                "recommended_vehicle": "Low-clearance 2WD accessible during dry weather via well-graded gravel Buckhorn Draw Road",
                "road_type_and_condition": "Smooth gravel road for 20 miles from Castle Dale. Clay sections slick when wet.",
                "scores": {
                    "front_wheel_drive_clearance": 8,
                    "high_clearance_necessary": 3,
                    "four_wheel_drive_necessary": 2,
                    "seasonal_impassability_risk": 5
                }
            },
            "nearest_supply_towns": [
                {
                    "town_name": "Castle Dale, UT",
                    "distance_miles": 21,
                    "amenities_available": "Grocery store, gas stations, hardware, diner"
                },
                {
                    "town_name": "Price, UT",
                    "distance_miles": 48,
                    "amenities_available": "Full city services, hospital, Walmart, auto repair"
                }
            ],
            "seasonal_weather_and_best_times": "Spring and autumn (April-June, September-October). Cool canyon breezes. Winters freezing cold.",
            "dangers_and_hazards": "1,200-foot sheer vertical canyon drop into the 'Little Grand Canyon'. Keep leashed. Wind gusts.",
            "nomad_connectivity_rating": {
                "t_mobile_signal": "2 bars 4G LTE",
                "verizon_signal": "3 bars 4G LTE",
                "att_signal": "2-3 bars 4G LTE",
                "terrain_obstruction_risk": "Low on plateau rim",
                "distance_to_nearest_tower_miles": 15.0,
                "is_cellular_internet_dependable": True,
                "recommendation_for_remote_workers": "Excellent rim top signal for remote working with incredible canyon backdrop."
            },
            "amenities_and_features": [
                "'Little Grand Canyon' Overlook",
                "San Rafael River Access Nearby",
                "Pet Friendly Rim Pullouts",
                "Rock Art Sites Nearby"
            ],
            "location_scores": {
                "scenery": 10,
                "privacy": 8,
                "accessibility": 8,
                "shade_coverage": 3,
                "water_proximity": 2,
                "safety": 8
            },
            "flora_fauna_and_ecosystem": "Piñon-juniper woodland on sandstone plateau. Desert bighorn sheep, mountain lions, coyotes, golden eagles.",
            "spiritual_cultural_and_folklore": "Buckhorn Draw rock art panel nearby features ancient Fremont culture pictographs dating back over 2,000 years.",
            "hiking_trails_and_outdoor_recreation": "Wedge Rim Trail, Buckhorn Draw hiking, mountain biking, rock art viewing, canyon photography.",
            "nearest_hospital_and_emergency": "Castleview Hospital, 300 N Hospital Dr, Price, UT (Approx 48 miles)",
            "trash_and_waste_policy": "Strict Pack-In/Pack-Out policy.",
            "last_updated": "2026-09-12"
        },
        {
            "campsite_name": "Little Sahara Dispersed / Sage Hen (BLM Fillmore)",
            "state": "Utah",
            "managing_agency": "Bureau of Land Management (Fillmore Field Office)",
            "gps_coordinates": "39.7125, -112.3856",
            "is_100_percent_free": True,
            "total_cost_or_fees": "$0 - 100% Free Public Land (Free dispersed areas on public land outside main OHV fee gate)",
            "maximum_stay_length": "14 days",
            "rules_and_regulations": "Free primitive dispersed camping on open BLM lands surrounding the sand dune complex outside fee boundaries.",
            "poop_disposal_rules": "Cathole 6-8 inches deep 200 feet from camp/roads or pack out in human waste bag.",
            "campfire_rules": "Contain fires in existing rock rings or fire pans. Douse cold with water.",
            "ranger_agency_contact": "BLM Fillmore Field Office: (435) 743-3100",
            "access_and_road_conditions": {
                "recommended_vehicle": "Low-clearance 2WD accessible on main gravel roads; 4WD required if pulling into soft dune edges",
                "road_type_and_condition": "Paved access road leading to hard-packed dirt/gravel side tracks.",
                "scores": {
                    "front_wheel_drive_clearance": 8,
                    "high_clearance_necessary": 4,
                    "four_wheel_drive_necessary": 3,
                    "seasonal_impassability_risk": 3
                }
            },
            "nearest_supply_towns": [
                {
                    "town_name": "Lynndyl, UT",
                    "distance_miles": 14,
                    "amenities_available": "Gas pump, small convenience store"
                },
                {
                    "town_name": "Eureka, UT",
                    "distance_miles": 22,
                    "amenities_available": "Gas station, diner, convenience store"
                },
                {
                    "town_name": "Nephi, UT",
                    "distance_miles": 32,
                    "amenities_available": "Full groceries, hardware, medical clinic, restaurants"
                }
            ],
            "seasonal_weather_and_best_times": "Spring and fall (April-May, September-October). High summer heat on exposed sand.",
            "dangers_and_hazards": "Getting stuck in deep loose sand if driving off hard tracks. High wind dust storms.",
            "nomad_connectivity_rating": {
                "t_mobile_signal": "3 bars 4G LTE",
                "verizon_signal": "4 bars 5G/4G LTE",
                "att_signal": "3 bars 4G LTE",
                "terrain_obstruction_risk": "Low",
                "distance_to_nearest_tower_miles": 8.0,
                "is_cellular_internet_dependable": True,
                "recommendation_for_remote_workers": "Very reliable Verizon cell signal across open flats for remote working."
            },
            "amenities_and_features": [
                "Sand Dune Views",
                "Flat Open Parking",
                "OHV Trail Access Nearby",
                "Stargazing"
            ],
            "location_scores": {
                "scenery": 8,
                "privacy": 7,
                "accessibility": 9,
                "shade_coverage": 2,
                "water_proximity": 1,
                "safety": 9
            },
            "flora_fauna_and_ecosystem": "Great Basin desert sagebrush and active sand dunes. Indian ricegrass, juniper. Kangaroo rats, kit foxes, pronghorn, lizards.",
            "spiritual_cultural_and_folklore": "Remnant dunes deposited by wind from prehistoric Lake Bonneville 15,000 years ago.",
            "hiking_trails_and_outdoor_recreation": "Sand dune hiking, OHV riding, photography, stargazing.",
            "nearest_hospital_and_emergency": "Central Valley Medical Center, 48 W 1500 N, Nephi, UT (Approx 32 miles)",
            "trash_and_waste_policy": "Pack-In/Pack-Out mandatory.",
            "last_updated": "2026-09-12"
        },
        {
            "campsite_name": "Notch Peak / Tule Valley Dispersed (BLM Fillmore)",
            "state": "Utah",
            "managing_agency": "Bureau of Land Management (Fillmore Field Office)",
            "gps_coordinates": "39.1412, -113.3489",
            "is_100_percent_free": True,
            "total_cost_or_fees": "$0 - 100% Free Public Land",
            "maximum_stay_length": "14 days",
            "rules_and_regulations": "Free primitive dispersed camping on open BLM desert lands at base of Notch Peak. Pack out all trash and waste.",
            "poop_disposal_rules": "Dig cathole 6-8 inches deep 200 feet from dry washes and camp area.",
            "campfire_rules": "Fire in existing rings only. Extinguish cold before leaving camp.",
            "ranger_agency_contact": "BLM Fillmore Field Office: (435) 743-3100",
            "access_and_road_conditions": {
                "recommended_vehicle": "High-clearance 2WD/4WD recommended for rocky dirt wash access road",
                "road_type_and_condition": "Off US-50/6 down 10 miles of dirt and gravel wash roads. Rocky and ruts.",
                "scores": {
                    "front_wheel_drive_clearance": 5,
                    "high_clearance_necessary": 7,
                    "four_wheel_drive_necessary": 4,
                    "seasonal_impassability_risk": 6
                }
            },
            "nearest_supply_towns": [
                {
                    "town_name": "Delta, UT",
                    "distance_miles": 50,
                    "amenities_available": "Full grocery store, hospital, gas stations, hardware"
                }
            ],
            "seasonal_weather_and_best_times": "Spring and autumn (April-May, September-October). Elevation 5,500 ft. Hot summers (95°F+).",
            "dangers_and_hazards": "Extreme solitude, lack of cell signal in washes, flash floods in Sawtooth Canyon, high desert sun.",
            "nomad_connectivity_rating": {
                "t_mobile_signal": "0-1 bar (Weak/No Data)",
                "verizon_signal": "1-2 bars 4G LTE (Elevated ground only)",
                "att_signal": "1 bar 4G LTE",
                "terrain_obstruction_risk": "High near 2,200-foot Notch Peak cliff face",
                "distance_to_nearest_tower_miles": 26.0,
                "is_cellular_internet_dependable": False,
                "recommendation_for_remote_workers": "Cell signal is weak. Starlink required for remote work at Notch Peak base."
            },
            "amenities_and_features": [
                "2,200-Foot Vertical Cliff View (2nd Pure Drop in North America)",
                "Bristlecone Pine Forest Nearby",
                "Wilderness Solitude",
                "Dark Sky Stargazing"
            ],
            "location_scores": {
                "scenery": 10,
                "privacy": 10,
                "accessibility": 5,
                "shade_coverage": 3,
                "water_proximity": 1,
                "safety": 7
            },
            "flora_fauna_and_ecosystem": "Great Basin desert transitioning to ancient bristlecone pine on high ridges. Desert bighorn sheep, golden eagles, mountain lions.",
            "spiritual_cultural_and_folklore": "Notch Peak features the highest pure vertical cliff drop in the United States second only to El Capitan.",
            "hiking_trails_and_outdoor_recreation": "Notch Peak Summit Trail (strenuous 9-mile round trip), Sawtooth Canyon hiking, fossil hunting in Tule Valley.",
            "nearest_hospital_and_emergency": "Delta Community Hospital, 130 White Sage Ave, Delta, UT (Approx 50 miles)",
            "trash_and_waste_policy": "Strict Pack-In/Pack-Out policy.",
            "last_updated": "2026-09-12"
        },
        {
            "campsite_name": "Book Cliffs / Nine Mile Canyon Dispersed (BLM Vernal)",
            "state": "Utah",
            "managing_agency": "Bureau of Land Management (Vernal & Price Field Offices)",
            "gps_coordinates": "39.7754, -110.4512",
            "is_100_percent_free": True,
            "total_cost_or_fees": "$0 - 100% Free Public Land",
            "maximum_stay_length": "14 days",
            "rules_and_regulations": "Free primitive dispersed camping on BLM side pullouts. Strictly illegal to touch, deface, or camp directly underneath rock art panels.",
            "poop_disposal_rules": "Pack out human waste or bury 6-8 inches deep 200 feet from Nine Mile Creek channel.",
            "campfire_rules": "Fires in existing rings only. Extinguish fully. Do not collect wood from archaeological structures.",
            "ranger_agency_contact": "BLM Price Field Office: (435) 636-3600",
            "access_and_road_conditions": {
                "recommended_vehicle": "Low-clearance 2WD accessible via paved Nine Mile Canyon Road",
                "road_type_and_condition": "Paved main canyon road with gravel side canyon spurs.",
                "scores": {
                    "front_wheel_drive_clearance": 9,
                    "high_clearance_necessary": 3,
                    "four_wheel_drive_necessary": 2,
                    "seasonal_impassability_risk": 4
                }
            },
            "nearest_supply_towns": [
                {
                    "town_name": "Wellington, UT",
                    "distance_miles": 28,
                    "amenities_available": "Gas station, diner, convenience store"
                },
                {
                    "town_name": "Price, UT",
                    "distance_miles": 36,
                    "amenities_available": "Full urban services, hospital, Walmart, auto repair"
                }
            ],
            "seasonal_weather_and_best_times": "Spring and autumn (April-June, September-October). Summer heat (~90°F), cool night canyon downdrafts.",
            "dangers_and_hazards": "Flash flooding in narrow side canyons, coal truck traffic on paved road, rattlesnakes.",
            "nomad_connectivity_rating": {
                "t_mobile_signal": "0-1 bar (Weak inside canyon)",
                "verizon_signal": "1-2 bars 4G LTE (Spotty)",
                "att_signal": "1 bar 4G LTE",
                "terrain_obstruction_risk": "High inside 1,000-foot sandstone canyon walls",
                "distance_to_nearest_tower_miles": 20.0,
                "is_cellular_internet_dependable": False,
                "recommendation_for_remote_workers": "Cellular coverage is poor inside canyon. Remote workers should utilize satellite setups or stay near canyon mouth."
            },
            "amenities_and_features": [
                "'World's Longest Art Gallery' (Thousands of Petroglyphs)",
                "Paved Scenic Canyon Drive",
                "Fremont Culture Ruins",
                "Stream Side Camping"
            ],
            "location_scores": {
                "scenery": 10,
                "privacy": 8,
                "accessibility": 9,
                "shade_coverage": 5,
                "water_proximity": 4,
                "safety": 8
            },
            "flora_fauna_and_ecosystem": "Cottonwood canyon bottom flanked by sandstone cliffs and piñon-juniper. Elk, mule deer, wild turkeys, bighorn sheep.",
            "spiritual_cultural_and_folklore": "Contains over 10,000 ancient Fremont and Ute rock art images dating from 300 AD to 1500 AD, including the famous 'Great Hunt' panel.",
            "hiking_trails_and_outdoor_recreation": "Rock art self-guided tours, Cottonwood Canyon hiking, wildlife viewing, road cycling.",
            "nearest_hospital_and_emergency": "Castleview Hospital, 300 N Hospital Dr, Price, UT (Approx 36 miles)",
            "trash_and_waste_policy": "Strict Pack-In/Pack-Out policy. Protect world-class archaeological site.",
            "last_updated": "2026-09-12"
        }
    ],
    "Washington": [
        {
            "campsite_name": "Smackout Pass Dispersed (Colville National Forest)",
            "state": "Washington",
            "managing_agency": "US Forest Service - Colville National Forest (Sullivan Lake District)",
            "gps_coordinates": "48.7845, -117.5123",
            "is_100_percent_free": True,
            "total_cost_or_fees": "$0 - 100% Free Public Land",
            "maximum_stay_length": "14 days",
            "rules_and_regulations": "Dispersed camping allowed along Forest Service roads. Food storage rules strictly enforced (Grizzly bear recovery zone).",
            "poop_disposal_rules": "Bury waste 6-8 inches deep 200 feet from streams and wetlands.",
            "campfire_rules": "Observe USFS fire danger ratings. Keep fires contained and drown cold before leaving.",
            "ranger_agency_contact": "Sullivan Lake Ranger District (Ione): (509) 442-3141",
            "access_and_road_conditions": {
                "recommended_vehicle": "Low-clearance 2WD accessible on gravel NF-1900 road",
                "road_type_and_condition": "Graded gravel Forest Service road with minor potholes.",
                "scores": {
                    "front_wheel_drive_clearance": 8,
                    "high_clearance_necessary": 3,
                    "four_wheel_drive_necessary": 2,
                    "seasonal_impassability_risk": 7
                }
            },
            "nearest_supply_towns": [
                {
                    "town_name": "Ione, WA",
                    "distance_miles": 12,
                    "amenities_available": "Gas station, general store, cafe, post office"
                },
                {
                    "town_name": "Colville, WA",
                    "distance_miles": 45,
                    "amenities_available": "Full city services, Walmart, hospital, hardware"
                }
            ],
            "seasonal_weather_and_best_times": "Summer and early autumn (June-September). Mild summer temps (75°F-85°F). Snow blocks pass October-May.",
            "dangers_and_hazards": "Grizzly bear and black bear habitat (bear canister or certified food hanging mandatory), moose encounters.",
            "nomad_connectivity_rating": {
                "t_mobile_signal": "1-2 bars 4G LTE",
                "verizon_signal": "2-3 bars 4G LTE",
                "att_signal": "2 bars 4G LTE",
                "terrain_obstruction_risk": "Moderate due to dense timber and mountain ridges",
                "distance_to_nearest_tower_miles": 12.0,
                "is_cellular_internet_dependable": True,
                "recommendation_for_remote_workers": "Cellular internet is functional in elevated clearings along Smackout Pass."
            },
            "amenities_and_features": [
                "Lush Cedar & Pine Forest Shade",
                "Wilderness Solitude",
                "Mountain Views",
                "Berry Picking (Huckleberries in August)"
            ],
            "location_scores": {
                "scenery": 9,
                "privacy": 9,
                "accessibility": 8,
                "shade_coverage": 9,
                "water_proximity": 4,
                "safety": 8
            },
            "flora_fauna_and_ecosystem": "Interior Pacific Northwest rainforest transition. Western red cedar, Douglas fir, huckleberry. Grizzly bears, black bears, gray wolves, moose, lynx.",
            "spiritual_cultural_and_folklore": "Traditional hunting and berry gathering grounds of the Kalispel Tribe of Indians.",
            "hiking_trails_and_outdoor_recreation": "Smackout Pass trails, Sullivan Lake hiking trails, wildlife watching, huckleberry picking.",
            "nearest_hospital_and_emergency": "Mount Carmel Hospital, 982 E Columbia Ave, Colville, WA (Approx 45 miles)",
            "trash_and_waste_policy": "Strict Pack-In/Pack-Out. Bear-proof food storage required.",
            "last_updated": "2026-09-12"
        },
        {
            "campsite_name": "Toats Coulee Dispersed (Okanogan-Wenatchee NF)",
            "state": "Washington",
            "managing_agency": "US Forest Service - Okanogan-Wenatchee NF (Tonasket District)",
            "gps_coordinates": "48.8812, -119.7418",
            "is_100_percent_free": True,
            "total_cost_or_fees": "$0 - 100% Free Public Land",
            "maximum_stay_length": "14 days",
            "rules_and_regulations": "Dispersed camping along Toats Coulee Creek road. Keep camp 100 ft back from creek bank. Food storage precautions.",
            "poop_disposal_rules": "Dig cathole 6-8 inches deep 200 feet from creek.",
            "campfire_rules": "Follow seasonal fire bans. Extinguish fires completely cold.",
            "ranger_agency_contact": "Tonasket Ranger District: (509) 486-2186",
            "access_and_road_conditions": {
                "recommended_vehicle": "Low-clearance 2WD accessible on primary gravel road",
                "road_type_and_condition": "Well-maintained Forest Service gravel road.",
                "scores": {
                    "front_wheel_drive_clearance": 8,
                    "high_clearance_necessary": 3,
                    "four_wheel_drive_necessary": 2,
                    "seasonal_impassability_risk": 7
                }
            },
            "nearest_supply_towns": [
                {
                    "town_name": "Loomis, WA",
                    "distance_miles": 8,
                    "amenities_available": "General store, gas pump, tavern"
                },
                {
                    "town_name": "Tonasket, WA",
                    "distance_miles": 26,
                    "amenities_available": "Groceries, hardware, gas, medical clinic"
                }
            ],
            "seasonal_weather_and_best_times": "Late spring through autumn (May-October). Sunny dry Okanogan climate with warm summer days (~85°F).",
            "dangers_and_hazards": "Wildfire season in late summer, black bears, rattlesnakes in lower canyon.",
            "nomad_connectivity_rating": {
                "t_mobile_signal": "1-2 bars 4G LTE",
                "verizon_signal": "2-3 bars 4G LTE",
                "att_signal": "2 bars 4G LTE",
                "terrain_obstruction_risk": "Moderate",
                "distance_to_nearest_tower_miles": 14.0,
                "is_cellular_internet_dependable": False,
                "recommendation_for_remote_workers": "Cell signal is weak inside canyon. Satellite internet recommended."
            },
            "amenities_and_features": [
                "Creek Side Camping",
                "Aspen & Ponderosa Forest",
                "Fishing Access",
                "Pasayten Wilderness Gateway"
            ],
            "location_scores": {
                "scenery": 9,
                "privacy": 8,
                "accessibility": 8,
                "shade_coverage": 8,
                "water_proximity": 9,
                "safety": 9
            },
            "flora_fauna_and_ecosystem": "Dry interior forest transition. Ponderosa pine, aspen, Douglas fir. Mule deer, black bears, bighorn sheep, rainbow trout.",
            "spiritual_cultural_and_folklore": "Historic 19th-century gold mining and cattle drive corridor leading to Palmer Mountain.",
            "hiking_trails_and_outdoor_recreation": "Pasayten Wilderness trailheads nearby, trout fishing in Toats Coulee Creek, wildlife photography.",
            "nearest_hospital_and_emergency": "North Valley Hospital, 203 S Western Ave, Tonasket, WA (Approx 26 miles)",
            "trash_and_waste_policy": "Pack-In/Pack-Out mandatory.",
            "last_updated": "2026-09-12"
        },
        {
            "campsite_name": "Middle Fork Snoqualmie Dispersed (Mount Baker-Snoqualmie NF)",
            "state": "Washington",
            "managing_agency": "US Forest Service - Mount Baker-Snoqualmie National Forest",
            "gps_coordinates": "47.5512, -121.5412",
            "is_100_percent_free": True,
            "total_cost_or_fees": "$0 - 100% Free Public Land (Primitive dispersed pullouts beyond paved section)",
            "maximum_stay_length": "14 days",
            "rules_and_regulations": "Dispersed camping allowed in designated pullouts along Middle Fork Road past the paved corridor. Pack out all garbage.",
            "poop_disposal_rules": "Bury human waste 6-8 inches deep 200 feet from Middle Fork Snoqualmie River.",
            "campfire_rules": "Extinguish campfires completely. Observe summer burn bans.",
            "ranger_agency_contact": "Snoqualmie Ranger District (North Bend): (425) 888-1421",
            "access_and_road_conditions": {
                "recommended_vehicle": "Low-clearance 2WD accessible on paved road and initial smooth gravel pullouts",
                "road_type_and_condition": "Paved for first 12 miles, paved-to-gravel transition with smooth pullouts.",
                "scores": {
                    "front_wheel_drive_clearance": 9,
                    "high_clearance_necessary": 2,
                    "four_wheel_drive_necessary": 1,
                    "seasonal_impassability_risk": 4
                }
            },
            "nearest_supply_towns": [
                {
                    "town_name": "North Bend, WA",
                    "distance_miles": 14,
                    "amenities_available": "Full grocery stores, gas, gear shops, restaurants, urgent care"
                },
                {
                    "town_name": "Seattle, WA",
                    "distance_miles": 42,
                    "amenities_available": "Major metropolitan services"
                }
            ],
            "seasonal_weather_and_best_times": "Late spring through autumn (May-October). Moderate temps (~75°F summer). Frequent Pacific Northwest rain.",
            "dangers_and_hazards": "Swift river currents, falling tree branches during rain/wind, black bears.",
            "nomad_connectivity_rating": {
                "t_mobile_signal": "2-3 bars 4G LTE",
                "verizon_signal": "3-4 bars 4G LTE",
                "att_signal": "3 bars 4G LTE",
                "terrain_obstruction_risk": "Moderate due to tall forest canopy and mountain valley walls",
                "distance_to_nearest_tower_miles": 10.0,
                "is_cellular_internet_dependable": True,
                "recommendation_for_remote_workers": "Dependable signal for remote work close to Seattle metro area."
            },
            "amenities_and_features": [
                "Lush Old-Growth Rainforest Canopy",
                "River Swimming & Kayaking",
                "Close Proximity to Seattle Metro",
                "Hiking Trailheads"
            ],
            "location_scores": {
                "scenery": 9,
                "privacy": 6,
                "accessibility": 9,
                "shade_coverage": 10,
                "water_proximity": 9,
                "safety": 9
            },
            "flora_fauna_and_ecosystem": "Temperate rainforest. Douglas fir, western hemlock, sword ferns, moss-draped bigleaf maples. Black bears, Roosevelt elk, bald eagles, salmon.",
            "spiritual_cultural_and_folklore": "Traditional lands of the Snoqualmie Tribe; valley held deep spiritual significance and trade pathways across Snoqualmie Pass.",
            "hiking_trails_and_outdoor_recreation": "Middle Fork Trail, Garfield Ledges trail, Pratt River trail, kayaking and fly fishing.",
            "nearest_hospital_and_emergency": "Snoqualmie Valley Hospital, 9801 Frontier Ave SE, Snoqualmie, WA (Approx 16 miles)",
            "trash_and_waste_policy": "Strict Pack-In/Pack-Out policy.",
            "last_updated": "2026-09-12"
        },
        {
            "campsite_name": "Babyshoe Pass Dispersed (Gifford Pinchot NF)",
            "state": "Washington",
            "managing_agency": "US Forest Service - Gifford Pinchot National Forest (Mt. Adams District)",
            "gps_coordinates": "46.2214, -121.5889",
            "is_100_percent_free": True,
            "total_cost_or_fees": "$0 - 100% Free Public Land",
            "maximum_stay_length": "14 days",
            "rules_and_regulations": "Dispersed primitive camping along Forest Road 23 near Babyshoe Pass. Camp in established turnouts.",
            "poop_disposal_rules": "Bury waste 6-8 inches deep 200 feet from streams and meadows.",
            "campfire_rules": "Observe Gifford Pinchot NF fire restrictions. Extinguish cold before departure.",
            "ranger_agency_contact": "Mt. Adams Ranger District (Trout Lake): (509) 395-3400",
            "access_and_road_conditions": {
                "recommended_vehicle": "Low-clearance 2WD accessible via paved/gravel Forest Road 23",
                "road_type_and_condition": "Paved and hard-packed gravel Forest Service road.",
                "scores": {
                    "front_wheel_drive_clearance": 8,
                    "high_clearance_necessary": 3,
                    "four_wheel_drive_necessary": 2,
                    "seasonal_impassability_risk": 8
                }
            },
            "nearest_supply_towns": [
                {
                    "town_name": "Trout Lake, WA",
                    "distance_miles": 16,
                    "amenities_available": "General store, gas station, cafe"
                },
                {
                    "town_name": "White Salmon / Hood River, WA/OR",
                    "distance_miles": 42,
                    "amenities_available": "Full groceries, gear stores, medical, craft breweries"
                }
            ],
            "seasonal_weather_and_best_times": "Summer and early autumn (July-September). Snow blocks pass late fall through June.",
            "dangers_and_hazards": "Active volcano proximity (Mount Adams), snow pack on high pass road into early summer, black bears.",
            "nomad_connectivity_rating": {
                "t_mobile_signal": "1-2 bars 4G LTE",
                "verizon_signal": "2-3 bars 4G LTE",
                "att_signal": "2 bars 4G LTE",
                "terrain_obstruction_risk": "Moderate",
                "distance_to_nearest_tower_miles": 15.0,
                "is_cellular_internet_dependable": False,
                "recommendation_for_remote_workers": "Cell coverage is spotty under dense canopy. Satellite internet recommended for critical work."
            },
            "amenities_and_features": [
                "Mount Adams Volcano Views",
                "Huckleberry Fields",
                "Subalpine Meadows",
                "PCT Access Nearby"
            ],
            "location_scores": {
                "scenery": 10,
                "privacy": 8,
                "accessibility": 8,
                "shade_coverage": 8,
                "water_proximity": 5,
                "safety": 9
            },
            "flora_fauna_and_ecosystem": "Cascade mountain subalpine forest. Noble fir, mountain hemlock, huckleberry bushes. Cascade frogs, black bears, elk, mountain pikas.",
            "spiritual_cultural_and_folklore": "Mount Adams (Pahto) is sacred to the Yakama Nation as a revered medicine mountain.",
            "hiking_trails_and_outdoor_recreation": "Pacific Crest Trail access nearby, Mount Adams summit climbing trails, Council Lake hiking.",
            "nearest_hospital_and_emergency": "Skyline Health Hospital, 211 Skyline Dr, White Salmon, WA (Approx 42 miles)",
            "trash_and_waste_policy": "Strict Pack-In/Pack-Out policy.",
            "last_updated": "2026-09-12"
        },
        {
            "campsite_name": "Yakima River Canyon BLM Dispersed",
            "state": "Washington",
            "managing_agency": "Bureau of Land Management (Wenatchee Field Office)",
            "gps_coordinates": "46.8123, -120.4612",
            "is_100_percent_free": True,
            "total_cost_or_fees": "$0 - 100% Free Public Land (Free dispersed pullouts along BLM ridge roads above canyon)",
            "maximum_stay_length": "14 days",
            "rules_and_regulations": "Free primitive dispersed camping on BLM ridge lands above the canyon outside fee recreation sites.",
            "poop_disposal_rules": "Pack out human waste or dig cathole 6-8 inches deep 200 feet from canyon rim and washes.",
            "campfire_rules": "Extremely strict fire bans during summer dry season due to high cheatgrass wildfire hazard.",
            "ranger_agency_contact": "BLM Wenatchee Field Office: (509) 665-2100",
            "access_and_road_conditions": {
                "recommended_vehicle": "High-clearance 2WD/4WD recommended for dirt ridge roads above canyon",
                "road_type_and_condition": "Paved SR-821 down canyon, steep dirt/gravel tracks accessing top ridge pullouts.",
                "scores": {
                    "front_wheel_drive_clearance": 7,
                    "high_clearance_necessary": 6,
                    "four_wheel_drive_necessary": 3,
                    "seasonal_impassability_risk": 4
                }
            },
            "nearest_supply_towns": [
                {
                    "town_name": "Ellensburg, WA",
                    "distance_miles": 12,
                    "amenities_available": "Full city amenities, CWU campus, groceries, hospital, hardware"
                },
                {
                    "town_name": "Yakima, WA",
                    "distance_miles": 22,
                    "amenities_available": "Full regional urban services, airport, medical"
                }
            ],
            "seasonal_weather_and_best_times": "Spring and autumn (April-June, September-October). High summer temps (85°F-95°F) with intense sun exposure.",
            "dangers_and_hazards": "Rattlesnakes, high summer wildfire risk, high canyon winds.",
            "nomad_connectivity_rating": {
                "t_mobile_signal": "3-4 bars 5G/4G LTE",
                "verizon_signal": "4 bars 5G/4G LTE",
                "att_signal": "3-4 bars 5G/4G LTE",
                "terrain_obstruction_risk": "Low on ridge tops",
                "distance_to_nearest_tower_miles": 5.5,
                "is_cellular_internet_dependable": True,
                "recommendation_for_remote_workers": "Excellent cell signal on ridge pullouts with line-of-sight to Ellensburg/Yakima towers."
            },
            "amenities_and_features": [
                "Basalt Canyon Views",
                "Yakima River Fishing Nearby",
                "Bighorn Sheep Habitat",
                "Blue-Ribbon Fly Fishing"
            ],
            "location_scores": {
                "scenery": 9,
                "privacy": 8,
                "accessibility": 8,
                "shade_coverage": 2,
                "water_proximity": 3,
                "safety": 9
            },
            "flora_fauna_and_ecosystem": "Shrub-steppe desert ecosystem. Big sagebrush, bluebunch wheatgrass. Rocky Mountain bighorn sheep, golden eagles, blue-ribbon blueback trout.",
            "spiritual_cultural_and_folklore": "Deep basalt gorge carved through Columbia River basalt flows over millions of years.",
            "hiking_trails_and_outdoor_recreation": "Umtanum Creek Falls trail, Yakima River Canyon float trips, fly fishing, bird watching.",
            "nearest_hospital_and_emergency": "Kittitas Valley Healthcare, 603 S Chestnut St, Ellensburg, WA (Approx 12 miles)",
            "trash_and_waste_policy": "Pack-In/Pack-Out mandatory.",
            "last_updated": "2026-09-12"
        }
    ],
    "Wyoming": [
        {
            "campsite_name": "Vedauwoo Dispersed (Medicine Bow National Forest)",
            "state": "Wyoming",
            "managing_agency": "US Forest Service - Medicine Bow-Routt National Forests (Laramie District)",
            "gps_coordinates": "41.1612, -105.3789",
            "is_100_percent_free": True,
            "total_cost_or_fees": "$0 - 100% Free Public Land (Dispersed pullouts along NF roads outside recreation fee area)",
            "maximum_stay_length": "14 days",
            "rules_and_regulations": "Dispersed camping allowed on Forest Service lands outside the developed Vedauwoo Recreation Area fee boundary. Camp in existing pullouts.",
            "poop_disposal_rules": "Dig 6-8 inch catholes 200 feet from streams and rock formations.",
            "campfire_rules": "Use existing fire rings. Douse completely cold with water.",
            "ranger_agency_contact": "Laramie Ranger District: (307) 745-2300",
            "access_and_road_conditions": {
                "recommended_vehicle": "Low-clearance 2WD accessible on main gravel forest roads",
                "road_type_and_condition": "Gravel forest roads off I-80. Smooth with minor washboarding.",
                "scores": {
                    "front_wheel_drive_clearance": 8,
                    "high_clearance_necessary": 3,
                    "four_wheel_drive_necessary": 2,
                    "seasonal_impassability_risk": 7
                }
            },
            "nearest_supply_towns": [
                {
                    "town_name": "Laramie, WY",
                    "distance_miles": 16,
                    "amenities_available": "Full city amenities, UW campus, groceries, hospital, gear shops"
                },
                {
                    "town_name": "Cheyenne, WY",
                    "distance_miles": 30,
                    "amenities_available": "State capital services, full urban amenities"
                }
            ],
            "seasonal_weather_and_best_times": "Summer and early autumn (June-September). Elevation 8,000 ft provides crisp summer weather (70°F-80°F). Strong winds year-round.",
            "dangers_and_hazards": "High wind gusts, sudden summer afternoon lightning storms, severe cold outside summer months.",
            "nomad_connectivity_rating": {
                "t_mobile_signal": "3-4 bars 5G/4G LTE",
                "verizon_signal": "4 bars 5G/4G LTE",
                "att_signal": "3-4 bars 5G/4G LTE",
                "terrain_obstruction_risk": "Low to Moderate around massive granite domes",
                "distance_to_nearest_tower_miles": 5.0,
                "is_cellular_internet_dependable": True,
                "recommendation_for_remote_workers": "Excellent cell signal along I-80 corridor near Laramie for remote work."
            },
            "amenities_and_features": [
                "World-Class Granite Rock Climbing",
                "Iconic Sherman Granite Rock Domes",
                "Aspen Groves",
                "Close Proximity to I-80"
            ],
            "location_scores": {
                "scenery": 10,
                "privacy": 7,
                "accessibility": 9,
                "shade_coverage": 6,
                "water_proximity": 3,
                "safety": 9
            },
            "flora_fauna_and_ecosystem": "1.4 billion-year-old Sherman granite rock formations surrounded by aspen and lodgepole pine. Moose, mule deer, pronghorn, bobcats.",
            "spiritual_cultural_and_folklore": "Sacred place to Arapaho and Cheyenne peoples known as 'Land of the Earthborn Spirits'.",
            "hiking_trails_and_outdoor_recreation": "Turtle Rock Trail, world-class crack rock climbing, mountain biking, photography.",
            "nearest_hospital_and_emergency": "Ivinson Memorial Hospital, 255 N 30th St, Laramie, WY (Approx 16 miles)",
            "trash_and_waste_policy": "Strict Pack-In/Pack-Out policy.",
            "last_updated": "2026-09-12"
        },
        {
            "campsite_name": "Upper Green River Dispersed (Bridger-Teton NF)",
            "state": "Wyoming",
            "managing_agency": "US Forest Service - Bridger-Teton National Forest (Pinedale District)",
            "gps_coordinates": "43.2845, -109.9812",
            "is_100_percent_free": True,
            "total_cost_or_fees": "$0 - 100% Free Public Land",
            "maximum_stay_length": "14 days",
            "rules_and_regulations": "Dispersed camping allowed along Green River Lakes road (FR 600). Food storage rules strictly enforced (Grizzly bear territory).",
            "poop_disposal_rules": "Bury waste 6-8 inches deep 200 feet from Green River and tributaries.",
            "campfire_rules": "Fires in existing rings only. Extinguish dousing with water until cool to touch.",
            "ranger_agency_contact": "Pinedale Ranger District: (307) 367-4326",
            "access_and_road_conditions": {
                "recommended_vehicle": "Low-clearance 2WD accessible on main gravel FR 600 during summer",
                "road_type_and_condition": "25 miles of unpaved washboard gravel road off US-191.",
                "scores": {
                    "front_wheel_drive_clearance": 7,
                    "high_clearance_necessary": 4,
                    "four_wheel_drive_necessary": 2,
                    "seasonal_impassability_risk": 8
                }
            },
            "nearest_supply_towns": [
                {
                    "town_name": "Pinedale, WY",
                    "distance_miles": 38,
                    "amenities_available": "Groceries, hardware, outfitters, medical clinic, restaurants"
                }
            ],
            "seasonal_weather_and_best_times": "Summer (July-September). High elevation (~7,800 ft). Pristine summer temps (70°F-78°F) with cold nights (35°F). Snow Oct-June.",
            "dangers_and_hazards": "Grizzly bears and black bears (certified bear canisters or hanging mandatory), high elevation cold.",
            "nomad_connectivity_rating": {
                "t_mobile_signal": "0 bars (No Service)",
                "verizon_signal": "0-1 bar (Weak/No Data)",
                "att_signal": "0 bars (No Service)",
                "terrain_obstruction_risk": "High in deep valley beneath Wind River Peaks",
                "distance_to_nearest_tower_miles": 32.0,
                "is_cellular_internet_dependable": False,
                "recommendation_for_remote_workers": "Cell signal is practically non-existent. High performance Starlink required for remote work."
            },
            "amenities_and_features": [
                "Squaretop Mountain Iconic Views",
                "Green River Fly Fishing",
                "Wind River Wilderness Gateway",
                "Glacial River Headwaters"
            ],
            "location_scores": {
                "scenery": 10,
                "privacy": 9,
                "accessibility": 6,
                "shade_coverage": 6,
                "water_proximity": 10,
                "safety": 8
            },
            "flora_fauna_and_ecosystem": "Subalpine river valley. Lodgepole pine, Engelmann spruce, quaking aspen. Grizzly bears, wolves, moose, trumpeter swans, cutthroat trout.",
            "spiritual_cultural_and_folklore": "Headwaters of the 730-mile Green River, major tributary of the Colorado River; historic Rendezvous site for 1830s mountain men.",
            "hiking_trails_and_outdoor_recreation": "Green River Lakes Trail, Highline Trail, Wind River Range backpacking, trout fly fishing, canoeing.",
            "nearest_hospital_and_emergency": "Pinedale Medical Clinic / St. John's Health, 625 E Hennick St, Pinedale, WY (Approx 38 miles)",
            "trash_and_waste_policy": "Strict Pack-In/Pack-Out. Mandatory bear safe storage.",
            "last_updated": "2026-09-12"
        },
        {
            "campsite_name": "Red Gulch Dispersed Camping (BLM Worland)",
            "state": "Wyoming",
            "managing_agency": "Bureau of Land Management (Worland Field Office)",
            "gps_coordinates": "44.2812, -107.8214",
            "is_100_percent_free": True,
            "total_cost_or_fees": "$0 - 100% Free Public Land",
            "maximum_stay_length": "14 days",
            "rules_and_regulations": "Free primitive dispersed camping on BLM land along Red Gulch Byway. Protect dinosaur tracksite fossils.",
            "poop_disposal_rules": "Bury waste 6-8 inches deep 200 feet from dry gullies and roads.",
            "campfire_rules": "Extinguish fires cold with water. Carry fire pan where available.",
            "ranger_agency_contact": "BLM Worland Field Office: (307) 347-5100",
            "access_and_road_conditions": {
                "recommended_vehicle": "High-clearance 2WD/4WD recommended; bentonite clay road impassable when wet",
                "road_type_and_condition": "32-mile unpaved gravel and clay scenic byway.",
                "scores": {
                    "front_wheel_drive_clearance": 6,
                    "high_clearance_necessary": 6,
                    "four_wheel_drive_necessary": 4,
                    "seasonal_impassability_risk": 9
                }
            },
            "nearest_supply_towns": [
                {
                    "town_name": "Greybull, WY",
                    "distance_miles": 22,
                    "amenities_available": "Groceries, gas, hardware, diner, motel"
                },
                {
                    "town_name": "Worland, WY",
                    "distance_miles": 38,
                    "amenities_available": "Full groceries, hospital, gas, auto parts"
                }
            ],
            "seasonal_weather_and_best_times": "Spring and autumn (May-June, September-October). High summer heat (90°F-95°F) with zero shade.",
            "dangers_and_hazards": "Bentonite clay roads turn into slick impassable grease when wet, flash floods in badlands, heat exposure.",
            "nomad_connectivity_rating": {
                "t_mobile_signal": "1-2 bars 4G LTE",
                "verizon_signal": "2-3 bars 4G LTE",
                "att_signal": "2 bars 4G LTE",
                "terrain_obstruction_risk": "Moderate in red rock canyons",
                "distance_to_nearest_tower_miles": 18.0,
                "is_cellular_internet_dependable": True,
                "recommendation_for_remote_workers": "Cell signal is surprisingly functional on elevated badland ridges."
            },
            "amenities_and_features": [
                "Red Rock Canyon Badlands",
                "Dinosaur Trackway Nearby",
                "Red Gulch Scenic Byway",
                "Dark Sky Stargazing"
            ],
            "location_scores": {
                "scenery": 9,
                "privacy": 9,
                "accessibility": 6,
                "shade_coverage": 1,
                "water_proximity": 1,
                "safety": 8
            },
            "flora_fauna_and_ecosystem": "Bighorn Basin badlands. Juniper, sagebrush, wild buckwheat. Pronghorn, horned lizards, golden eagles, coyotes.",
            "spiritual_cultural_and_folklore": "Site of the Red Gulch Dinosaur Tracksite, featuring Middle Jurassic dinosaur footprints preserved in limestone from 167 million years ago.",
            "hiking_trails_and_outdoor_recreation": "Red Gulch Dinosaur Trackway boardwalk, badland wilderness hiking, fossil hunting in surrounding public lands.",
            "nearest_hospital_and_emergency": "Washakie Medical Center, 400 S 15th St, Worland, WY (Approx 38 miles)",
            "trash_and_waste_policy": "Strict Pack-In/Pack-Out policy.",
            "last_updated": "2026-09-12"
        },
        {
            "campsite_name": "Muddy Mountain Dispersed (BLM Casper)",
            "state": "Wyoming",
            "managing_agency": "Bureau of Land Management (Casper Field Office)",
            "gps_coordinates": "42.6612, -106.2845",
            "is_100_percent_free": True,
            "total_cost_or_fees": "$0 - 100% Free Public Land (Free dispersed camping outside developed campgrounds)",
            "maximum_stay_length": "14 days",
            "rules_and_regulations": "Dispersed camping allowed on BLM lands along Muddy Mountain Road outside fee campground loops.",
            "poop_disposal_rules": "Bury waste 6-8 inches deep 200 feet from streams.",
            "campfire_rules": "Use existing fire rings. Douse completely cold.",
            "ranger_agency_contact": "BLM Casper Field Office: (307) 261-7600",
            "access_and_road_conditions": {
                "recommended_vehicle": "Low-clearance 2WD accessible on main gravel road during dry summer months",
                "road_type_and_condition": "Paved Casper Mountain road transitioning to well-graded gravel Muddy Mountain road.",
                "scores": {
                    "front_wheel_drive_clearance": 8,
                    "high_clearance_necessary": 3,
                    "four_wheel_drive_necessary": 2,
                    "seasonal_impassability_risk": 7
                }
            },
            "nearest_supply_towns": [
                {
                    "town_name": "Casper, WY",
                    "distance_miles": 20,
                    "amenities_available": "Full urban services, hospital, Walmart, REI, regional airport"
                }
            ],
            "seasonal_weather_and_best_times": "Summer and early autumn (June-September). Elevation 8,200 ft provides escape from summer heat in Casper (75°F vs 95°F). Snow blocks road Oct-May.",
            "dangers_and_hazards": "Sudden mountain thunderstorms, winter snowstorms in late spring/early fall, black bears.",
            "nomad_connectivity_rating": {
                "t_mobile_signal": "3-4 bars 5G/4G LTE",
                "verizon_signal": "4 bars 5G/4G LTE",
                "att_signal": "3-4 bars 5G/4G LTE",
                "terrain_obstruction_risk": "Low on top mountain plateau",
                "distance_to_nearest_tower_miles": 7.0,
                "is_cellular_internet_dependable": True,
                "recommendation_for_remote_workers": "Excellent high-speed cell coverage with line-of-sight to Casper valley towers."
            },
            "amenities_and_features": [
                "Cool Mountain Pine Forest",
                "Casper City Lights Overlook Views",
                "Interpretive Nature Trails",
                "Close Proximity to Supply Hub"
            ],
            "location_scores": {
                "scenery": 9,
                "privacy": 8,
                "accessibility": 8,
                "shade_coverage": 8,
                "water_proximity": 2,
                "safety": 9
            },
            "flora_fauna_and_ecosystem": "Lodgepole pine and subalpine fir forest interspersed with mountain meadows. Elk, mule deer, wild turkey, black bears.",
            "spiritual_cultural_and_folklore": "Prominent landmark overlooking historic Oregon Trail, Mormon Trail, and Pony Express routes through Casper.",
            "hiking_trails_and_outdoor_recreation": "Rim Rock Interpretive Trail, Muddy Mountain Loop mountain biking, wildlife watching.",
            "nearest_hospital_and_emergency": "Banner Wyoming Medical Center, 1233 E 2nd St, Casper, WY (Approx 20 miles)",
            "trash_and_waste_policy": "Pack-In/Pack-Out mandatory.",
            "last_updated": "2026-09-12"
        },
        {
            "campsite_name": "Oregon Basin Dispersed Camping (BLM Cody)",
            "state": "Wyoming",
            "managing_agency": "Bureau of Land Management (Cody Field Office)",
            "gps_coordinates": "44.3812, -108.9812",
            "is_100_percent_free": True,
            "total_cost_or_fees": "$0 - 100% Free Public Land",
            "maximum_stay_length": "14 days",
            "rules_and_regulations": "Free primitive dispersed camping on BLM badland tracks outside oil lease operations.",
            "poop_disposal_rules": "Bury waste 6-8 inches deep 200 feet from dry drainages.",
            "campfire_rules": "Contain fires in rock rings. Ensure drowning cold before leaving.",
            "ranger_agency_contact": "BLM Cody Field Office: (307) 578-5900",
            "access_and_road_conditions": {
                "recommended_vehicle": "Standard 2WD suitable on primary gravel tracks; high-clearance advised for secondary spurs",
                "road_type_and_condition": "Gravel oilfield access roads off WY-120. Well-graded with gravel surface.",
                "scores": {
                    "front_wheel_drive_clearance": 8,
                    "high_clearance_necessary": 4,
                    "four_wheel_drive_necessary": 2,
                    "seasonal_impassability_risk": 5
                }
            },
            "nearest_supply_towns": [
                {
                    "town_name": "Cody, WY",
                    "distance_miles": 14,
                    "amenities_available": "Full groceries, hospital, rodeo, outdoor gear, gas, Cody airport"
                }
            ],
            "seasonal_weather_and_best_times": "Spring and autumn (May-June, September-October). Warm summer days (~85°F) with cool evening mountain breeze.",
            "dangers_and_hazards": "High wind gusts across open basin, rattlesnakes, oilfield truck traffic on main gravel arterial.",
            "nomad_connectivity_rating": {
                "t_mobile_signal": "3-4 bars 5G/4G LTE",
                "verizon_signal": "4 bars 5G/4G LTE",
                "att_signal": "3-4 bars 5G/4G LTE",
                "terrain_obstruction_risk": "Low",
                "distance_to_nearest_tower_miles": 6.0,
                "is_cellular_internet_dependable": True,
                "recommendation_for_remote_workers": "Excellent cell coverage close to Cody tower corridor for remote working."
            },
            "amenities_and_features": [
                "Absaroka Mountain Panorama Views",
                "Close to Yellowstone Gateway Town",
                "Open High Desert Landscape",
                "Stargazing"
            ],
            "location_scores": {
                "scenery": 8,
                "privacy": 8,
                "accessibility": 9,
                "shade_coverage": 1,
                "water_proximity": 1,
                "safety": 9
            },
            "flora_fauna_and_ecosystem": "High desert sagebrush basin. Sagebrush, rabbitbrush, wheatgrass. Pronghorn antelope, sage grouse, coyotes.",
            "spiritual_cultural_and_folklore": "Historic badland basin named after the Oregon Territory claims; gateway to Buffalo Bill Cody's historic Absaroka mountain domain.",
            "hiking_trails_and_outdoor_recreation": "Desert badland hiking, photography of Absaroka range sunsets, close proximity to Yellowstone East Entrance.",
            "nearest_hospital_and_emergency": "Cody Regional Health, 707 Sheridan Ave, Cody, WY (Approx 14 miles)",
            "trash_and_waste_policy": "Pack-In/Pack-Out mandatory.",
            "last_updated": "2026-09-12"
        }
    ]
}

state_filename_map = {
    "New Mexico": "new_mexico.json",
    "Oregon": "oregon.json",
    "Utah": "utah.json",
    "Washington": "washington.json",
    "Wyoming": "wyoming.json"
}

for state_name, sites in new_sites_by_state.items():
    filename = state_filename_map[state_name]
    filepath = os.path.join(STATES_DIR, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # append sites
    data.extend(sites)
    
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"Added {len(sites)} sites to {filename}. Total now: {len(data)}")
