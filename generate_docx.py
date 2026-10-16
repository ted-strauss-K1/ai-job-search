"""
Generate DOCX versions of all 6 job application documents.
Output: docx/ directory
"""
from docx import Document
from docx.shared import Pt, RGBColor, Inches, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import os

os.makedirs("docx", exist_ok=True)

BLUE = RGBColor(0x21, 0x6F, 0xAA)
BLACK = RGBColor(0x00, 0x00, 0x00)
GRAY = RGBColor(0x55, 0x55, 0x55)

def set_margins(doc, top=1.5, bottom=1.5, left=2.0, right=2.0):
    for section in doc.sections:
        section.top_margin = Cm(top)
        section.bottom_margin = Cm(bottom)
        section.left_margin = Cm(left)
        section.right_margin = Cm(right)

def add_name_header(doc, name, contact):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(name)
    run.bold = True
    run.font.size = Pt(28)
    run.font.color.rgb = BLUE

    p2 = doc.add_paragraph()
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run2 = p2.add_run(contact)
    run2.font.size = Pt(10)
    run2.font.color.rgb = GRAY
    p2.paragraph_format.space_after = Pt(6)

def add_section_heading(doc, title):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(2)
    run = p.add_run(title.upper())
    run.bold = True
    run.font.size = Pt(11)
    run.font.color.rgb = BLUE
    # bottom border
    pPr = p._p.get_or_add_pPr()
    pBdr = OxmlElement('w:pBdr')
    bottom = OxmlElement('w:bottom')
    bottom.set(qn('w:val'), 'single')
    bottom.set(qn('w:sz'), '6')
    bottom.set(qn('w:space'), '1')
    bottom.set(qn('w:color'), '21' + '6F' + 'AA')
    pBdr.append(bottom)
    pPr.append(pBdr)

def add_job_entry(doc, dates, title, org, location, bullets):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(0)
    r1 = p.add_run(title)
    r1.bold = True
    r1.font.size = Pt(10.5)
    r1.font.color.rgb = BLACK
    r2 = p.add_run(f"  —  {org}")
    r2.font.size = Pt(10.5)
    r2.font.color.rgb = GRAY
    if location:
        r3 = p.add_run(f", {location}")
        r3.font.size = Pt(10.5)
        r3.font.color.rgb = GRAY

    p2 = doc.add_paragraph()
    p2.paragraph_format.space_before = Pt(0)
    p2.paragraph_format.space_after = Pt(2)
    r4 = p2.add_run(dates)
    r4.italic = True
    r4.font.size = Pt(9.5)
    r4.font.color.rgb = GRAY

    for b in bullets:
        bp = doc.add_paragraph(style='List Bullet')
        bp.paragraph_format.space_before = Pt(1)
        bp.paragraph_format.space_after = Pt(1)
        bp.paragraph_format.left_indent = Inches(0.25)
        # handle bold within bullet via ** markers
        parts = b.split('**')
        for i, part in enumerate(parts):
            if not part:
                continue
            r = bp.add_run(part)
            r.font.size = Pt(10)
            r.bold = (i % 2 == 1)

def add_bullet(doc, text, indent=0.25):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after = Pt(1)
    p.paragraph_format.left_indent = Inches(indent)
    parts = text.split('**')
    for i, part in enumerate(parts):
        if not part:
            continue
        r = p.add_run(part)
        r.font.size = Pt(10)
        r.bold = (i % 2 == 1)

def add_para(doc, text, size=10, italic=False, color=None, space_after=4):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(space_after)
    r = p.add_run(text)
    r.font.size = Pt(size)
    r.italic = italic
    if color:
        r.font.color.rgb = color
    return p

# ============================================================
# CV — Air Canada
# ============================================================

def cv_aircanada():
    doc = Document()
    set_margins(doc)
    add_name_header(doc, "Ted Strauss",
        "Montreal, Quebec, Canada  |  514-475-2374  |  ted.strauss@gmail.com  |  linkedin.com/in/tedstrauss-63b01821")

    add_para(doc, "Data governance and policy specialist with over a decade of experience across Canada's academic and research ecosystem. Led cross-institutional data stewardship at the McConnell Brain Imaging Centre (McGill University), developed governance frameworks aligned with national policy, and contributed to federal-level data strategy through Portage, CONP, and RDA committee work. Brings direct experience with Collibra, policy development, training delivery, and AI tool evaluation in enterprise contexts. Bilingual (EN/FR); 9 peer-reviewed publications; citation count 630; h-index 9.", size=10, space_after=6)

    add_section_heading(doc, "Core Competencies")
    add_bullet(doc, "**Data governance & stewardship**: metadata standards, data ownership frameworks, lifecycle management, FAIR principles, DMP authoring, Collibra, OwnCloud — operationalized governance programs for 100+ researchers at McGill University")
    add_bullet(doc, "**Policy development & compliance**: contributed to national RDM policy through Portage, CONP, and RDA; developed data acquisition and handling policies for high-throughput research workflows; managed regulatory compliance for government LMS deployments")
    add_bullet(doc, "**AI governance & responsible adoption**: evaluated and adopted AI tools in enterprise learning contexts; assessed governance implications including accountability, bias, and explainability; familiar with emerging AI governance frameworks and regulatory considerations")
    add_bullet(doc, "**Training delivery & L&D**: designed and administered training programs for faculty, students, and non-technical teams; built Moodle-based self-serve education portals; developed public-facing knowledge bases on data governance and open science")
    add_bullet(doc, "**Data infrastructure**: Collibra, OwnCloud, LAMP++ (Linux, Apache/Nginx, MySQL/PostgreSQL, PHP, JavaScript), SSO, LDAP, Docker, AWS, Azure; R, Python (pandas, plotly), Tableau")
    add_bullet(doc, "**Stakeholder engagement**: cross-institutional collaboration, national committee representation, bilingual (EN/FR) facilitation, change management, Agile/Scrum")

    add_section_heading(doc, "Professional Experience")
    add_job_entry(doc, "07/2025 – 01/2026", "Moodle Analyst", "Premergency Inc.", "Canada", [
        "Coordinated between government clients and development teams to deploy LMS solutions meeting regulatory compliance requirements",
        "Managed legacy LMS migrations to Moodle; designed bespoke learning & development solutions for government programs",
    ])
    add_job_entry(doc, "01/2024 – 10/2024", "Full Stack Developer", "KnowledgeOne", "Montreal, QC", [
        "Developed LMS features for active clients on the eConcordia Moodle platform (LAMP++, LXD)",
        "Evaluated and integrated AI tools into enterprise learning contexts, assessing responsible adoption and governance implications",
    ])
    add_job_entry(doc, "09/2016 – 10/2021", "Manager of Data Resources", "McConnell Brain Imaging Centre, The Neuro, McGill University", "Montreal, QC", [
        "Led data governance, metadata standards, and stewardship workflows for one of Canada's leading brain imaging centres, supporting dozens of PIs and hundreds of researchers",
        "Developed and enforced data acquisition and handling policies for daily neuroimaging workflows; managed data quality measures across research pipelines",
        "Launched OwnCloud portal for self-serve data management; deployed Collibra for institutional data cataloguing and governance tracking",
        "Contributed to national research data policy through Portage, CONP, and RDA committee work; co-authored governance and data sharing frameworks adopted at the national level",
        "Designed a Moodle-based self-serve education portal and administered training workshops to build data literacy across research teams",
    ])
    add_job_entry(doc, "08/2020 – 10/2021", "Data Management & Sharing Coordinator (p/t)", "Tanenbaum Open Science Institute, The Neuro, McGill University", "Montreal, QC", [
        "Designed and delivered training workshops on data management and responsible open science practices for students, faculty, and research teams",
        "Built a public-facing knowledge base on open science concepts, data governance, and FAIR principles",
    ])
    add_job_entry(doc, "04/2017 – 08/2021", "Founder and Director", "Sur Place Media", "Montreal, QC", [
        "Founded and operated a neighbourhood arts school; hosted 150 workshop groups with 20 instructors; led a successful pivot to fully virtual delivery during the COVID-19 pandemic",
    ])
    add_job_entry(doc, "02/2015 – 09/2016", "Software Developer", "McGill Centre for Integrative Neuroscience, McGill University", "Montreal, QC", [
        "Programmed the data acquisition pipeline for the national CCNA study on aging and the brain using the LORIS platform (PHP, MySQL, JavaScript); contributed to national longitudinal research infrastructure",
    ])

    add_section_heading(doc, "Additional Experience")
    add_bullet(doc, "Language Mate — Developer and UX designer (2007–2010)")
    add_bullet(doc, "Moss Rehabilitation Hospital — Research software developer (2007–2010)")
    add_bullet(doc, "University of Connecticut — Research assistant & software developer (2005–2008)")
    add_bullet(doc, "Columbia University & Universität Bremen — Research assistant (2003–2005)")

    add_section_heading(doc, "Education")
    add_job_entry(doc, "1998–2003", "B.A. (Honours), Cognitive Science", "McGill University", "Montreal, QC", [
        "Minor: Music Technology. Topics: Psycholinguistics, cognitive science, computational modeling of language.",
    ])
    add_job_entry(doc, "2021", "Scientific Community Engagement Fundamentals", "CSCCE", "", [])

    add_section_heading(doc, "Languages")
    add_para(doc, "English (native), French (bilingual).", size=10)

    add_section_heading(doc, "Selected Publications")
    add_bullet(doc, "Poline, J.-B., et al. (2023). Data and tools integration in the Canadian open neuroscience platform. Scientific Data, 10(1), 189.")
    add_bullet(doc, "Halchenko, Y. O., et al. (2021). DataLad: distributed system for joint management of code, data, and their relationship. JOSS, 6(63), 3262.")
    add_bullet(doc, "Strauss, T. (2021). Data Management Plan Template: Neuroimaging in the Neurosciences. Zenodo. doi:10.5281/zenodo.4673558")
    add_para(doc, "Citation count: 630 | h-index: 9 | Full list: scholar.google.com/citations", size=9, italic=True, color=GRAY)

    add_section_heading(doc, "References")
    add_para(doc, "Available upon request.", size=10)

    doc.save("docx/cv_aircanada.docx")
    print("✓ cv_aircanada.docx")

# ============================================================
# CV — CAE
# ============================================================

def cv_cae():
    doc = Document()
    set_margins(doc)
    add_name_header(doc, "Ted Strauss",
        "Montreal, Quebec, Canada  |  514-475-2374  |  ted.strauss@gmail.com  |  linkedin.com/in/tedstrauss-63b01821")

    add_para(doc, "Data governance leader with over a decade of experience designing and implementing data stewardship programs across Canada's academic and research ecosystem. Led governance at the McConnell Brain Imaging Centre (McGill University), managing metadata standards, data quality measures, and stewardship policies for dozens of research teams. Contributed to national data governance strategy through Portage, CONP, and RDA committee work. Combines technical infrastructure depth with a practitioner record in stakeholder engagement, data literacy program development, and cross-functional team coordination. Bilingual (EN/FR); 9 peer-reviewed publications; citation count 630; h-index 9.", size=10, space_after=6)

    add_section_heading(doc, "Core Competencies")
    add_bullet(doc, "**Data governance leadership**: designed and implemented governance frameworks, data ownership accountability structures, metadata standards, and stewardship policies at institutional and national levels; 5+ years directing governance programs across multi-stakeholder research environments")
    add_bullet(doc, "**Stakeholder engagement & data literacy**: built communities of practice; embedded governance and data literacy into research workflows through education and change management rather than compliance enforcement; facilitated cross-institutional delivery nationally")
    add_bullet(doc, "**Data quality & pipeline management**: defined data quality measures and operational policies for high-throughput data acquisition workflows; managed data cataloguing with Collibra; DBA experience across SQL and NoSQL systems")
    add_bullet(doc, "**Team coordination & mentoring**: coordinated multi-stakeholder delivery at national scale (Portage, CONP, RDA); supervised research staff and junior data professionals; managed government client relationships for LMS regulatory compliance")
    add_bullet(doc, "**Data infrastructure**: Collibra, OwnCloud, LAMP++ (Linux, Apache/Nginx, MySQL/PostgreSQL, PHP, JavaScript), SSO, LDAP, Active Directory, Docker, cloud (AWS, Azure), ETL, data modeling")
    add_bullet(doc, "**Program management**: Agile/Scrum, change management, grant writing, regulatory compliance, bilingual (EN/FR) facilitation across government, academic, and enterprise contexts")

    add_section_heading(doc, "Professional Experience")
    add_job_entry(doc, "07/2025 – 01/2026", "Moodle Analyst", "Premergency Inc.", "Canada", [
        "Coordinated between government clients and development teams to deliver LMS solutions meeting regulatory compliance requirements; managed stakeholder expectations across client and technical teams",
        "Managed legacy LMS migrations to Moodle; designed bespoke learning & development solutions for clients",
    ])
    add_job_entry(doc, "01/2024 – 10/2024", "Full Stack Developer", "KnowledgeOne", "Montreal, QC", [
        "Developed LMS features for active clients on the eConcordia Moodle platform (LAMP++, LXD)",
        "Evaluated and adopted AI tools in enterprise learning contexts",
    ])
    add_job_entry(doc, "09/2016 – 10/2021", "Manager of Data Resources", "McConnell Brain Imaging Centre, The Neuro, McGill University", "Montreal, QC", [
        "Led data governance program for one of Canada's leading brain imaging centres, managing metadata standards, data ownership frameworks, and stewardship policies for dozens of PIs and hundreds of researchers",
        "Developed and enforced data quality measures and operational data acquisition policies for daily neuroimaging workflows across the centre's research pipelines",
        "Launched OwnCloud portal for self-serve data management; deployed Collibra for institutional data cataloguing; managed database administration across SQL and NoSQL systems",
        "Contributed to national research data governance policy through Portage, CONP, and RDA committee work; co-authored data sharing frameworks adopted at the federal level",
        "Designed a Moodle-based education portal and ran training workshops to build data literacy and governance awareness across diverse research teams",
    ])
    add_job_entry(doc, "08/2020 – 10/2021", "Data Management & Sharing Coordinator (p/t)", "Tanenbaum Open Science Institute, The Neuro, McGill University", "Montreal, QC", [
        "Supported launch of a new academic unit focused on Open Science; coordinated across faculty, students, and institutional stakeholders",
        "Designed and delivered training workshops on data management and governance practices; built a public-facing knowledge base on open science and FAIR data principles",
    ])
    add_job_entry(doc, "04/2017 – 08/2021", "Founder and Director", "Sur Place Media", "Montreal, QC", [
        "Founded and operated a neighbourhood arts school; hosted 150 workshop groups with 20 instructors; led full pivot to virtual delivery during the COVID-19 pandemic",
    ])
    add_job_entry(doc, "02/2015 – 09/2016", "Software Developer", "McGill Centre for Integrative Neuroscience, McGill University", "Montreal, QC", [
        "Programmed the data acquisition pipeline for the national CCNA longitudinal dementia study using the LORIS platform (PHP, MySQL, JavaScript); contributed to national research data infrastructure",
    ])

    add_section_heading(doc, "Additional Experience")
    add_bullet(doc, "Photonic Knowledge — Database administrator & software developer (2012–2014)")
    add_bullet(doc, "Language Mate — Developer and UX designer (2007–2010)")
    add_bullet(doc, "Moss Rehabilitation Hospital — Research software developer (2007–2010)")
    add_bullet(doc, "University of Connecticut & Columbia University — Research assistant & software developer (2004–2008)")

    add_section_heading(doc, "Education")
    add_job_entry(doc, "1998–2003", "B.A. (Honours), Cognitive Science", "McGill University", "Montreal, QC", [
        "Minor: Music Technology. Topics: Psycholinguistics, cognitive science, computational modeling of language.",
    ])
    add_job_entry(doc, "2021", "Scientific Community Engagement Fundamentals", "CSCCE", "", [])

    add_section_heading(doc, "Languages")
    add_para(doc, "English (native), French (bilingual).", size=10)

    add_section_heading(doc, "Selected Publications")
    add_bullet(doc, "Poline, J.-B., et al. (2023). Data and tools integration in the Canadian open neuroscience platform. Scientific Data, 10(1), 189.")
    add_bullet(doc, "Halchenko, Y. O., et al. (2021). DataLad: distributed system for joint management of code, data, and their relationship. JOSS, 6(63), 3262.")
    add_bullet(doc, "Strauss, T. (2021). Data Management Plan Template: Neuroimaging in the Neurosciences. Zenodo. doi:10.5281/zenodo.4673558")
    add_para(doc, "Citation count: 630 | h-index: 9 | Full list: scholar.google.com/citations", size=9, italic=True, color=GRAY)

    add_section_heading(doc, "References")
    add_para(doc, "Available upon request.", size=10)

    doc.save("docx/cv_cae.docx")
    print("✓ cv_cae.docx")

# ============================================================
# CV — Points
# ============================================================

def cv_points():
    doc = Document()
    set_margins(doc)
    add_name_header(doc, "Ted Strauss",
        "Montréal, Québec, Canada  |  514-475-2374  |  ted.strauss@gmail.com  |  linkedin.com/in/tedstrauss-63b01821")

    add_para(doc, "Learning & development specialist and LMS expert with experience across government, higher education, and enterprise environments. Built and operated Moodle-based training platforms for government and institutional clients; designed L&D programs for researchers, faculty, and professional teams; and championed LMS adoption as a performance and culture tool. Background spans Premergency Inc. (government Moodle deployments), KnowledgeOne/eConcordia (enterprise LMS development), and McConnell Brain Imaging Centre at McGill (self-serve researcher education portal). Bilingual (EN/FR); skilled in content design, micro-learning, and platform adoption strategy.", size=10, space_after=6)

    add_section_heading(doc, "Core Competencies")
    add_bullet(doc, "**LMS platform management**: Moodle administration, development, migration, and full-stack deployment across government, higher education, and enterprise contexts; platform ownership from architecture through user adoption; LXD, EdX")
    add_bullet(doc, "**Instructional design & content creation**: training program design for diverse audiences including researchers, government clients, faculty, and business teams; workshops, e-learning modules, knowledge bases, micro-learning, and blended formats")
    add_bullet(doc, "**L&D strategy & adoption**: positioned LMS as a strategic performance tool through stakeholder engagement and change management; driven adoption across complex organizations; communities of practice development")
    add_bullet(doc, "**Bilingual facilitation**: designed and delivered programs in French and English; managed bilingual LMS environments for government clients; bilingual content development and translation")
    add_bullet(doc, "**Technical stack**: Moodle, LXD, EdX, LAMP++ (Linux, Apache, MySQL, PHP, JavaScript), Microsoft Office, SharePoint, WordPress, Docker; multimedia production (Adobe suite, videography, podcasting)")
    add_bullet(doc, "**Analytics & continuous improvement**: measured LMS usage, adoption, and learning impact; adjusted L&D strategy based on field feedback; evaluated and adopted AI tools to enhance enterprise learning contexts")

    add_section_heading(doc, "Professional Experience")
    add_job_entry(doc, "07/2025 – 01/2026", "Moodle Analyst", "Premergency Inc.", "Canada", [
        "Acted as coordinator between government clients and development teams to deliver tailored LMS solutions; maintained regulatory compliance requirements throughout",
        "Managed full migrations of legacy LMS systems to Moodle, including data migration, configuration, and user onboarding",
        "Designed bespoke learning & development solutions aligned to client training objectives and compliance requirements",
    ])
    add_job_entry(doc, "01/2024 – 10/2024", "Full Stack Developer", "KnowledgeOne", "Montréal, QC", [
        "Developed and maintained LMS features for active clients on the eConcordia Moodle platform (LAMP++, LXD)",
        "Evaluated and adopted AI tools to enhance enterprise learning contexts; assessed usability, adoption pathways, and governance implications",
    ])
    add_job_entry(doc, "09/2016 – 10/2021", "Manager of Data Resources", "McConnell Brain Imaging Centre, The Neuro, McGill University", "Montréal, QC", [
        "Designed and deployed a Moodle-based self-serve education portal for researcher onboarding, reducing time-to-productivity for new research staff",
        "Managed data workflows and platforms for one of Canada's leading brain imaging centres, supporting dozens of PIs and hundreds of researchers",
        "Built and delivered training programs for non-specialist audiences on data management practices, platform usage, and open science workflows",
    ])
    add_job_entry(doc, "08/2020 – 10/2021", "Data Management & Sharing Coordinator (p/t)", "Tanenbaum Open Science Institute, The Neuro, McGill University", "Montréal, QC", [
        "Designed and administered training workshops for students, faculty, and research staff on data management and open science practices",
        "Built an online knowledge base to educate the public and research community about core open science concepts; developed content in both English and French",
        "Coordinated learning content across institutional stakeholders; facilitated adoption of new data practices through training rather than compliance",
    ])
    add_job_entry(doc, "04/2017 – 08/2021", "Founder and Director", "Sur Place Media", "Montréal, QC", [
        "Founded and operated a neighbourhood arts school offering workshops in creative writing, media arts, and visual arts",
        "Hosted 150 workshop groups with 20 instructors; managed programming, scheduling, and operations across a bilingual (EN/FR) learner community",
        "Led a successful and rapid pivot to fully virtual delivery during the COVID-19 pandemic, adapting all programming formats for online engagement",
    ])
    add_job_entry(doc, "02/2015 – 09/2016", "Software Developer", "McGill Centre for Integrative Neuroscience, McGill University", "Montréal, QC", [
        "Programmed the data acquisition pipeline for the national CCNA longitudinal study; contributed to research infrastructure development",
    ])

    add_section_heading(doc, "Additional Experience")
    add_bullet(doc, "Language Mate — Developer and UX designer (2007–2010)")
    add_bullet(doc, "Moss Rehabilitation Hospital — Research software developer (2007–2010)")
    add_bullet(doc, "University of Connecticut & Columbia University — Research assistant & software developer (2004–2008)")

    add_section_heading(doc, "Education")
    add_job_entry(doc, "1998–2003", "B.A. (Honours), Cognitive Science", "McGill University", "Montréal, QC", [
        "Minor: Music Technology. Topics: Psycholinguistics, cognitive science, computational modeling of language.",
    ])
    add_job_entry(doc, "2021", "Scientific Community Engagement Fundamentals", "CSCCE", "", [])

    add_section_heading(doc, "Languages")
    add_para(doc, "Anglais (langue maternelle), Français (bilingue).", size=10)

    add_section_heading(doc, "Selected Publications")
    add_bullet(doc, "Poline, J.-B., et al. (2023). Data and tools integration in the Canadian open neuroscience platform. Scientific Data, 10(1), 189.")
    add_bullet(doc, "Strauss, T. (2021). Data Management Plan Template: Neuroimaging in the Neurosciences. Zenodo. doi:10.5281/zenodo.4673558")
    add_para(doc, "9 publications | citation count: 630 | h-index: 9 | Full list: scholar.google.com/citations", size=9, italic=True, color=GRAY)

    add_section_heading(doc, "References")
    add_para(doc, "Available upon request.", size=10)

    doc.save("docx/cv_points.docx")
    print("✓ cv_points.docx")

# ============================================================
# Cover letter helper
# ============================================================

def make_cover_letter(doc, salutation, paragraphs, closing, date_str):
    set_margins(doc, top=2.0, bottom=2.0, left=2.5, right=2.5)
    add_name_header(doc, "Ted Strauss",
        "514-475-2374  |  ted.strauss@gmail.com  |  linkedin.com/in/tedstrauss-63b01821")

    add_para(doc, date_str, size=10, space_after=12)
    add_para(doc, salutation, size=10, space_after=6)

    for para in paragraphs:
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(8)
        r = p.add_run(para)
        r.font.size = Pt(10)

    add_para(doc, closing, size=10, space_after=24)
    add_para(doc, "Ted Strauss", size=10)

# ============================================================
# Cover Letter — Air Canada
# ============================================================

def cover_aircanada():
    doc = Document()
    make_cover_letter(doc,
        salutation="Dear Air Canada Hiring Team,",
        paragraphs=[
            "I am applying for the Specialist, Data & AI Governance position because it sits at the intersection of data stewardship and responsible technology adoption — the space where I have spent the last decade working across Canada's academic and research ecosystem.",
            "At the McConnell Brain Imaging Centre and Tanenbaum Open Science Institute at McGill University, I led governance programs for one of Canada's leading neuroimaging research environments, managing data ownership frameworks, metadata standards, and stewardship policies for dozens of principal investigators and hundreds of researchers. This work included deploying Collibra for institutional data cataloguing, contributing to national research data policy through Portage, CONP, and RDA committee work, and designing training programs to build data literacy across non-specialist research teams. The governance challenge I encountered most consistently was not technical: it was adoption. Getting researchers to internalize governance as a practice that protects and amplifies their work, rather than as a compliance burden, required sustained stakeholder engagement and a change-management approach. That framing maps directly to the kind of responsible AI governance program Air Canada is building.",
            "At KnowledgeOne, I evaluated and adopted AI tools in enterprise learning contexts, assessing governance implications alongside usability and performance. I have followed the evolution of AI governance frameworks closely and understand the organizational and policy challenges of governing systems whose behaviour must be explainable, auditable, and continuously monitored.",
            "I am bilingual in French and English, based in Montreal, and experienced working with distributed technology teams and cross-functional stakeholders in regulated environments. Collibra experience, noted as a preferred qualification, is part of my current toolkit.",
            "I would welcome the opportunity to contribute to Air Canada's data and AI governance programs. Thank you for your consideration.",
        ],
        closing="Kind regards,",
        date_str="May 25, 2026",
    )
    doc.save("docx/cover_aircanada.docx")
    print("✓ cover_aircanada.docx")

# ============================================================
# Cover Letter — CAE
# ============================================================

def cover_cae():
    doc = Document()
    make_cover_letter(doc,
        salutation="Dear CAE Hiring Team,",
        paragraphs=[
            "I am applying for the Senior Manager, Data Governance & Excellence position because it combines two areas where I have spent the last decade building expertise: the design and implementation of governance frameworks, and the stakeholder engagement and data literacy work that makes governance actually take hold across an organization.",
            "At the McConnell Brain Imaging Centre at McGill University, I managed data governance for one of Canada's leading brain imaging environments: defining metadata standards, developing data ownership accountability structures, deploying Collibra for institutional data cataloguing, and establishing data quality measures for high-throughput daily acquisition workflows. The role required working across a complex multi-stakeholder environment: supporting dozens of principal investigators with different research practices, data platforms, and governance maturity levels. My approach throughout was to build governance as a culture of data literacy rather than a system of compliance enforcement — a distinction that is the difference between frameworks that get adopted and frameworks that get worked around.",
            "Beyond the institutional program, I contributed to national research data policy through Portage, CONP, and RDA committee work, representing our centre's interests in federal-level data governance strategy and helping shape frameworks that were adopted across Canadian institutions. I also designed and ran the training programs that translated governance requirements into practical, accessible workflows for non-specialist research audiences.",
            "I am bilingual in French and English, based in Montreal, and bring a record of cross-functional coordination at both the institutional and national level. I have managed government client relationships for regulated technology deployments and led multi-stakeholder teams under Agile delivery models.",
            "I would welcome the opportunity to bring this combination of governance design, stakeholder engagement, and data literacy leadership to CAE's data excellence program. Thank you for your consideration.",
        ],
        closing="Kind regards,",
        date_str="May 25, 2026",
    )
    doc.save("docx/cover_cae.docx")
    print("✓ cover_cae.docx")

# ============================================================
# Cover Letter — Points (French)
# ============================================================

def cover_points():
    doc = Document()
    make_cover_letter(doc,
        salutation="Madame, Monsieur,",
        paragraphs=[
            "Je souhaite vous soumettre ma candidature pour le poste de Concepteur(trice) pédagogique & gestion LMS chez Point S Canada. Ce rôle correspond directement à l'ensemble de mon parcours en conception pédagogique, en gestion de plateformes d'apprentissage et en adoption technologique au sein d'organisations diversifiées.",
            "Au cours des cinq dernières années, j'ai occupé des fonctions centrées sur la conception et la gestion de systèmes LMS dans des contextes variés. À titre d'analyste Moodle chez Premergency Inc., j'ai coordonné le déploiement de solutions LMS pour des clients gouvernementaux en assurant la conformité réglementaire, géré des migrations complètes de plateformes existantes vers Moodle, et conçu des parcours de formation sur mesure répondant aux objectifs de chaque client. Chez KnowledgeOne, j'ai développé des fonctionnalités LMS pour la plateforme eConcordia et évalué l'intégration d'outils d'intelligence artificielle dans des contextes d'apprentissage en entreprise. À l'Université McGill, j'ai conçu et déployé un portail éducatif Moodle en libre-service destiné à l'intégration des chercheurs, ainsi que des ateliers de formation pour des publics non spécialistes dans les deux langues officielles.",
            "Ce qui m'attire dans ce poste chez Point S Canada, c'est la dimension stratégique du rôle : faire du LMS non pas un simple outil administratif, mais un levier de performance et de développement des compétences à l'échelle du réseau. J'ai mené exactement ce type de démarche dans des environnements gouvernementaux et de recherche, en positionnant la formation comme un facteur de changement organisationnel et en accompagnant les gestionnaires dans l'adoption de nouvelles pratiques pédagogiques.",
            "Je suis bilingue anglais-français, basé à Montréal, disponible immédiatement, et à l'aise avec le travail à distance en mode hybride. Je serais ravi de discuter de la façon dont mon profil peut répondre à vos besoins.",
            "Je vous remercie de l'attention portée à ma candidature et reste disponible pour un entretien à votre convenance.",
        ],
        closing="Cordialement,",
        date_str="22 mai 2026",
    )
    doc.save("docx/cover_points.docx")
    print("✓ cover_points.docx")

# ============================================================
# Run all
# ============================================================

cv_aircanada()
cv_cae()
cv_points()
cover_aircanada()
cover_cae()
cover_points()
print("\nDone. Files in docx/")
