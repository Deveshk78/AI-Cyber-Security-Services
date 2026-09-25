'''
(Handles Layer 1: Semantic Knowledge Graph Architecture using NetworkX)
'''
from pydantic import BaseModel
import networkx as nx

class AIAsset(BaseModel):
    asset_id: str
    model_name: str
    framework_version: str
    owner: str

class Control(BaseModel):
    control_id: str
    title: str
    description: str
    regulation_ref: str

class GRCKnowledgeGraph:
    def __init__(self):
        self.graph = nx.MultiDiGraph()

    def add_asset(self, asset: AIAsset):
        self.graph.add_node(asset.asset_id, type="Asset", data=asset.model_dump())

    def add_control(self, control: Control):
        self.graph.add_node(control.control_id, type="Control", data=control.model_dump())

    def link_asset_to_control(self, asset_id: str, control_id: str, status: str):
        self.graph.add_edge(asset_id, control_id, relation="GOVERNED_BY", compliance_status=status)

    def get_asset_compliance_status(self, asset_id: str):
        controls = []
        for _, target, data in self.graph.edges(asset_id, data=True):
            control_data = self.graph.nodes[target]["data"]
            controls.append({
                "control_id": target,
                "title": control_data["title"],
                "status": data["compliance_status"]
            })
        return controls