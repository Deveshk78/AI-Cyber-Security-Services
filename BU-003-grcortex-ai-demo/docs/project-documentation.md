# GRCortex AI Project Documentation

## Executive summary

GRCortex AI is a working prototype that demonstrates how an organization can connect AI system governance to live compliance verification. The platform merges three capabilities: graph-based control mapping, semantic policy matching, and real-time telemetry assessment.

## Objective

The project aims to translate legal and regulatory obligations into operational AI governance controls that can be checked automatically and traced across the lifecycle of an AI asset.

## System architecture

### Layer 1: semantic knowledge graph

The graph stores assets and governance controls and links them through semantic relationships. This allows teams to inspect which controls govern a given AI model and understand compliance posture quickly.

### Layer 2: policy intelligence

The vector engine compares a regulatory statement against internally defined policies using dense embeddings. This enables approximate semantic alignment even when wording differs across legislation, policy documents, and engineering standards.

### Layer 3: telemetry compliance service

The FastAPI endpoint accepts telemetry from a model or monitoring system and tests thresholds for drift, bias disparity, and hallucination. When thresholds are exceeded, the system returns flagged controls and an action-required state.

## Implementation notes

- `database/knowledge_graph.py` implements the governance graph.
- `intelligence/vector_matcher.py` provides semantic policy matching.
- `monitoring/telemetry_engine.py` exposes the compliance webhook.
- `main.py` orchestrates the demo workflow.

## Risk and compliance model

The project uses the following guardrails:

- Drift threshold: 0.15
- Bias threshold: 0.05
- Hallucination threshold: 0.02

If any metric exceeds its configured threshold, the system returns an `ACTION_REQUIRED` state and lists the associated controls.

## Suggested extension paths

- Add persistent storage or a database backend.
- Integrate with model registry and MLOps tools.
- Add policy versioning and change auditing.
- Support regulatory mapping for ISO 42001, NIST AI RMF, and EU AI Act.
- Produce regulator-facing evidence packs from the graph and telemetry stream.

## Contact

Devesh Kumar
Email: devesh2178@gmail.com
