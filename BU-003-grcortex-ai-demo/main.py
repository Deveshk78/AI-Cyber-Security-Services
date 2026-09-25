'''
(Orchestration script tying all components together and demonstrating console logs & local checks)
'''
import uvicorn
from database.knowledge_graph import GRCKnowledgeGraph, AIAsset, Control
from intelligence.vector_matcher import VectorPolicyEngine
from monitoring.telemetry_engine import app

def run_simulation():
    print("="*60)
    print("INITIALIZING GRCORTEX AI (CYGENIQ) SIMULATION ENGINE")
    print("="*60)

    # 1. Test Layer 1: Knowledge Graph
    print("\n[Layer 1] Building Semantic Knowledge Graph...")
    kg = GRCKnowledgeGraph()
    kg.add_asset(AIAsset(asset_id="mod_01", model_name="CreditScorer-LLM", framework_version="v1.2", owner="RiskTeam"))
    kg.add_control(Control(control_id="CTRL_BIAS_01", title="Disparate Impact Evaluation", description="Ensure demographic parity across scoring metrics.", regulation_ref="EU_AI_Act_Annex_III"))
    kg.link_asset_to_control("mod_01", "CTRL_BIAS_01", status="NON_COMPLIANT")
    
    status_report = kg.get_asset_compliance_status("mod_01")
    print(f"Asset mod_01 Linked Controls: {status_report}")

    # 2. Test Layer 2: Vector Semantic Policy Matching
    print("\n[Layer 2] Initializing Vector Policy Engine...")
    vector_engine = VectorPolicyEngine()
    vector_engine.register_internal_policies([
        "We must review fairness and demographic performance across credit decisions bi-weekly.",
        "All data pipelines must encrypt customer PII at rest using AES-256.",
        "Model drift parameters must be monitored hourly via automated metrics dashboards."
    ])
    
    query_clause = "The deployer of a high-risk AI system shall ensure regular evaluation of demographic bias and disparate impact."
    matches = vector_engine.find_matching_policy(query_clause)
    print(f"Regulatory Clause: '{query_clause}'")
    print(f"Top Semantic Policy Match: {matches}")

    print("\n[Layer 3] Starting FastAPI Continuous Telemetry Web Hook server...")
    print("You can test the real-time hook by sending a POST request to http://127.0.0.1:8000/v1/grc/telemetry-hook")
    print("="*60)

if __name__ == "__main__":
    run_simulation()
    # Start the continuous monitoring webhook server
    uvicorn.run(app, host="127.0.0.1", port=8000)