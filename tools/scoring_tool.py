def calculate_lead_score(company_content):

    content = company_content.lower()

    score = 0

    scoring_factors = []

    # AI relevance
    if "ai" in content:

        score += 20

        scoring_factors.append(
            "AI-focused operations"
        )

    # Workflow / automation
    if (
        "workflow" in content or
        "automation" in content or
        "process" in content
    ):

        score += 20

        scoring_factors.append(
            "Workflow automation potential"
        )

    # Enterprise scaling
    if (
        "enterprise" in content or
        "platform" in content or
        "scaling" in content
    ):

        score += 20

        scoring_factors.append(
            "Operational scaling complexity"
        )

    # Collaboration / management
    if (
        "collaboration" in content or
        "management" in content or
        "coordination" in content
    ):

        score += 20

        scoring_factors.append(
            "Operational management use cases"
        )

    # SaaS / software
    if (
        "software" in content or
        "cloud" in content or
        "saas" in content
    ):

        score += 20

        scoring_factors.append(
            "Strong SaaS/product fit"
        )

    return {

        "score": score,

        "factors": scoring_factors
    }