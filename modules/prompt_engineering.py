def enhance_prompt(user_prompt):
    return f"""
You are an elite AI prompt engineer.

Convert this idea into a highly detailed AI image prompt:

{user_prompt}

Enhance with:
- cinematic lighting
- ultra realistic
- 8k resolution
- DSLR, 50mm lens
- depth of field
- sharp focus
- professional composition
- detailed textures

Return ONLY the final prompt.
"""