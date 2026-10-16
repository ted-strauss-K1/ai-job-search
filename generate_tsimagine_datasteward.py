"""
Generate application docs for TS Imagine — Data Product Steward, Data Office.
Montreal (on-site 4 days/week + 1 flexible). Full-time permanent.
Outputs (in docx/):
  - cv_tsimagine_datasteward.docx     / .pdf
  - cover_tsimagine_datasteward.docx  / .pdf

Content is defined ONCE below, then rendered to both docx (python-docx) and
pdf (reportlab) so the two formats never drift.

Targeting note: the role pairs classic data stewardship (definitions,
documentation, quality rules, root-cause analysis, stakeholder communication)
with AI enablement (Snowflake semantic layers, prompt engineering for AI
agents). CV leads with governance/stewardship depth at the Brain Imaging
Centre and the AI-adoption record (Claude Code). Snowflake and capital-markets
reference data acknowledged as gaps in the letter, never claimed.
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
    "Data governance and stewardship specialist with five years managing the data resources of "
    "McGill's McConnell Brain Imaging Centre: data definitions, documentation, quality "
    "control, and access management for sensitive research data serving dozens of principal "
    "investigators and hundreds of researchers. Published open science contributor (DataLad, "
    "Canadian Open Neuroscience Platform) with deep metadata and FAIR-principles practice. "
    "Hands-on prompt engineering and enterprise AI-tool adoption, including Claude Code. SQL "
    "grounded in a decade of LAMP-stack development and database administration. Bilingual "
    "(EN/FR), based in Montreal."
)

COMPETENCIES = [
    ("Data stewardship and domain ownership",
     ": five years of end-to-end stewardship for a leading brain imaging centre's data domains: "
     "business definitions, documentation, governance policy, quality control, and continuous improvement; "
     "the centre's trusted point of contact for data questions, requests, and issue resolution"),
    ("Data quality and root-cause analysis",
     ": built acquisition pipelines with data checks for daily research workflows; investigated "
     "data discrepancies back to their source across instruments, transformations, and human "
     "process, and coordinated fixes with engineers and researchers"),
    ("Metadata and semantic modeling",
     ": led metadata standards for neuroimaging data; hands-on FAIR practice through the Canadian "
     "Open Neuroscience Platform, which integrates distributed repositories under shared "
     "definitions and vocabularies; co-author of DataLad, a provenance and lineage system for "
     "research data; authored a published Data Management Plan template"),
    ("AI enablement and prompt engineering",
     ": evaluated and adopted AI tooling, including Claude Code, in enterprise learning contexts; "
     "practical prompt engineering for content generation and workflow automation; strong interest "
     "in grounding AI outputs in well-governed, clearly defined data"),
    ("Stakeholder communication",
     ": designed and delivered training that translates technical data practices into plain "
     "business language for non-specialists; represented the centre on national data-policy bodies "
     "(Portage, CONP, RDA); certified in community engagement (CSCCE)"),
    ("Technical toolkit",
     ": SQL across MySQL and PostgreSQL with database administration experience; Python (pandas), "
     "R, Git, Docker, Kubernetes, AWS and Azure; Collibra, OwnCloud, and LDAP/SSO administration"),
]

EXPERIENCE = [
    ("09/2016 – 10/2021", "Manager of Data Resources", "McConnell Brain Imaging Centre, The Neuro, McGill University", "Montreal, QC", [
        "Owned stewardship of the centre's research data domains, supporting dozens of principal investigators and hundreds of researchers working with sensitive multimodal data",
        "Maintained data definitions, documentation, and data-sharing policy; led metadata standards and quality practices from instrument output through storage and archiving",
        "Acted as the centre's point of contact for data requests, incidents, and access questions; designed and launched an OwnCloud self-serve portal, an internal data product that replaced manual data-request handling",
        "Investigated data discrepancies to root cause across acquisition pipelines and coordinated resolution with engineering and research teams",
        "Represented the centre on national research data bodies (Portage, CONP, RDA), aligning local practice with emerging national standards",
    ]),
    ("07/2025 – 01/2026", "Moodle Analyst", "Premergency Inc.", "Canada", [
        "Coordinated between government clients and development teams to deliver learning-platform solutions, maintaining regulatory compliance for government deployments",
    ]),
    ("01/2024 – 10/2024", "Full Stack Developer", "KnowledgeOne", "Montreal, QC", [
        "Evaluated and adopted AI tools including Claude Code in enterprise learning contexts; developed learning platform features for active clients (LAMP++, Moodle, LXD)",
    ]),
    ("08/2020 – 10/2021", "Data Management & Sharing Coordinator (p/t)", "Tanenbaum Open Science Institute, The Neuro, McGill University", "Montreal, QC", [
        "Designed and delivered research data management training for students and faculty, translating governance concepts into day-to-day practice",
    ]),
    ("2015–2016", "Software Developer, national CCNA dementia study", "McGill Centre for Integrative Neuroscience", "Montreal, QC", [
        "Programmed the data acquisition pipeline for a pan-Canadian longitudinal study on aging (LORIS platform: PHP, MySQL, JavaScript)",
    ]),
    ("04/2017 – 08/2021", "Founder and Director", "Sur Place Media", "Montreal, QC", [
        "Founded and directed a neighbourhood arts school; coordinated 20 instructors across 150 workshop groups, and led the pivot to virtual delivery during the pandemic",
    ]),
]

ADDITIONAL = [
    "Photonic Knowledge — Database administrator and software developer (2012–2014)",
    "Kitikmeot Heritage Society — Researcher, writer, and producer (2010–2012)",
]

EDUCATION = [
    ("1998–2003", "Bachelor of Arts (Honours), Cognitive Science", "McGill University", "Montreal, QC",
     ["Minor: Music Technology. Topics: psycholinguistics, cognitive science, computational modeling of language."]),
    ("2021", "Scientific Community Engagement Fundamentals", "The Center for Scientific Collaboration and Community Engagement (CSCCE)", "", []),
]

PUBLICATIONS = [
    "Poline, J.-B., et al. (2023). Data and tools integration in the Canadian open neuroscience platform. Scientific Data, 10(1), 189.",
    "Halchenko, Y. O., et al. (2021). DataLad: distributed system for joint management of code, data, and their relationship. Journal of Open Source Software, 6(63).",
    "Strauss, T. (2021). Data Management Plan Template: Neuroimaging in the Neurosciences. Zenodo. doi:10.5281/zenodo.4673558",
]
PUB_FOOT = "9 publications | citation count 630 | h-index 9 | Full list: scholar.google.com/citations"

COVER_DATE = "September 2, 2026"
COVER_SUBJECT = "Subject: Application: Data Product Steward, Data Office"
COVER_SALUTATION = "Dear Hiring Manager,"
COVER_PARAS = [
    "I am applying for the Data Product Steward position in TS Imagine's Data Office. The role "
    "sits at the intersection of two things I have spent my career on: getting data definitions "
    "exactly right, and making complex data usable by people who are not specialists. Extending "
    "that second audience to AI agents is the natural next step for stewardship.",

    "TS Imagine's approach is a large part of why I am applying. Grounding TSIQ in each client's "
    "own governed data, on a unified data layer with one shared set of business definitions, is a "
    "bet that trustworthy AI starts with trustworthy definitions. TSIQ's Explain tier, which "
    "grounds each response in deterministic calculations with evidence and lineage, makes that "
    "thesis visible: every definition a steward gets right becomes evidence a client can check.",

    "For five years I ran data stewardship in production at McGill's McConnell Brain Imaging "
    "Centre, serving dozens of principal investigators and hundreds of researchers working with "
    "sensitive data. I owned the definitions, documentation, and data-sharing policy for the "
    "centre's data domains, led its metadata standards, and investigated quality issues to root "
    "cause across instruments and pipelines. When manual request handling became a bottleneck, I designed and "
    "launched a self-serve data portal. My open science record backs the semantic side of "
    "the role: I contributed to the Canadian Open Neuroscience Platform, which integrates "
    "distributed repositories under shared definitions and vocabularies, and co-authored DataLad, "
    "a system for managing data with provenance tracking.",

    "On the AI side, I have evaluated and adopted AI tooling in enterprise settings since 2024, "
    "including Claude Code, and prompt engineering is part of my daily practice rather than an "
    "aspiration. I know from that work how much an agent's usefulness depends on the clarity of "
    "the definitions and context it is given.",

    "Two honest notes. My SQL depth comes from a decade of LAMP-stack development and database "
    "administration on MySQL and PostgreSQL rather than Snowflake, so the platform specifics "
    "would be new, though the modeling and query work underneath is not. With TS Imagine's data "
    "platform built on Snowflake through to Cortex-based AI, closing that gap fast would be my "
    "first priority. And capital markets would be a new domain for me: my "
    "stewardship experience comes from regulated, confidentiality-heavy research data. I learn "
    "domains through their data, and instrument reference data is well-structured territory to "
    "learn in. I am Montreal-based, the four-day on-site arrangement works for me, and I am "
    "bilingual in French and English.",

    "I would welcome the opportunity to discuss how disciplined stewardship can make TSIQ's "
    "answers more trustworthy. Thank you for your consideration.",
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
    doc.save("docx/cv_tsimagine_datasteward.docx")
    print("OK cv_tsimagine_datasteward.docx")


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
    doc.save("docx/cover_tsimagine_datasteward.docx")
    print("OK cover_tsimagine_datasteward.docx")


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

    _render("docx/cv_tsimagine_datasteward.pdf", story)


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
    story += [Spacer(1, 6),
              KeepTogether([Paragraph(_esc(COVER_CLOSING), S["body"]),
                            Spacer(1, 12),
                            Paragraph(_esc(NAME), S["body"])])]
    _render("docx/cover_tsimagine_datasteward.pdf", story, top=1.6, bottom=1.2, left=2.5, right=2.5)


if __name__ == "__main__":
    build_docx_cv()
    build_docx_cover()
    build_pdf_cv()
    build_pdf_cover()
    print("\nDone. Files in docx/")
