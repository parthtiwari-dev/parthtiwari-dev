<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venom&color=0:000000,50:0a0a1a,100:000d1f&height=280&section=header&text=PARTH%20TIWARI&fontSize=78&fontColor=00e5ff&fontAlignY=45&desc=AI%20Systems%20Engineer%20%E2%80%93%20Bengaluru%2C%20India&descSize=20&descAlignY=67&descColor=4fc3f7&animation=fadeIn&stroke=00e5ff&strokeWidth=1" width="100%"/>

<br/>

[![Typing SVG](https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=700&size=20&duration=2800&pause=1000&color=00E5FF&center=true&vCenter=true&width=750&lines=I+don't+call+APIs+and+claim+to+be+an+AI+Engineer.;I+build+systems+that+survive+production.;Evaluation-driven.+Failure-aware.+Deployed.;From+first+principles+%E2%80%94+always.)](https://git.io/typing-svg)

<br/>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/parth-tiwar1)
[![Email](https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:parthti2003@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-171515?style=for-the-badge&logo=github&logoColor=white)](https://github.com/parthtiwari-dev)
![Profile Views](https://komarev.com/ghpvc/?username=parthtiwari-dev&style=for-the-badge&color=00e5ff&label=PROFILE+VIEWS)

</div>

---

<br>

## ◈ &nbsp; WHO I AM

> *Most AI engineers are prompt wrappers. Here's what's different.*

```diff
@@  diff --git a/generic-ai-engineer b/parth-tiwari  @@

- calls LLM API, ships demo, calls it production
+ builds evaluation harness before writing first line of model code

- RAG app with no faithfulness score
+ RAG system benchmarked on 20 structured queries, RAGAS measured, logged

- ML model trained and deployed, drift discovered in prod
+ day-by-day backtester exposed 0.895→0.60 drift before it ever deployed

- "the agent works" (tested once on happy path)
+ 95.7% execution success across 82-query benchmark with self-correction loop

- features engineered, leakage not checked
+ 20+ temporal integrity tests, zero leakage baked in by design

- "I use LLMs to build AI"
+ I use first principles to build systems. LLMs are one component.
```

```
  Location  ›  Bengaluru, India
  Status    ›  Open to AI Engineer roles
  Signal    ›  Systems that ship > slides that pitch
```

<br>

---

<br>

## ◈ &nbsp; DEPLOYED SYSTEMS &nbsp; *(click → live)*

> Every project below is running right now. Not on my laptop. On the internet. With real constraints.

<br>

---

### ⚡ &nbsp; [QUERYPILOT](https://github.com/parthtiwari-dev/querypilot) &nbsp;·&nbsp; Self-Correcting Text-to-SQL Agent

<div align="center">

[![Live API](https://img.shields.io/badge/LIVE%20API-DOCS-00e5ff?style=for-the-badge&logo=fastapi)](https://querypilot-backend.onrender.com/docs)
[![Code](https://img.shields.io/badge/SOURCE-CODE-1a1a2e?style=for-the-badge&logo=github)](https://github.com/parthtiwari-dev/querypilot)

</div>

```
╔══════════════════════════════════════════════════════════════════╗
║  Natural Language ──► Schema-Aware RAG ──► SQL Generation        ║
║                           │                                       ║
║                    Static Validation                              ║
║                           │                                       ║
║              ┌────────────┼────────────┐                          ║
║         Regex Repair   LLM Fix    Execution                       ║
║              └────────────┴────────────┘                          ║
║                    Self-Correction Loop                           ║
╚══════════════════════════════════════════════════════════════════╝
```

| Metric | Score | What it means |
|--------|-------|---------------|
| **First-attempt execution success** | `90.0%` | SQL ran correctly on first try |
| **After self-correction** | `95.7%` | 3-stage loop caught and fixed the rest |
| **Syntactic hallucination rate** | `0.0%` | Zero made-up columns or tables |
| **Cross-schema generalization** | `100%` | Zero tuning on a brand-new library schema |
| **Cold-start reduction** | `~400ms` | Per-schema agent caching |

> Built with: `Python` `FastAPI` `LangGraph` `Groq/OpenAI` `ChromaDB` `PostgreSQL` `Docker` `GitHub Actions`

<br>

---

### 🛡 &nbsp; [UPI FRAUD ENGINE](https://github.com/parthtiwari-dev/upi-fraud-engine) &nbsp;·&nbsp; Real-Time Fraud Decision System

<div align="center">

[![Live API](https://img.shields.io/badge/LIVE%20API-DOCS-00e5ff?style=for-the-badge&logo=fastapi)](https://upi-fraud-engine.onrender.com/docs)
[![Live UI](https://img.shields.io/badge/LIVE%20UI-APP-4fc3f7?style=for-the-badge&logo=streamlit)](https://upi-fraud-engine.streamlit.app/)
[![Code](https://img.shields.io/badge/SOURCE-CODE-1a1a2e?style=for-the-badge&logo=github)](https://github.com/parthtiwari-dev/upi-fraud-engine)

</div>

```
╔══════════════════════════════════════════════════════════════════╗
║  CONSTRAINT: Score transaction at T using only pre-T data        ║
║  CONSTRAINT: ≤0.5% daily alert budget — precision is everything  ║
║  CONSTRAINT: Delayed fraud labels — no peeking into the future   ║
╠══════════════════════════════════════════════════════════════════╣
║  590K transactions → 480+ point-in-time features                 ║
║  DuckDB + online feature store → temporal integrity enforced     ║
║  Day-by-day backtesting exposed 0.895→0.60 train/serve drift     ║
║  A/B selected: XGBoost vs two-stage ensemble under real budget   ║
╚══════════════════════════════════════════════════════════════════╝
```

| Metric | Score | What it means |
|--------|-------|---------------|
| **ROC-AUC (offline)** | `0.895` | Strong discriminative power |
| **Precision within alert budget** | `92%` | Only flags what matters |
| **P95 inference latency** | `<500ms` | Production SLA enforced |
| **Leakage validation tests** | `20+` | Temporal integrity proven, not assumed |
| **Modeled fraud savings** | `₹21.6 Cr/yr` | Stakes are real |

> Built with: `Python` `XGBoost` `FastAPI` `DuckDB` `Pydantic` `Great Expectations` `Docker`

<br>

---

### 🧬 &nbsp; [EVIDENCE-BOUND DRUG RAG](https://github.com/parthtiwari-dev/Evidence-Bound-Drug-RAG) &nbsp;·&nbsp; Medical Knowledge Retrieval

<div align="center">

[![Live App](https://img.shields.io/badge/LIVE%20APP-STREAMLIT-00e5ff?style=for-the-badge&logo=streamlit)](https://evidence-bound-drug-rag.streamlit.app/)
[![HuggingFace](https://img.shields.io/badge/HUGGINGFACE-SPACE-4fc3f7?style=for-the-badge&logo=huggingface)](https://huggingface.co/spaces/parthtiwar1/drug-rag-api)
[![Code](https://img.shields.io/badge/SOURCE-CODE-1a1a2e?style=for-the-badge&logo=github)](https://github.com/parthtiwari-dev/Evidence-Bound-Drug-RAG)

</div>

```
╔══════════════════════════════════════════════════════════════════╗
║  CONSTRAINT: Medical domain — hallucination is not acceptable    ║
║  CONSTRAINT: Every claim needs a citation. Full stop.            ║
╠══════════════════════════════════════════════════════════════════╣
║  FDA + NICE PDFs → 853 semantic chunks → Hybrid retrieval        ║
║  Vector + BM25 fusion → domain-aware filtering                   ║
║  RAGAS benchmark: 20 structured queries, measured, logged        ║
║  Adversarial queries trigger controlled refusal — not guesses    ║
╚══════════════════════════════════════════════════════════════════╝
```

| Metric | Score | What it means |
|--------|-------|---------------|
| **RAGAS Faithfulness** | `0.80` | 80% of claims grounded in source |
| **Overall RAGAS Score** | `0.71` | Holistic quality measured, not assumed |
| **Eval cost** | `$0.168` | Cost-aware — not burning tokens blindly |
| **Out-of-scope refusal** | `Controlled` | Hallucination suppressed by design |

> Built with: `Python` `FastAPI` `ChromaDB` `SentenceTransformers` `LangChain` `Groq` `Streamlit` `RAGAS`

<br>

---

<br>

## ◈ &nbsp; ENGINEERING PHILOSOPHY

<div align="center">

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│   "Non-deterministic systems demand deterministic discipline."      │
│                                                                     │
│    Most AI engineers:      │    How I build:                        │
│    ─────────────────────   │    ─────────────────────────           │
│    Vibe until it works     │    Define success metrics first        │
│    Skip evaluation         │    Build evaluation harnesses          │
│    Ship, hope for best     │    Expose drift before production      │
│    LLM call = AI Engineer  │    System design = AI Engineering      │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

</div>

<br>

**What I obsess over:**

🔬 &nbsp; **Evaluation harnesses** — if you can't measure it, you're guessing &nbsp;&nbsp;&nbsp; 🧪 &nbsp; **Leakage-safe validation** — temporal integrity is non-negotiable

📉 &nbsp; **Drift detection** — train/serve gap will haunt you &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ⏱ &nbsp; **Latency budgets** — real systems have SLAs

🔁 &nbsp; **Bounded agent loops** — autonomy without guardrails is chaos &nbsp;&nbsp; 🧱 &nbsp; **First principles** — understand the system, don't just assemble it

<br>

---

<br>

## ◈ &nbsp; TECH STACK

<div align="center">

**Core**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=postgresql&logoColor=white)

**ML & AI**

![XGBoost](https://img.shields.io/badge/XGBoost-FF6600?style=for-the-badge&logo=xgboost&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-000000?style=for-the-badge&logo=langgraph&logoColor=00e5ff)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

**RAG & Retrieval**

![ChromaDB](https://img.shields.io/badge/ChromaDB-FF6B6B?style=for-the-badge&logo=chromadb&logoColor=white)
![SentenceTransformers](https://img.shields.io/badge/Sentence_Transformers-FF9900?style=for-the-badge&logo=huggingface&logoColor=white)

**Infrastructure**

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![DuckDB](https://img.shields.io/badge/DuckDB-FFF000?style=for-the-badge&logo=duckdb&logoColor=black)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

</div>

<br>

---

<br>

## ◈ &nbsp; GITHUB STATS

<div align="center">

<img height="180em" src="https://github-readme-stats.vercel.app/api?username=parthtiwari-dev&show_icons=true&theme=chartreuse-dark&hide_border=true&bg_color=000d1f&title_color=00e5ff&icon_color=4fc3f7&text_color=a0d4ff&include_all_commits=true&count_private=true"/>
<img height="180em" src="https://github-readme-stats.vercel.app/api/top-langs/?username=parthtiwari-dev&layout=compact&theme=chartreuse-dark&hide_border=true&bg_color=000d1f&title_color=00e5ff&text_color=a0d4ff&langs_count=6"/>

</div>

<div align="center">

<img src="https://github-readme-streak-stats.herokuapp.com?user=parthtiwari-dev&theme=dark&hide_border=true&background=000d1f&ring=00e5ff&fire=4fc3f7&currStreakLabel=00e5ff&sideLabels=a0d4ff&dates=4a6fa5&sideNums=00e5ff&currStreakNum=4fc3f7" alt="GitHub Streak"/>

</div>

<div align="center">

<img src="https://github-readme-activity-graph.vercel.app/graph?username=parthtiwari-dev&bg_color=000d1f&color=4fc3f7&line=00e5ff&point=ffffff&area=true&hide_border=true&area_color=001428" alt="Activity Graph" width="95%"/>

</div>

<br>

---

<br>

<div align="center">

[![Typing SVG](https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=700&size=18&duration=3500&pause=1200&color=4FC3F7&center=true&vCenter=true&width=700&lines=Open+to+AI+Engineer+roles.;Let%27s+build+something+that+actually+works.;Hit+the+LinkedIn.+Send+the+email.+Let%27s+talk.)](https://git.io/typing-svg)

<br>

[![LinkedIn](https://img.shields.io/badge/Let's%20Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/parth-tiwar1)
&nbsp;&nbsp;
[![Email](https://img.shields.io/badge/Hire%20Me-Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:parthti2003@gmail.com)

</div>

<br>

```
┌─────────────────────────────────────────────────────────────────────────┐
│                                                                         │
│   $ ./parth --status                                                    │
│                                                                         │
│   > systems    : deployed and running                                   │
│   > open to    : the right AI Engineer role                             │
│   > contact    : linkedin  ·  email                                     │
│   > philosophy : build systems, not demos                               │
│                                                                         │
│   ready to build something that survives reality?  let's talk.          │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```
