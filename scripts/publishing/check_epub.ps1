param(
    [string[]]$Epub = @(
        "tmp/CH01-V2-draft-preview/CH01-zh-TW-draft.epub",
        "tmp/CH01-V2-draft-preview/CH01-en-US-draft.epub"
    ),
    [string]$Jar = $env:EPUBCHECK_JAR
)

$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '../..')).Path
if (-not $Jar) {
    $Jar = Join-Path $env:LOCALAPPDATA 'Programs/EPUBCheck/5.4.0/epubcheck-5.4.0/epubcheck.jar'
}
if (-not (Test-Path -LiteralPath $Jar -PathType Leaf)) {
    throw "EPUBCheck jar not found: $Jar. Install EPUBCheck 5.4.0 from https://github.com/w3c/epubcheck/releases/tag/v5.4.0 or set EPUBCHECK_JAR."
}

$failed = $false
foreach ($relative in $Epub) {
    $path = Join-Path $root $relative
    if (-not (Test-Path -LiteralPath $path -PathType Leaf)) {
        Write-Error "EPUB not found: $path"
        $failed = $true
        continue
    }
    Write-Host "=== EPUBCheck $([IO.Path]::GetFileName($path)) ==="
    & java -jar $Jar $path
    if ($LASTEXITCODE -ne 0) { $failed = $true }
}
if ($failed) { exit 1 }
Write-Host 'All EPUBCheck validations passed.'
