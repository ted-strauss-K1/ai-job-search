# Search Queries for Job Scraper

## Installed portal CLIs (primary for `/scrape`)

`/scrape` discovers every portal skill under `.agents/skills/*/SKILL.md` and runs its CLI first. Shipped country-agnostic CLIs include `linkedin-search` and `freehire-search`; Danish demos and any skill you add with `/add-portal` are included the same way. You do **not** need a matching `site:` line below for those CLIs to run.

The `site:` query templates in this file are the **WebSearch fallback** — for portals without a CLI, company career pages, or when a CLI fails.

**Language scope:** write every query category in every language listed in your CLAUDE.md Languages table (typically 1-2, sometimes more). A posting requiring a language you have *not* declared, as a job condition, is excluded before scoring; a posting requiring a *higher level* than you declared in a language you *do* work in is flagged for your own judgment, not excluded — see `04-job-evaluation.md`'s Language Gate, the single source of truth for this rule. Translate each category's keywords rather than machine-translating word-for-word (e.g. "Frontend Developer" -> "Desarrollador Frontend", not a literal word-for-word translation) if you work in more than one language.

## Search Sites

Primary (Canadian job market — scaffold more with `/add-portal`):
- **linkedin.com/jobs** — LinkedIn job listings (filter: Montreal, Quebec, Canada or Remote); also covered by `linkedin-search` CLI
- **indeed.ca** — Indeed Canada (major general job board)
- **jobs.gc.ca** — Government of Canada job board (federal positions; highly relevant for Ted's profile)
- **workopolis.com** — Canadian job board
- **glassdoor.ca** — Job listings with company reviews

Secondary (sector-specific):
- **jobs.realventures.com** — Real Ventures (Montreal VC) portfolio-company job board, ~85 companies across Canada/US/international; covered by `realventures-search` CLI
- **alliancecan.ca/en/latest/careers** — Digital Research Alliance of Canada postings (direct HTML; #1 target)
- **careers.lassoinformatics.info/jobs** — Lasso Informatics (research data platform; ~10 openings, Study Operations roles fit). Covered by `lassoinformatics-search` CLI; fallback is `https://careers.lassoinformatics.info/api/postings` (public JSON, plain WebFetch/curl works, the HTML page is JS-rendered and returns nothing)
- **rimuhc.ca/careers** — RI-MUHC (McGill University Health Centre research institute) openings, WebFetch-able; it currently features only a few postings, so treat it as a spot check, not a full list. Its full ATS is `cusm.njoyn.com` (`CLID=55242`, same portal as the hospital, so "THIS IS NOT A HOSPITAL POSITION" in a posting marks the research-institute ones). That ATS sits behind a Radware captcha and returns a challenge page to scripts, so there is **no CLI for it**: do not try to bypass it. Browse it by hand if wanted (the `tbtoken`/`chk` in a shared URL are session tokens; use `https://cusm.njoyn.com/cl3/xweb/Xweb.asp?CLID=55242&page=joblisting&lang=1` in a real browser). RI-MUHC roles also surface through `linkedin-search`.
- University HR pages (concordia.ca/careers, mcgill.ca/hr, umontreal.ca) — search directly for IT/data roles
- **charityvillage.com** — Nonprofit and research sector jobs
- Direct Google searches with `site:` filters for known target organizations

## Additional Sources & Scraping Methods

WebSearch cannot see fresh LinkedIn/Indeed postings (JS-rendered index pages only). Prefer these
directly-fetchable sources. Grouped by scrape mechanism.

### Tier 1 — ATS JSON/API endpoints (cleanest; plain WebFetch, no browser)

Many company career pages are front-ends over public ATS endpoints. Query the endpoint directly:

- **Greenhouse**: `https://boards-api.greenhouse.io/v1/boards/<company>/jobs` → JSON list of all openings.
  Known: LawZero (`lawzero`). Try slug = company name lowercased.
- **Lever**: `https://api.lever.co/v0/postings/<company>?mode=json` → JSON.
- **Workday**: career sites on `*.myworkdayjobs.com`. Search endpoint:
  `POST https://<tenant>.<dc>.myworkdayjobs.com/wday/cxs/<tenant>/<site>/jobs`
  with JSON body `{"appliedFacets":{},"limit":20,"offset":0,"searchText":"data governance"}`.
  Known Workday tenants: **CAE** (`cae.wd3.myworkdayjobs.com`), Bombardier, many crown corps + universities.
  If unsure of the path, load the career page in Playwright and read the XHR to `/wday/cxs/.../jobs`.
- **iCIMS** (`*.icims.com`): JS-rendered. Use Playwright; the job body lives in an iframe
  (extract `iframe.contentDocument.body.innerText`). Confirmed working on BC Ferries.

### Tier 2 — Public sector / crown corporations (target sector)

- **jobs.gc.ca** (GC Jobs, federal) — search "data governance", "data steward", "open science"
- **carrieres.gouv.qc.ca** — Quebec provincial government
- Direct crown-corp career portals: **BDC, CDPQ, Hydro-Québec, VIA Rail, Loto-Québec, Canada Post,
  CMHC/SCHL, Business Development Bank** — many on Workday (see Tier 1 method)

### Tier 3 — Quebec job boards (browser-scrapable; catch FR postings)

- **jobillico.com**, **jobboom.com** — Quebec-specific; surface `gouvernance des données`,
  `technopédagogique`, `conseiller pédagogique` roles LinkedIn misses. Use Playwright for listings.

### Tier 4 — University HR (RDM / open-science / edtech fit)

- McGill (`mcgill.ca/hr` → Workday), Concordia, Université de Montréal, UQAM, Polytechnique, HEC,
  École de technologie supérieure (ÉTS). Search IT/data/library/learning-technology roles.

### Tier 5 — Niche RDM / library / research-infrastructure boards

- **Digital Research Alliance careers** (alliancecan.ca) — direct HTML
- **Code4Lib job board**: `https://jobs.code4lib.org/` (tag pages e.g. `/tags/Research%20Data`;
  has RSS — trivial to parse). Strong RDM/data-curation fit.
- **partnership.ca** (CARL/ABRC library jobs), **archivists.ca** job board

### Scrape order (default)

Run Tier 5 (Alliance + Code4Lib) and Tier 2 (gc.ca + crown corps) first — highest public-mandate
fit. Then Tier 1 Workday queries for CAE/universities. Playwright fallback for iCIMS/Jobillico.

## Query Categories

Queries are grouped by priority. Write **each category in every language from your Languages table** (see Language scope above) - for Ted that is English and French. Combine each query with location terms ("Montreal", "Quebec", "remote Canada") where the site supports it.

### Priority 1: Data Governance / Research Data Management

Ted's strongest and most desired career direction.

```
site:linkedin.com/jobs "data governance" Montreal
site:linkedin.com/jobs "research data management" Canada
site:linkedin.com/jobs "data steward" Montreal
site:indeed.ca "data governance specialist" Montreal
site:indeed.ca "research data management" Montreal OR Quebec
site:jobs.gc.ca "data governance" Montreal
site:jobs.gc.ca "data steward"
site:jobbank.gc.ca "data governance" OR "data steward" Montreal
site:jobbank.gc.ca "gestion des donnees" Montreal
"data governance" OR "research data management" site:alliancecan.ca
```

> `jobbank.gc.ca` and `alliancecan.ca` both have CLIs (`jobbankca-search`,
> `alliancecan-search`) that `/scrape` runs directly. These `site:` lines are the
> WebSearch fallback for when a CLI fails.

### Priority 2: LMS / Learning Ecosystem Management

Strong match; concrete Moodle expertise differentiates Ted.

```
site:linkedin.com/jobs "Moodle" Montreal
site:linkedin.com/jobs "learning management system" Montreal
site:linkedin.com/jobs "learning ecosystem" Montreal
site:indeed.ca "Moodle administrator" Montreal OR Quebec
site:indeed.ca "LMS" "learning" manager Montreal
site:linkedin.com/jobs "instructional technology" Montreal
site:linkedin.com/jobs "learning and development" "Moodle" Canada
site:jobbank.gc.ca "Moodle" OR "learning management system" Montreal
site:jobbank.gc.ca "conception pedagogique" OR "formation" Montreal
```

### Priority 3: Open Science / Research Infrastructure

Niche but strong fit; Digital Research Alliance is a primary target.

```
site:linkedin.com/jobs "open science" Canada
site:linkedin.com/jobs "data curation" Montreal OR Canada
site:indeed.ca "open science" OR "research data" Montreal
"curation officer" OR "data curator" site:alliancecan.ca
site:alliancecan.ca/en/career-opportunities
site:alliancecan.ca/fr/career-opportunities
site:jobs.gc.ca "open science"
site:jobbank.gc.ca "open science" OR "research data"
site:linkedin.com/jobs "FAIR data" Canada
```

### Priority 4: Broader Technical / Web Development

Wider net; LAMP+Moodle experience opens doors to general web dev roles.

```
site:linkedin.com/jobs "full stack developer" "Moodle" Canada
site:indeed.ca "LAMP" developer Montreal
site:linkedin.com/jobs "web developer" "data" Montreal
site:linkedin.com/jobs "technical consultant" "data" Montreal
site:indeed.ca "software developer" "research" Montreal
site:jobbank.gc.ca "developpeur" OR "developer" Montreal
```

### Priority 5: Knowledge Management / Content and Information Governance

Added after the dcbel Product Knowledge Specialist application (2026-10-15). Fits when the role is
about governed, structured knowledge (taxonomy, metadata, terminology, standards), not pure
technical writing. Scored Moderate (58) on the first posting: strong on governance and clarity
for non-specialists, thinner on titled KM/documentation years, so expect to state that gap.
Titles tried: Knowledge Specialist, Knowledge Manager, Information Architect, Taxonomist,
Content Strategist, Information Governance Specialist.

```
site:linkedin.com/jobs "knowledge specialist" Montreal
site:linkedin.com/jobs "knowledge management" Montreal OR Canada
site:linkedin.com/jobs "knowledge manager" Montreal
site:linkedin.com/jobs "information architect" Montreal OR remote Canada
site:linkedin.com/jobs "taxonomy" OR "taxonomist" Canada
site:linkedin.com/jobs "content strategist" OR "content governance" Montreal
site:linkedin.com/jobs "information governance" OR "records and information management" Montreal
site:linkedin.com/jobs "metadata specialist" OR "metadata librarian" Canada
site:indeed.ca "knowledge management specialist" Montreal OR Quebec
site:indeed.ca "specialiste en gestion des connaissances" Montreal
site:indeed.ca "architecte de l'information" Montreal
site:jobs.gc.ca "knowledge management" OR "information management" Montreal
site:jobbank.gc.ca "knowledge" "gestion des connaissances" Montreal
```

Adjacent titles to match on (also use as keyword variants in the portal CLIs):

- **Knowledge management:** Knowledge Specialist, Knowledge Manager, Knowledge Base Manager, Knowledge Operations, Knowledge Engineer
- **Structure and standards:** Information Architect, Taxonomist / Taxonomy Specialist, Ontology or Metadata Specialist, Content Standards Lead
- **Content and documentation:** Content Strategist, Content Designer, Documentation Manager, Senior Technical Writer (only where the role owns standards, not just drafting)
- **Information governance:** Information Governance Specialist, Records and Information Management (RIM) Analyst, Digital Asset Manager
- **AI + content:** AI Enablement Specialist, AI Content Operations, Prompt and Content Standards roles
- **Product-adjacent:** Product Operations Specialist, Customer Education / Enablement Manager, Learning Content Manager
- **French:** Spécialiste en gestion des connaissances, Architecte de l'information, Gestionnaire de contenu, Conseiller en gestion de l'information, Taxonomiste, Rédacteur technique principal

## Location Filter

When evaluating results, verify the job location is within reasonable commute distance or is remote-eligible:

- **Ideal:** Montreal (Plateau, Mile End, downtown, NDG, Rosemont, Verdun)
- **Acceptable:** Greater Montreal (Laval, Longueuil, South Shore, West Island)
- **Acceptable:** Remote-first with occasional Montreal travel
- **Borderline:** Remote Canada (outside Quebec) — flag for Ted to evaluate
- **Too far:** On-site roles outside Quebec requiring relocation

## Language Filter

Your working languages and levels are in CLAUDE.md's Languages table. When filtering scraped results, apply `04-job-evaluation.md`'s Language Gate: a posting requiring a language you haven't declared at all is excluded; a posting requiring a higher level than you declared in a language you do work in is not excluded, flag it clearly instead (see `job-scraper/SKILL.md`'s Step 3 "Quick Fit Assessment" for how the flag surfaces in `/scrape` output). Postings simply *written* in a language you don't work in, that don't require it on the job, are fine.

## Date Filter

Only include jobs posted within the last 14 days, or with an application deadline that has not yet passed. If a posting date cannot be determined, include it but flag as "date unknown".

## Role Types Ted May Not Have Considered

Proactively suggest these if the core categories yield thin results:

- **"Knowledge management specialist"** — governance + training combination; appears in federal and university contexts (now covered by Priority 5)
- **"Digital scholarship librarian"** or **"data services librarian"** — RDM in university library setting; Ted's open science background is a strong fit
- **"Technical trainer" / "Moodle trainer"** — at Moodle vendor companies or edtech firms
- **"Research computing analyst"** — Compute Canada / Digital Research Alliance regional support roles
- **"AI adoption specialist"** or **"digital transformation advisor"** — emerging role type in government and crown corps; Ted's AI evaluation experience at KnowledgeOne and Premergency is directly relevant

## Adapting Queries

If the user specifies a focus area, select queries from the matching category and also generate 2-3 custom queries for that focus. For example:
- `/scrape data governance` — Priority 1 queries + custom "data quality" / "data stewardship" variants
- `/scrape Moodle` — Priority 2 queries + any known target companies (Premergency, KnowledgeOne competitors)
- `/scrape federal` — jobs.gc.ca queries across all priority categories
