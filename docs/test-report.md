# Test report

Run date: 2026-10-18 (Asia/Taipei); publication build and visual recheck: 2026-10-18

## Passed

- Project validator: 12 parts and 60 TOC entries; 1 canonical chapter; 20 term records; 5 reference records. Chapter front matter and the S03 shot JSON passed their JSON Schemas; registry IDs and local chapter links resolved.
- External-link checker: 5 unique registered/source URLs discovered. Publisher and Runway URLs responded; SAGE and Adobe returned HTTP 403 to automated HEAD requests and remain for manual browser review. A 403 is not treated as a dead source.
- HTML build: succeeded. Chapter page contains 4 rendered tables and 1 rendered image; all local `href` and `src` targets checked in the generated chapter page exist.
- SVG XML parse, JSON parse, source-pack ZIP integrity and archive member path checks succeeded. The loose original manuscript SHA-256 matches the chapter manuscript inside the preserved ZIP.
- Git whitespace check: clean after staging.
- DOCX and PDF builds: succeeded after correcting chapter-relative image paths. Inkscape converts SVG to PNG for DOCX and PDF for XeLaTeX. DOCX contains one embedded inline image; the PDF render visibly contains the figure.
- PDF: 8 pages. All four fonts returned extractable embedded font data through PyMuPDF. Visual review at 120 dpi found no clipped text; headings, lists, tables, and the figure render. The terms table continues across pages, and the final reference page has expected unused space in this draft.
- CJK layout: explicitly set Pandoc's `CJKmainfont` to `Noto Serif TC`; this corrected the prior horizontal overflow caused by using only `mainfont`.

## Pending environment/tooling and release checks

- MiKTeX emitted a non-fatal warning that package updates have not been checked and that the available LaTeX release is older than the requested date. Run MiKTeX Console updates before release, then rebuild and review again.
- `pdffonts` is unavailable in the Codex build shell, so the CLI checker could not report embedding there. PyMuPDF independently confirmed non-empty embedded font data for all four PDF font entries.
- The chapter is a draft. Shot/scene definitions still need source page locators; the SAGE article's full text should be reviewed before making detailed claims.

Automated checks do not confer `verified` editorial status.
