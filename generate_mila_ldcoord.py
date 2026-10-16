"""
Generate application docs for Mila - Quebec Artificial Intelligence Institute,
Coordonnateur.trice, Apprentissage et developpement. Montreal (Mile-Ex). Full-time.
Posting: https://ca.linkedin.com/jobs/view/coordonnateur-trice-apprentissage-et-d%C3%A9veloppement-at-mila-quebec-artificial-intelligence-institute-4475830752
Outputs (in docx/):
  - cv_mila_ldcoord.docx    / .pdf   (English CV)
  - cover_mila_ldcoord.docx / .pdf   (French cover letter, as the posting is in French)

Content is defined ONCE below, then rendered to both docx (python-docx) and
pdf (reportlab) so the two formats never drift.

Targeting note: coordination and program operations lead, backed by training
design and LMS administration. Genuine gaps, stated plainly: titles on the CV are
more senior and more technical than a coordinator role; no HR-team L&D
experience; Google Workspace and survey tools are not on the profile and are not
claimed.

Company facts used in the cover letter were verified independently on Mila's own
site (mila.quebec/en and education.mila.quebec), not from the posting text:
more than 1,400 researchers, more than 140 affiliated professors from eight
universities, and the TRAIL (Trustworthy and Responsible AI Learning) program
among its education programs for researchers, industry and policy-makers.

Gender-neutral French throughout: Ted's pronouns are not recorded, so no
gendered adjectives or participles refer to the writer.
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
    "Learning and development professional who coordinates training programs end to end and runs the "
    "learning platforms behind them. Ran 150 workshop groups with 20 instructors as founder and director "
    "of an arts school, designed and administered training workshops for faculty and graduate students at "
    "McGill's Tanenbaum Open Science Institute, and launched a Moodle-based self-serve education portal for "
    "a research centre. Experienced with LMS administration, vendor and stakeholder coordination, and the "
    "logistics of in-person, virtual, and on-demand delivery. Bilingual (EN/FR), Montreal-based."
)

COMPETENCIES = [
    ("Program coordination and operations",
     ": ran 150 workshop groups end to end, owning curriculum scheduling, budget, invoicing, purchasing, "
     "venue, and vendor logistics; led a full pivot to virtual delivery during the pandemic"),
    ("Training design and delivery support",
     ": designed and administered training workshops on data management and open science for graduate "
     "students and faculty; in-person, virtual, and on-demand formats; certified in Scientific Community "
     "Engagement Fundamentals (CSCCE)"),
    ("Learning management systems",
     ": Moodle administration and development, learning experience design (LXD), legacy LMS migration, "
     "SSO and LDAP integration; built a Moodle-based self-serve education portal serving dozens of "
     "research groups"),
    ("Facilitator, vendor, and partner liaison",
     ": recruited, scheduled, and coached 20 instructors; coordinated between clients and development "
     "teams; represented a research centre on national committees (Portage, CONP, RDA)"),
    ("Adult learning and communication",
     ": grounding in learning and language from a cognitive science degree (psycholinguistics); wrote a "
     "public knowledge base and instructional text for mixed technical and non-technical readers; "
     "builds communities of practice instead of issuing rules"),
    ("AI tooling and adoption",
     ": evaluated and adopted AI tools in enterprise learning contexts, including Claude Code, weighing "
     "data handling and confidentiality alongside productivity"),
]

# each: (dates, title, org, location, [bullets]) - ordered by relevance, not chronology
EXPERIENCE = [
    ("04/2017 – 08/2021", "Founder and Director", "Sur Place Media", "Montreal, QC", [
        "Founded and ran a neighbourhood arts school, recruiting, scheduling, and coaching 20 instructors across 150 workshop groups",
        "Owned program operations end to end: curriculum scheduling, budgeting, invoicing, purchasing, venue, and vendor logistics",
        "Led a full pivot to virtual delivery during the pandemic, reworking in-person formats for remote audiences",
    ]),
    ("08/2020 – 10/2021", "Data Management & Sharing Coordinator (p/t)", "Tanenbaum Open Science Institute, The Neuro, McGill University", "Montreal, QC", [
        "Designed and administered training workshops on data management and open science for graduate students and faculty",
        "Built a public online knowledge base explaining open science concepts to non-specialists, used as on-demand material alongside the live sessions",
    ]),
    ("09/2016 – 10/2021", "Manager of Data Resources", "McConnell Brain Imaging Centre, The Neuro, McGill University", "Montreal, QC", [
        "Designed and launched a Moodle-based self-serve education portal that replaced repetitive one-to-one instruction with curriculum available on demand to dozens of research groups",
        "Drove adoption through hands-on training and communities of practice rather than compliance rules",
        "Led data governance for one of Canada's leading brain imaging centres, defining metadata standards and stewardship workflows",
        "Represented the centre on national research data bodies (Portage, CONP, RDA), coordinating shared standards across Canadian institutions",
    ]),
    ("07/2025 – 01/2026", "Moodle Analyst", "Premergency Inc.", "Canada", [
        "Coordinated between government clients and development teams to build LMS solutions and migrate legacy platforms to Moodle, maintaining regulatory compliance",
        "Designed bespoke learning and development solutions for client needs rather than from a fixed catalogue",
    ]),
    ("01/2024 – 10/2024", "Full Stack Developer", "KnowledgeOne", "Montreal, QC", [
        "Built learning platform features for active clients using Moodle, LAMP++, and learning experience design (LXD)",
        "Evaluated and adopted AI tools in enterprise learning contexts, including Claude Code, weighing data handling and governance implications",
    ]),
    ("02/2015 – 09/2016", "Software Developer", "McGill Centre for Integrative Neuroscience, McGill University", "Montreal, QC", [
        "Programmed the data acquisition pipeline for the national CCNA longitudinal dementia study on the LORIS platform (PHP, MySQL, JavaScript)",
    ]),
]

ADDITIONAL = [
    "Photonic Knowledge: Database administrator and software developer (2012–2014), built a Drupal ERP system and its underlying data model for the mining exploration sector",
    "Moss Rehabilitation Hospital: Research software developer (2007–2010)",
    "University of Connecticut & Columbia University: Research assistant and software developer (2004–2008)",
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

COVER_DATE = "6 octobre 2026"
COVER_SUBJECT = "Objet : Candidature au poste de coordonnateur·trice, apprentissage et développement"
COVER_SALUTATION = "Madame, Monsieur,"
COVER_PARAS = [
    "Je pose ma candidature au poste de coordonnateur·trice, apprentissage et développement. Votre "
    "affichage décrit le travail qui fait qu'un programme d'apprentissage se déroule sans accroc : "
    "inscriptions, facilitateurs, fournisseurs, plateforme, suivis. J'ai fait ce travail en milieu de "
    "recherche à Montréal, des deux côtés, celui de la conception et celui de l'exploitation.",

    "Mila réunit plus de 1 400 chercheurs et plus de 140 professeurs affiliés issus de huit universités, "
    "et offre des programmes de formation à la recherche, à l'industrie et aux décideurs, dont TRAIL, "
    "consacré à l'IA digne de confiance et responsable. Un public aussi varié demande une coordination "
    "qui rend chaque séance simple à suivre pour les participants et sans surprise pour les "
    "facilitateurs. J'ai l'expérience de ce travail et je veux l'exercer dans une communauté de "
    "recherche.",

    "À l'Institut Tanenbaum de science ouverte de l'Université McGill, j'ai conçu et administré des "
    "ateliers de formation pour des étudiants et des professeurs, puis bâti la base de connaissances en "
    "ligne qui les accompagnait. Au Centre d'imagerie cérébrale McConnell, j'ai lancé un portail éducatif "
    "libre-service sur Moodle, et je connais les LMS de l'intérieur, de l'administration à la migration. "
    "J'ai aussi fondé et dirigé une école d'arts de quartier : j'y ai recruté et encadré 20 enseignants "
    "et organisé 150 groupes d'ateliers, du calendrier au budget, en passant par les lieux et les "
    "fournisseurs, puis mené le passage complet à la prestation virtuelle pendant la pandémie.",

    "Je veux être direct sur deux points. Mes derniers titres sont plus techniques et plus seniors que "
    "celui d'un poste de coordination, et je n'ai pas travaillé au sein d'une équipe RH ou de "
    "développement des personnes. Je cherche ce poste parce que l'apprentissage en est le cœur, et "
    "parce qu'une coordination soignée détermine si une formation atteint son public.",

    "Je suis bilingue (français et anglais) et je vis à Montréal. Je me réjouis à l'idée d'en discuter "
    "avec vous, et je vous remercie de votre attention.",
]
COVER_CLOSING = "Veuillez agréer, Madame, Monsieur, mes salutations distinguées,"

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
    r2 = p.add_run(f"  |  {org}"); r2.font.size = Pt(10.5); r2.font.color.rgb = GRAY
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
    doc.save("docx/cv_mila_ldcoord.docx")
    print("OK cv_mila_ldcoord.docx")


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
    doc.save("docx/cover_mila_ldcoord.docx")
    print("OK cover_mila_ldcoord.docx")


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
                f'<font color="#555555">&nbsp;&nbsp;|&nbsp;&nbsp;{_esc(org)}{loc}</font>')
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

    _render("docx/cv_mila_ldcoord.pdf", story)


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
    _render("docx/cover_mila_ldcoord.pdf", story, top=1.8, bottom=1.1, left=2.5, right=2.5)


if __name__ == "__main__":
    build_docx_cv()
    build_docx_cover()
    build_pdf_cv()
    build_pdf_cover()
    print("\nDone. Files in docx/")
