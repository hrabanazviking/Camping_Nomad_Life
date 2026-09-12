#!/usr/bin/env python3
import json
import glob
import os
import sys

SCHEMA_FILE = os.path.join(os.path.dirname(__file__), "schema.json")
STATES_DIR = os.path.join(os.path.dirname(__file__), "states")

REQUIRED_TOP_KEYS = [
    "id", "name", "state", "county", "coordinates", "management_agency",
    "rules_and_regulations", "waste_disposal_rules", "campfire_rules",
    "access_and_road_conditions", "nomad_connectivity_rating", "amenities",
    "location_scores", "nearest_supply_towns", "seasonal_weather_effects",
    "dangers_and_hazards", "acoustic_environment", "flora_and_fauna",
    "human_demographics_and_culture", "spiritual_and_folklore_data",
    "nearby_hiking_trails", "public_reviews_summary", "other_data", "last_updated"
]

def validate_site(site, state_name, file_path, index):
    errors = []
    for k in REQUIRED_TOP_KEYS:
        if k not in site or site[k] is None:
            errors.append(f"Missing required key '{k}' at index {index}")
            
    # Validate score ranges 1-10
    if "location_scores" in site and isinstance(site["location_scores"], dict):
        for score_key, val in site["location_scores"].items():
            if not isinstance(val, int) or val < 1 or val > 10:
                errors.append(f"Invalid score '{score_key}' = {val} (must be int 1-10) at index {index}")

    if "access_and_road_conditions" in site and "scores" in site["access_and_road_conditions"]:
        for score_key, val in site["access_and_road_conditions"]["scores"].items():
            if not isinstance(val, int) or val < 1 or val > 10:
                errors.append(f"Invalid road score '{score_key}' = {val} (must be int 1-10) at index {index}")
                
    if site.get("last_updated") != "2026-09-12":
        errors.append(f"Invalid last_updated '{site.get('last_updated')}' (expected 2026-09-12) at index {index}")
        
    return errors

def main():
    json_files = sorted(glob.glob(os.path.join(STATES_DIR, "*.json")))
    if not json_files:
        print(f"No state JSON files found in {STATES_DIR}")
        sys.exit(1)
        
    total_sites = 0
    total_files = 0
    all_passed = True
    
    print(f"Found {len(json_files)} state JSON files. Validating...\n")
    
    for fpath in json_files:
        fname = os.path.basename(fpath)
        try:
            with open(fpath, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            print(f"❌ FAIL: {fname} - Failed to parse JSON: {e}")
            all_passed = False
            continue
            
        if not isinstance(data, list):
            print(f"❌ FAIL: {fname} - Top-level JSON structure must be an array")
            all_passed = False
            continue
            
        file_errors = []
        for idx, site in enumerate(data):
            errs = validate_site(site, fname, fpath, idx)
            file_errors.extend(errs)
            
        if file_errors:
            print(f"❌ FAIL: {fname} ({len(data)} sites)")
            for err in file_errors:
                print(f"   - {err}")
            all_passed = False
        else:
            print(f"✅ PASS: {fname} ({len(data)} sites verified)")
            total_sites += len(data)
            total_files += 1
            
    print("\n----------------------------------------")
    if all_passed:
        print(f"SUCCESS: All {total_files} state files and {total_sites} primitive campsites passed validation!")
        sys.exit(0)
    else:
        print("FAILURE: Validation errors encountered.")
        sys.exit(1)

if __name__ == "__main__":
    main()
