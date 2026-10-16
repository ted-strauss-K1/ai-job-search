"""
Generate application docs for CAE — Data Governance & Stewardship Lead (temporary), Req 122823.
Location: Montreal (St. Laurent). 14-month fixed term.
Outputs (in docx/):
  - cv_cae_datagov.docx     / cv_cae_datagov.pdf
  - cover_cae_datagov.docx  / cover_cae_datagov.pdf

Content is defined ONCE below, then rendered to both docx (python-docx) and
pdf (reportlab) so the two formats never drift.

Note: named *_datagov to avoid overwriting the May 2026 cv_cae.docx / cover_cae.docx
from an earlier, unrelated CAE application.
"""
import os

os.makedirs("docx", exist_ok=True)

# ------------------------------------------------------------------
# SHARED CONTENT
# ------------------------------------------------------------------

NAME = "Ted Strauss"
CV_CONTACT = "Montreal, Quebec, Canada  |  514-475-2374  |  ted.strauss@gmail.com  |  linkedin.com/in/tedstrauss-63b01821"
COVER_CONTACT = "514-475-2374  |  ted.strauss@gmail.com  |  linkedin.com/in/tedstrauss-63b01821"

PROFILE = (
    "Data governance and stewardship specialist with over a decade of experience building metadata "
    "standards, data definitions, and data quality practices across Canada's research and "
    "public-sector ecosystem. Led data governance and stewardship at McGill University's McConnell "
    "Brain Imaging Centre, defining standards, ownership structures, and retention and access "
    "policies across dozens of research groups, with Collibra as the institutional data catalogue. "
    "Contributed to national research data standards through Portage, CONP, and RDA committee work. "
    "Known for making governance hold: building data literacy and communities of practice rather "
    "than enforcing compliance from above. Bilingual (EN/FR); 9 publications; citation count 630; "
    "h-index 9."
)

# (bold label, remaining text) — label is emphasised
COMPETENCIES = [
    ("Stewardship and domain relationships",
     ": worked directly with dozens of research groups to establish data ownership, responsibilities, "
     "and governance expectations per domain; facilitated alignment where groups defined the same "
     "data differently"),
    ("Standards, glossary and metadata management",
     ": defined and maintained metadata standards, data definitions, and naming conventions; used "
     "Collibra as the institutional data catalogue; reviewed and refined definitions for consistency "
     "across the catalogue"),
    ("Data quality and pipeline integrity",
     ": authored data acquisition, classification, retention, and access policies for daily "
     "neuroimaging pipelines; defined quality expectations and monitoring practices, and worked with "
     "technical teams to trace quality issues back through the pipeline and correct them at source"),
    ("Cross-functional governance coordination",
     ": fielded, prioritized, and coordinated governance questions between research groups and "
     "technical teams; translated frameworks and policies into actionable guidance and onboarding "
     "material"),
    ("Data literacy, onboarding and communication",
     ": designed a Moodle-based self-serve education portal for researcher onboarding and delivered "
     "hands-on training on data management; built a public knowledge base on FAIR principles; "
     "certified in Scientific Community Engagement Fundamentals (CSCCE)"),
    ("Data analysis and tooling",
     ": SQL and NoSQL, data wrangling and cleaning, ETL and data modeling, Python (pandas, plotly), "
     "R, Tableau; experimental design and quantitative analysis from cognitive science training and "
     "nine published research and data-tooling papers; Collibra, LAMP++, SSO, LDAP, Docker, AWS and "
     "Azure; evaluated and adopted AI tools including Claude Code for enterprise workflows"),
]

# each: (dates, title, org, location, [bullets])
EXPERIENCE = [
    ("07/2025 – 01/2026", "Moodle Analyst", "Premergency Inc.", "Canada", [
        "Coordinated between government clients and development teams to deliver regulated LMS solutions, maintaining compliance obligations throughout and aligning expectations across business and technical stakeholders",
        "Managed legacy LMS migrations to Moodle; designed bespoke learning and development solutions for public-sector clients",
    ]),
    ("01/2024 – 10/2024", "Full Stack Developer", "KnowledgeOne", "Montreal, QC", [
        "Developed LMS features for active clients on the eConcordia Moodle platform (LAMP++, LXD)",
        "Evaluated and adopted AI tools in enterprise learning contexts, assessing data handling and usability before rollout",
    ]),
    ("09/2016 – 10/2021", "Manager of Data Resources", "McConnell Brain Imaging Centre, The Neuro, McGill University", "Montreal, QC", [
        "Led data governance and stewardship for one of Canada's leading brain imaging centres, defining metadata standards, data definitions, ownership structures, and quality expectations across dozens of principal investigators and hundreds of researchers",
        "Served as the central point of contact for data practice across research domains, clarifying who owned what, and facilitating alignment where groups defined the same data differently",
        "Used Collibra as the institutional data catalogue; maintained the data glossary, metadata fields, and naming conventions; launched an OwnCloud portal that moved researchers to self-serve data management",
        "Built the daily neuroimaging acquisition pipelines and the policies governing acquisition, classification, retention, and access; traced quality issues back to their source in the pipeline and corrected them there",
        "Drove adoption through a Moodle-based education portal and hands-on training, building data literacy and communities of practice rather than top-down compliance",
        "Represented the centre on national research data bodies (Portage, CONP, RDA); authored a published neuroimaging data management plan template (Zenodo, 2021) and co-authored the Canadian Open Neuroscience Platform data and tools integration paper (Scientific Data, 2023)",
    ]),
    ("08/2020 – 10/2021", "Data Management & Sharing Coordinator (p/t)", "Tanenbaum Open Science Institute, The Neuro, McGill University", "Montreal, QC", [
        "Supported the launch of a new academic unit focused on open science; coordinated across faculty, students, and institutional stakeholders",
        "Designed and delivered training on data management and governance practices; built a public-facing knowledge base explaining FAIR principles to non-specialist audiences",
    ]),
    ("04/2017 – 08/2021", "Founder and Director", "Sur Place Media", "Montreal, QC", [
        "Founded and operated a neighbourhood arts school; hosted 150 workshop groups with 20 instructors; led a full pivot to virtual delivery during the COVID-19 pandemic",
    ]),
    ("02/2015 – 09/2016", "Software Developer", "McGill Centre for Integrative Neuroscience, McGill University", "Montreal, QC", [
        "Programmed the data acquisition pipeline for the national CCNA longitudinal dementia study using the LORIS platform (PHP, MySQL, JavaScript); contributed to national research data infrastructure",
    ]),
]

ADDITIONAL = [
    "Photonic Knowledge — Database administrator & software developer (2012–2014): built a Drupal ERP system and its underlying data model for mining-sector core sample imaging",
    "Moss Rehabilitation Hospital — Research software developer (2007–2010)",
    "University of Connecticut & Columbia University — Research assistant & software developer (2004–2008)",
]

EDUCATION = [
    ("1998–2003", "B.A. (Honours), Cognitive Science", "McGill University", "Montreal, QC",
     ["Minor: Music Technology. Topics: psycholinguistics, cognitive science, computational modeling of language, music technology."]),
    ("2021", "Scientific Community Engagement Fundamentals", "CSCCE", "", []),
]

PUBLICATIONS = [
    "Poline, J.-B., et al. (2023). Data and tools integration in the Canadian open neuroscience platform. Scientific Data, 10(1), 189.",
    "Strauss, T. (2021). Data Management Plan Template: Neuroimaging in the Neurosciences. Zenodo. doi:10.5281/zenodo.4673558",
]
PUB_FOOT = "Citation count: 630 | h-index: 9 | Full list: scholar.google.com/citations"

COVER_DATE = "August 7, 2026"
COVER_SUBJECT = "Subject: Application: Data Governance & Stewardship Lead (temporary), Req 122823"
COVER_SALUTATION = "Dear CAE Hiring Team,"
COVER_PARAS = [
    "I am applying for the Data Governance & Stewardship Lead position at CAE's Saint-Laurent campus. "
    "Your posting describes working with data stewards across business domains, holding the line on "
    "definitions and metadata quality, and turning governance standards into something people follow. "
    "That is the work I did for five years at McGill, and the relationship side of it is the part I "
    "know best.",

    "CAE's fiscal 2026 results set out a transformation plan that includes investments to modernize "
    "the operating platform, its systems and its processes. Consistent, trusted definitions are the "
    "part of that work no tool delivers on its own, and in a fourteen-month term the constraint is "
    "how quickly stewards across Civil Aviation and Defense and Security can be brought to one "
    "definition and kept there. One more reason this posting caught my attention: my career has been "
    "spent governing learning and training data, the data your civil business runs on. I claim no "
    "aviation domain knowledge, but I know what makes training records trustworthy.",

    "At McGill University's McConnell Brain Imaging Centre, I led data governance across dozens of "
    "research groups: establishing who owned what, maintaining the glossary, metadata fields, and "
    "naming conventions with Collibra as the institutional catalogue, and writing the policies "
    "governing how imaging data was acquired, retained, and accessed. Much of my time went to what "
    "your posting calls cross-domain alignment, sitting between groups who had defined the same data "
    "differently and getting them to one definition.",

    "The obstacle was never the framework, it was adoption. I treated governance as a literacy "
    "problem, building a Moodle-based education portal that became our governance onboarding, so "
    "people understood why a definition mattered before being asked to approve one.",

    "On your minimum qualifications, my quantitative grounding comes from research rather than from a "
    "data scientist title: experimental design, hypothesis testing, and statistical analysis from "
    "cognitive science training and nine publications, with SQL, Python, and R used across my career "
    "for data wrangling and quality work. The applied side is concrete: I have administered databases, "
    "built a Drupal ERP data model in the mining sector, and programmed the acquisition pipeline for "
    "the national CCNA longitudinal dementia study. I am bilingual in French and English, based in "
    "Montreal, and available immediately for the full term.",

    "I would welcome the opportunity to discuss how I can help CAE build out its steward "
    "relationships, its governance onboarding, and the definitions underneath them. Thank you for "
    "your consideration.",
]
COVER_CLOSING = "Kind regards,"

# ==================================================================
# DOCX RENDERING
# ==================================================================
from docx import Document
from docx.shared import Pt, RGBColor, Inches, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

BLUE = RGBColor(0x21, 0x6F, 0xAA)
BLACK = RGBColor(0x00, 0x00, 0x00)
GRAY = RGBColor(0x55, 0x55, 0x55)


def _margins(doc, top=1.5, bottom=1.5, left=2.0, right=2.0):
    for s in doc.sections:
        s.top_margin, s.bottom_margin = Cm(top), Cm(bottom)
        s.left_margin, s.right_margin = Cm(left), Cm(right)


def _name_header(doc, name, contact):
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(name); r.bold = True; r.font.size = Pt(28); r.font.color.rgb = BLUE
    p2 = doc.add_paragraph(); p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r2 = p2.add_run(contact); r2.font.size = Pt(10); r2.font.color.rgb = GRAY
    p2.paragraph_format.space_after = Pt(6)


def _heading(doc, title):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10); p.paragraph_format.space_after = Pt(2)
    r = p.add_run(title.upper()); r.bold = True; r.font.size = Pt(11); r.font.color.rgb = BLUE
    pPr = p._p.get_or_add_pPr(); pBdr = OxmlElement('w:pBdr'); bottom = OxmlElement('w:bottom')
    bottom.set(qn('w:val'), 'single'); bottom.set(qn('w:sz'), '6')
    bottom.set(qn('w:space'), '1'); bottom.set(qn('w:color'), '216FAA')
    pBdr.append(bottom); pPr.append(pBdr)


def _entry(doc, dates, title, org, location, bullets):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(6); p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.keep_with_next = True
    r1 = p.add_run(title); r1.bold = True; r1.font.size = Pt(10.5); r1.font.color.rgb = BLACK
    r2 = p.add_run(f"  —  {org}"); r2.font.size = Pt(10.5); r2.font.color.rgb = GRAY
    if location:
        r3 = p.add_run(f", {location}"); r3.font.size = Pt(10.5); r3.font.color.rgb = GRAY
    p2 = doc.add_paragraph()
    p2.paragraph_format.space_before = Pt(0); p2.paragraph_format.space_after = Pt(2)
    p2.paragraph_format.keep_with_next = True
    r4 = p2.add_run(dates); r4.italic = True; r4.font.size = Pt(9.5); r4.font.color.rgb = GRAY
    for b in bullets:
        _bullet(doc, b)


def _bullet(doc, text, indent=0.25):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_before = Pt(1); p.paragraph_format.space_after = Pt(1)
    p.paragraph_format.left_indent = Inches(indent)
    for i, part in enumerate(text.split('**')):
        if not part:
            continue
        r = p.add_run(part); r.font.size = Pt(10); r.bold = (i % 2 == 1)


def _para(doc, text, size=10, italic=False, color=None, space_after=4):
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(space_after)
    r = p.add_run(text); r.font.size = Pt(size); r.italic = italic
    if color:
        r.font.color.rgb = color
    return p


def build_docx_cv():
    doc = Document(); _margins(doc)
    _name_header(doc, NAME, CV_CONTACT)
    _para(doc, PROFILE, size=10, space_after=6)
    _heading(doc, "Core Competencies")
    for label, rest in COMPETENCIES:
        _bullet(doc, f"**{label}**{rest}")
    _heading(doc, "Professional Experience")
    for e in EXPERIENCE:
        _entry(doc, *e)
    _heading(doc, "Additional Experience")
    for a in ADDITIONAL:
        _bullet(doc, a)
    _heading(doc, "Education")
    for e in EDUCATION:
        _entry(doc, *e)
    _heading(doc, "Languages")
    _para(doc, "English (native), French (bilingual, professional working proficiency).", size=10)
    _heading(doc, "Selected Publications")
    for pub in PUBLICATIONS:
        _bullet(doc, pub)
    _para(doc, PUB_FOOT, size=9, italic=True, color=GRAY)
    doc.save("docx/cv_cae_datagov.docx")
    print("OK cv_cae_datagov.docx")


def build_docx_cover():
    doc = Document(); _margins(doc, top=2.0, bottom=2.0, left=2.5, right=2.5)
    _name_header(doc, NAME, COVER_CONTACT)
    _para(doc, COVER_DATE, size=10, space_after=12)
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(6)
    r = p.add_run(COVER_SUBJECT); r.bold = True; r.font.size = Pt(10)
    _para(doc, COVER_SALUTATION, size=10, space_after=6)
    for para in COVER_PARAS:
        pp = doc.add_paragraph(); pp.paragraph_format.space_after = Pt(8)
        rr = pp.add_run(para); rr.font.size = Pt(10)
    _para(doc, COVER_CLOSING, size=10, space_after=24)
    _para(doc, NAME, size=10)
    doc.save("docx/cover_cae_datagov.docx")
    print("OK cover_cae_datagov.docx")


# ==================================================================
# PDF RENDERING (separate CV and cover letter, for page-count inspection)
# ==================================================================
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer,
    HRFlowable, ListFlowable, ListItem, KeepTogether,
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

PDF_BLUE = HexColor("#216FAA")
PDF_GRAY = HexColor("#555555")


def _esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _bold_md(t):
    t = _esc(t)
    parts = t.split("**")
    out = ""
    for i, p in enumerate(parts):
        out += f"<b>{p}</b>" if i % 2 == 1 else p
    return out


def _styles():
    styles = getSampleStyleSheet()
    return {
        "name": ParagraphStyle("Name", parent=styles["Normal"], fontName="Helvetica-Bold",
                               fontSize=22, textColor=PDF_BLUE, alignment=TA_CENTER, spaceAfter=2, leading=26),
        "contact": ParagraphStyle("Contact", parent=styles["Normal"], fontName="Helvetica",
                                  fontSize=9, textColor=PDF_GRAY, alignment=TA_CENTER, spaceAfter=8, leading=12),
        "heading": ParagraphStyle("Heading", parent=styles["Normal"], fontName="Helvetica-Bold",
                                  fontSize=11, textColor=PDF_BLUE, spaceBefore=8, spaceAfter=2, leading=13),
        "body": ParagraphStyle("Body", parent=styles["Normal"], fontName="Helvetica", fontSize=10,
                               leading=13, spaceAfter=3),
        "bullet": ParagraphStyle("Bullet", parent=styles["Normal"], fontName="Helvetica",
                                 fontSize=9.5, leading=12, spaceAfter=1),
        "entry_title": ParagraphStyle("EntryTitle", parent=styles["Normal"], fontName="Helvetica",
                                      fontSize=10.5, spaceBefore=5, spaceAfter=0, leading=12),
        "entry_dates": ParagraphStyle("EntryDates", parent=styles["Normal"], fontName="Helvetica",
                                      fontSize=9, textColor=PDF_GRAY, spaceAfter=2, leading=11),
        "letter": ParagraphStyle("Letter", parent=styles["Normal"], fontName="Helvetica",
                                 fontSize=10.5, leading=15, spaceAfter=8),
        "small_italic": ParagraphStyle("SmallItalic", parent=styles["Normal"],
                                       fontName="Helvetica-Oblique", fontSize=8.5,
                                       textColor=PDF_GRAY, spaceAfter=2, leading=11),
    }


def _render(path, story, top=1.5, bottom=1.3, left=2.0, right=2.0):
    doc = BaseDocTemplate(path, pagesize=letter,
                          topMargin=top * cm, bottomMargin=bottom * cm,
                          leftMargin=left * cm, rightMargin=right * cm)
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="main")
    doc.addPageTemplates([PageTemplate(id="all", frames=[frame])])
    doc.build(story)
    print(f"OK {os.path.basename(path)}")


def build_pdf_cv():
    S = _styles()

    def rule():
        return HRFlowable(width="100%", thickness=0.6, color=PDF_BLUE, spaceBefore=1, spaceAfter=3)

    def heading(text):
        return [Paragraph(_esc(text.upper()), S["heading"]), rule()]

    def bullets(items):
        return ListFlowable(
            [ListItem(Paragraph(_bold_md(t), S["bullet"]), leftIndent=10, value="•") for t in items],
            bulletType="bullet", bulletColor=PDF_BLUE, leftIndent=12, bulletFontSize=8,
        )

    def entry(dates, title, org, location, bl):
        loc = f", {_esc(location)}" if location else ""
        head = (f'<b>{_esc(title)}</b>'
                f'<font color="#555555">&nbsp;&nbsp;—&nbsp;&nbsp;{_esc(org)}{loc}</font>')
        header = [Paragraph(head, S["entry_title"]), Paragraph(_esc(dates), S["entry_dates"])]
        if not bl:
            return [KeepTogether(header)]
        # Bind the title, dates and FIRST bullet together so a title can never strand at the
        # foot of a page. Remaining bullets flow freely: binding the whole entry pushes a long
        # six-bullet role wholesale onto the next page and leaves a third of this one blank.
        out = [KeepTogether(header + [bullets(bl[:1])])]
        if len(bl) > 1:
            out.append(bullets(bl[1:]))
        return out

    story = [Paragraph(_esc(NAME), S["name"]),
             Paragraph(_esc(CV_CONTACT), S["contact"]),
             Paragraph(_esc(PROFILE), S["body"])]
    story += heading("Core Competencies")
    story.append(bullets([f"**{l}**{r}" for l, r in COMPETENCIES]))
    story += heading("Professional Experience")
    for e in EXPERIENCE:
        story += entry(*e)
    story += heading("Additional Experience")
    story.append(bullets(ADDITIONAL))
    story += heading("Education")
    for e in EDUCATION:
        story += entry(*e)
    story += heading("Languages")
    story.append(Paragraph("English (native), French (bilingual, professional working proficiency).", S["body"]))
    story += heading("Selected Publications")
    story.append(bullets(PUBLICATIONS))
    story.append(Paragraph(_esc(PUB_FOOT), S["small_italic"]))

    _render("docx/cv_cae_datagov.pdf", story)


def build_pdf_cover():
    S = _styles()
    story = [Paragraph(_esc(NAME), S["name"]),
             Paragraph(_esc(COVER_CONTACT), S["contact"]),
             Spacer(1, 6),
             Paragraph(_esc(COVER_DATE), S["body"]),
             Spacer(1, 8),
             Paragraph(f"<b>{_esc(COVER_SUBJECT)}</b>", S["body"]),
             Spacer(1, 4),
             Paragraph(_esc(COVER_SALUTATION), S["letter"])]
    for para in COVER_PARAS:
        story.append(Paragraph(_esc(para), S["letter"]))
    # Bind the closing and signature so the name can never strand alone on page 2.
    story += [Spacer(1, 8),
              KeepTogether([Paragraph(_esc(COVER_CLOSING), S["body"]),
                            Spacer(1, 14),
                            Paragraph(_esc(NAME), S["body"])])]
    _render("docx/cover_cae_datagov.pdf", story, top=2.0, bottom=1.5, left=2.5, right=2.5)


if __name__ == "__main__":
    build_docx_cv()
    build_docx_cover()
    build_pdf_cv()
    build_pdf_cover()
    print("\nDone. Files in docx/")
