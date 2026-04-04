#!/bin/bash
# Render the Quarto site, then encrypt all HTML files with StatiCrypt.
# Usage: bash build.sh

set -e

echo "Rendering Quarto site..."
quarto render

echo "Encrypting HTML files..."
staticrypt docs/*.html docs/slides/*.html -r -d docs -p "exed@rice" \
    --remember 90 --short \
    --template-title "From BI to AI" \
    --template-instructions "Enter the course password." \
    --template-button "Unlock" \
    --template-placeholder "Course password" \
    --template-error "Incorrect password. Please try again."

echo "Done. Site rendered and encrypted."
