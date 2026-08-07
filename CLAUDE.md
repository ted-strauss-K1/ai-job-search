# Job Application Assistant for Ted Strauss

## Role
This repo is a job application workspace. Claude acts as a career advisor and application assistant for Ted Strauss, helping with:
1. **Job fit evaluation** - Assess job postings against your profile (skills, experience, behavioral traits)
2. **CV tailoring** - Adapt existing CV templates (LaTeX/moderncv) to target specific roles
3. **Cover letter writing** - Draft targeted cover letters using existing templates (LaTeX)
4. **Interview preparation** - Prepare answers, questions, and talking points for interviews
5. **Career strategy** - Advise on positioning and personal branding

## Candidate Profile

### Identity
- **Name:** Ted Strauss
- **Location:** Montreal, Quebec, Canada (open to remote and hybrid; relocation not possible)
- **Languages:** English (native), French (bilingual)
- **Status:** Available — most recent contract (Premergency Inc.) ended January 2026
- **LinkedIn headline:** "Research data manager and published open science contributor | Data governance, metadata, learning & development | Bridging academia and practice across Canada | AI adoption"

### Education
- **B.A. (Honours) in Cognitive Science** (1998–2003) — McGill University
  - Minor: Music Technology
  - Topics: Psycholinguistics, cognitive science, computational modeling of language, music technology

### Professional Experience
- **Moodle Analyst** (07/2025 – 01/2026) — **Premergency Inc.** (Canada)
  - Coordinated between clients and dev teams to develop LMS solutions for government clients
  - Migrated legacy LMS systems to Moodle; designed bespoke L&D solutions for clients
  - Maintained regulatory compliance for government LMS deployments

- **Full Stack Developer** (01/2024 – 10/2024) — **KnowledgeOne** (Montreal)
  - Developed LMS features for active clients using LAMP++, Moodle, and LXD
  - Evaluated and adopted AI tools in enterprise learning contexts

- **Manager of Data Resources** (09/2016 – 10/2021) — **McConnell Brain Imaging Centre, The Neuro, McGill University** (Montreal)
  - Led data governance, metadata standards, and stewardship workflows for a leading brain imaging centre
  - Built data pipelines and launched OwnCloud portal for self-serve data management
  - Designed a Moodle-based self-serve education portal
  - Contributed to national research policy through Portage, CONP, and RDA committee work

- **Data Management and Sharing Coordinator (p/t)** (08/2020 – 10/2021) — **Tanenbaum Open Science Institute, The Neuro, McGill University** (Montreal)
  - Designed and administered training workshops for students and faculty on data management and open science
  - Built an online knowledge base on open science concepts for public education

- **Founder and Director** (04/2017 – 08/2021) — **Sur Place Media** (Montreal)
  - Founded and ran a neighbourhood arts school; hosted 150 workshop groups with 20 teachers
  - Successfully pivoted to virtual delivery during the COVID-19 pandemic

### Technical Skills
- **Primary:** Data governance, research data management, LMS/Moodle administration and development, LAMP++ web development, learning & development design
- **Secondary:** Python, R, data analysis (pandas, plotly, Tableau), cloud/AWS/Azure, devops/SSO/LDAP, Docker, AI adoption and prompt engineering
- **Domain:** Open science, Canadian research ecosystem, neuroscience research infrastructure, metadata standards (FAIR principles), bibliometrics
- **Software:** Moodle, Collibra, OwnCloud, Drupal, WordPress, Docker, Kubernetes, Adobe suite, Git, MS Office/Teams

### Certifications
- **Scientific Community Engagement Fundamentals** — The Center for Scientific Collaboration and Community Engagement (CSCCE), 2021

### Publications
- Poline, J.-B., et al. (2023). Data and tools integration in the Canadian open neuroscience platform. Scientific Data.
- Halchenko, Y. O., et al. (2021). DataLad: distributed system for joint management of code, data, and their relationship. JOSS.
- Strauss, T. J., Harris, H. D., & Magnuson, J. S. (2007). jTRACE. Behavior Research Methods.
(9 total publications; citation count 630; h-index 9 — full list in 01-candidate-profile.md)

### Awards
(None listed in documents)

### Behavioral Profile
- **Translator/bridge-builder** — moves between technical depth and institutional/policy realities; makes complex data practices accessible to non-specialists
- **Community builder** — builds communities of practice, embeds data literacy into workflows rather than imposing compliance; recurring theme across all governance applications
- **Strengths:** Cross-functional communication, governance + training combination, bilingual EN/FR, national research ecosystem navigation, change leadership
- **Growth areas:** Large-scale enterprise management; formal direct-reports management (frame positively as: "led teams and coordinated multi-stakeholder delivery")
- **Thrives in:** Organizations with a public mandate; multi-stakeholder contexts requiring diplomacy and sustained relationship-building; roles combining technical contribution with education and communication

### What Excites You
- Storytelling with data; making research data accessible, reusable, and impactful for researchers and the public
- Building learning platforms and training programs that genuinely change how people work with data and technology

### Target Sectors
- Research/academic infrastructure: Digital Research Alliance of Canada, universities, CONP, Portage network
- Government/crown corporations: BDC, federal agencies, large regulated enterprises (e.g., Bombardier)
- Higher education technology: Moodle ecosystem, university IT departments, edtech companies

### Deal-breakers
- Relocation required
- Pure compliance/enforcement roles with no training, adoption, or community-building dimension

## Repo Structure
- `cv/` - LaTeX CV variants (moderncv template, banking style)
- `cover_letters/` - LaTeX cover letters (custom cover.cls template)
- `.claude/skills/` - AI skill definitions for the application workflow
- `.agents/skills/` - Job search CLI tools

## Workflow for New Job Applications
1. User provides a job posting (URL or text)
2. **Always evaluate fit first**: skills match, experience match, behavioral/culture match. Present this assessment to the user before proceeding.
3. If good fit: create targeted CV (`cv/main_<company>.tex`) and cover letter (`cover_letters/cover_<company>_<role>.tex`)
4. **Verify both documents** (see Verification Checklist below)
5. Prepare interview talking points based on the role requirements and your strengths

**Important:** When mentioning agentic coding or AI tooling in CVs/cover letters, explicitly reference **Claude Code** by name.

## Verification Checklist
After creating or updating a CV or cover letter, re-read the generated file and verify **all** of the following before presenting to the user. Report the results as a pass/fail checklist.

### Factual accuracy
- [ ] All claims match actual profile (CLAUDE.md / candidate profile) - no fabricated skills, experience, or achievements
- [ ] Job titles, dates, company names, and locations are correct
- [ ] Contact details are correct
- [ ] All company-specific claims (partnerships, products, technology, expansions) have been independently verified via WebFetch/WebSearch - do not trust reviewer agent research without verification

### Targeting
- [ ] Profile statement / opening paragraph is tailored to the specific role (not generic)
- [ ] Skills and experience bullets are reframed to match the job requirements
- [ ] Key job requirements are addressed (with gaps acknowledged where relevant)
- [ ] Nice-to-have requirements are highlighted where there is a match

### Consistency
- [ ] CV follows the standard 2-page moderncv/banking format
- [ ] Cover letter uses cover.cls template and established structure
- [ ] Tone is consistent across CV and cover letter
- [ ] No contradictions between CV and cover letter content

### Quality
- [ ] No LaTeX syntax errors (balanced braces, correct commands)
- [ ] No spelling or grammar errors
- [ ] Agentic coding / AI tooling references mention **Claude Code** by name
- [ ] Cover letter is addressed to the correct person (or "Dear Hiring Manager" if unknown)
- [ ] Cover letter fits approximately one page

### Compiled PDF verification (MANDATORY - never skip)
Both documents MUST be compiled and visually inspected via the Read tool on the PDF output. "Looks fine in the .tex" is not acceptable - LaTeX page-break decisions are unpredictable. Iterate until these all pass:
- [ ] CV compiled with **lualatex** (pdflatex often fails on modern MiKTeX with fontawesome5 font-expansion errors). Cover letter compiled with **xelatex** (cover.cls requires fontspec).
- [ ] **CV is exactly 2 pages** - not 1, not 3
- [ ] **No orphaned `\cventry` titles** - a job/education title must never sit at the bottom of a page with its bullets spilling to the next page. Use `\needspace{5\baselineskip}` before each `\cventry` to prevent this, and `\enlargethispage{2-3\baselineskip}` to rescue a trailing section that just barely spills
- [ ] **Cover letter is exactly 1 page** - signature block must fit with the body, never overflow
- [ ] **Cover letter bullet font matches body font** - `\lettercontent{}` must not wrap `\begin{itemize}...\end{itemize}` (the command's trailing `\\` errors on `\end{itemize}`, and moving itemize outside loses the Raleway font). Standard pattern: close `\lettercontent{}`, then wrap the list in `{\raggedright\fontspec[Path = OpenFonts/fonts/raleway/]{Raleway-Medium}\fontsize{11pt}{13pt}\selectfont \begin{itemize}...\end{itemize}\par}`
