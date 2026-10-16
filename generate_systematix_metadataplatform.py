"""
Generate the combined application for Systematix: Ingenieur(e) de Plateforme
Gouvernance des Donnees & Metadonnees. Montreal, hybrid, full-time, long-term mandate.
Source: LinkedIn job 4475464959.

Output (in docx/): systematix_metadataplatform_application.docx / .pdf
  Page 1   : cover letter in FRENCH (posting requires French)
  Pages 2-3: CV in ENGLISH (per CV-language policy)

Content is defined ONCE below, then rendered to docx (python-docx) and pdf
(reportlab) so formats never drift.

Targeting: leads with metadata/governance platform work (Collibra, SSO/LDAP,
pipelines, stewardship workflows) and the training/adoption dimension the
posting lists. Genuine gaps stated plainly in the letter and NOT claimed on the
CV: Microsoft Purview, Unity Catalog, Azure Databricks, governance at
enterprise scale, metadata-coverage dashboards.

Company facts used in the letter were verified on systematix.com (fetched
2026-10-08): "for over 50 years", supports government organizations and private
enterprises, consulting areas include Intelligence & Analytics and AI &
Automation, Montreal office. NOT used: 800+ consultants / office count, to keep
the letter short; anything from search snippets or the LinkedIn posting links.
"""
import os

os.makedirs("docx", exist_ok=True)

NAME = "Ted Strauss"
CV_CONTACT = "Montreal, Quebec, Canada  |  514-475-2374  |  ted.strauss@gmail.com  |  linkedin.com/in/tedstrauss-63b01821"
COVER_CONTACT = "Montréal (Québec)  |  514-475-2374  |  ted.strauss@gmail.com  |  linkedin.com/in/tedstrauss-63b01821"

# ------------------------------------------------------------------
# COVER LETTER (FRENCH)
# ------------------------------------------------------------------
COVER_DATE = "8 octobre 2026"
COVER_SUBJECT = "Objet : Candidature au poste d'ingénieur(e) de plateforme, gouvernance des données et métadonnées"
COVER_SALUTATION = "Madame, Monsieur,"
COVER_PARAS = [
    "Je pose ma candidature au poste d'ingénieur de plateforme en gouvernance des données et métadonnées, "
    "un mandat à long terme à Montréal. Ce poste combine l'administration d'une plateforme de catalogage et "
    "l'accompagnement des équipes qui s'en servent, deux volets que j'ai réunis pendant cinq ans comme "
    "gestionnaire des ressources de données au Centre d'imagerie cérébrale McConnell (The Neuro, Université "
    "McGill), l'un des principaux centres d'imagerie cérébrale au Canada.",

    "Systematix accompagne depuis plus de 50 ans des organisations publiques et des entreprises privées, et "
    "son offre comprend l'analytique et l'automatisation et l'IA. Un mandat qui relie gouvernance, analytique "
    "avancée et IA repose sur une chose : des métadonnées fiables et bien documentées avant que les modèles "
    "ne s'en servent. C'est le travail de fond que je sais faire et que je veux faire.",

    "Au Centre McConnell, j'ai défini les normes de métadonnées, les flux de stewardship et les politiques de "
    "cycle de vie des données pour des dizaines de chercheurs principaux et des centaines de chercheurs. J'ai "
    "travaillé avec Collibra, OwnCloud, LDAP et l'authentification unique (SSO) pour gérer l'accès, les rôles "
    "et la gestion de données en libre-service, et j'ai développé les pipelines de données d'imagerie et les "
    "politiques du flux d'acquisition quotidien, en équipe Agile. J'ai aussi représenté le centre au sein de "
    "Portage, du CONP et de la Research Data Alliance. Ce que les propriétaires de données font réellement "
    "avec une plateforme dépend de la formation et de l'accompagnement qu'ils reçoivent, et c'est pourquoi "
    "j'ai conçu des ateliers, une base de connaissances publique et des communautés de pratique autour des "
    "outils que je mettais en place. Plus récemment, j'ai évalué et adopté des outils d'IA en contexte "
    "d'entreprise, dont Claude Code, en tenant compte de la gouvernance des données.",

    "Je veux être direct sur les limites de mon profil. Mon expérience de gouvernance s'est construite en "
    "recherche plutôt que dans une grande entreprise, et je n'ai pas encore utilisé Microsoft Purview, "
    "Unity Catalog ni Azure Databricks en production. Collibra, SQL, Python, Git, l'infonuagique (AWS, Azure) "
    "et l'administration des accès me donnent une base solide pour les aborder, et je prévois de monter en "
    "compétence sur votre environnement dès le début du mandat.",

    "Je suis bilingue en français et en anglais, avec une compétence professionnelle dans les deux langues, "
    "et je vis à Montréal. J'aimerais discuter de la façon dont je pourrais contribuer à vos mandats de "
    "gouvernance des données. Merci de considérer ma candidature.",
]
COVER_CLOSING = "Veuillez agréer, Madame, Monsieur, mes salutations distinguées,"

# ------------------------------------------------------------------
# CV (ENGLISH)
# ------------------------------------------------------------------
PROFILE = (
    "Data governance and metadata specialist who has built and run the stewardship workflows, access "
    "controls and data pipelines behind one of Canada's leading brain imaging research centres "
    "(McConnell Brain Imaging Centre, The Neuro, McGill University). Defined metadata standards and "
    "lifecycle policies, worked with Collibra, SSO and LDAP, and contributed to national data governance "
    "bodies (Portage, CONP, RDA). Pairs platform-level technical skills (Python, SQL, Git, Docker, AWS/Azure) "
    "with training and adoption work that gets data owners using governance tools. Bilingual (EN/FR), "
    "Montreal-based."
)

COMPETENCIES = [
    ("Data governance and metadata management",
     ": defined metadata standards (FAIR principles), stewardship workflows, and data lifecycle "
     "policies for a national-scale research data environment"),
    ("Governance and cataloging tools",
     ": worked with Collibra alongside OwnCloud, LDAP, and SSO to support access, roles, and self-serve "
     "data management across research groups"),
    ("Data pipelines and automation",
     ": developed brain imaging data pipelines and policies for a daily acquisition workflow; built "
     "data applications in LAMP++, Python, R, and SQL; version control with Git"),
    ("Security, roles, and permissions",
     ": SSO, LDAP, Active Directory, and identity provider configuration; Docker and Kubernetes; "
     "AWS and Azure cloud exposure"),
    ("AI and data governance",
     ": evaluated and adopted AI tools in enterprise settings, including Claude Code, assessing data "
     "handling and governance implications alongside the productivity case"),
    ("Training and adoption",
     ": designed workshops, a public knowledge base, and communities of practice so that data owners "
     "and stakeholders use governance tools in daily work; Agile delivery with multidisciplinary teams"),
]

# (dates, title, org, location, [bullets])
EXPERIENCE = [
    ("09/2016 – 10/2021", "Manager of Data Resources", "McConnell Brain Imaging Centre, The Neuro, McGill University", "Montreal, QC", [
        "Led data governance and metadata management for one of Canada's leading brain imaging centres, supporting dozens of principal investigators and hundreds of researchers",
        "Defined metadata standards, stewardship workflows, and data lifecycle policies, and built them into the daily acquisition workflow",
        "Worked across Collibra, OwnCloud, LDAP, and SSO to support access control, roles, and self-serve data management; launched an OwnCloud portal for researchers",
        "Developed brain imaging data pipelines and data-centric research applications in an Agile team",
        "Designed a Moodle-based self-serve education portal; contributed to national research policy through Portage, CONP, and Research Data Alliance committee work",
    ]),
    ("08/2020 – 10/2021", "Data Management and Sharing Coordinator (p/t)", "Tanenbaum Open Science Institute, The Neuro, McGill University", "Montreal, QC", [
        "Designed and administered training workshops on data management practices for faculty and graduate students",
        "Built an online knowledge base translating open science and data management requirements into practical guidance for non-specialists",
    ]),
    ("07/2025 – 01/2026", "Moodle Analyst", "Premergency Inc.", "Canada", [
        "Coordinated between client and development teams to deliver LMS solutions for government clients",
        "Managed regulatory compliance requirements for government LMS deployments; migrated legacy LMS systems to Moodle",
    ]),
    ("01/2024 – 10/2024", "Full Stack Developer", "KnowledgeOne", "Montreal, QC", [
        "Developed LMS features for active clients in LAMP++, Moodle, and LXD",
        "Evaluated and adopted AI tools in enterprise learning contexts, including Claude Code",
    ]),
]

ADDITIONAL = [
    "McGill Centre for Integrative Neuroscience, Software Developer (2015–2016): built the data acquisition pipeline for the national CCNA longitudinal dementia study on the LORIS platform (PHP, MySQL, JavaScript)",
    "Sur Place Media, Founder and Director (2017–2021): founded and ran a neighbourhood arts school hosting 150 workshop groups with 20 teachers; led the pivot to virtual delivery during COVID-19",
    "Photonic Knowledge, Database Administrator and Software Developer (2012–2014): built a Drupal ERP system and its data model for the mining exploration sector",
]

EDUCATION = [
    ("1998–2003", "B.A. (Honours), Cognitive Science", "McGill University", "Montreal, QC",
     ["Minor: Music Technology. Topics: psycholinguistics, cognitive science, computational modeling of language."]),
    ("2021", "Scientific Community Engagement Fundamentals", "CSCCE", "", []),
]

PUBLICATIONS = [
    "Poline, J.-B., et al. (2023). Data and tools integration in the Canadian open neuroscience platform. Scientific Data, 10(1), 189.",
    "Halchenko, Y. O., et al. (2021). DataLad: distributed system for joint management of code, data, and their relationship. JOSS, 6(63), 3262.",
    "Strauss, T. (2021). Data Management Plan Template: Neuroimaging in the Neurosciences. Zenodo. doi:10.5281/zenodo.4673558",
]
PUB_FOOT = "9 publications | citation count 630 | h-index 9 | Full list: scholar.google.com/citations"
LANG_LINE = "English (native), French (bilingual, professional working proficiency)."
SKILLS_LINE = ("Collibra, SQL, Python, R, Git, Docker, Kubernetes, AWS, Azure, SSO, LDAP, Active Directory, "
               "Moodle, OwnCloud, Drupal, Tableau, Agile/Scrum.")

OUT = "docx/systematix_metadataplatform_application"

# ==================================================================
# DOCX RENDERING
# ==================================================================
from docx import Document
from docx.shared import Pt, RGBColor, Inches, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

BLUE = RGBColor(0x21, 0x6F, 0xAA)
BLACK = RGBColor(0x00, 0x00, 0x00)
GRAY = RGBColor(0x55, 0x55, 0x55)


def _name_header(doc, name, contact):
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(name); r.bold = True; r.font.size = Pt(26); r.font.color.rgb = BLUE
    p2 = doc.add_paragraph(); p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r2 = p2.add_run(contact); r2.font.size = Pt(9.5); r2.font.color.rgb = GRAY
    p2.paragraph_format.space_after = Pt(6)


def _heading(doc, title):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10); p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(title.upper()); r.bold = True; r.font.size = Pt(11); r.font.color.rgb = BLUE
    pPr = p._p.get_or_add_pPr(); pBdr = OxmlElement('w:pBdr'); bottom = OxmlElement('w:bottom')
    bottom.set(qn('w:val'), 'single'); bottom.set(qn('w:sz'), '6')
    bottom.set(qn('w:space'), '1'); bottom.set(qn('w:color'), '216FAA')
    pBdr.append(bottom); pPr.append(pBdr)


def _bullet(doc, text, indent=0.25):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_before = Pt(1); p.paragraph_format.space_after = Pt(1)
    p.paragraph_format.left_indent = Inches(indent)
    for i, part in enumerate(text.split('**')):
        if not part:
            continue
        r = p.add_run(part); r.font.size = Pt(10); r.bold = (i % 2 == 1)


def _entry(doc, dates, title, org, location, bullets):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(6); p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.keep_with_next = True
    r1 = p.add_run(title); r1.bold = True; r1.font.size = Pt(10.5)
    r2 = p.add_run(f" | {org}"); r2.font.size = Pt(10.5); r2.font.color.rgb = GRAY
    if location:
        r3 = p.add_run(f", {location}"); r3.font.size = Pt(10.5); r3.font.color.rgb = GRAY
    p2 = doc.add_paragraph()
    p2.paragraph_format.space_before = Pt(0); p2.paragraph_format.space_after = Pt(2)
    p2.paragraph_format.keep_with_next = bool(bullets)
    r4 = p2.add_run(dates); r4.italic = True; r4.font.size = Pt(9.5); r4.font.color.rgb = GRAY
    for b in bullets:
        _bullet(doc, b)


def _para(doc, text, size=10, italic=False, color=None, space_after=4):
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(space_after)
    r = p.add_run(text); r.font.size = Pt(size); r.italic = italic
    if color:
        r.font.color.rgb = color
    return p


def build_docx():
    doc = Document()
    for s in doc.sections:
        s.top_margin, s.bottom_margin = Cm(1.6), Cm(1.5)
        s.left_margin, s.right_margin = Cm(2.2), Cm(2.2)
    # --- page 1: French cover letter ---
    _name_header(doc, NAME, COVER_CONTACT)
    _para(doc, COVER_DATE, size=10.5, space_after=10)
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(6)
    r = p.add_run(COVER_SUBJECT); r.bold = True; r.font.size = Pt(10.5)
    _para(doc, COVER_SALUTATION, size=10.5, space_after=6)
    for para in COVER_PARAS:
        pp = doc.add_paragraph(); pp.paragraph_format.space_after = Pt(7)
        pp.add_run(para).font.size = Pt(10.5)
    _para(doc, COVER_CLOSING, size=10.5, space_after=14)
    _para(doc, NAME, size=10.5)
    # --- pages 2-3: English CV ---
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
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
    _heading(doc, "Technical Skills")
    _para(doc, SKILLS_LINE, size=10)
    _heading(doc, "Languages")
    _para(doc, LANG_LINE, size=10)
    _heading(doc, "Selected Publications")
    for pub in PUBLICATIONS:
        _bullet(doc, pub)
    _para(doc, PUB_FOOT, size=9, italic=True, color=GRAY)
    doc.save(OUT + ".docx")
    print("OK", OUT + ".docx")


# ==================================================================
# PDF RENDERING
# ==================================================================
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, PageBreak,
    HRFlowable, ListFlowable, ListItem, KeepTogether,
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

PDF_BLUE = HexColor("#216FAA")
PDF_GRAY = HexColor("#555555")


def _esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _bold_md(t):
    parts = _esc(t).split("**")
    return "".join(f"<b>{p}</b>" if i % 2 == 1 else p for i, p in enumerate(parts))


def _styles():
    s = getSampleStyleSheet()
    return {
        "name": ParagraphStyle("Name", parent=s["Normal"], fontName="Helvetica-Bold",
                               fontSize=22, textColor=PDF_BLUE, alignment=TA_CENTER, spaceAfter=2, leading=26),
        "contact": ParagraphStyle("Contact", parent=s["Normal"], fontName="Helvetica",
                                  fontSize=9, textColor=PDF_GRAY, alignment=TA_CENTER, spaceAfter=8, leading=12),
        "heading": ParagraphStyle("Heading", parent=s["Normal"], fontName="Helvetica-Bold",
                                  fontSize=11, textColor=PDF_BLUE, spaceBefore=8, spaceAfter=2, leading=13),
        "body": ParagraphStyle("Body", parent=s["Normal"], fontName="Helvetica", fontSize=10,
                               leading=13, spaceAfter=3),
        "bullet": ParagraphStyle("Bullet", parent=s["Normal"], fontName="Helvetica",
                                 fontSize=9.5, leading=12, spaceAfter=1),
        "entry_title": ParagraphStyle("EntryTitle", parent=s["Normal"], fontName="Helvetica",
                                      fontSize=10.5, spaceBefore=5, spaceAfter=0, leading=12),
        "entry_dates": ParagraphStyle("EntryDates", parent=s["Normal"], fontName="Helvetica",
                                      fontSize=9, textColor=PDF_GRAY, spaceAfter=2, leading=11),
        "letter": ParagraphStyle("Letter", parent=s["Normal"], fontName="Helvetica",
                                 fontSize=10, leading=13.2, spaceAfter=6),
        "small_italic": ParagraphStyle("SmallItalic", parent=s["Normal"],
                                       fontName="Helvetica-Oblique", fontSize=8.5,
                                       textColor=PDF_GRAY, spaceAfter=2, leading=11),
    }


def _bullets(S, items, md=True):
    f = _bold_md if md else _esc
    return ListFlowable(
        [ListItem(Paragraph(f(t), S["bullet"]), leftIndent=10, value="•") for t in items],
        bulletType="bullet", bulletColor=PDF_BLUE, leftIndent=12, bulletFontSize=8,
    )


def build_pdf():
    S = _styles()

    def heading(text):
        return [Paragraph(_esc(text.upper()), S["heading"]),
                HRFlowable(width="100%", thickness=0.6, color=PDF_BLUE, spaceBefore=1, spaceAfter=3)]

    def entry(dates, title, org, location, bl):
        loc = f", {_esc(location)}" if location else ""
        head = (f'<b>{_esc(title)}</b>'
                f'<font color="#555555">&nbsp;|&nbsp;{_esc(org)}{loc}</font>')
        header = [Paragraph(head, S["entry_title"]), Paragraph(_esc(dates), S["entry_dates"])]
        if not bl:
            return [KeepTogether(header)]
        if len(bl) <= 2:
            return [KeepTogether(header + [_bullets(S, bl)])]
        return [KeepTogether(header + [_bullets(S, bl[:1])]), _bullets(S, bl[1:])]

    story = [Paragraph(_esc(NAME), S["name"]),
             Paragraph(_esc(COVER_CONTACT), S["contact"]),
             Spacer(1, 4),
             Paragraph(_esc(COVER_DATE), S["body"]),
             Spacer(1, 6),
             Paragraph(f"<b>{_esc(COVER_SUBJECT)}</b>", S["body"]),
             Spacer(1, 3),
             Paragraph(_esc(COVER_SALUTATION), S["letter"])]
    for para in COVER_PARAS:
        story.append(Paragraph(_esc(para), S["letter"]))
    story.append(KeepTogether([Paragraph(_esc(COVER_CLOSING), S["body"]),
                               Spacer(1, 8), Paragraph(_esc(NAME), S["body"])]))
    story.append(PageBreak())

    story += [Paragraph(_esc(NAME), S["name"]),
              Paragraph(_esc(CV_CONTACT), S["contact"]),
              Paragraph(_esc(PROFILE), S["body"])]
    story += heading("Core Competencies")
    story.append(_bullets(S, [f"**{l}**{r}" for l, r in COMPETENCIES]))
    story += heading("Relevant Experience")
    for e in EXPERIENCE:
        story += entry(*e)
    story += heading("Additional Experience")
    story.append(_bullets(S, ADDITIONAL))
    story += heading("Education")
    for e in EDUCATION:
        story += entry(*e)
    story += heading("Technical Skills")
    story.append(Paragraph(_esc(SKILLS_LINE), S["body"]))
    story += heading("Languages")
    story.append(Paragraph(_esc(LANG_LINE), S["body"]))
    story += heading("Selected Publications")
    story.append(_bullets(S, PUBLICATIONS, md=False))
    story.append(Paragraph(_esc(PUB_FOOT), S["small_italic"]))

    doc = BaseDocTemplate(OUT + ".pdf", pagesize=letter,
                          topMargin=1.5 * cm, bottomMargin=1.3 * cm,
                          leftMargin=2.2 * cm, rightMargin=2.2 * cm)
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="main")
    doc.addPageTemplates([PageTemplate(id="all", frames=[frame])])
    doc.build(story)
    print("OK", OUT + ".pdf")


if __name__ == "__main__":
    build_docx()
    build_pdf()
