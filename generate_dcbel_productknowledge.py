"""
Application for dcbel: Product Knowledge Specialist, Montreal (on-site per posting address), full-time.
BambooHR posting id 248 (dcbel.bamboohr.com/careers/248), first seen 2026-10-15. No deadline or salary stated.
English posting. Asks for 5+ years "building clarity from complexity" in knowledge management, information
architecture, product documentation, content strategy or product operations; knowledge-system design
(taxonomy, governance, content frameworks); guardrails for AI-assisted content creation; turning requirements
into scenarios and release scope.

Output (docx/): dcbel_productknowledge_application.docx / .pdf
  Page 1   : cover letter in ENGLISH
  Pages 2-3: CV in ENGLISH

Company facts verified on dcbel's own domain (fetched 2026-10-15): support.dcbel.energy/about-us states dcbel is
"headquartered in Montreal, Canada" and that the flagship product is the dcbel Ara, a Home Energy Station;
mission "clean, efficient, and sustainable energy accessible to all". Not used: founding year, funding, office
list (found only in third-party search results, not re-verified on dcbel's domain).

Gaps stated in the letter, NOT claimed on the CV: 5+ years in a titled knowledge-management / documentation /
content-strategy role, consumer hardware or energy domain. (Release scope / scenario documents dropped as a
gap at Ted's request: he has written many document types. CV lists all 9 publications to show writing range.)
AI guardrails: claimed only as evaluating and adopting AI tools incl. Claude Code, not as having
authored an AI content policy.
"""
import os
from app_render import build_all
from generate_brp_datagov_advisor import ADDITIONAL, EDUCATION

os.makedirs("docx", exist_ok=True)

# Full list from 01-candidate-profile.md, shown in full here to support the document-writing range.
PUBLICATIONS = [
    "Halchenko, Y. O., et al. (2024). HeuDiConv: flexible DICOM conversion into structured directory layouts. JOSS, 9(99), 5839.",
    "Poline, J.-B., et al. (2023). Data and tools integration in the Canadian open neuroscience platform. Scientific Data, 10(1), 189.",
    "Halchenko, Y. O., et al. (2021). DataLad: distributed system for joint management of code, data, and their relationship. JOSS, 6(63), 3262.",
    "Maussion, G., et al. (2021). Auto-qPCR: a python-based web app for automated and reproducible analysis of qPCR data. Scientific Reports, 11(1), 21293.",
    "Strauss, T. (2021). Data Management Plan Template: Neuroimaging in the Neurosciences. Zenodo. doi:10.5281/zenodo.4673558",
    "Magnuson, J. S., Mirman, D., Luthra, S., Strauss, T., & Harris, H. D. (2018). Commentary on \"Interaction in Spoken Word Recognition Models\". Frontiers in Psychology, 9.",
    "Strauss, T., & Griebel, B. (2012). The Art of Inuinnait Drum Dancing. Kitikmeot Heritage Society.",
    "Mirman, D., Strauss, T. J., et al. (2010). A large, searchable, web-based database of aphasic performance on picture naming and other tests of cognitive function. Cognitive Neuropsychology, 27(6), 495-504.",
    "Strauss, T. J., Harris, H. D., & Magnuson, J. S. (2007). jTRACE: A reimplementation and extension of the TRACE model of speech perception and spoken word recognition. Behavior Research Methods, 39(1), 19-30.",
]

PARAS = [
    "I am applying for the Product Knowledge Specialist position in Montreal. The role asks for someone who "
    "turns complex product definitions into structured, governed knowledge that people can trust, rather than "
    "writing documents one at a time. That is the work I did for five years as Manager of Data Resources at the "
    "McConnell Brain Imaging Centre (The Neuro, McGill University): setting the metadata standards, terminology "
    "and stewardship workflows that kept a complex body of information accurate, consistent and reusable, and "
    "then making it understandable to people who were not specialists.",

    "dcbel's mission is to make clean, efficient and sustainable energy accessible to all, and the Ara Home "
    "Energy Station asks customers to trust a system that makes decisions on their behalf. Knowledge that "
    "is scattered across documents, tickets and support replies undermines that trust. At McConnell I "
    "replaced that pattern with a single governed source: FAIR-based metadata standards, data lifecycle "
    "policies and a shared vocabulary, applied through tools such as Collibra. At the Tanenbaum Open Science "
    "Institute I built a public online knowledge base that translated open science and data management "
    "requirements into plain guidance for non-specialists, and I designed the training workshops that went "
    "with it. I treated adoption as a literacy problem, and I kept standards alive through communities of "
    "practice rather than enforcement. I write in many formats for different audiences, from user guides and "
    "a published Data Management Plan Template to peer-reviewed articles and a co-authored book.",

    "On AI-assisted content, I evaluated and adopted AI tools in enterprise learning contexts at KnowledgeOne, "
    "including Claude Code, and I work with them daily. I would bring that hands-on practice to the guardrails "
    "this role defines: clear terminology, tone and quality standards that let AI speed up drafting while a "
    "human-owned source of truth keeps the content accurate. More recently at Premergency I coordinated between "
    "clients and development teams to turn requirements into working learning solutions for government clients, "
    "which is the same translation from requirement to customer-facing outcome that your Release Scope and "
    "Scenarios call for.",

    "I want to be direct about where my background differs from your posting. My knowledge-system work was "
    "built in research data governance and learning platforms rather than under a documentation or content "
    "strategy title, so the five-year bar is met through adjacent roles rather than a direct match. I have not "
    "worked on consumer hardware or in the energy sector. I would learn the product, the customer profiles and "
    "your release process first, and I am comfortable doing that quickly.",

    "I am bilingual in English and French, based in Montreal, and available immediately. I would welcome the "
    "opportunity to discuss how I can help dcbel build its product knowledge system. Thank you for your "
    "consideration.",
]

PROFILE = (
    "Knowledge and data governance specialist who designs the standards, terminology, taxonomy and stewardship "
    "workflows that keep complex information accurate, discoverable and reusable, then makes it understandable "
    "to non-specialists through knowledge bases, training and communities of practice. Led data governance and "
    "metadata management at the McConnell Brain Imaging Centre (The Neuro, McGill University). Evaluated and "
    "adopted AI tools in enterprise learning contexts, including Claude Code. Bilingual (EN/FR), Montreal-based."
)

COMPETENCIES = [
    ("Knowledge system design and governance",
     ": defined metadata standards (FAIR principles), shared terminology, data lifecycle policies and "
     "stewardship workflows so information stayed accurate, consistent and discoverable across teams"),
    ("Information architecture and taxonomy",
     ": structured metadata and classification for a national-scale research data environment; worked with "
     "Collibra alongside OwnCloud, LDAP and SSO"),
    ("Clarity from complexity",
     ": built a public online knowledge base that turned open science and data management requirements into "
     "practical guidance for non-specialists; designed workshops, user guides and a Moodle-based education portal"),
    ("AI-assisted content and adoption",
     ": evaluated and adopted AI tools in enterprise learning contexts, including Claude Code; grew adoption "
     "through hands-on training and communities of practice rather than enforcement"),
    ("Cross-team translation",
     ": coordinated between clients and development teams to turn requirements into LMS solutions; "
     "represented the centre on Portage, CONP and Research Data Alliance committees, coordinating standards "
     "across institutions"),
    ("Analysis and reporting",
     ": Python, R, SQL and Tableau; usage and participation reporting for stakeholders; bilingual (EN/FR) "
     "communication"),
]

EXPERIENCE = [
    ("07/2025 – 01/2026", "Moodle Analyst", "Premergency Inc.", "Canada", [
        "Coordinated between client and development teams to turn requirements into LMS solutions for government clients",
        "Migrated legacy LMS systems to Moodle and designed bespoke learning and development solutions",
        "Managed regulatory compliance requirements for government LMS deployments",
    ]),
    ("01/2024 – 10/2024", "Full Stack Developer", "KnowledgeOne", "Montreal, QC", [
        "Developed LMS features for active clients in LAMP++, Moodle, and LXD",
        "Evaluated and adopted AI tools in enterprise learning contexts, including Claude Code",
    ]),
    ("09/2016 – 10/2021", "Manager of Data Resources", "McConnell Brain Imaging Centre, The Neuro, McGill University", "Montreal, QC", [
        "Led data governance and metadata management for one of Canada's leading brain imaging centres, supporting dozens of principal investigators and hundreds of researchers",
        "Defined metadata standards, terminology, stewardship workflows and data lifecycle policies, and built them into the daily workflow",
        "Grew adoption through hands-on training and communities of practice rather than enforcement; launched an OwnCloud portal and a Moodle-based education portal for self-serve use",
        "Worked across Collibra, OwnCloud, LDAP and SSO to support access control, roles and data management",
        "Represented the centre on Portage, CONP and Research Data Alliance committees, coordinating standards across institutions",
    ]),
    ("08/2020 – 10/2021", "Data Management and Sharing Coordinator (p/t)", "Tanenbaum Open Science Institute, The Neuro, McGill University", "Montreal, QC", [
        "Designed and administered training workshops on data management practices for faculty and graduate students",
        "Built an online knowledge base translating open science concepts into practical guidance for non-specialists",
    ]),
]

SKILLS = ("Collibra, metadata standards (FAIR), Moodle, OwnCloud, SQL, Python, R, Tableau, Git, Docker, AWS, "
          "Azure, SSO, LDAP, Drupal, WordPress, Agile/Scrum, training design and facilitation.")

if __name__ == "__main__":
    build_all(dict(
        out="docx/dcbel_productknowledge_application",
        cover=dict(contact="Montreal, Quebec  |  514-475-2374  |  ted.strauss@gmail.com  |  linkedin.com/in/tedstrauss-63b01821",
                   date="October 15, 2026",
                   subject="Subject: Application: Product Knowledge Specialist",
                   salutation="Dear Hiring Team,", paras=PARAS,
                   closing="Kind regards,"),
        cv=dict(profile=PROFILE, competencies=COMPETENCIES, experience=EXPERIENCE, additional=ADDITIONAL,
                education=EDUCATION, skills=SKILLS, publications=PUBLICATIONS)))
