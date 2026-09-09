# Summary of Datasets Used in SQLi Detection Research

| Dataset | Source | Size | Attack Types | Strengths | Limitations |
|---|---|---|---|---|---|
| **Kaggle SQLi Dataset** | Kaggle (Public) | ~40,000 queries | Classic tautologies, union-based, admin bypass | Clean formatting, minimal preprocessing | Static, lacks modern API patterns, no obfuscated payloads |
| **HTTP CSIC 2010** | CSIC (Academic) | ~100,000 requests | SQLi, XSS, parameter tampering | Standardized benchmark, complex query paths | Dated syntax, lacks contemporary evasion tactics |
| **GitHub SQLi Repositories** | GitHub (Public) | Varies | Multiple SQLi types | Diverse payloads, community-contributed | Quality varies, may contain duplicates |
| **ModSecurity/OWASP CRS** | OWASP (Public) | Varies | OWASP Top 10 attacks | Industry standard, real-world rules | Signature-based, not ML-ready |
