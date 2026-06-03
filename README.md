```
██████╗  █████╗ ██████╗ ████████╗██╗  ██╗    ████████╗██╗██╗    ██╗ █████╗ ██████╗ ██╗
██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██║  ██║    ╚══██╔══╝██║██║    ██║██╔══██╗██╔══██╗██║
██████╔╝███████║██████╔╝   ██║   ███████║       ██║   ██║██║ █╗ ██║███████║██████╔╝██║
██╔═══╝ ██╔══██║██╔══██╗   ██║   ██╔══██║       ██║   ██║██║███╗██║██╔══██║██╔══██╗██║
██║     ██║  ██║██║  ██║   ██║   ██║  ██║       ██║   ██║╚███╔███╔╝██║  ██║██║  ██║██║
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝       ╚═╝   ╚═╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝
```

<div align="center">

[![Typing SVG](https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=700&size=18&duration=2800&pause=1000&color=00E5FF&center=true&vCenter=true&width=760&lines=AI+Systems+Engineer+%E2%80%94+Bengaluru%2C+India;Evidence-bound.+Failure-aware.+Deployed.;I+don't+ship+wrappers.+I+ship+evaluated+systems.;9+systems+mapped+inside+EVIDENCEBOUND.)](https://git.io/typing-svg)

<br/>

[![Portfolio](https://img.shields.io/badge/Portfolio-EVIDENCEBOUND-00e5ff?style=for-the-badge)](https://parth-tiwari-1.vercel.app/)
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
[✓] philosophy        →  evidence before claims
[✓] vibe-coding       →  NOT DETECTED
[✓] evaluation        →  ACTIVE
[✓] evidence systems  →  9 mapped in EVIDENCEBOUND
[✓] current build     →  SecondSelf
[✓] work node         →  Stick and Dot  (AI/ML Intern)

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
fix:    leakage validation, point-in-time enforcement, rebuilt from scratch
result: precision stayed useful under a real alert budget
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
model_id         : parth-tiwari-v2
type             : early-career AI systems engineer
architecture     : first-principles → build → evaluate → break → fix → deploy
training_data    : production constraints, real failure modes, measurable outcomes

benchmarks:
  text_to_sql_execution_success  : 95.7%     # 82-query ecommerce benchmark
  cross_schema_generalization    : 100%      # zero-shot on unseen library schema
  syntactic_hallucination_rate   : 0.0%      # schema-grounded generation
  fraud_precision_in_budget      : 92.06%    # 0.5% daily alert constraint
  fraud_p95_latency              : ~386ms    # API scoring path
  medrag_answered_faithfulness   : ~0.99     # cited medical retrieval answers
  medrag_refusal_accuracy        : 100%      # insufficient evidence => refusal
  vivid_beta_users               : 10+       # creative AI work under Stick and Dot

serving:
  portfolio          : EVIDENCEBOUND — 9 evidence systems, same-world overlays
  deployment         : Docker · Render · Streamlit · HuggingFace · Vercel
  current_focus      : SecondSelf · evidence-bound career/application OS

known_limitations    : early-career · still learning · high ownership · ships with boundaries
```

<br/>

---

<br/>

## ◈ &nbsp; DEPLOYED SYSTEMS

> Featured below: 3 public systems. Full map: [EVIDENCEBOUND](https://parth-tiwari-1.vercel.app/) — 9 nodes across personal projects, work evidence, current builds, and tooling.

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

  transactions → point-in-time features → leakage tests → alert-budget model
  train/serve drift surfaced → rebuilt → re-tested under real decision constraints
```

| Metric | Result | Context |
|--------|--------|---------|
| Precision in alert budget | `92.06%` | Only flags what matters |
| P95 latency | `~386ms` | API scoring path |
| Leakage tests | `55+` | Temporal integrity checks |
| Backtest mode | `day-by-day` | Production-like replay |

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
  ├── every claim needs source evidence
  ├── insufficient evidence must trigger refusal, not a guess
  └── faithfulness is measured, not assumed

  FDA + NICE PDFs → semantic chunks → retrieval → citation → refusal policy
```

| Metric | Result | Context |
|--------|--------|---------|
| Answered faithfulness | `~0.99` | Claims grounded in source |
| Refusal accuracy | `100%` | Unsupported requests refused |
| Eval cost | `$0.168` | Cost-aware evaluation |
| Boundary | `non-diagnostic` | Not medical advice |

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

> *This is how suspicious metrics become trustworthy.*
> *This is how a metric bug gets caught before it becomes a product lie.*
> *This is how a smaller system with gates beats a bigger prompt with vibes.*

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
![Vue](https://img.shields.io/badge/Vue-42B883?style=for-the-badge&logo=vue.js&logoColor=white)
![Three.js](https://img.shields.io/badge/Three.js-111111?style=for-the-badge&logo=three.js&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)

</div>

<br/>

---

<br/>

## ◈ &nbsp; STATS

<div align="center">

<img height="175em" alt="Parth Tiwari GitHub stats" src="https://github-readme-stats.vercel.app/api?username=parthtiwari-dev&show_icons=true&hide_border=true&bg_color=0d1117&title_color=00e5ff&icon_color=4fc3f7&text_color=a0d4ff&include_all_commits=true&rank_icon=github&cache_seconds=21600"/>
<img height="175em" alt="Most used languages" src="https://github-readme-stats.vercel.app/api/top-langs/?username=parthtiwari-dev&layout=compact&hide_border=true&bg_color=0d1117&title_color=00e5ff&text_color=a0d4ff&langs_count=6&cache_seconds=21600"/>

</div>

<div align="center">

<img alt="GitHub contribution streak" src="https://streak-stats.demolab.com?user=parthtiwari-dev&hide_border=true&background=0d1117&ring=00e5ff&fire=4fc3f7&currStreakLabel=00e5ff&sideLabels=a0d4ff&dates=4a6fa5&sideNums=00e5ff&currStreakNum=4fc3f7"/>

</div>

<div align="center">

<img alt="GitHub activity graph" src="https://github-readme-activity-graph.vercel.app/graph?username=parthtiwari-dev&bg_color=0d1117&color=4fc3f7&line=00e5ff&point=ffffff&area=true&hide_border=true&area_color=001428&custom_title=Contribution%20Graph&radius=8" width="95%"/>

</div>

<br/>

---

<br/>

<div align="center">

[![Typing SVG](https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=700&size=22&duration=3000&pause=1200&color=00E5FF&center=true&vCenter=true&width=820&repeat=1&lines=AI+Systems+Engineer+%7C+Bengaluru+India+%7C+Remote+OK;Evidence-driven.+Production-aware.+No+wrapper+theatre.;Open+to+roles+India+wide+-+systems+that+WORK.)](https://git.io/typing-svg)

<br/>

[![Portfolio](https://img.shields.io/badge/View%20Portfolio-EVIDENCEBOUND-00e5ff?style=for-the-badge)](https://parth-tiwari-1.vercel.app/)
&nbsp;
[![LinkedIn](https://img.shields.io/badge/Let's%20Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/parth-tiwar1)
&nbsp;
[![Email](https://img.shields.io/badge/Hire%20Me-Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:parthti2003@gmail.com)

</div>

<br/>

```
$ ./parth --shutdown

[saving state]   ✓  9 evidence systems mapped
[saving state]   ✓  3 featured systems public
[saving state]   ✓  all evaluation harnesses active
[saving state]   ✓  open to the right problem

[goodbye]  see you on the other side of the next PR.
```
