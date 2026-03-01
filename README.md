# 👨‍🔬 Parth Tiwari

<div align="center">

[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=26&duration=2800&pause=800&color=00F7FF&center=true&vCenter=true&width=700&lines=AI+Systems+Engineer;Agentic+%26+Evaluation-Driven+AI;Production-Grade+ML+Infrastructure;RAG+%7C+LLMs+%7C+Real-Time+Systems)](https://git.io/typing-svg)

</div>

---

## ⚡ Who I Am

I design and deploy **evaluation-driven AI systems** that operate under real-world constraints.

Not demo notebooks.  
Not prompt wrappers.  
Actual systems with:

- Structured validation
- Regression testing
- Latency budgets
- Drift awareness
- Controlled failure modes

Currently focused on:
- Agentic AI systems
- RAG architectures
- ML reliability
- Production-grade ML pipelines

---

# 🧠 Deployed Systems

---

## 🔁 QueryPilot — Self-Correcting Text-to-SQL Agent
**Multi-agent LLM system with schema-aware retrieval & bounded correction**

🔗 Repo: https://github.com/parthtiwari-dev/querypilot  
🌐 Live API: https://querypilot-backend.onrender.com/docs  

**What it does**
- Converts natural language → executable SQL
- Uses schema-linking + retrieval filtering
- Bounded LangGraph-style correction loop
- Structured static validation before execution

**Evaluation**
- ~95% execution success (80-query benchmark)
- Cross-schema generalization testing
- Hallucination + correction lift metrics tracked

This is not prompt chaining.
It’s a controlled agent interacting with a database environment.

---

## 🛡️ UPI Fraud Detection Engine
**Real-time fraud decision system with strict temporal validation**

🔗 Repo: https://github.com/parthtiwari-dev/upi-fraud-engine  
🌐 API: https://upi-fraud-engine.onrender.com/docs  
🖥 UI: https://upi-fraud-engine.streamlit.app/

**Highlights**
- 482+ point-in-time features
- Strict leakage validation
- Offline ROC-AUC: ~0.895
- <500ms inference latency
- Alert budget constraint: ≤0.5%

Includes:
- Temporal split with delay simulation
- Training-serving drift analysis
- Day-by-day backtesting

Built like a real payment system, not a Kaggle model.

---

## 🧬 Evidence-Bound Drug RAG
**Hybrid retrieval medical knowledge system with controlled refusal**

🔗 Repo: https://github.com/parthtiwari-dev/Evidence-Bound-Drug-RAG  
🌐 Live API: https://evidence-bound-drug-rag.streamlit.app/  
🤗 HF Space: https://huggingface.co/spaces/parthtiwar1/drug-rag-api  

**Architecture**
- 20 FDA/NICE documents
- 853 semantic chunks
- Hybrid search (vector + BM25)
- Citation-grounded generation

**Evaluation**
- RAGAS Score: ~0.71
- Faithfulness: ~0.80
- 100% refusal accuracy on unsupported queries

Designed to reduce hallucination in high-risk domains.

---

# 🏗 Engineering Philosophy

> AI systems are non-deterministic.  
> Reliability must be engineered — not assumed.

I focus on:

- Measuring before optimizing  
- Designing for adversarial failure  
- Enforcing validation layers  
- Tracking regressions across versions  
- Building systems that survive distribution shift  

---

# 🛠 Core Stack

**Languages**  
Python, SQL  

**LLM / GenAI**  
RAG, LangGraph-style orchestration, Tool-calling workflows, Hybrid retrieval  

**ML & Modeling**  
XGBoost, Feature Engineering, Drift Analysis, Evaluation Harnesses  

**Infra & Systems**  
FastAPI, Docker, PostgreSQL, DuckDB, Chroma, CI-driven testing  

---

# 📊 System Metrics Snapshot

| System | Key Metric |
|--------|------------|
| QueryPilot | ~95% SQL execution success |
| Fraud Engine | ROC-AUC ~0.895 |
| Drug RAG | Faithfulness ~0.80 |

---

# 🛰 Currently Exploring

- Agentic AI at scale
- Evaluation frameworks for non-deterministic systems
- Reinforcement-inspired improvement loops
- Latency-sensitive AI deployment

---

<div align="center">

### 🧠 Building AI that survives reality.

[LinkedIn](https://www.linkedin.com/in/parth-tiwar1) • 
[GitHub](https://github.com/parthtiwari-dev)

</div>
