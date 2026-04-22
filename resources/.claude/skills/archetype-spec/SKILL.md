---
name: archetype-spec
description: "Scaffold a GUIDELINE.md + baseline build prompt for a new AI app by picking one of 7 UX archetypes. Use when student says 'archetype spec', 'scaffold app', 'tạo GUIDELINE', 'viết spec app', 'pick archetype', 'app em là archetype nào', 'bắt đầu app mới', 'generate starter spec', 'help me spec this app', 'chọn pattern cho app', 'UI template cho topic của em', or is at the blank-page moment before any code exists. Also trigger when a team has backend-only and is asking where to start on the frontend."
---

# Archetype Spec — From topic to GUIDELINE.md in 4 questions

Student has a topic and a backend plan, but no UI yet. Blank-page paralysis is the #1 reason teams ship ugly demos. This skill asks 4 questions, picks **one of 7 archetypes**, writes a `GUIDELINE.md` into the repo, and prints a **baseline build prompt** the student pastes into Claude Code to get a working skeleton.

The goal is to remove decisions, not add them. One archetype, one prompt, one working skeleton — in under 10 minutes.

## What this skill does

1. Asks 4 short questions (in Vietnamese by default) to narrow to one archetype
2. Writes `GUIDELINE.md` at repo root with archetype + T-C-R checklist
3. Prints a baseline prompt the student pastes into Claude Code
4. Tells the student what to expect and what to paste next (→ `/tcr-apply`)

## When to use it

- Team has backend agent working but no frontend
- Team is about to start a new repo and wants a paved path
- Team cloned a starter that doesn't match their topic and wants to re-spec

If the team already has UI code, route them to `/tcr-apply` instead — that skill retrofits T-C-R on existing code.

## The 7 archetypes

Same list as `/tcr-apply`. Keep names identical across skills so students memorize them.

1. **Chat + context panel** — conversation left, evidence panel right. AI TA, RAG chatbot, Socratic tutor, admissions.
2. **Upload → dashboard** — file in, structured insights out. Survey analysis, report summarizer, invoice extractor.
3. **Query → structured result** — NL question in, table/chart out. Text-to-SQL, digital twin Q&A, knowledge graph search.
4. **Wizard + inline audit** — multi-step form with AI checking each step. Syllabus generator, compliance-form builder, onboarding flow.
5. **Draft → approve → send** — AI drafts, human reviews + approves, system dispatches. Emergency comms, email assistant, scheduled announcements.
6. **Queue + approval** — batch of AI-labeled items, human clears the queue. Moderation, grading at scale, contract review.
7. **Real-time streaming** — live voice/video/text pipeline. Voice Q&A moderator, live transcription, streaming tutor.

### Meta-pattern — "Conversational UI + Evidence Panel"

Archetype 1 (Chat + panel) is secretly a meta-pattern: swap what the panel shows and it covers 5 other use cases:

- panel = **sources** → RAG chatbot
- panel = **progress** → long-running agent
- panel = **reasoning** → research / planning agent
- panel = **chart** → data Q&A
- panel = **queue** → inbox / approval

When in doubt between archetypes 1, 3, and 6, default to **1** and choose the panel payload. It ships faster and is the most transferable.

## Step 1: Ask 4 questions

Ask one at a time. Wait for each answer. Use Vietnamese with dấu by default; switch to English only if the student answers in English.

### Q1 — What does the user *give* the app? (input modality)

> **Câu 1:** User đưa gì cho app?
> a) Câu hỏi / tin nhắn (text ngắn)
> b) File (CSV, PDF, audio, ảnh)
> c) Form điền nhiều bước (nhập dần dần)
> d) Danh sách việc cần duyệt (bulk)
> e) Giọng nói / stream liên tục

Map: a → 1/3, b → 2, c → 4, d → 6, e → 7.

### Q2 — What does the user *get back*? (output shape)

> **Câu 2:** User nhận lại gì?
> a) Câu trả lời dạng text + nguồn / lập luận
> b) Bảng / biểu đồ / dashboard
> c) Bản nháp (email, tin nhắn, báo cáo) để sửa rồi gửi đi
> d) Danh sách items đã gán label (approve/reject từng cái)
> e) Output tiếp diễn theo thời gian thực

Map: a → 1, b → 2/3, c → 4/5, d → 6, e → 7.

### Q3 — Is the action *reversible* or *irreversible*?

> **Câu 3:** AI làm xong thì hành động đó có undo được không?
> a) Có — user chỉ đọc / xem (low stakes)
> b) Có nhưng tốn effort — user edit lại tốn thời gian (medium stakes)
> c) Không — gửi đi / xoá / trừ tiền / thông báo ra ngoài (high stakes)

If c → strongly prefer archetype 5 (draft → approve → send) even if Q1/Q2 suggest something else. High-stakes actions without a preview step is the #1 AI-app failure.

### Q4 — Single user, batch work, or multi-user roles?

> **Câu 4:** Ai dùng app?
> a) 1 user, 1 câu hỏi / 1 phiên làm việc
> b) 1 user nhưng cần xử lý hàng loạt (nhiều items)
> c) Nhiều role khác nhau (admin + end user, teacher + student)

Map: a → 1/2/3/7, b → 6, c → **ship one role first**, usually the end-user-facing one. If c, ask which role is demo day-facing — spec that one only.

## Step 2: Decide the archetype

Apply this priority (tie-breakers, top wins):

1. **Q3 = c (irreversible)** → archetype 5.
2. **Q4 = b (batch)** → archetype 6.
3. **Q1 = e or Q2 = e (streaming)** → archetype 7.
4. **Q1 = c (multi-step form)** → archetype 4.
5. **Q1 = b (file upload)** → archetype 2.
6. **Q1 = a + Q2 = b (question in, chart out)** → archetype 3.
7. **Q1 = a + Q2 = a (question in, text + sources out)** → archetype 1.
8. **Still ambiguous** → default to archetype 1 and set panel payload from Q2.

Tell the student the archetype + one-line reason. If the pick feels forced, offer the alternative: "Mình chọn 1 vì Q1+Q2 giống chat. Nhưng nếu em thấy workflow giống archetype 3 hơn (data Q&A), nói mình biết, mình sẽ đổi."

## Step 3: Write GUIDELINE.md

Write to `<repo-root>/GUIDELINE.md`. Overwrite if exists (warn first, show diff). Template:

```markdown
# GUIDELINE.md — {topic name}

## Archetype
**{archetype number}. {archetype name}**

Why this archetype: {1-2 lines tying Q1-Q4 answers to the pick}

{If archetype 1: add the "Conversational UI + Evidence Panel" note with suggested panel payload from Q2}

## User flow (in 3 steps)
1. User {does Q1 thing}
2. App {AI processing step — be concrete about what the LLM sees}
3. User {interacts with Q2 output}

## T-C-R checklist for this archetype

### T — Transparency (what AI work is visible)
- [ ] {archetype-specific T item 1}
- [ ] {archetype-specific T item 2}
- [ ] {archetype-specific T item 3}

### C — Control (what user can stop / edit / override)
- [ ] {archetype-specific C item 1}
- [ ] {archetype-specific C item 2}
- [ ] {archetype-specific C item 3}

### R — Recovery (validation + retry + undo)
- [ ] {archetype-specific R item 1}
- [ ] {archetype-specific R item 2}
- [ ] {archetype-specific R item 3}

## Stack (suggested, not mandated)
- Framework: {React+Vite | Next.js | Streamlit — pick what team is already comfortable with}
- LLM call: `src/llmService.js` (single file, swappable provider)
- State: component state is fine; add zustand/redux only if >3 screens
- Style: minimal — no design system dependency for week 1

## What NOT to build yet
- {thing that feels urgent but isn't — e.g., auth, persistent DB, complex routing}
- {another low-priority thing}
- Demo day cares about the core loop working end-to-end, not polish.

## Next step
Paste the baseline prompt into Claude Code (generated above). After skeleton works, run `/tcr-apply` to layer T-C-R onto it.
```

Fill the T-C-R checklist from the matrix in **"T-C-R matrix by archetype"** below. Don't invent — copy.

## Step 4: Print the baseline prompt

Print (do not write to a file) this prompt for the student to copy:

```
Read GUIDELINE.md. Build a {framework from GUIDELINE} skeleton for the archetype described there.

Scope:
- Single page / single screen — no routing yet
- Fake LLM responses (setTimeout + canned data) — real calls come later
- Include placeholder for src/llmService.js with TODO comment showing where to swap in real calls
- User-facing strings in Vietnamese with dấu
- Minimal CSS — readable, not polished

Do NOT add:
- Authentication
- Database / persistence
- Multi-page routing
- Any T-C-R features yet — those come in a separate prompt

Output: working skeleton I can run with `npm run dev` (or `streamlit run`). Show me the diff when done.
```

Then tell the student:

> Paste prompt này vào Claude Code ở repo root. Sau khi skeleton chạy được, chạy `/tcr-apply` để thêm T-C-R.

## T-C-R matrix by archetype

Use this to fill the checklist in `GUIDELINE.md`. Exact same items `/tcr-apply` emits — consistency matters.

### 1. Chat + context panel
- **T:** sources panel (2–4 refs), streaming status line, confidence dot (green/yellow/red)
- **C:** stop button during streaming, edit-last-user-message, Cmd+K clear chat
- **R:** error bubble with retry + report, thumbs-down on each assistant message

### 2. Upload → dashboard
- **T:** parse/extract/analyze progress panel, per-insight source link back to file
- **C:** cancel during processing, preview modal before analyze if file is large
- **R:** pre-flight file validation (type/size/non-empty), "try different file", keep-previous-file undo

### 3. Query → structured result
- **T:** collapsible "view SQL" panel, confidence badge on result, meta line (rows/ms/model)
- **C:** edit generated SQL before run, confirm modal for destructive queries, Enter/Esc shortcuts
- **R:** retry on fail, "rephrase question" button that feeds error back to LLM, query history

### 4. Wizard + inline audit
- **T:** per-field audit (✓/⚠/✗) with 1-line reason, end-of-wizard summary card
- **C:** back/forward without data loss, save draft to localStorage, override AI warning
- **R:** validate per step, don't block on audit fail, preview + edit before final submit

### 5. Draft → approve → send
- **T:** confidence score per section, recipient/subject/attachment preview, generation meta log
- **C:** mandatory preview step (no generate-and-send), edit any field, save-as-draft option
- **R:** "sent · undo" toast with 10s window, sent log with retry, keep draft on send failure

### 6. Queue + approval
- **T:** confidence dot per item, 1-line AI reasoning, header counts (pending/auto-approvable/low-conf)
- **C:** bulk select + shift-click range, keyboard (J/K/A/R/U), filter by confidence threshold
- **R:** undo stack of 10, "flag for review" instead of reject, re-surface on data update

### 7. Real-time streaming
- **T:** live status ("listening/transcribing/analyzing"), token-by-token output, latency meta bar
- **C:** stop button aborts stream, pause/resume for transcription, Space/Esc shortcuts
- **R:** auto-reconnect (max 3), preserve transcript buffer on reconnect, manual restart button

## Examples

### Example A: Text-to-SQL for tuition data

Q1: a (text question). Q2: b (chart). Q3: a (read-only). Q4: a (single user).

→ Q1+Q2 = query + chart → **archetype 3**.

`GUIDELINE.md` written with Query→result T-C-R checklist. Baseline prompt emitted for React+Vite skeleton.

### Example B: Emergency notifications to parents

Q1: c (form, draft message). Q2: c (draft to send). Q3: **c (irreversible — goes to Zalo/SMS)**. Q4: c (admin + parents).

→ Q3=c wins → **archetype 5** (draft → approve → send).

Warn: "Q4=c means 2 roles. Mình spec admin-facing trước vì demo day là admin duyệt + send. Parent view để sau."

### Example C: AI Teaching Assistant with sources + progress tracking

Q1: a (question). Q2: a (answer + sources) but also wants to show progress. Q3: a. Q4: a.

→ **archetype 1 (Chat + panel)**, panel payload = **sources + progress** (dual panel).

Note added to GUIDELINE: "Panel payload = sources (for this question) + progress bar (concepts mastered). This is the 'Conversational UI + Evidence Panel' meta-pattern."

## Anti-patterns — do NOT do these

- **Don't ask all 4 questions at once.** Ask one, wait, ask next. Students need to think.
- **Don't pick 2 archetypes.** Commit to one. "Hybrid" = confused students.
- **Don't write the full app.** Only `GUIDELINE.md` + the baseline prompt. Student runs the prompt in Claude Code — that's the learning moment.
- **Don't design the backend.** This skill is about UX archetype only. Assume backend exists or will be faked with setTimeout.
- **Don't add T-C-R features in the baseline prompt.** Baseline = skeleton. T-C-R = separate step via `/tcr-apply`. Keep the two phases distinct so students feel the pattern, not the soup.
- **Don't use English in user-facing strings.** Vietnamese with dấu. Code identifiers stay English.
- **Don't invent a new archetype.** If nothing fits, default to 1 and adjust panel payload. The 7 cover >95% of student topics.
- **Don't skip the "Why this archetype" line.** Students who can explain the pick will pick correctly next time without this skill.

## Principles

- **4 questions, 1 archetype, 1 GUIDELINE, 1 prompt.** Constraint is the feature.
- **Skeleton before T-C-R.** Never bundle the baseline build with T-C-R upgrades. Two phases, two prompts, two commits.
- **Pattern over framework.** The archetype picks the UX shape; the team picks React / Streamlit / whatever. Both answers are valid.
- **Vietnamese-first UX strings.** These students build for Vietnamese users.
- **Commit to the pick.** Ambiguous case → archetype 1 with adapted panel. Consistency across the class beats per-team perfection.
