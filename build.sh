#!/bin/bash
# Build slide PDFs and/or render+encrypt the site.
#
# Usage:
#   bash build.sh              Build all 8 slide PDFs, render site, encrypt
#   bash build.sh 3            Build PDF for session 3 only
#   bash build.sh 1 4 6        Build PDFs for sessions 1, 4, and 6
#   bash build.sh render       Render site and encrypt (no PDF generation)

set -e

build_pdf() {
    local n=$1
    echo "Building PDF for session ${n}..."
    mkdir -p slides/pdf
    npx decktape reveal "docs/slides/session${n}.html" "slides/pdf/session${n}.pdf" --size 1920x1080
    echo "  -> slides/pdf/session${n}.pdf"
}

render_site() {
    echo "Rendering Quarto site..."
    quarto render

    echo "Encrypting slides page..."
    staticrypt docs/slides.html -r -d docs -p "execed@rice" \
        --remember 90 --short \
        --template-title "From BI to AI" \
        --template-instructions "Enter the course password." \
        --template-button "Unlock" \
        --template-placeholder "Course password" \
        --template-error "Incorrect password. Please try again." \
        --template-color-primary "#00205B" \
        --template-color-secondary "#7C7E7F"
}

if [ $# -eq 0 ]; then
    # Build all PDFs, then render
    for i in 1 2 3 4 5 6 7 8; do
        build_pdf "$i"
    done
    render_site
elif [ "$1" = "render" ]; then
    render_site
else
    # Build specific session PDFs
    for n in "$@"; do
        build_pdf "$n"
    done
    echo "Run 'bash build.sh render' to update the site."
fi

echo "Done."
