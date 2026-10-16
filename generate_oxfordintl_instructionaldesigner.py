"""
Generate application docs for Oxford International (Oxford International Career
Colleges) - Digital Education and Instructional Designer. Canada (campus city
not stated in posting; OICC operates campuses in Halifax, Toronto, and
Vancouver, none in Montreal). Full-time. $63,000/year.
Outputs (in docx/), per user request - ONE combined doc (cover + CV):
  - application_oxfordintl_instructionaldesigner.docx / .pdf

Content is defined ONCE below, then rendered to both docx (python-docx) and
pdf (reportlab) so the two formats never drift.

Targeting note: this is the strongest LMS/L&D fit found this run. CV leads
with instructional design, Moodle/LMS administration, and workshop delivery
(150 groups / 20 instructors at Sur Place Media) ahead of the data-governance
material, which is reframed as evidence of documentation/quality rigor rather
than led with.

GAPS, NAMED IN THE LETTER (never hidden or implied away):
  1. No hands-on Articulate 360 (Storyline/Rise) experience - the posting's
     specific authoring-tool requirement. Ted's e-learning/multimedia
     experience is Adobe suite + Moodle content authoring, not Articulate.
  2. No formal instructional design certification (asset, not required).
  3. No prior career-college / regulated vocational-education environment
     (an "asset" in the posting, not a stated requirement).
  4. Campus city unstated in the posting; OICC's Canadian campuses (Halifax,
     Toronto, Vancouver) do not include Montreal - relocation or full remote
     status is unconfirmed and named as an open question for Ted to raise.

Company facts used in the letter (OICC campuses/programs, Great Place to Work
certification in Canada) were verified independently via WebSearch and
WebFetch against oxfordinternationaleducationgroup.com and
oxfordinternational.com, not from the posting text itself.
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
    "Instructional designer and learning-technology specialist with a decade of experience turning "
    "specialist content into clear, engaging learning experiences and administering the LMS platforms "
    "that deliver them. Designed and delivered instructional programming across 150 workshop groups "
    "with a team of 20 instructors, then rebuilt that programming for virtual delivery during the "
    "pandemic. Administered and developed on Moodle across three organizations, most recently "
    "coordinating LMS solutions for government clients. Builds accessible, learner-centred materials "
    "and manages instructional-design projects from scoping through implementation and review. "
    "Bilingual (EN/FR), Montreal-based, open to relocation anywhere in Canada."
)

COMPETENCIES = [
    ("Instructional design and project management",
     ": ran instructional-design projects end to end, from content scoping with subject matter "
     "experts through development, implementation, and review, across 150 workshop groups with "
     "20 instructors and multiple government LMS deployments"),
    ("Adult learning and learner-centred design",
     ": designed and delivered data management and open science training that translated technical "
     "concepts into practice for non-specialist adult learners; certified in community engagement "
     "(CSCCE)"),
    ("Learning management system (LMS) administration and development",
     ": administered and developed Moodle across three organizations, including course structure, "
     "user roles and access, content upload, troubleshooting, and regulatory compliance for "
     "government deployments; built LMS features using LAMP++, Moodle, and LXD"),
    ("Digital and multimedia content development",
     ": produced videos, podcasts, and other multimedia learning content; skilled in the Adobe suite; "
     "built a Moodle-based self-serve education portal and a public online knowledge base"),
    ("Stakeholder collaboration",
     ": worked directly with subject matter experts to translate specialist content (neuroimaging "
     "research data, open science practice) into accessible materials for non-specialist audiences"),
    ("Data-informed continuous improvement",
     ": builds and analyzes program-effectiveness data (R, Python/pandas, Tableau) to guide "
     "iteration; strong documentation practice from five years of data governance work"),
    ("AI and emerging edtech tools",
     ": evaluated and adopted AI tools, including Claude Code, in enterprise learning contexts; "
     "practical prompt engineering for content development and workflow automation"),
    ("Bilingual EN/FR",
     ": professional working proficiency in French and English"),
]

# each: (dates, title, org, location, [bullets])
EXPERIENCE = [
    ("07/2025 - 01/2026", "Moodle Analyst", "Premergency Inc.", "Canada", [
        "Acted as lead coordinator between government clients and development teams to design and deliver bespoke LMS learning solutions, managing projects from scoping through implementation",
        "Migrated legacy LMS systems to Moodle and maintained regulatory compliance for government LMS deployments",
    ]),
    ("04/2017 - 08/2021", "Founder and Director", "Sur Place Media", "Montreal, QC", [
        "Designed and delivered instructional programming across 150 workshop groups with a team of 20 instructors at a community arts school, managing curriculum and scheduling across multiple concurrent programs",
        "Led a full redesign and pivot to virtual delivery during the COVID-19 pandemic, adapting all instructional materials and multimedia content for online engagement",
        "Produced videos, podcasts, and other multimedia learning content using the Adobe suite",
    ]),
    ("01/2024 - 10/2024", "Full Stack Developer", "KnowledgeOne", "Montreal, QC", [
        "Developed LMS features for active clients using LAMP++, Moodle, and LXD; evaluated and adopted AI tools including Claude Code in enterprise learning contexts",
    ]),
    ("09/2016 - 10/2021", "Manager of Data Resources", "McConnell Brain Imaging Centre, The Neuro, McGill University", "Montreal, QC", [
        "Designed and delivered training workshops that translated complex data-management concepts into day-to-day practice for researchers, and built a Moodle-based self-serve education portal",
        "Wrote data policy, documentation, and technical guides, and used engagement data to guide continuous improvement of training materials",
    ]),
    ("08/2020 - 10/2021", "Data Management and Sharing Coordinator (p/t)", "Tanenbaum Open Science Institute, The Neuro, McGill University", "Montreal, QC", [
        "Designed and administered training workshops for students and faculty on data management and open science practices",
        "Built a public-facing online knowledge base to educate the research community and public on open science concepts",
    ]),
]

ADDITIONAL = [
    "Photonic Knowledge - Database administrator and software developer (2012-2014)",
    "McGill Centre for Integrative Neuroscience - Software Developer, national CCNA dementia study (2015-2016)",
    "Kitikmeot Heritage Society - Researcher, writer, and producer (2010-2012)",
]

EDUCATION = [
    ("1998-2003", "Bachelor of Arts (Honours), Cognitive Science", "McGill University", "Montreal, QC",
     ["Minor: Music Technology. Topics: psycholinguistics, cognitive science, computational modeling of language."]),
    ("2021", "Scientific Community Engagement Fundamentals", "The Center for Scientific Collaboration and Community Engagement (CSCCE)", "", []),
]

PUBLICATIONS = [
    "Poline, J.-B., et al. (2023). Data and tools integration in the Canadian open neuroscience platform. Scientific Data, 10(1), 189.",
    "Halchenko, Y. O., et al. (2021). DataLad: distributed system for joint management of code, data, and their relationship. Journal of Open Source Software, 6(63), 3262.",
]
PUB_FOOT = "9 publications | citation count 630 | h-index 9 | Full list: scholar.google.com/citations"

# ------------------------------------------------------------------
# COVER LETTER
# ------------------------------------------------------------------

COVER_DATE = "September 28, 2026"
COVER_SUBJECT = "Subject: Application: Digital Education and Instructional Designer"
COVER_SALUTATION = "Dear Hiring Team,"
COVER_PARAS = [
    "I am applying for the Digital Education and Instructional Designer position at Oxford "
    "International Career Colleges. This role asks for exactly the combination I have built my "
    "career on: working closely with subject matter experts to turn specialist content into clear, "
    "engaging learning experiences, and administering the LMS that delivers them.",

    "At Sur Place Media, a neighbourhood arts school I founded and directed, I designed and delivered "
    "instructional programming across 150 workshop groups with a team of 20 instructors, then led a "
    "full pivot to virtual delivery during the pandemic, rebuilding materials for online engagement "
    "under real time pressure. Since then, my LMS and instructional-design work has continued "
    "directly:",

    "I have designed adult-learning training in a research setting, at the McConnell Brain Imaging "
    "Centre and the Tanenbaum Open Science Institute, and in a vocational LMS setting, most recently "
    "coordinating between government clients and development teams as Moodle Analyst at Premergency. "
    "Across both, my pattern has been the same: work with the expert who holds the content, and build "
    "the learning experience and the platform around them.",

    "Two honest notes. I have not built e-learning modules in Articulate 360 specifically; my "
    "content-development and multimedia experience runs through Moodle authoring and the Adobe suite, "
    "and I would expect to pick up Storyline and Rise quickly given how much of the underlying design "
    "work transfers. I also have not worked inside a regulated career-college environment before, "
    "though I have maintained regulatory compliance for government LMS deployments, which is the "
    "closest analogue in my record.",

    "Oxford International's Great Place to Work certification in Canada, and the growth of Oxford "
    "International Career Colleges' campuses here, suggest an organization investing in the people "
    "who deliver its programs, which matters to me. I am bilingual in French and English and open to "
    "relocation anywhere in Canada; the posting does not name a campus city, so I would welcome "
    "clarification on that and on remote-work options. Thank you for your consideration.",
]
COVER_BULLETS = [
    "Administered and developed Moodle across three organizations: course structure, user roles and access, content upload, troubleshooting, and regulatory compliance for government deployments",
    "Coordinated instructional-design projects from scoping through implementation, working directly with subject matter experts, most recently on government learning-platform deployments",
    "Built a Moodle-based self-serve education portal and a public online knowledge base, translating specialist content for non-specialist adult learners",
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


def build_docx_cv(doc=None):
    standalone = doc is None
    if standalone:
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
    if standalone:
        doc.save("docx/cv_oxfordintl_instructionaldesigner.docx")
        print("OK cv_oxfordintl_instructionaldesigner.docx")


def build_docx_cover(doc=None):
    standalone = doc is None
    if standalone:
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
    if standalone:
        doc.save("docx/cover_oxfordintl_instructionaldesigner.docx")
        print("OK cover_oxfordintl_instructionaldesigner.docx")


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


def build_pdf_cv(story_only=False):
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

    if story_only:
        return story
    _render("docx/cv_oxfordintl_instructionaldesigner.pdf", story)


def build_pdf_cover(story_only=False):
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
    if story_only:
        return story
    _render("docx/cover_oxfordintl_instructionaldesigner.pdf", story, top=1.8, bottom=1.1, left=2.5, right=2.5)


# ==================================================================
# COMBINED (single doc: cover letter + CV), per user request
# ==================================================================
def build_docx_combined():
    from docx.enum.section import WD_SECTION
    doc = Document(); _margins(doc, top=2.0, bottom=2.0, left=2.5, right=2.5)
    build_docx_cover(doc)
    sec = doc.add_section(WD_SECTION.NEW_PAGE)
    sec.top_margin, sec.bottom_margin = Cm(1.5), Cm(1.5)
    sec.left_margin, sec.right_margin = Cm(2.0), Cm(2.0)
    build_docx_cv(doc)
    doc.save("docx/application_oxfordintl_instructionaldesigner.docx")
    print("OK application_oxfordintl_instructionaldesigner.docx")


def build_pdf_combined():
    from reportlab.platypus import NextPageTemplate, PageBreak
    cover = build_pdf_cover(story_only=True)
    cv = build_pdf_cv(story_only=True)
    path = "docx/application_oxfordintl_instructionaldesigner.pdf"
    doc = BaseDocTemplate(path, pagesize=letter)
    f_cover = Frame(2.5 * cm, 1.1 * cm, letter[0] - 5.0 * cm, letter[1] - 2.9 * cm, id="cover")
    f_cv = Frame(2.0 * cm, 1.3 * cm, letter[0] - 4.0 * cm, letter[1] - 2.8 * cm, id="cv")
    doc.addPageTemplates([PageTemplate(id="cover", frames=[f_cover]),
                          PageTemplate(id="cv", frames=[f_cv])])
    doc.build(cover + [NextPageTemplate("cv"), PageBreak()] + cv)
    print("OK application_oxfordintl_instructionaldesigner.pdf")


if __name__ == "__main__":
    build_docx_combined()
    build_pdf_combined()
    print()
    print("Done. Files in docx/")
