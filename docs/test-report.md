# Test report

Run date: 2026-10-18 (Asia/Taipei); font alias recheck: 2026-10-18

## Passed

- Project validator: 12 parts and 60 TOC entries; 1 canonical chapter; 20 term records; 5 reference records. Chapter front matter and the S03 shot JSON passed their JSON Schemas; registry IDs and local chapter links resolved.
- External-link checker: 5 unique registered/source URLs discovered. Publisher and Runway URLs responded; SAGE and Adobe returned HTTP 403 to automated HEAD requests and remain for manual browser review. A 403 is not treated as a dead source.
- HTML build: succeeded. Chapter page contains 4 rendered tables and 1 rendered image; all local `href` and `src` targets checked in the generated chapter page exist.
- SVG XML parse, JSON parse, source-pack ZIP integrity and archive member path checks succeeded. The loose original manuscript SHA-256 matches the chapter manuscript inside the preserved ZIP.
- Git whitespace check: clean after staging.

## Pending environment/tooling

- DOCX build not produced: neither Pandoc nor `python-docx` is installed in this environment.
- PDF build not produced: Pandoc, XeLaTeX, and Inkscape (SVG-to-PDF conversion) are not installed.
- Windows font registry contains `Noto Serif TC` and `Noto Sans TC`; the old check used a mismatched family alias. The checker now accepts the installed TC family names. PDF embedding and final PDF rendering remain unverified because no PDF was generated.
- The chapter is a draft. Shot/scene definitions still need source page locators; the SAGE article's full text should be reviewed before making detailed claims.

Automated checks do not confer `verified` editorial status.
