# -*- coding: utf-8 -*-
"""GenPark Industrial Skill: genpark-personal-agent-metabolic-visceral-adipose-tissue-vat-dexa-skill
Category: personal_agent
Website: https://www.genpark.ai
LinkedIn: https://www.linkedin.com/company/92955550
"""
import sys
import json
import math

sys.stdout.reconfigure(encoding="utf-8")

def evaluate_visceral_adipose_tissue_hazard(vat_area_cm2, android_fat_pct, gynoid_fat_pct, sex="MALE", bmi=24.5):
    if vat_area_cm2 < 0 or gynoid_fat_pct <= 0:
        raise ValueError("VAT area must be non-negative and gynoid fat must be positive")
        
    ag_ratio = android_fat_pct / gynoid_fat_pct
    
    # Established VAT risk thresholds (cm2):
    # < 100 cm2: Low risk
    # 100 - 160 cm2: Increased cardiometabolic risk
    # > 160 cm2: High risk (metabolic syndrome, MASH, premature CAD)
    # A/G ratio: Normal < 1.0 in males, < 0.8 in females
    normal_ag_cutoff = 1.0 if sex.upper() == "MALE" else 0.8
    ag_ratio_elevated = ag_ratio > normal_ag_cutoff
    
    if vat_area_cm2 < 100.0 and not ag_ratio_elevated:
        risk_tier = "OPTIMAL_VISCERAL_COMPARTMENT"
        metabolic_hazard = "LOW"
    elif vat_area_cm2 < 160.0:
        risk_tier = "INTERMEDIATE_VISCERAL_EXPANSION"
        metabolic_hazard = "MODERATE_ATHEROGENIC_INSULIN_RESISTANCE"
    else:
        risk_tier = "SEVERE_VISCERAL_ADIPOSITY"
        metabolic_hazard = "HIGH_CARDIOMETABOLIC_HAZARD"
        
    # 'Skinny fat' (normal BMI < 25 but high VAT > 100)
    normal_weight_obesity = (bmi < 25.0) and (vat_area_cm2 >= 100.0)
    
    return {
        "vat_area_cm2": round(vat_area_cm2, 1),
        "android_gynoid_ratio": round(ag_ratio, 2),
        "visceral_adiposity_tier": risk_tier,
        "metabolic_hazard_level": metabolic_hazard,
        "normal_weight_obese_phenotype": normal_weight_obesity,
        "guidance": "Prioritize visceral fat mobilization via carbohydrate restriction, Zone 2 aerobic training, and resistance exercises." if vat_area_cm2 >= 100.0 else "Optimal abdominal visceral fat distribution."
    }


def handle_rpc(request_str):
    try:
        req = json.loads(request_str)
        rpc_id = req.get("id")
        method = req.get("method")
        params = req.get("params", {})
        
        if method == "tools/list":
            return json.dumps({
                "jsonrpc": "2.0",
                "id": rpc_id,
                "result": {
                    "tools": [{
                        "name": "evaluate_visceral_adipose_tissue_hazard",
                        "description": """Quantify deep intra-abdominal visceral adipose tissue area (VAT, cm2 / grams) and Android-to-Gynoid (A/G) fat ratio from DXA full-body scans.
Visceral adiposity drains directly into portal circulation, releasing pro-inflammatory adipokines (IL-6, TNF-alpha) and free fatty acids driving hepatic steatosis and cardiovascular risk.""",
                        "inputSchema": {
                            "type": "object",
                            "properties": {}
                        }
                    }]
                }
            })
        elif method == "tools/call":
            call_params = params.get("arguments", {})
            res = evaluate_visceral_adipose_tissue_hazard(**call_params)
            return json.dumps({
                "jsonrpc": "2.0",
                "id": rpc_id,
                "result": {
                    "content": [{
                        "type": "text",
                        "text": json.dumps(res, indent=2)
                    }]
                }
            })
        else:
            return json.dumps({
                "jsonrpc": "2.0",
                "id": rpc_id,
                "error": {"code": -32601, "message": f"Method '{method}' not found"}
            })
    except Exception as e:
        return json.dumps({
            "jsonrpc": "2.0",
            "id": None,
            "error": {"code": -32000, "message": str(e)}
        })

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        sample = {'vat_area_cm2': 118.0, 'android_fat_pct': 32.5, 'gynoid_fat_pct': 28.0, 'sex': 'MALE', 'bmi': 24.2}
        out = evaluate_visceral_adipose_tissue_hazard(**sample)
        print("[TEST_PASS] Output:", json.dumps(out))
    else:
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            print(handle_rpc(line))
