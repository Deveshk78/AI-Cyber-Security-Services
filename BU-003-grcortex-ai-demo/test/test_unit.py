from database.knowledge_graph import AIAsset, Control, GRCKnowledgeGraph


def test_knowledge_graph_tracks_asset_control_status():
    graph = GRCKnowledgeGraph()
    graph.add_asset(AIAsset(asset_id="mod_01", model_name="CreditScorer-LLM", framework_version="v1.2", owner="RiskTeam"))
    graph.add_control(Control(control_id="CTRL_BIAS_01", title="Disparate Impact Evaluation", description="Ensure demographic parity across scoring metrics.", regulation_ref="EU_AI_Act_Annex_III"))
    graph.link_asset_to_control("mod_01", "CTRL_BIAS_01", status="NON_COMPLIANT")

    status = graph.get_asset_compliance_status("mod_01")

    assert len(status) == 1
    assert status[0]["control_id"] == "CTRL_BIAS_01"
    assert status[0]["status"] == "NON_COMPLIANT"


def test_control_title_is_preserved_in_graph():
    control = Control(control_id="CTRL_DRIFT_05", title="Monthly Drift Review", description="Review drift output monthly.", regulation_ref="NIST_AI_RMF")
    graph = GRCKnowledgeGraph()
    graph.add_control(control)

    node = graph.graph.nodes["CTRL_DRIFT_05"]

    assert node["data"]["title"] == "Monthly Drift Review"
