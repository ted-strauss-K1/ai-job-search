"""
Generate application docs for McGill University — Research Data Management
Specialist, McGill Libraries (Research & Scholarship unit / Digital Research
Services team). Academic Associate or Senior Academic Associate (Unranked
Contract Academic Staff), 3-year term with possibility of renewal. Redpath
Library, Montreal. Salary commensurate with experience (no range posted).
Req JR0000080513. No submission deadline stated; anticipated interviews
Nov 9-20, 2026.
Outputs (in docx/):
  - cv_mcgill_rdmspecialist.docx     / .pdf
  - cover_mcgill_rdmspecialist.docx  / .pdf

Content is defined ONCE below, then rendered to both docx (python-docx) and
pdf (reportlab) so formats never drift.

CRITICAL GAP, ADDRESSED DIRECTLY (per Ted's explicit instruction, not hidden
or implied away): the posting's first Required selection criterion is a
"Ph.D. in a research data-focused discipline." Ted holds a B.A. (Honours),
not a doctorate, and the posting states no equivalency clause. The cover
letter names this gap in its own paragraph rather than burying it, and
argues applied RDM leadership + national committee service + peer-reviewed
co-authorship (citation count 630, h-index 9) as the offered alternative.
Nothing in the CV implies a doctorate is held.

Targeting note: Professional Experience is reordered by relevance, not
strict reverse-chronological (matching the precedent set in
generate_mcgill_webapp.py) - McConnell and TOSI (McGill RDM/open-science
work) lead, ahead of the more recent but less relevant Premergency/
KnowledgeOne roles. Sur Place Media is promoted out of "Additional
Experience" because "designing and delivering instruction, workshops...
educational resources" is a Required selection criterion and the 150
workshop groups / 20 instructors detail speaks to it directly.

Publications list is longer than usual (4 vs. the usual 2-3) because
scholarly engagement is a genuine, relevant strength here, not padding -
this is an academic-track appointment.

Company facts used in the cover letter (Digital Research Services Hub as a
joint VP-Research/Libraries/IT initiative, its RDM/research-software/
computing-infrastructure mandate, and its link to the Digital Research
Alliance of Canada) were verified independently via WebFetch against
mcgill.ca/drs/ - not from the job posting text itself. Posting text itself
was pulled directly from McGill's own Workday API
(mcgill.wd3.myworkdayjobs.com), not the LinkedIn aggregator copy.

OUTSTANDING BEFORE SUBMISSION: the posting requires "the names and
addresses of three referees" as part of the application package - this is
not the CV's standard "available upon request" footer. Real referee names
and contact details are needed from Ted before this application is
complete; none are fabricated here.
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
    "Research data management practitioner with a decade of applied leadership inside Canada's "
    "academic and open-science ecosystem, most recently building and running the RDM program at the "
    "McConnell Brain Imaging Centre (McGill University). Represented the institution nationally through "
    "Portage, the Canadian Open Neuroscience Platform, and the Research Data Alliance, work that "
    "intersects directly with the Digital Research Alliance of Canada's national mandate. Co-author on "
    "peer-reviewed data-infrastructure publications including DataLad (JOSS) and the Canadian Open "
    "Neuroscience Platform (Scientific Data); citation count 630, h-index 9. Designed and delivered RDM "
    "and open science training at the Tanenbaum Open Science Institute. Bilingual (EN/FR), "
    "Montreal-based, McGill alumnus."
)

COMPETENCIES = [
    ("Research data management consultation",
     ": advised principal investigators and research teams on data management planning, curation, "
     "deposit, and sharing across a leading brain imaging research centre"),
    ("RDM instruction and training design",
     ": designed and delivered data management and open science workshops; built a Moodle-based "
     "self-serve education portal and led instructional programming across 150 workshop groups with a "
     "team of 20 instructors"),
    ("Open science, FAIR data, and national RDM partnerships",
     ": represented McGill on Portage, CONP, and the Research Data Alliance, the ecosystem the Digital "
     "Research Alliance of Canada now coordinates nationally"),
    ("Scholarly research engagement",
     ": 9 peer-reviewed publications on data infrastructure and open science, including DataLad (JOSS) "
     "and the Canadian Open Neuroscience Platform (Scientific Data); citation count 630, h-index 9"),
    ("Data stewardship and repository infrastructure",
     ": launched a self-serve OwnCloud data portal and deployed Collibra for institutional data "
     "cataloguing and governance tracking"),
    ("Equity, diversity, and Indigenous data governance",
     ": direct grounding in CARE Principles for Indigenous Data Governance through work with the "
     "Kitikmeot Heritage Society; embedded EDI commitments across every training program designed"),
    ("Bilingual EN/FR",
     ": professional working proficiency in French and English, Montreal-based"),
]

# each: (dates, title, org, location, [bullets]) — ordered by relevance to this posting
EXPERIENCE = [
    ("09/2016 - 10/2021", "Manager of Data Resources", "McConnell Brain Imaging Centre, The Neuro, McGill University", "Montreal, QC", [
        "Provided expert consultation on data management planning, curation, and sharing to dozens of principal investigators and hundreds of researchers across a leading brain imaging research centre",
        "Designed and delivered RDM training workshops and built a Moodle-based self-serve education portal to embed data management practices into daily research workflows",
        "Represented the institution nationally on Portage, the Canadian Open Neuroscience Platform (CONP), and the Research Data Alliance, work that connects directly to the Digital Research Alliance of Canada's national RDM mandate",
        "Developed metadata standards, data acquisition policies, and a self-serve OwnCloud portal for institution-wide data stewardship",
        "Deployed Collibra for institutional data cataloguing and governance tracking",
    ]),
    ("08/2020 - 10/2021", "Data Management and Sharing Coordinator (p/t)", "Tanenbaum Open Science Institute, The Neuro, McGill University", "Montreal, QC", [
        "Designed and administered training workshops for students and faculty on data management and open science practices, directly supporting the launch of a new academic open science unit",
        "Built a public-facing knowledge base to educate the research community and public on FAIR data principles and open science concepts",
    ]),
    ("04/2017 - 08/2021", "Founder and Director", "Sur Place Media", "Montreal, QC", [
        "Designed and delivered instructional programming across 150 workshop groups with a team of 20 instructors at a community arts school",
        "Led a full pivot to virtual delivery during the COVID-19 pandemic, adapting all instructional materials for online engagement",
    ]),
    ("07/2025 - 01/2026", "Moodle Analyst", "Premergency Inc.", "Canada", [
        "Coordinated between government clients and development teams on LMS solutions, maintaining regulatory compliance for public-sector deployments",
        "Migrated legacy LMS systems to Moodle and designed bespoke learning solutions",
    ]),
    ("01/2024 - 10/2024", "Full Stack Developer", "KnowledgeOne", "Montreal, QC", [
        "Developed LMS features for active clients using LAMP++, Moodle, and LXD container-based deployment",
    ]),
]

ADDITIONAL = [
    "McGill Centre for Integrative Neuroscience — Software Developer (2015-2016): programmed the LORIS-based data acquisition pipeline for the national CCNA longitudinal dementia study (PHP, MySQL, JavaScript)",
    "Photonic Knowledge — Database Administrator and Software Developer (2012-2014): built a Drupal ERP system and its underlying data model for the mining exploration sector",
    "Language Mate; Moss Rehabilitation Hospital; University of Connecticut; Columbia University; Universität Bremen — research assistant and software developer roles (2003-2010)",
]

EDUCATION = [
    ("1998-2003", "B.A. (Honours), Cognitive Science", "McGill University", "Montreal, QC",
     ["Minor: Music Technology. Topics: psycholinguistics, cognitive science, computational modeling of language."]),
    ("2021", "Scientific Community Engagement Fundamentals", "CSCCE", "", []),
]

PUBLICATIONS = [
    "Halchenko, Y. O., et al. (2024). HeuDiConv — flexible DICOM conversion into structured directory layouts. Journal of Open Source Software, 9(99), 5839.",
    "Poline, J.-B., et al. (2023). Data and tools integration in the Canadian open neuroscience platform. Scientific Data, 10(1), 189.",
    "Halchenko, Y. O., et al. (2021). DataLad: distributed system for joint management of code, data, and their relationship. JOSS, 6(63), 3262.",
    "Strauss, T. (2021). Data Management Plan Template: Neuroimaging in the Neurosciences. Zenodo. doi:10.5281/zenodo.4673558",
]
PUB_FOOT = "9 publications | citation count 630 | h-index 9 | Full list: scholar.google.com/citations"

# ------------------------------------------------------------------
# COVER LETTER
# ------------------------------------------------------------------

COVER_DATE = "September 24, 2026"
COVER_SUBJECT = "Subject: Application: Research Data Management Specialist (JR0000080513)"
COVER_SALUTATION = "Dear Members of the Search Committee,"
COVER_PARAS = [
    "I am writing to express my interest in the Research Data Management Specialist position with the "
    "Digital Research Services team at McGill Libraries. For five years I built and led the practical "
    "equivalent of this role at McGill, as Manager of Data Resources at the McConnell Brain Imaging "
    "Centre, before moving briefly into learning and development work. This is less a new direction "
    "than a return to work I know well.",

    "At the McConnell Brain Imaging Centre and the Tanenbaum Open Science Institute, I supported dozens "
    "of principal investigators and hundreds of researchers directly:",

    "I want to address directly where my background does not match the posting on paper. I hold a B.A. "
    "(Honours) in Cognitive Science, not the Ph.D. your posting lists as a required qualification. What "
    "I can offer instead is nine years of applied RDM leadership inside a research-intensive "
    "institution, national committee service shaping RDM policy, and peer-reviewed data-infrastructure "
    "co-authorship (citation count 630, h-index 9). If the committee considers equivalent experience "
    "against the stated credential, I would welcome that conversation.",

    "The Digital Research Services Hub's mandate, spanning RDM, research software, and computing "
    "infrastructure across the Libraries, IT, and the Office of the Vice-Principal (Research and "
    "Innovation), matches how I have worked throughout my career: as a translator between technical "
    "systems and the researchers who depend on them. My work with the Kitikmeot Heritage Society also "
    "gave me direct grounding in the CARE Principles for Indigenous Data Governance.",

    "I am bilingual in French and English, based in Montreal, and McGill is where I built this career. "
    "I would welcome the opportunity to bring it back to the Libraries. Thank you for your "
    "consideration.",
]
COVER_BULLETS = [
    "Consulted on data management plans, curation, deposit, and sharing",
    "Designed and delivered RDM and open science training workshops, and built a Moodle-based self-serve education portal",
    "Represented the institution on Portage, CONP, and the Research Data Alliance, and co-authored peer-reviewed infrastructure publications including DataLad (JOSS) and the Canadian Open Neuroscience Platform (Scientific Data)",
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
    _heading(doc, "References")
    _para(doc, "Available upon request.", size=10)
    doc.save("docx/cv_mcgill_rdmspecialist.docx")
    print("OK cv_mcgill_rdmspecialist.docx")


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
        if i == 1:
            for b in COVER_BULLETS:
                _bullet(doc, b)
    _para(doc, COVER_CLOSING, size=10, space_after=24)
    _para(doc, NAME, size=10)
    doc.save("docx/cover_mcgill_rdmspecialist.docx")
    print("OK cover_mcgill_rdmspecialist.docx")


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
    story += heading("References")
    story.append(Paragraph("Available upon request.", S["body"]))

    _render("docx/cv_mcgill_rdmspecialist.pdf", story)


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
        if i == 1:
            story.append(ListFlowable(
                [ListItem(Paragraph(_esc(t), S["bullet"]), leftIndent=10, value="•") for t in COVER_BULLETS],
                bulletType="bullet", bulletColor=PDF_BLUE, leftIndent=12, bulletFontSize=8,
            ))
            story.append(Spacer(1, 4))
    story += [Spacer(1, 2),
              KeepTogether([Paragraph(_esc(COVER_CLOSING), S["body"]),
                            Spacer(1, 10),
                            Paragraph(_esc(NAME), S["body"])])]
    _render("docx/cover_mcgill_rdmspecialist.pdf", story, top=1.8, bottom=1.1, left=2.5, right=2.5)


if __name__ == "__main__":
    build_docx_cv()
    build_docx_cover()
    build_pdf_cv()
    build_pdf_cover()
    print("\nDone. Files in docx/")
