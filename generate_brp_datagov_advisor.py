"""
Application for BRP: Advisor, Data Governance (Temporary, 12 months), Montreal, hybrid.
Posting source: freehire/whatjobs aggregator listing of 2026-10-05 (BRP's own careers page is
JS-rendered and returned no listing, so requirements come from the aggregator text; the
req ID is unknown).

Outputs (docx/):
  brp_datagov_advisor_application.docx / .pdf   (EN cover letter + EN CV)
  cover_brp_datagov_advisor_fr.docx / .pdf      (FR cover letter alone; role needs FR/EN)

Targeting: leads with governance + adoption/training (the posting's change-enablement focus).
Gaps stated in the letter, NOT claimed on the CV: ADKAR, manufacturing / large-enterprise
governance, the 7+ years bar (5 years dedicated governance), SOX/Law 25 specifics.

Company facts verified on brp.com (fetched 2026-10-08): brands Ski-Doo, Lynx, Sea-Doo, Can-Am,
Rotax. NOT used: headquarters, headcount, plants (brp.com did not state them; they appear only in
the posting text).
"""
import os
from app_render import build_all

os.makedirs("docx", exist_ok=True)

COVER_CONTACT_EN = "Montreal, Quebec  |  514-475-2374  |  ted.strauss@gmail.com  |  linkedin.com/in/tedstrauss-63b01821"
COVER_CONTACT_FR = "Montréal (Québec)  |  514-475-2374  |  ted.strauss@gmail.com  |  linkedin.com/in/tedstrauss-63b01821"

PARAS_EN = [
    "I am applying for the Advisor, Data Governance position (temporary, 12 months) in Montreal. The posting "
    "asks for someone who deploys governance and enables its adoption: standards and operating processes on "
    "one side, coaching data stewards and building training on the other. That intersection of governance and "
    "adoption is the work I did for five years as Manager of Data Resources at the McConnell Brain Imaging "
    "Centre (The Neuro, McGill University), one of Canada's leading brain imaging centres.",

    "BRP's brands, Ski-Doo, Lynx, Sea-Doo, Can-Am and Rotax, span product lines that each generate their own "
    "data, and the federated model your posting describes, with domain owners accountable under shared "
    "enterprise standards, is the approach I know best. At McConnell I defined metadata standards, stewardship "
    "workflows and data lifecycle policies for dozens of principal investigators and hundreds of researchers, "
    "and I worked with Collibra and with access tooling (LDAP, SSO) to put those standards into daily practice. "
    "I treated adoption as a literacy problem rather than an enforcement one: hands-on workshops, a public "
    "knowledge base on data management, and communities of practice that gave data owners a reason to follow "
    "the standards. I also represented the centre on national bodies (Portage, CONP and the Research Data "
    "Alliance), where I coordinated standards with institutions that did not report to me.",

    "For this role I would bring bilingual (French and English) training materials and toolkits that make "
    "governance concepts accessible to executive, business and technical audiences, and a habit of measuring "
    "what people actually adopt. More recently I evaluated and adopted AI tools in enterprise settings, "
    "including Claude Code, weighing data handling and governance implications alongside the productivity case.",

    "I want to be direct about where my background differs from your posting. My governance experience was built "
    "in research rather than in manufacturing or a large enterprise, and my five years of dedicated governance "
    "work sit below your seven-year mark, supported by later work on compliance and platforms. I have not "
    "applied ADKAR formally; my change work has been communities of practice and hands-on training, and I would "
    "adopt ADKAR as a shared vocabulary with your team. I have not worked directly with SOX, though I have "
    "managed regulatory compliance requirements for government systems.",

    "I am bilingual in French and English, based in Montreal, and available immediately for a 12-month "
    "mandate. I would welcome the opportunity to discuss how I can help BRP's governance adoption. Thank you "
    "for your consideration.",
]

PARAS_FR = [
    "Je pose ma candidature au poste de conseiller en gouvernance des données (temporaire, 12 mois) à "
    "Montréal. Votre affichage recherche une personne qui déploie la gouvernance et en facilite l'adoption : "
    "normes et processus d'une part, accompagnement des intendants de données et formation d'autre part. Ce "
    "croisement de la gouvernance et de l'adoption est le travail que j'ai fait pendant cinq ans comme "
    "gestionnaire des ressources de données au Centre d'imagerie cérébrale McConnell (The Neuro, Université "
    "McGill), l'un des principaux centres d'imagerie cérébrale au Canada.",

    "Les marques de BRP, Ski-Doo, Lynx, Sea-Doo, Can-Am et Rotax, couvrent des gammes de produits qui "
    "génèrent chacune leurs propres données. Le modèle fédéré décrit dans votre affichage, où les responsables "
    "de domaines répondent de leurs données selon des normes d'entreprise communes, est l'approche que je "
    "connais le mieux. Au Centre McConnell, j'ai défini les normes de métadonnées, les flux d'intendance et "
    "les politiques de cycle de vie des données pour des dizaines de chercheurs principaux et des centaines "
    "de chercheurs, et j'ai travaillé avec Collibra, LDAP et l'authentification unique (SSO) pour mettre ces "
    "normes en pratique. J'ai abordé l'adoption comme un enjeu de littératie plutôt que de contrainte : des "
    "ateliers pratiques, une base de connaissances publique et des communautés de pratique qui donnaient aux "
    "responsables des données une raison de suivre les normes. J'ai aussi représenté le centre auprès "
    "d'organismes nationaux (Portage, CONP et Research Data Alliance), en coordonnant des normes avec des "
    "établissements qui ne relevaient pas de moi.",

    "Pour ce poste, j'apporterais du matériel de formation et des trousses d'outils bilingues qui rendent la "
    "gouvernance accessible aux publics de la direction, du milieu des affaires et des équipes techniques, "
    "ainsi que l'habitude de mesurer ce que les gens adoptent réellement. Plus récemment, j'ai évalué et "
    "adopté des outils d'IA en contexte d'entreprise, dont Claude Code, en tenant compte de la gouvernance des "
    "données.",

    "Je tiens à être direct sur les écarts avec votre affichage. Mon expérience de gouvernance s'est "
    "construite en recherche plutôt que dans le secteur manufacturier ou une grande entreprise, et mes cinq "
    "ans de travail dédié en gouvernance se situent sous votre seuil de sept ans, complétés par du travail "
    "ultérieur en conformité et en plateformes. Je n'ai pas appliqué ADKAR formellement; mon travail de "
    "changement a reposé sur des communautés de pratique et de la formation pratique, et j'adopterais ADKAR "
    "comme langage commun avec votre équipe. Je n'ai pas travaillé directement avec SOX, mais j'ai géré des "
    "exigences de conformité réglementaire pour des systèmes gouvernementaux.",

    "Je suis bilingue en français et en anglais, je vis à Montréal et je suis disponible immédiatement pour un "
    "mandat de 12 mois. J'aimerais discuter de la façon dont je peux soutenir l'adoption de la gouvernance "
    "chez BRP. Merci de considérer ma candidature.",
]

PROFILE = (
    "Data governance specialist who builds the standards, stewardship workflows and training that get data "
    "owners to adopt governance in daily work. Led data governance and metadata management at the McConnell "
    "Brain Imaging Centre (The Neuro, McGill University), worked with Collibra, SSO and LDAP, and contributed "
    "to national data governance bodies (Portage, CONP, RDA). Designs bilingual training, toolkits and "
    "communities of practice that make governance concepts accessible to non-specialists. Bilingual (EN/FR), "
    "Montreal-based."
)

COMPETENCIES = [
    ("Data governance and stewardship",
     ": defined metadata standards (FAIR principles), data classification and lifecycle policies, and "
     "stewardship workflows for a national-scale research data environment"),
    ("Governance adoption and change",
     ": grew adoption by treating governance as a literacy problem, through hands-on workshops, "
     "communities of practice, and a public knowledge base; coordinated standards with institutions "
     "that did not report to me"),
    ("Training and communication",
     ": designed and delivered workshops and learning resources for faculty, students, and "
     "non-specialists; bilingual (EN/FR) communication with executive, business, and technical audiences"),
    ("Metadata tools and access",
     ": worked with Collibra alongside OwnCloud, LDAP, and SSO to support access, roles, and "
     "self-serve data management; data pipelines in LAMP++, Python, R, and SQL"),
    ("Compliance and policy",
     ": managed regulatory compliance requirements for government LMS deployments; contributed to "
     "national research policy through Portage, CONP, and the Research Data Alliance"),
    ("AI adoption and governance",
     ": evaluated and adopted AI tools in enterprise settings, including Claude Code, assessing data "
     "handling and governance implications alongside the productivity case"),
]

EXPERIENCE = [
    ("09/2016 – 10/2021", "Manager of Data Resources", "McConnell Brain Imaging Centre, The Neuro, McGill University", "Montreal, QC", [
        "Led data governance and metadata management for one of Canada's leading brain imaging centres, supporting dozens of principal investigators and hundreds of researchers",
        "Defined metadata standards, stewardship workflows, and data lifecycle policies, and built them into the daily acquisition workflow",
        "Grew governance adoption through hands-on training and communities of practice rather than enforcement; launched an OwnCloud portal and a Moodle-based education portal for self-serve data management",
        "Worked across Collibra, OwnCloud, LDAP, and SSO to support access control, roles, and data management; developed brain imaging data pipelines in an Agile team",
        "Represented the centre on Portage, CONP, and Research Data Alliance committees, coordinating standards across institutions",
    ]),
    ("08/2020 – 10/2021", "Data Management and Sharing Coordinator (p/t)", "Tanenbaum Open Science Institute, The Neuro, McGill University", "Montreal, QC", [
        "Supported the launch of a new academic unit focused on Open Science; designed and administered training workshops on data management practices for faculty and graduate students",
        "Built an online knowledge base translating open science and data management requirements into practical guidance for non-specialists",
    ]),
    ("07/2025 – 01/2026", "Moodle Analyst", "Premergency Inc.", "Canada", [
        "Coordinated between client and development teams to deliver LMS solutions for government clients",
        "Managed regulatory compliance requirements for government LMS deployments; designed bespoke learning and development solutions",
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

SKILLS = ("Collibra, SQL, Python, R, Git, Docker, AWS, Azure, SSO, LDAP, Moodle, OwnCloud, Drupal, Tableau, "
          "Agile/Scrum, training design and facilitation.")

CV = dict(profile=PROFILE, competencies=COMPETENCIES, experience=EXPERIENCE, additional=ADDITIONAL,
          education=EDUCATION, skills=SKILLS, publications=PUBLICATIONS)

if __name__ == "__main__":
    build_all(dict(
        out="docx/brp_datagov_advisor_application",
        cover=dict(contact=COVER_CONTACT_EN, date="October 8, 2026",
                   subject="Subject: Application: Advisor, Data Governance (Temporary, 12 months)",
                   salutation="Dear Hiring Team,", paras=PARAS_EN, closing="Kind regards,"),
        cv=CV))
    build_all(dict(
        out="docx/cover_brp_datagov_advisor_fr",
        cover=dict(contact=COVER_CONTACT_FR, date="8 octobre 2026",
                   subject="Objet : Candidature au poste de conseiller en gouvernance des données (temporaire, 12 mois)",
                   salutation="Madame, Monsieur,", paras=PARAS_FR,
                   closing="Veuillez agréer, Madame, Monsieur, mes salutations distinguées,"),
        cv=None))
