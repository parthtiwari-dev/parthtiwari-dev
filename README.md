<div align="center">

<a href="https://parth-tiwari-1.vercel.app/"><img alt="Parth Tiwari. I build whole products. Open to roles. Full-Stack Lead AI Developer (contract) at Stick and Dot, building Kanata." src="assets/hero.svg" width="100%"></a>

**[Portfolio](https://parth-tiwari-1.vercel.app/)** &nbsp;·&nbsp; **[Kanata](https://kanata.studio)** &nbsp;·&nbsp; **[LinkedIn](https://www.linkedin.com/in/parth-tiwar1)** &nbsp;·&nbsp; **[Email](mailto:parthti2003@gmail.com)**

<sub>Full-Stack Lead AI Developer (contract) at Stick and Dot, since July 2026. Building Kanata. Open to roles and opportunities.</sub>

<img alt="Live check of five things I have shipped, redrawn once a day." src="assets/status.svg" width="100%">

</div>

<br>

<div align="center">

<a href="https://www.beatmind.tech"><img alt="BeatMind. A track is split into vocals, drums, bass and other stems, and one section of one stem is repainted." src="assets/p01-beatmind.svg" width="100%"></a>

</div>

An AI music workspace, built for Stick and Dot. Upload a track and it separates the stems and reads the tempo, key, chords and structure, then slices it into a library you can rebuild from. Or describe a track and generate one. Solo build, 24 days, 307 commits, 180 users as of 2026-10-23. Next.js on Vercel, four Python GPU services on Modal. Private repo.

<br>

<div align="center">

<a href="https://vivid-alpha.vercel.app"><img alt="Vivid. A script is typed out, six storyboard frames fill in, and each is checked so the same face carries through every shot." src="assets/p02-vivid.svg" width="100%"></a>

</div>

An LLM plans the shots, FLUX.2 draws them, and CLIP and ArcFace check that each shot matches the script and that the faces stay the same person. It runs on a LoRA I trained myself, with an eval harness that measures every change. Alpha.

<br>

<div align="center">

<img alt="Arrivo. Cars glide into parking bays. It runs on Android phones and is not in the app stores yet." src="assets/p03-arrivo.svg" width="100%">

</div>

Designed and built in 17 days for an airport car-park operator. React Native and Expo, a Hono API, Neon Postgres. It runs on Android phones and is not in the app stores yet (October 2026).

<br>

<div align="center">

<a href="https://kanata.studio"><img alt="Kanata, 彼方, far beyond. A design and engineering studio. A sun rises over a horizon." src="assets/p04-kanata.svg" width="100%"></a>

</div>

*Kanata* (彼方) is Japanese for "far beyond": what lies past the horizon. It is the studio I'm building: beautiful software with serious engineering underneath. It designs and builds apps and AI products, and shows the numbers behind every build. Early days.

<br>

<div align="center">

<img alt="My year as a beat. 1,965 GitHub contributions over twelve months drawn as a step sequencer; a playhead sweeps across and lights each active day." src="assets/p07-year.svg" width="100%">

<img alt="Night shift. A 24-hour clock of when I commit. 38% of commits on BeatMind and Arrivo land between midnight and 6 am." src="assets/p08-night.svg" width="100%">

</div>

<br>

<div align="center">

<img alt="What I got wrong. Six things I believed, then measured, and what I did about each." src="assets/p09-errata.svg" width="100%">

</div>

<details>
<summary><b>Read the errata as text</b></summary>

<br>

| Where | I believed | Then I measured | So I |
|---|---|---|---|
| **BeatMind**, GPU | The GPU was doing the work | It had silently fallen back to the CPU. One missing library, `libcublasLt.so.13` | Fixed it. About a minute became 23 seconds (two different tracks, so "about") |
| **BeatMind**, rights | A tick box saying "I own this" is enough | A checkbox is not a rights check | Deleted it. Export now needs a fingerprint match |
| **BeatMind**, billing, 2026-09-20 | Refunds on a downgrade were fair | They refunded cash for credits already spent | Found it fact-checking one sentence for a client. Fixed the same day |
| **Vivid**, speed | A "turbo" model, 5.9× cheaper, was a win | Faces got worse and people were duplicated | Did not ship it |
| **UPI Fraud Engine**, Jan 2026 | 0.9106 ROC-AUC, ready to go | A column that only existed in my synthetic data matched the label 100% | Removed it and retrained. 0.8953 is the honest number |
| **QueryPilot** | A hallucination rate of 100% | My detector was reading dictionary keys, not table names. The real rate was 0% | Fixed the detector |

</details>

<br>

<div align="center">

<table>
<tr>
<td width="50%"><a href="https://github.com/parthtiwari-dev/querypilot"><img alt="QueryPilot. 95.7% of 70 test questions answered correctly after self-correction." src="assets/c1-querypilot.svg" width="100%"></a></td>
<td width="50%"><a href="https://github.com/parthtiwari-dev/upi-fraud-engine"><img alt="UPI Fraud Engine. 92.06% of alerts were real fraud inside a 0.5% daily alert budget." src="assets/c2-upi.svg" width="100%"></a></td>
</tr>
<tr>
<td width="50%"><a href="https://github.com/parthtiwari-dev/Evidence-Bound-Drug-RAG"><img alt="Evidence-Bound Drug RAG. RAGAS faithfulness 0.80, refuses when the documents are silent." src="assets/c3-rag.svg" width="100%"></a></td>
<td width="50%"><a href="https://github.com/parthtiwari-dev/tathya"><img alt="Tathya. Sources from government, media and citizens cluster into one sourced case file. You decide." src="assets/c4-tathya.svg" width="100%"></a></td>
</tr>
</table>

</div>

<br>

<div align="center">

<a href="https://tabla-tuner.vercel.app"><img alt="Tabla Tuner. A tabla skin ripples when struck while a cents needle swings and settles on zero, in tune." src="assets/p05-tabla.svg" width="100%"></a>

</div>

I've played tabla for ten years and never once managed to tune it. Tuning is taught last, by ear, standing next to someone who knows, and my lessons stopped before we got there. So I built the tuner I needed. It runs in the browser, with no install, no account and no server, and the sound never leaves your phone. I wrote the pitch detector by hand, because ordinary tuners lock onto the wrong harmonic on a tabla. I was wrong about the design three times, and each fix deleted code. [Code](https://github.com/parthtiwari-dev/tabla-tuner).

<br>

<div align="center">

<a href="https://from-zero-to-mozart.vercel.app"><img alt="From Zero to Mozart. Notes of Ode to Joy light up one by one on a staff as a playhead passes. I just started the violin." src="assets/p06-mozart.svg" width="100%"></a>

</div>

I just started learning the violin. The course I'm learning from is a 193-page PDF, so I'm rebuilding it as a calm site I can read with the violin in my hands. Phase 0: planned and scaffolded, first lesson to come. [Code](https://github.com/parthtiwari-dev/from-zero-to-mozart).

<br>

<div align="center">

<a href="mailto:parthti2003@gmail.com"><img alt="Say hello. Open to roles and opportunities. parthti2003@gmail.com" src="assets/hello.svg" width="100%"></a>

<sub>Built with Claude Code and Codex. What to build, what to measure and what to throw away is my call. The art on this page is generated by the scripts in <a href="scripts">scripts/</a>.</sub>

</div>
