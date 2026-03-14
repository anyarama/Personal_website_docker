"""Curated portfolio content used by the public website."""

SITE_CONTENT = {
    "profile": {
        "name": "Aneesh Yaramati",
        "headline": "Data Engineer + MSIS @ Kelley for enterprise systems, analytics, and AI",
        "subheadline": (
            "I build enterprise data systems that make reporting trustworthy, migrations safer, and "
            "analytics useful at scale. This portfolio connects SLB execution with current enterprise "
            "systems, cloud integration strategy, and AI work at Kelley."
        ),
        "location": "Bloomington, Indiana",
        "email": "anyarama@iu.edu",
        "phone": "(812) 340-3132",
        "linkedin_url": "https://www.linkedin.com/in/aneesh-yaramati/",
        "github_profile_url": "https://github.com/anyarama",
        "github_repo_url": "https://github.com/anyarama/Personal_website_docker",
        "resume_asset": "resume/Yaramati_Aneesh_Resume.pdf",
        "availability": "Open to data engineering, enterprise systems, analytics, and digital transformation roles.",
    },
    "nav_items": [
        {"endpoint": "index", "label": "Home"},
        {"endpoint": "about", "label": "About"},
        {"endpoint": "resume", "label": "Resume"},
        {"endpoint": "projects", "label": "Portfolio"},
        {"endpoint": "contact", "label": "Contact"},
    ],
    "brand_logos": [
        {
            "name": "Indiana University Kelley School of Business",
            "filename": "images/logos/iu-kelley.svg",
            "caption": "Kelley MSIS",
            "tier": "primary",
        },
        {
            "name": "SLB",
            "filename": "images/logos/slb.svg",
            "caption": "Enterprise data engineering",
            "tier": "primary",
        },
        {
            "name": "TMHNA Digital Momentum",
            "filename": "images/logos/tmhna.svg",
            "caption": "Case competition finalist",
            "tier": "primary",
        },
        {
            "name": "Philips Healthcare",
            "filename": "images/logos/philips.svg",
            "caption": "Engineering internship",
            "tier": "secondary",
        },
        {
            "name": "Springer",
            "filename": "images/logos/springer.svg",
            "caption": "Published research",
            "tier": "secondary",
        },
        {
            "name": "Amrita Vishwa Vidyapeetham",
            "filename": "images/logos/amrita.svg",
            "caption": "Undergraduate foundation",
            "tier": "secondary",
        },
    ],
    "impact_metrics": [
        {
            "value": "40M+",
            "label": "records unified",
            "context": "Golden records created across 10+ legacy systems at SLB.",
        },
        {
            "value": "99%",
            "label": "data readiness",
            "context": "Achieved through validation rules and quality checks for downstream analytics.",
        },
        {
            "value": "30%",
            "label": "faster sync",
            "context": "Delivered via SOAP-based material number reservation services.",
        },
        {
            "value": "3rd",
            "label": "place finish",
            "context": "Kelley MSIS CORE final project for TMHNA Digital Momentum.",
        },
    ],
    "focus_areas": [
        {
            "title": "Enterprise Data Foundations",
            "description": "Designing reliable pipelines, governance checks, and golden-record systems for reporting and analytics.",
        },
        {
            "title": "Digital Enterprise Systems",
            "description": "Connecting SAP, Snowflake, and cloud-aware process design into decision-ready operating models.",
        },
        {
            "title": "Analytics & AI Readiness",
            "description": "Turning architecture into scalable datasets, KPI definitions, and AI-enabled workflows.",
        },
    ],
    "about_story": [
        (
            "My best work sits at the intersection of engineering detail and business clarity. At SLB, "
            "I learned that enterprise data is only valuable when teams trust it enough to act on it."
        ),
        (
            "That mindset now shapes my MSIS work at Kelley, where I am building stronger fluency in "
            "enterprise platforms, AI-driven development, governance, and operating models."
        ),
        (
            "This portfolio is built for recruiters and hiring teams who want evidence: quantified "
            "impact, credible systems work, and a clear view of how data platforms support decisions."
        ),
    ],
    "credibility_points": [
        "Dean's Global Fellowship and MSIS Graduate Assistantship recipient",
        "3rd Place, Kelley MSIS CORE Final Project for TMHNA Digital Momentum",
        "2+ years of enterprise data engineering experience at SLB",
        "Springer-published academic project in deep learning for road-safety use cases",
    ],
    "education_entries": [
        {
            "institution": "Indiana University, Kelley School of Business",
            "location": "Bloomington, IN",
            "degree": "Master of Science in Information Systems",
            "details": "Concentration: Digital Enterprise Systems and AI",
            "date": "December 2026",
            "gpa": "3.70 / 4.00",
            "bullets": [
                "Core coursework: IT Strategy, Enterprise Platforms, AI Driven Development (RAG, LLM), IT Governance, Risk & Controls, Data Analytics, Agility, Process & Automation, Cloud / Platform Architecture, and Design Thinking.",
                "Concentration coursework: Enterprise Digital Core, Enterprise Data Management, Big Data Technologies, Digital Platforms and AI, Agentic AI Systems, Foundations in AI Research, and Designing & Deploying AI Solutions.",
                "Recipient, Dean's Global Fellowship and MSIS Graduate Assistantship.",
                "3rd Place, Kelley MSIS CORE Final Project (TMHNA Digital Momentum).",
            ],
        },
        {
            "institution": "Amrita Vishwa Vidyapeetham, Amrita School of Engineering",
            "location": "Coimbatore, India",
            "degree": "Bachelor of Technology in Electrical, Electronics and Communication Engineering",
            "details": "",
            "date": "June 2022",
            "gpa": "3.84 / 4.00",
            "bullets": [
                "Recipient, Amrita Vidyanidhi 75% Merit Scholarship awarded to top rankers nationwide.",
            ],
        },
    ],
    "experience_entries": [
        {
            "company": "Schlumberger (SLB)",
            "role": "Data Engineer",
            "location": "Pune, India",
            "date": "August 2022 - May 2025",
            "logo": "images/logos/slb.svg",
            "highlights": ["40M+ governed records", "99% readiness", "30% faster sync"],
            "bullets": [
                "Consolidated 10+ legacy systems by optimizing 40+ ETL/ELT workflows and processing 40M+ records into enterprise-ready golden records.",
                "Led archival workflow design that improved troubleshooting availability and increased MDM system reliability by 20%.",
                "Implemented 25+ data-quality rules, improving accuracy by 10% and driving 99% readiness for downstream analytics and ML use cases.",
                "Optimized SAP migration conversions by integrating pre-load and post-load validation checks aligned to governance requirements.",
                "Developed SOAP-based web services for real-time material number reservation and updates, reducing synchronization time by 30%.",
                "Managed CI/CD deployments in Azure DevOps Git to improve release discipline, compliance, and code quality.",
                "Monitored source-level record trends across ETL layers to flag anomalies early and support operational issue resolution.",
            ],
        },
        {
            "company": "Philips Healthcare",
            "role": "Project Intern",
            "location": "Pune, India",
            "date": "April 2022 - July 2022",
            "logo": "images/logos/philips.svg",
            "highlights": ["DXR continuity", "Supplier risk reduction"],
            "bullets": [
                "Mitigated PCBA obsolescence risk for DXR systems by optimizing Bill of Materials strategy and protecting production continuity.",
                "Identified drop-in replacements and reverse-engineered legacy designs to improve cost efficiency and reduce supplier dependency.",
            ],
        },
    ],
    "portfolio_cases": [
        {
            "slug": "slb-enterprise-data-engineering",
            "title": "SLB Enterprise Data Engineering",
            "organization": "Schlumberger (SLB)",
            "period": "August 2022 - May 2025",
            "logo": "images/logos/slb.svg",
            "tag": "Enterprise data systems",
            "summary": (
                "Scaled master-data and integration workflows across legacy systems to improve reporting trust, "
                "migration readiness, and analytics quality."
            ),
            "challenge": (
                "The operating environment spanned fragmented systems, inconsistent records, and migration pressure. "
                "The goal was to make enterprise data reliable enough for reporting, governance, and future analytics."
            ),
            "approach": [
                "Optimized 40+ ETL/ELT workflows spanning 10+ source systems.",
                "Built archival and monitoring patterns to improve troubleshooting visibility.",
                "Introduced 25+ validation checks to catch quality issues before downstream consumption.",
                "Added SOAP-based services for real-time material number reservation and synchronization.",
            ],
            "impact": [
                "40M+ records transformed into unified golden records.",
                "20% increase in MDM system reliability.",
                "99% data readiness for downstream analytics and ML use cases.",
                "30% reduction in synchronization time for material number workflows.",
            ],
            "preview_metric": "40M+ records unified",
            "preview_support": "10+ legacy systems consolidated into governed enterprise data.",
            "stack": ["Python", "SQL / PLSQL", "Informatica", "SAP", "Azure DevOps", "Data Governance"],
        },
        {
            "slug": "tmhna-digital-momentum",
            "title": "TMHNA Digital Momentum",
            "organization": "Kelley MSIS CORE Final Project",
            "period": "November 2025 - December 2025",
            "logo": "images/logos/tmhna.svg",
            "tag": "Digital operating model",
            "summary": (
                "Designed a target-state recommendation for TMHNA to align systems, processes, and finance data "
                "across TMH, Raymond, and THD."
            ),
            "challenge": (
                "A $7B enterprise needed a clearer target state for finance intelligence across multiple ERP and analytics platforms, "
                "without losing flexibility as reporting requirements matured."
            ),
            "approach": [
                "Defined a target-state financial intelligence model spanning SAP S/4HANA, SAP ECC, and Snowflake.",
                "Focused on KPI standardization, scalable data modeling, and analytics-ready datasets.",
                "Balanced business storytelling with technical feasibility for executive and systems stakeholders.",
            ],
            "impact": [
                "3rd Place finish in the Kelley MSIS CORE final project.",
                "Created a clearer enterprise reporting blueprint for multi-system harmonization.",
                "Positioned finance data for more reliable KPI definitions and future-scale analytics use.",
            ],
            "preview_metric": "3rd place finish",
            "preview_support": "Future-state finance intelligence model across SAP S/4HANA, ECC, and Snowflake.",
            "stack": ["SAP S/4HANA", "SAP ECC", "Snowflake", "Enterprise Architecture", "Business Case Design"],
        },
        {
            "slug": "cloud-migration-multi-cloud-strategy",
            "title": "Cloud Migration & Multi-Cloud Integration Strategy",
            "organization": "Kelley MSIS Coursework",
            "period": "October 2025 - November 2025",
            "logo": "images/logos/iu-kelley.svg",
            "tag": "Cloud transformation",
            "summary": (
                "Designed a 100% cloud migration roadmap and integration architecture for a mixed enterprise "
                "application estate spanning ERP, CRM, HCM, custom .NET, and IoT systems."
            ),
            "challenge": (
                "The brief required a practical migration path for a fragmented legacy landscape while balancing "
                "platform fit, real-time orchestration, global scalability, security, and cost discipline."
            ),
            "approach": [
                "Mapped the estate across ERP, CRM, HCM, custom .NET applications, and IoT workloads.",
                "Selected SaaS, PaaS, and IaaS target-state platforms across OCI, Azure, Salesforce, and Workday.",
                "Designed an iPaaS-led multi-cloud integration layer for real-time orchestration and resiliency.",
                "Built security, HA / DR, and cost-optimization controls into the proposed architecture.",
            ],
            "impact": [
                "Produced a full cloud migration plan for the target enterprise landscape.",
                "Created a multi-cloud integration blueprint aligned to real-time data movement and global scale.",
                "Connected platform selection with governance, resilience, and implementation priorities.",
            ],
            "preview_metric": "100% cloud migration plan",
            "preview_support": "OCI, Azure, Salesforce, Workday, and iPaaS integration strategy in one roadmap.",
            "stack": ["OCI", "Azure", "Salesforce", "Workday", "iPaaS", "Integration Architecture"],
        },
        {
            "slug": "pothole-detection-research",
            "title": "Pothole Detection Using Deep Learning",
            "organization": "Springer Publication",
            "period": "October 2021 - February 2022",
            "logo": "images/logos/springer.svg",
            "tag": "Applied AI research",
            "summary": (
                "Built an ADAS-oriented pothole detection workflow focused on data curation, benchmarking, "
                "and practical model selection."
            ),
            "challenge": (
                "The project required a model that could balance accuracy and inference efficiency in a real-time road-safety context."
            ),
            "approach": [
                "Built and augmented a dataset of 1,995 Indian road images.",
                "Benchmarked YOLOv5 variants against Faster-RCNN with a ResNet101 backbone.",
                "Selected YOLOv5m based on balanced precision-recall trade-offs and practical deployment speed.",
            ],
            "impact": [
                "82% accuracy for the chosen model variant.",
                "Produced a research-backed system design for ADAS-aligned pothole detection.",
                "Demonstrated fluency in experiment design, evaluation, and model selection trade-offs.",
            ],
            "preview_metric": "82% model accuracy",
            "preview_support": "ADAS-oriented vision workflow balancing inference speed and precision-recall trade-offs.",
            "stack": ["Python", "YOLOv5", "Faster-RCNN", "Computer Vision", "Model Evaluation"],
        },
    ],
    "academic_projects": [
        {
            "title": "TMHNA Digital Momentum, Kelley MSIS CORE Final Project",
            "date": "November 2025 - December 2025",
            "bullets": [
                "Developed a business and technology recommendation for TMHNA ($7B) to harmonize systems, processes, and data across TMH, Raymond, and THD.",
                "Designed a target-state financial intelligence model across SAP S/4HANA, SAP ECC, and Snowflake with analytics-ready datasets and KPI standardization.",
            ],
        },
        {
            "title": "Cloud Migration & Multi-Cloud Integration Strategy",
            "date": "October 2025 - November 2025",
            "bullets": [
                "Designed a 100% cloud migration plan for legacy ERP, CRM, HCM, custom .NET applications, and IoT systems, aligning workloads to OCI, Azure, Salesforce, and Workday.",
                "Built a unified multi-cloud integration architecture using an iPaaS platform to support real-time orchestration, HA / DR, security, and cost optimization.",
            ],
        },
        {
            "title": "Pothole Detection using Deep Learning Algorithms (Springer)",
            "date": "October 2021 - February 2022",
            "bullets": [
                "Designed a real-time pothole detection system to support Advanced Driver-Assistance Systems (ADAS).",
                "Built and augmented a dataset of 1,995 Indian road images and benchmarked YOLOv5 variants against Faster-RCNN.",
            ],
        },
    ],
    "skill_groups": [
        {
            "title": "Data Engineering & Platforms",
            "items": ["Python", "SQL / PLSQL", "MySQL", "ETL / ELT", "Data Modeling", "Data Warehousing", "Snowflake", "Spark", "Hive"],
        },
        {
            "title": "Enterprise Systems",
            "items": ["SAP (MM, ME, MDG)", "SAP S/4HANA", "SAP ECC", "Informatica", "Azure DevOps", "Governance & Controls"],
        },
        {
            "title": "Analytics & AI",
            "items": ["Machine Learning", "Tableau", "Power BI", "Cloud Analytics", "Agentic AI Systems", "AI Driven Development", "RAG / LLM"],
        },
        {
            "title": "Delivery & Collaboration",
            "items": ["Agile / Scrum", "JIRA", "Project Management", "MVC Architecture", "Business Storytelling", "Cross-functional Delivery", "Alteryx", "Design Thinking"],
        },
    ],
    "contact_links": [
        {
            "label": "Email",
            "href": "mailto:anyarama@iu.edu",
            "support": "Best for recruiting outreach, interviews, and collaboration.",
            "cta_label": "Send Email",
        },
        {
            "label": "LinkedIn",
            "href": "https://www.linkedin.com/in/aneesh-yaramati/",
            "support": "Professional background, recommendations, and network context.",
            "cta_label": "Open LinkedIn",
        },
        {
            "label": "Resume",
            "href": "resume/Yaramati_Aneesh_Resume.pdf",
            "support": "Latest PDF resume aligned to the current portfolio content.",
            "cta_label": "Download PDF",
        },
        {
            "label": "GitHub",
            "href": "https://github.com/anyarama",
            "support": "Code, experiments, and implementation-oriented work.",
            "cta_label": "View GitHub",
        },
    ],
    "contact_notes": [
        "Recruiting conversations in data engineering, enterprise systems, analytics, and digital transformation.",
        "Graduate roles and internships where platform thinking and business context matter.",
        "Projects tying enterprise data foundations to reporting, AI readiness, or operating-model redesign.",
    ],
}
