# Parth Tiwari

**I make AI features safe to ship** — RAG, agents and models that know when they're wrong, with the evaluation harness that proves it.

AI systems engineer in Bengaluru, India. Remote. **Currently taking on 1–2 freelance projects**, and open to full-time roles.

[![Portfolio](https://img.shields.io/badge/Portfolio-EVIDENCEBOUND-00e5ff?style=flat-square)](https://parth-tiwari-1.vercel.app/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/parth-tiwar1)
[![Email](https://img.shields.io/badge/parthti2003@gmail.com-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:parthti2003@gmail.com)

---

## Work with me

Most teams ship an LLM feature and then discover they have no idea whether it is getting better or worse. That is the problem I solve.

| | What you get | Timeline | From |
|---|---|---|---|
| **Reliability audit** | I take your RAG or agent, build a real evaluation set against it, and hand you a report: where it fails, how often, and what each fix is worth. | 1 week | $500 |
| **Eval harness + fixes** | The harness above, wired into CI, plus the failures it surfaces actually fixed. | 2–4 weeks | $1,500 |
| **Retainer** | Ongoing evaluation, regression monitoring and iteration as your system and your data drift. | monthly | $1,000/mo |

**Bring me:** a chatbot that makes things up · a text-to-SQL feature you can't trust with a real schema · a model that looked good in the notebook and died in production · an LLM pipeline nobody has ever measured.

📧 **[parthti2003@gmail.com](mailto:parthti2003@gmail.com)** — tell me what's failing and I'll tell you, free, whether I think I can fix it.

---

## Selected work

### BeatMind — AI music generation and dissection
**[beatmind.tech](https://www.beatmind.tech)** · production, real users · *private repo, walkthrough on request*

Upload a track and it comes back as an editable arrangement: separated stems, detected structure, per-section fragments you can regenerate, repaint and mix down. Built and run solo.

- **~95,000 lines** across a Next.js app on Vercel and **four Python workers on Modal** — generation, separation and analysis on GPU, render on CPU
- Real audio ML in the pipeline: **BS-RoFormer** vocals, **htdemucs_ft** drums/bass, **all-in-one-fix** structure, **essentia** key, **madmom** chords
- A fenced, webhook-driven job state machine with dispatch attempt tokens, a reconciler cron and idempotent at-least-once callbacks — because GPU containers are cold, slow and allowed to fail
- Measured rather than assumed: benchmarked L40S vs A100 vs H100 on a pinned seed and **declined the upgrade** — L40S was both cheaper and faster, and diffusion turned out to be 0.42s of a 16.3s pipeline

### [QueryPilot](https://github.com/parthtiwari-dev/querypilot) — self-correcting text-to-SQL agent
[Live API](https://querypilot-backend.onrender.com/docs) · `Python` `LangGraph` `FastAPI` `ChromaDB` `PostgreSQL` `Docker`

Natural language → schema-aware retrieval → SQL → static validation → a three-stage self-correction loop before anything executes.

| First-attempt success | After self-correction | Invented tables/columns | Unseen schema, zero tuning |
|---|---|---|---|
| 90.0% | **95.7%** | 0 | generalised |

*Measured on an 82-query e-commerce benchmark; generalisation tested zero-shot on a separate library schema.*

### [UPI Fraud Engine](https://github.com/parthtiwari-dev/upi-fraud-engine) — real-time fraud decisioning
[Live API](https://upi-fraud-engine.onrender.com/docs) · [Live UI](https://upi-fraud-engine.streamlit.app/) · `Python` `XGBoost` `FastAPI` `DuckDB` `Great Expectations`

Built under the constraints a real fraud desk actually has: score at time *T* using only pre-*T* features, stay inside a **0.5% daily alert budget**, and survive delayed fraud labels.

| Precision within alert budget | P95 scoring latency | Temporal leakage tests | Backtest |
|---|---|---|---|
| **92.06%** | ~386ms | 55+ | day-by-day replay |

### [Evidence-Bound Drug RAG](https://github.com/parthtiwari-dev/Evidence-Bound-Drug-RAG) — medical retrieval that refuses
[Live app](https://evidence-bound-drug-rag.streamlit.app/) · [HuggingFace Space](https://huggingface.co/spaces/parthtiwar1/drug-rag-api) · `FastAPI` `ChromaDB` `LangChain` `RAGAS`

FDA and NICE source documents, where a hallucination is patient harm. Every claim carries its citation, and insufficient evidence triggers a refusal instead of a guess.

| Answered faithfulness | Refusal on unsupported queries | Full eval cost | Scope |
|---|---|---|---|
| ~0.99 | correct | $0.168 | non-diagnostic, not medical advice |

---

## How I find things other people ship

I build the evaluation harness before I trust the system. Three times that has caught something that would have shipped as a lie.

**A fraud model that was lying to itself.**
```
train ROC-AUC   0.895     looked great
production ROC  0.60      temporal features had bled future signal into past training windows
```
Fixed with point-in-time enforcement and 55+ leakage tests, then rebuilt from scratch. Precision held up under a real alert budget.

**A hallucination rate of 100% that was a bug in the metric, not the system.**
`schema_tables_used` was returning `["schema_dict", "tables"]` — dict keys, not table names. Actual rate: 0%. A one-line patch. I only found it because I had written a hallucination detector in the first place.

**An LLM answering a revenue question with `SELECT SUM(amount) FROM fines`.**
Two schemas were sharing one Chroma collection and the embeddings leaked across them. Fixed with prompt isolation and schema-scoped retrieval, then the full 82-query benchmark was re-run rather than spot-checked.

```diff
- ship it because it works on my machine
+ define "working" → build the harness → break it on purpose → fix → measure again → ship
```

---

## Stack

**Core** Python · FastAPI · PostgreSQL · Docker
**AI/ML** LangGraph · LangChain · RAG · ChromaDB · RAGAS · XGBoost · PyTorch audio models
**Infra** Modal (GPU) · Vercel · Render · GitHub Actions · Neon · R2
**Frontend** TypeScript · Next.js · Vue · Three.js

Also: AI/ML intern at **Stick and Dot**, where I build [Vivid](https://parth-tiwari-1.vercel.app/) — creative AI tooling now in beta with real users.

---

<div align="center">

**Something in your AI stack you can't measure?**

[**Email me**](mailto:parthti2003@gmail.com) · [Portfolio](https://parth-tiwari-1.vercel.app/) · [LinkedIn](https://www.linkedin.com/in/parth-tiwar1)

</div>
