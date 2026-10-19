import tempfile
import unittest
import sys
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

from scripts.check_fonts import check_pdf_fonts, main


class PdfFontValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.pdf = Path(self.temp.name) / "sample.pdf"
        self.pdf.write_bytes(b"test fixture")

    def tearDown(self):
        self.temp.cleanup()

    @patch("scripts.check_fonts.shutil.which", return_value="pdffonts")
    @patch("scripts.check_fonts.subprocess.run")
    def test_strict_gate_accepts_requested_embedded_font(self, run, _which):
        run.return_value = SimpleNamespace(
            stdout="name type encoding emb sub uni object ID\n---\nABCDEF+NotoSerifCJKtc-Regular CID TrueType Identity-H yes yes yes 4 0\n",
            stderr="", returncode=0,
        )
        self.assertEqual(check_pdf_fonts(self.pdf, "Noto Serif TC", strict=True), 0)

    @patch("scripts.check_fonts.shutil.which", return_value="pdffonts")
    @patch("scripts.check_fonts.subprocess.run")
    def test_strict_gate_rejects_unembedded_font(self, run, _which):
        run.return_value = SimpleNamespace(
            stdout="name type encoding emb sub uni object ID\n---\nABCDEF+NotoSerifCJKtc-Regular CID TrueType Identity-H no yes yes 4 0\n",
            stderr="", returncode=0,
        )
        self.assertEqual(check_pdf_fonts(self.pdf, "Noto Serif TC", strict=True), 1)

    @patch("scripts.check_fonts.shutil.which", return_value="pdffonts")
    @patch("scripts.check_fonts.subprocess.run")
    def test_strict_gate_rejects_wrong_embedded_family(self, run, _which):
        run.return_value = SimpleNamespace(
            stdout="name type encoding emb sub uni object ID\n---\nABCDEF+Arial CID TrueType Identity-H yes yes yes 4 0\n",
            stderr="", returncode=0,
        )
        self.assertEqual(check_pdf_fonts(self.pdf, "Noto Serif TC", strict=True), 1)

    def test_cli_strict_gate_fails_when_pdffonts_missing(self):
        with patch("scripts.check_fonts.shutil.which", return_value=None), patch("scripts.check_fonts.font_is_installed", return_value=True), patch("sys.argv", ["check_fonts.py", "--pdf", str(self.pdf), "--require-pdffonts"]):
            self.assertEqual(main(), 2)


if __name__ == "__main__":
    unittest.main()
