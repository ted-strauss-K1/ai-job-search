"""
Generate application docs for McCarthy Tetrault — Manager, Learning and Development.
Montreal office (also posted for Toronto and Vancouver). Hybrid. Full-time.
Outputs (in docx/):
  - cv_mccarthy_ld.docx     / .pdf
  - cover_mccarthy_ld.docx  / .pdf

Content is defined ONCE below, then rendered to both docx (python-docx) and
pdf (reportlab) so the two formats never drift.

Targeting note: leads with AI-enabled learning, which is where the profile is
differentiated and where the firm is visibly investing, then backs it with
professional education delivery to expert adult audiences. Genuine gaps, stated
plainly and never hidden: no legal practice, no PD built for lawyers (three of
their profile bullets ask for this), and no instructional design certificate.

Spelling: Canadian conventions for this application — "program" not "programme",
"-ize" not "-ise", but "centre" and "catalogue" retained.

Company facts used in the cover letter were verified independently by search
(not from the posting text): the firm is co-developing "AI-Enabled Corporate
Practice: Business Law in Action" with Western University's Faculty of Law,
launching winter 2027, running students through simulated transactions and
AI-assisted drafting. NOT used as researched claims, because they appear only in
the posting itself: the "MT Academy" program name and the Top 100 Employers /
Best Diversity Employers streaks.
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
    "Learning and development specialist who designs professional education for expert adult audiences "
    "and builds the platforms it runs on. Designed and delivered training for faculty, principal "
    "investigators, and government clients; launched a Moodle-based self-serve education portal at "
    "McGill University; recruited and coached 20 instructors across 150 workshop groups as founder and "
    "director of an arts school. Evaluates and adopts AI tooling in enterprise and regulated settings, "
    "including Claude Code, weighing data handling and confidentiality alongside the productivity case. "
    "Bilingual (EN/FR), Montreal-based."
)

# (bold label, remaining text) — label is emphasised
COMPETENCIES = [
    ("AI-enabled learning and technology adoption",
     ": evaluated and adopted AI tools in enterprise and regulated learning contexts, including Claude "
     "Code, assessing data handling, confidentiality, and governance implications alongside productivity; "
     "translated technical workflows into training non-specialists could act on"),
    ("Professional education design and delivery",
     ": designed and delivered professional development programs for faculty, graduate students, "
     "principal investigators, and government clients; in-person, virtual, blended, and e-learning "
     "formats; facilitation of live sessions backed by on-demand material; certified in Scientific "
     "Community Engagement Fundamentals (CSCCE)"),
    ("Instructional design and curriculum development",
     ": built curriculum for audiences of experts who had not asked for training, working from capability "
     "requirements rather than an off-the-shelf catalogue; grounding in adult learning from a cognitive "
     "science degree focused on psycholinguistics; wrote instructional text for mixed technical and "
     "non-technical readers"),
    ("Learning platforms and instructional technology",
     ": Moodle administration and development, learning experience design (LXD), legacy LMS migration, "
     "LAMP++ development, SSO and LDAP integration; Drupal and WordPress; Adobe suite; MS Teams"),
    ("Faculty, SME, and stakeholder collaboration",
     ": recruited, scheduled, and coached 20 instructors; gathered and validated content from subject "
     "matter experts who did not report to me; coordinated between clients and development teams; briefed "
     "institutional leadership and national committees"),
    ("Program operations and team leadership",
     ": ran 150 workshop groups end to end, owning curriculum scheduling, budget, venue, vendor logistics, "
     "and delivery; led a full pivot to virtual delivery during the pandemic; managed regulatory "
     "compliance obligations on public-sector learning deployments"),
]

# each: (dates, title, org, location, [bullets])  — ordered by relevance, not chronology
EXPERIENCE = [
    ("07/2025 – 01/2026", "Moodle Analyst", "Premergency Inc.", "Canada", [
        "Ran needs assessments with government clients to identify capability gaps, then designed bespoke learning and development solutions against them rather than from a fixed catalogue",
        "Coordinated between clients and development teams to build LMS solutions and migrate legacy platforms to Moodle, maintaining the regulatory compliance obligations public-sector deployments carry",
    ]),
    ("01/2024 – 10/2024", "Full Stack Developer", "KnowledgeOne", "Montreal, QC", [
        "Built learning platform features for active clients using Moodle, LAMP++, and learning experience design (LXD)",
        "Evaluated and adopted AI tools in enterprise learning contexts, weighing data handling and governance implications alongside the productivity case",
    ]),
    ("08/2020 – 10/2021", "Data Management & Sharing Coordinator (p/t)", "Tanenbaum Open Science Institute, The Neuro, McGill University", "Montreal, QC", [
        "Designed and administered training workshops on data management and open science for graduate students and faculty, an audience of experts with no patience for generic training",
        "Built a public online knowledge base explaining specialist concepts to non-specialists, used as on-demand material alongside the live sessions",
    ]),
    ("09/2016 – 10/2021", "Manager of Data Resources", "McConnell Brain Imaging Centre, The Neuro, McGill University", "Montreal, QC", [
        "Designed and launched a Moodle-based self-serve education portal that replaced repetitive one-to-one instruction with curriculum available on demand to dozens of research groups",
        "Drove adoption as a literacy problem rather than a compliance one, building communities of practice through hands-on training instead of issuing rules",
        "Led data governance for one of Canada's leading brain imaging centres, defining metadata standards and the policies covering classification, retention, and access",
        "Represented the centre on national research data bodies (Portage, CONP, RDA), contributing to shared standards across Canadian research institutions",
    ]),
    ("04/2017 – 08/2021", "Founder and Director", "Sur Place Media", "Montreal, QC", [
        "Founded and ran a neighbourhood arts school, recruiting, scheduling, and coaching 20 instructors across 150 workshop groups",
        "Owned program operations end to end: curriculum scheduling, budgeting, invoicing, purchasing, venue, and vendor logistics",
        "Led a full pivot to virtual delivery during the pandemic, reworking in-person formats for remote audiences",
    ]),
    ("02/2015 – 09/2016", "Software Developer", "McGill Centre for Integrative Neuroscience, McGill University", "Montreal, QC", [
        "Programmed the data acquisition pipeline for the national CCNA longitudinal dementia study on the LORIS platform (PHP, MySQL, JavaScript)",
    ]),
]

ADDITIONAL = [
    "Photonic Knowledge — Database administrator and software developer (2012–2014): built a Drupal ERP system and its underlying data model for the mining exploration sector",
    "Moss Rehabilitation Hospital — Research software developer (2007–2010)",
    "University of Connecticut & Columbia University — Research assistant and software developer (2004–2008)",
]

EDUCATION = [
    ("1998–2003", "B.A. (Honours), Cognitive Science", "McGill University", "Montreal, QC",
     ["Minor: Music Technology. Topics: psycholinguistics, cognitive science, computational modeling of language, music technology."]),
    ("2021", "Scientific Community Engagement Fundamentals", "CSCCE", "", []),
]

PUBLICATIONS = [
    "Strauss, T. (2021). Data Management Plan Template: Neuroimaging in the Neurosciences. Zenodo. doi:10.5281/zenodo.4673558",
    "Poline, J.-B., et al. (2023). Data and tools integration in the Canadian open neuroscience platform. Scientific Data, 10(1), 189.",
]
PUB_FOOT = "9 publications | citation count 630 | h-index 9 | Full list: scholar.google.com/citations"

COVER_DATE = "August 7, 2026"
COVER_SUBJECT = "Subject: Application: Manager, Learning and Development (Montreal)"
COVER_SALUTATION = "Dear Hiring Manager,"
COVER_PARAS = [
    "I am applying for the Manager, Learning and Development position in your Montreal office. The "
    "posting describes two jobs held together: designing professional education across the lawyer "
    "development continuum, and building the AI-enabled learning that now has to sit inside it. I have "
    "spent the last several years on both halves, and the second is the harder one to hire for.",

    "The AI half is where I would be strongest. You are asking someone to translate Client Service "
    "Delivery workflows into learning experiences, to design AI-supported simulations and adaptive "
    "tools, and to identify which human skills matter more as AI absorbs drafting work. I have "
    "evaluated and adopted AI tooling in enterprise and regulated settings, including Claude Code, and I "
    "assess data handling and confidentiality alongside the productivity case before anything reaches "
    "users. In a firm where privilege sets the boundary on what a tool may touch, that is not optional. "
    "The course you are co-developing with Western University's Faculty of Law, running students through "
    "simulated transactions and AI-assisted drafting, is a firm treating AI literacy as curriculum "
    "rather than as a tool rollout. That is the work I want to do.",

    "On the education half, I have designed and delivered professional development for experts who did "
    "not ask for training. At McGill's Tanenbaum Open Science Institute I designed and ran workshops for "
    "faculty and graduate students and built the on-demand knowledge base behind them. At the McConnell "
    "Brain Imaging Centre I launched a Moodle-based education portal that replaced repetitive one-to-one "
    "instruction with curriculum. And I founded and directed an arts school where I recruited, "
    "scheduled, and coached 20 instructors across 150 workshop groups, owning budget, venue, and "
    "logistics end to end, and led a full pivot to virtual delivery during the pandemic.",

    "Two things to be straight about. I have not practised law and have not built professional "
    "development for lawyers, which three of your profile bullets ask for. What I have done is teach "
    "principal investigators, faculty, and government clients: expert audiences who are time-poor, "
    "skeptical of mandatory training, and quick to disengage from a session that is not immediately "
    "useful. I think that transfers, and I would rather argue it than obscure it. I also hold no "
    "instructional design certificate. My grounding in adult learning is a cognitive science degree "
    "focused on psycholinguistics, plus a decade of designing programs that had to work.",

    "I am bilingual in French and English at professional working proficiency and based in Montreal. I "
    "would welcome the opportunity to discuss how I would build AI literacy into MT Academy programming. "
    "Thank you for your consideration.",
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
    doc.save("docx/cv_mccarthy_ld.docx")
    print("OK cv_mccarthy_ld.docx")


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
    doc.save("docx/cover_mccarthy_ld.docx")
    print("OK cover_mccarthy_ld.docx")


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
        # Short entries stay whole; splitting a two-bullet entry across a page
        # break leaves a stranded second bullet at the top of the next page.
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

    _render("docx/cv_mccarthy_ld.pdf", story)


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
    story += [Spacer(1, 2),
              KeepTogether([Paragraph(_esc(COVER_CLOSING), S["body"]),
                            Spacer(1, 10),
                            Paragraph(_esc(NAME), S["body"])])]
    _render("docx/cover_mccarthy_ld.pdf", story, top=1.8, bottom=1.1, left=2.5, right=2.5)


if __name__ == "__main__":
    build_docx_cv()
    build_docx_cover()
    build_pdf_cv()
    build_pdf_cover()
    print("\nDone. Files in docx/")
