```
██████╗  █████╗ ██████╗ ████████╗██╗  ██╗    ████████╗██╗██╗    ██╗ █████╗ ██████╗ ██╗
██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██║  ██║    ╚══██╔══╝██║██║    ██║██╔══██╗██╔══██╗██║
██████╔╝███████║██████╔╝   ██║   ███████║       ██║   ██║██║ █╗ ██║███████║██████╔╝██║
██╔═══╝ ██╔══██║██╔══██╗   ██║   ██╔══██║       ██║   ██║██║███╗██║██╔══██║██╔══██╗██║
██║     ██║  ██║██║  ██║   ██║   ██║  ██║       ██║   ██║╚███╔███╔╝██║  ██║██║  ██║██║
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝       ╚═╝   ╚═╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝
```

<div align="center">

[![Typing SVG](https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=700&size=18&duration=2800&pause=1000&color=00E5FF&center=true&vCenter=true&width=700&lines=AI+Systems+Engineer+%E2%80%94+Bengaluru%2C+India;Evaluation-driven.+Failure-aware.+Deployed.;I+don't+call+APIs+and+claim+engineering.;I+build+systems+that+survive+production.)](https://git.io/typing-svg)

<br/>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/parth-tiwar1)
[![Email](https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:parthti2003@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-171515?style=for-the-badge&logo=github&logoColor=white)](https://github.com/parthtiwari-dev)
![Views](https://komarev.com/ghpvc/?username=parthtiwari-dev&style=for-the-badge&color=00e5ff&label=PROFILE+VIEWS)

</div>

---

<br/>

## ◈ &nbsp; SYSTEM BOOT

```bash
$ initializing parth_tiwari.profile ...

[✓] identity          →  AI Systems Engineer
[✓] location          →  Bengaluru, India
[✓] status            →  open to the right problem
[✓] philosophy        →  first principles, not tutorials
[✓] vibe-coding       →  NOT DETECTED
[✓] evaluation        →  ACTIVE
[✓] systems deployed  →  3  (running right now, not on my laptop)
[✓] slides shipped    →  0

[READY] parth_tiwari.profile loaded successfully.
```

<br/>

---

<br/>

## ◈ &nbsp; WHO I AM &nbsp; *(told through what broke)*

> *Most profiles show you the wins. Here's what actually happened.*

<br/>

**Building a fraud engine. Backtesting revealed this:**

```
train ROC-AUC      →  0.895   ← model looked great
production ROC     →  0.60    ← system was lying to itself the whole time

cause:  temporal features bled future signal into past training windows
fix:    20+ leakage validation tests, point-in-time enforcement, rebuilt from scratch
result: 0.895 ROC-AUC that's actually trustworthy
```

**Shipped a Text-to-SQL agent. Hallucination detector reported 100% hallucination:**

```
hallucination_rate  →  100%   ← every query hallucinating?
actual rate         →  0%     ← the metric was wrong, not the system

cause:  schema_tables_used returned ["schema_dict", "tables"] — dict keys, not table names
fix:    one-line patch
lesson: I found this because I wrote a hallucination detector in the first place
```

**Deployed to Render. LLM mixed up two different databases:**

```
question  →  "what is the total revenue?"      (ecommerce schema)
sql       →  SELECT SUM(amount) FROM fines      (library schema — wrong database entirely)

cause:  both schemas lived in the same Chroma collection, embeddings leaked cross-schema
fix:    prompt isolation + schema-scoped retrieval + re-evaluated full 82-query benchmark
```

**The pattern:** I find these things because I build evaluation harnesses *before* I trust results.

```diff
- "it works on my machine" → ship it
+ measure → break it intentionally → fix it → measure again → then ship it
```

<br/>

---

<br/>

## ◈ &nbsp; MODEL CARD

```yaml
model_id         : parth-tiwari-v1
type             : AI Systems Engineer  (fresher)
architecture     : first-principles → build → evaluate → break → fix → deploy
training_data    : production constraints, real failure modes, measurable outcomes

benchmarks:
  text_to_sql_execution_success  : 95.7%   # 82-query ecommerce benchmark
  cross_schema_generalization    : 100%    # zero-shot on unseen library schema
  syntactic_hallucination_rate   : 0.0%    # schema-grounded generation
  fraud_roc_auc                  : 0.895   # 590K transactions, temporal integrity enforced
  fraud_precision_in_budget      : 92%     # ≤0.5% daily alert constraint
  rag_faithfulness_score         : 0.80    # RAGAS evaluated, 20-query medical benchmark
  rag_overall_score              : 0.71    # holistic, not cherry-picked

serving:
  fraud_p95_latency   : < 500ms
  sql_agent_p50       : ~2.3s
  deployment          : Docker · Render · Neon PostgreSQL · Streamlit · HuggingFace

known_limitations    : still a fresher  ·  will fix this with time
```

<br/>

---

<br/>

## ◈ &nbsp; DEPLOYED SYSTEMS

> Every link below is live. Not a demo. Not a notebook. A running service.

<br/>

---

### ⚡ &nbsp; [QUERYPILOT](https://github.com/parthtiwari-dev/querypilot) &nbsp;·&nbsp; Self-Correcting Text-to-SQL Agent

<div align="center">

[![Live API](https://img.shields.io/badge/LIVE%20API-DOCS-00e5ff?style=for-the-badge&logo=fastapi)](https://querypilot-backend.onrender.com/docs)
[![Source](https://img.shields.io/badge/SOURCE-CODE-1a1a2e?style=for-the-badge&logo=github)](https://github.com/parthtiwari-dev/querypilot)

</div>

```
  Natural Language
        │
        ▼
  Schema-Aware RAG  ──►  SQL Generator
                               │
                         Static Validator
                               │
               ┌───────────────┼───────────────┐
          Regex Repair       LLM Fix        Executor
               └───────────────┴───────────────┘
                        Self-Correction Loop
                           (max 3 attempts)
```

| Metric | Result | Context |
|--------|--------|---------|
| First-attempt success | `90.0%` | No correction, cold generation |
| After self-correction | `95.7%` | 3-stage loop on 82-query benchmark |
| Hallucination rate | `0.0%` | Zero invented tables or columns |
| Cross-schema generalization | `100%` | Library schema, zero domain tuning |
| Cold-start reduction | `~400ms` | Per-schema agent caching |

`Python` `LangGraph` `FastAPI` `ChromaDB` `PostgreSQL` `Docker` `GitHub Actions`

<br/>

---

### 🛡 &nbsp; [UPI FRAUD ENGINE](https://github.com/parthtiwari-dev/upi-fraud-engine) &nbsp;·&nbsp; Real-Time Fraud Decision System

<div align="center">

[![Live API](https://img.shields.io/badge/LIVE%20API-DOCS-00e5ff?style=for-the-badge&logo=fastapi)](https://upi-fraud-engine.onrender.com/docs)
[![Live UI](https://img.shields.io/badge/LIVE%20UI-APP-4fc3f7?style=for-the-badge&logo=streamlit)](https://upi-fraud-engine.streamlit.app/)
[![Source](https://img.shields.io/badge/SOURCE-CODE-1a1a2e?style=for-the-badge&logo=github)](https://github.com/parthtiwari-dev/upi-fraud-engine)

</div>

```
  HARD CONSTRAINTS (non-negotiable):
  ├── score transaction at T using only pre-T features   (no future leakage)
  ├── ≤ 0.5% daily alert budget                         (precision is everything)
  └── simulate delayed fraud labels                     (real-world label lag)

  590K transactions → 480+ point-in-time features → DuckDB feature store
  day-by-day backtest surfaced 0.895→0.60 train/serve drift → rebuilt
  A/B: XGBoost vs two-stage ensemble → winner selected under real budget
```

| Metric | Result | Context |
|--------|--------|---------|
| ROC-AUC | `0.895` | Offline, leakage-validated |
| Precision in alert budget | `92%` | Only flags what matters |
| P95 latency | `< 500ms` | Production SLA |
| Leakage tests | `20+` | Temporal integrity proven |
| Modeled fraud savings | `₹21.6 Cr/yr` | Stakes were real |

`Python` `XGBoost` `FastAPI` `DuckDB` `Great Expectations` `Docker`

<br/>

---

### 🧬 &nbsp; [EVIDENCE-BOUND DRUG RAG](https://github.com/parthtiwari-dev/Evidence-Bound-Drug-RAG) &nbsp;·&nbsp; Medical Knowledge Retrieval

<div align="center">

[![Live App](https://img.shields.io/badge/LIVE%20APP-STREAMLIT-00e5ff?style=for-the-badge&logo=streamlit)](https://evidence-bound-drug-rag.streamlit.app/)
[![HuggingFace](https://img.shields.io/badge/HUGGINGFACE-SPACE-4fc3f7?style=for-the-badge&logo=huggingface)](https://huggingface.co/spaces/parthtiwar1/drug-rag-api)
[![Source](https://img.shields.io/badge/SOURCE-CODE-1a1a2e?style=for-the-badge&logo=github)](https://github.com/parthtiwari-dev/Evidence-Bound-Drug-RAG)

</div>

```
  HARD CONSTRAINT: medical domain — hallucination is patient harm
  ├── every claim needs a citation source
  ├── adversarial queries must trigger refusal, not a guess
  └── faithfulness is measured, not assumed

  FDA + NICE PDFs → 853 semantic chunks → hybrid retrieval (vector + BM25)
  RAGAS benchmark: 20 structured queries → faithfulness 0.80, overall 0.71
  zero-score failure cases logged → retrieval + refusal logic refined
```

| Metric | Result | Context |
|--------|--------|---------|
| RAGAS Faithfulness | `0.80` | Claims grounded in source |
| Overall RAGAS Score | `0.71` | Holistic, 20-query eval |
| Eval cost | `$0.168` | Cost-aware, not burning tokens |
| Refusal behavior | `controlled` | Hallucination suppressed by design |

`Python` `FastAPI` `ChromaDB` `SentenceTransformers` `LangChain` `RAGAS` `Streamlit`

<br/>

---

<br/>

## ◈ &nbsp; HOW I ACTUALLY BUILD

```
step 1  →  define what "working" means before writing a single line
step 2  →  build the evaluation harness
step 3  →  write the system
step 4  →  break it intentionally  (adversarial inputs, edge cases, drift simulation)
step 5  →  fix what breaks
step 6  →  measure again
step 7  →  deploy with monitoring hooks
step 8  →  repeat when production proves you wrong
```

> *This is how 0.895 ROC-AUC became trustworthy instead of suspicious.*
> *This is how "100% hallucination" turned out to be a metric bug, not a model bug.*
> *This is how a 3-stage correction loop beat a bigger model with a better prompt.*

<br/>

---

<br/>

## ◈ &nbsp; STACK

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=postgresql&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-FF6600?style=for-the-badge&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-000000?style=for-the-badge&logoColor=00e5ff)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![ChromaDB](https://img.shields.io/badge/ChromaDB-FF6B6B?style=for-the-badge&logoColor=white)
![DuckDB](https://img.shields.io/badge/DuckDB-FFF000?style=for-the-badge&logo=duckdb&logoColor=black)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)

</div>

<br/>

---

<br/>

## ◈ &nbsp; STATS

<div align="center">

<img height="175em" src="https://github-readme-stats.vercel.app/api?username=parthtiwari-dev&show_icons=true&hide_border=true&bg_color=0d1117&title_color=00e5ff&icon_color=4fc3f7&text_color=a0d4ff&include_all_commits=true&count_private=true"/>
<img height="175em" src="https://github-readme-stats.vercel.app/api/top-langs/?username=parthtiwari-dev&layout=compact&hide_border=true&bg_color=0d1117&title_color=00e5ff&text_color=a0d4ff&langs_count=6"/>

</div>

<div align="center">

<img src="https://github-readme-streak-stats.herokuapp.com?user=parthtiwari-dev&hide_border=true&background=0d1117&ring=00e5ff&fire=4fc3f7&currStreakLabel=00e5ff&sideLabels=a0d4ff&dates=4a6fa5&sideNums=00e5ff&currStreakNum=4fc3f7"/>

</div>

<div align="center">

<img src="https://github-readme-activity-graph.vercel.app/graph?username=parthtiwari-dev&bg_color=0d1117&color=4fc3f7&line=00e5ff&point=ffffff&area=true&hide_border=true&area_color=001428" width="95%"/>

</div>

<br/>

---

<br/>

<div align="center">

[![Typing SVG](https://readme-typing-svg.demolab.com
?font=JetBrains+Mono
&weight=600
&size=20
&duration=2500
&pause=800
&color=4FC3F7
&center=true
&vCenter=true
&multiline=true
&width=700
&lines=Open+to+AI+Engineer+%2F+Software+Engineer+roles;Bengaluru%2C+Mumbai%2C+Delhi+NCR%2C+Pune%2C+Hyderabad+%2B+Remote;I+care+about+systems+that+work%2C+not+just+flashy+demos%3B+let%27s+talk.)
](https://git.io/typing-svg)


<br/>

[![LinkedIn](https://img.shields.io/badge/Let's%20Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/parth-tiwar1)
&nbsp;
[![Email](https://img.shields.io/badge/Hire%20Me-Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:parthti2003@gmail.com)

</div>

<br/>

```
$ ./parth --shutdown

[saving state]   ✓  3 systems deployed
[saving state]   ✓  all evaluation harnesses active
[saving state]   ✓  no hallucinations in production
[saving state]   ✓  open to the right problem

[goodbye]  see you on the other side of the next PR.
```
