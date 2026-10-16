"""
Generate application docs for CRKN — Developer, Data Services and Interoperability.
Ottawa, ON / Remote in Canada. 18-month term (renewable pending funding). $67,658-$81,500.
Outputs (in docx/):
  - cv_crkn_dataservices.docx     / .pdf
  - cover_crkn_dataservices.docx  / .pdf

Content is defined ONCE below, then rendered to both docx (python-docx) and
pdf (reportlab) so formats never drift.

Targeting note: leads with hands-on development (LORIS/CCNA pipeline,
KnowledgeOne LAMP++/Docker work) rather than the governance/L&D track, since
this is a developer role, then uses the McConnell governance tenure to make
the Alliance-ecosystem connection explicit (CRKN's PID team collaborates
directly with the Digital Research Alliance of Canada, whose predecessor
Portage program Ted represented his institution on).

Genuine gaps stated plainly in the cover letter: no Java or TypeScript
specifically (posting names both "especially"; Ted's background is
PHP/JavaScript/Python), and no direct PID/RAiD ecosystem experience. Bridged
using the posting's own "equivalent combination of education and
experience" clause (Ted's degree is Cognitive Science, not CS/SE) and its
"ability to learn and adapt to new languages/frameworks" qualification.

Company facts used in the cover letter were verified independently via
WebSearch against crkn-rcdr.ca (88 member institutions, Canadiana
collections, open-access/shared-infrastructure mission) — not from the
job-posting text itself. Job requirements sourced from CRKN's own JD PDF
(JD_Data Services & Interoperability Deve.pdf, linked from CRKN's official
BambooHR posting), which is fuller than the BambooHR summary page.
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
    "Research data infrastructure developer with a decade of experience building and governing the "
    "systems behind national-scale Canadian research data programs. Programmed the data acquisition "
    "pipeline for the national CCNA longitudinal dementia study on the LORIS platform (PHP, MySQL, "
    "JavaScript), then led data governance for one of Canada's leading brain imaging centres, "
    "representing the institution on Portage, CONP, and the Research Data Alliance, work that fed "
    "directly into what is now the Digital Research Alliance of Canada. Full-stack development "
    "background (LAMP++, Docker, Linux/Unix) paired with a first-hand understanding of the academic "
    "research environment national data services are built to serve. Bilingual (EN/FR), Montreal-based, "
    "open to Ottawa or fully remote."
)

COMPETENCIES = [
    ("Full-stack development for national research platforms",
     ": built and maintained the LORIS-based data acquisition pipeline (PHP, MySQL, JavaScript) for the "
     "national CCNA longitudinal dementia study; developed web application features using LAMP++ and "
     "container-based deployment (LXD) for enterprise clients at KnowledgeOne"),
    ("Linux server administration and containerized deployment",
     ": production experience with Docker-based deployment and Linux server administration (Ubuntu, "
     "Debian, CentOS), plus devops fundamentals (SSO, LDAP, Active Directory) from managing research "
     "computing infrastructure"),
    ("Research data interoperability and national governance ecosystem",
     ": designed metadata standards and lifecycle policies for a national-scale research data "
     "environment, then represented the institution on Portage, CONP, and the Research Data Alliance, "
     "the governance ecosystem CRKN's PID program collaborates with directly through the Alliance"),
    ("Sole and small-team developer track record",
     ": built and maintained production data systems as the primary or sole developer across multiple "
     "roles, collaborating directly with non-technical researchers and translating feature requests "
     "into working software under short release cycles"),
    ("Rapid adoption of new tools and frameworks",
     ": evaluated and adopted new frameworks and AI-assisted development tools, including Claude Code, "
     "in production contexts, weighing technical fit and data-handling implications under real "
     "deadlines rather than in the abstract"),
    ("Bilingual EN/FR, Montreal-based",
     ": professional working proficiency in French and English; comfortable working remotely with a "
     "small, distributed technical team"),
]

# each: (dates, title, org, location, [bullets]) — ordered by relevance to hands-on development
EXPERIENCE = [
    ("02/2015 – 09/2016", "Software Developer", "McGill Centre for Integrative Neuroscience, McGill University", "Montreal, QC", [
        "Programmed the data acquisition pipeline for the national CCNA study on aging and the brain, a longitudinal dementia research program, using the LORIS platform (PHP, MySQL, JavaScript)",
        "Built and maintained the pipeline as part of a small technical team, working directly with researchers to translate study requirements into working software under short release cycles",
        "Administered the LAMP stack and servers supporting the pipeline in a Linux environment",
    ]),
    ("01/2024 – 10/2024", "Full Stack Developer", "KnowledgeOne", "Montreal, QC", [
        "Developed LMS features for active clients using LAMP++, Moodle, and LXD container-based deployment",
        "Evaluated and adopted AI-assisted development tools in enterprise contexts, weighing productivity gains against data-handling and governance implications",
    ]),
    ("09/2016 – 10/2021", "Manager of Data Resources", "McConnell Brain Imaging Centre, The Neuro, McGill University", "Montreal, QC", [
        "Led data governance for one of Canada's leading brain imaging research centres, defining metadata standards and lifecycle policies for dozens of principal investigators and hundreds of researchers",
        "Represented the centre on national research data governance bodies, Portage, CONP, and the Research Data Alliance, contributing to the shared Canadian data governance standards now carried forward by the Digital Research Alliance of Canada",
        "Launched a self-serve OwnCloud portal and a Moodle-based education portal, building and maintaining both as part of the centre's technical infrastructure",
        "Developed brain imaging data pipelines and policies for daily data acquisition workflows",
    ]),
    ("07/2025 – 01/2026", "Moodle Analyst", "Premergency Inc.", "Canada", [
        "Migrated legacy LMS systems to Moodle and maintained regulatory compliance requirements for government deployments, coordinating between client and development teams",
    ]),
]

ADDITIONAL = [
    "Photonic Knowledge — Database Administrator and Software Developer (2012–2014): built a Drupal ERP system and its underlying data model, as sole developer, for the mining exploration sector (LAMP++, CMS)",
    "Tanenbaum Open Science Institute, The Neuro — Data Management & Sharing Coordinator, p/t (2020–2021): designed training workshops and a public knowledge base on data management and open science",
    "Sur Place Media — Founder and Director (2017–2021): founded and ran a neighbourhood arts school, operating program delivery for 150 workshop groups and 20 instructors",
]

EDUCATION = [
    ("1998–2003", "B.A. (Honours), Cognitive Science", "McGill University", "Montreal, QC",
     ["Minor: Music Technology. Topics: psycholinguistics, computational modeling of language, music technology."]),
    ("2021", "Scientific Community Engagement Fundamentals", "CSCCE", "", []),
]

PUBLICATIONS = [
    "Poline, J.-B., et al. (2023). Data and tools integration in the Canadian open neuroscience platform. Scientific Data, 10(1), 189.",
    "Halchenko, Y. O., et al. (2021). DataLad: distributed system for joint management of code, data, and their relationship. JOSS, 6(63), 3262.",
]
PUB_FOOT = "9 publications | citation count 630 | h-index 9 | Full list: scholar.google.com/citations"

# ------------------------------------------------------------------
# COVER LETTER
# ------------------------------------------------------------------

COVER_DATE = "August 21, 2026"
COVER_SUBJECT = "Subject: Application: Developer, Data Services and Interoperability"
COVER_SALUTATION = "Dear Hiring Team,"
COVER_PARAS = [
    "I am applying for the Developer, Data Services and Interoperability position with the Canadian "
    "Persistent Identifier Program. The role asks for a full-stack developer who can adapt an existing "
    "code base for a new national research data service and deploy it in a Canadian cloud environment, "
    "while understanding the academic research context it serves. That is close to the work I did "
    "programming the data acquisition pipeline for the national CCNA longitudinal dementia study, and "
    "later leading data governance for one of Canada's leading brain imaging research centres.",

    "CRKN's network of 88 member institutions negotiates for equitable access to research and builds "
    "shared digital infrastructure, from the Canadiana collections to national data services like RAiD. "
    "I spent five years representing my institution on Portage, CONP, and the Research Data Alliance, "
    "the governance ecosystem that fed directly into what is now the Digital Research Alliance of "
    "Canada, so I understand both the researcher-facing side of a service like RAiD and the "
    "multi-institutional coordination behind it.",

    "At McGill, my development and infrastructure work included:",

    "I want to be direct about where my background does not line up cleanly with your posting. My "
    "production experience is in PHP, JavaScript, and Python rather than Java or TypeScript "
    "specifically, and I have not worked hands-on in the persistent identifier ecosystem before. My "
    "degree is in Cognitive Science rather than computer science, though it included computational "
    "modeling coursework and has sat alongside two decades of hands-on development work, which is the "
    "kind of equivalent combination your posting says it will consider. What I can point to instead is "
    "a track record of picking up new stacks under real deadlines, container-based deployment and Linux "
    "administration experience that map directly onto Docker and Kubernetes, and a first-hand "
    "understanding of the researchers RAiD is built to serve.",

    "I am based in Montreal, open to Ottawa or fully remote work, and bilingual in French and English. "
    "I would welcome the opportunity to discuss how I would contribute to the RAiD service. Thank you "
    "for your consideration.",
]
COVER_BULLETS = [
    "Programmed and maintained the LORIS-based data acquisition pipeline (PHP, MySQL, JavaScript) for the national CCNA dementia study, working as part of a small technical team",
    "Defined metadata standards and lifecycle policies for a national-scale research data environment supporting dozens of principal investigators and hundreds of researchers",
    "Built and deployed a self-serve OwnCloud portal and a Moodle-based education portal, maintaining both as production systems on Linux infrastructure",
    "Developed LMS features using LAMP++ and container-based deployment (LXD) for enterprise clients, evaluating new tools against real production constraints",
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
    _heading(doc, "Relevant Experience")
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
    doc.save("docx/cv_crkn_dataservices.docx")
    print("OK cv_crkn_dataservices.docx")


def build_docx_cover():
    doc = Document(); _margins(doc, top=2.0, bottom=2.0, left=2.5, right=2.5)
    _name_header(doc, NAME, COVER_CONTACT)
    _para(doc, COVER_DATE, size=10, space_after=12)
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(6)
    r = p.add_run(COVER_SUBJECT); r.bold = True; r.font.size = Pt(10)
    _para(doc, COVER_SALUTATION, size=10, space_after=6)
    for i, para in enumerate(COVER_PARAS):
        pp = doc.add_paragraph(); pp.paragraph_format.space_after = Pt(8)
        rr = pp.add_run(para); rr.font.size = Pt(10)
        if i == 2:
            for b in COVER_BULLETS:
                _bullet(doc, b)
    _para(doc, COVER_CLOSING, size=10, space_after=24)
    _para(doc, NAME, size=10)
    doc.save("docx/cover_crkn_dataservices.docx")
    print("OK cover_crkn_dataservices.docx")


# ==================================================================
# PDF RENDERING
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
                                 fontSize=10.5, leading=14, spaceAfter=7),
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
        if len(bl) <= 2:
            return [KeepTogether(header + [bullets(bl)])]
        out = [KeepTogether(header + [bullets(bl[:1])])]
        if len(bl) > 1:
            out.append(bullets(bl[1:]))
        return out

    story = [Paragraph(_esc(NAME), S["name"]),
             Paragraph(_esc(CV_CONTACT), S["contact"]),
             Paragraph(_esc(PROFILE), S["body"])]
    story += heading("Core Competencies")
    story.append(bullets([f"**{l}**{r}" for l, r in COMPETENCIES]))
    story += heading("Relevant Experience")
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

    _render("docx/cv_crkn_dataservices.pdf", story)


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
    for i, para in enumerate(COVER_PARAS):
        story.append(Paragraph(_esc(para), S["letter"]))
        if i == 2:
            story.append(ListFlowable(
                [ListItem(Paragraph(_esc(t), S["bullet"]), leftIndent=10, value="•") for t in COVER_BULLETS],
                bulletType="bullet", bulletColor=PDF_BLUE, leftIndent=12, bulletFontSize=8,
            ))
            story.append(Spacer(1, 4))
    story += [Spacer(1, 2),
              KeepTogether([Paragraph(_esc(COVER_CLOSING), S["body"]),
                            Spacer(1, 10),
                            Paragraph(_esc(NAME), S["body"])])]
    _render("docx/cover_crkn_dataservices.pdf", story, top=1.8, bottom=1.1, left=2.5, right=2.5)


if __name__ == "__main__":
    build_docx_cv()
    build_docx_cover()
    build_pdf_cv()
    build_pdf_cover()
    print("\nDone. Files in docx/")
