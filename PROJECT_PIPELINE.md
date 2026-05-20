# Godoy Auto Detailing Website - Project Pipeline

This file tracks the project timeline, implementation decisions, and reusable notes for future work.

## Project Snapshot

- Project: Godoy Auto Detailing website
- Type: Static HTML website
- Main entry: `index.html`
- Main assets: `assets/`
- Utility scripts: `scripts/`
- Local preview during this session: `http://localhost:4181`
- Permanent local backup: `/Users/vitor/Documents/Godoy-Auto-Detailing-Website`

## Current Structure

```text
index.html
assets/
  godoy-auto-detailing-logo.jpg
  godoy-auto-detailing-logo-transparent.png
  hero/
  gallery/
scripts/
  build_*_gallery.py
  build_*_cover.js
  remove_black_background.py
```

## Current Website Sections

- Header and navigation
- Hero
- Before/after transformations
- Services
- Results/gallery
- Customer reviews
- Booking process
- Service areas
- FAQ
- Quote/contact section
- Footer and mobile sticky actions

## Timeline

### 2026-05-11 - Initial Build

Status: Completed in previous Codex tab.

Summary:
- Built a static website for Godoy Auto Detailing.
- Created a single-page layout in `index.html`.
- Added logo assets, hero imagery, service content, gallery sections, reviews, FAQ, and contact CTAs.
- Added image-generation and image-processing helper scripts under `scripts/`.

Files involved:
- `index.html`
- `assets/`
- `scripts/`

### 2026-05-12 16:24 BST - Project Recovery

Status: Completed.

Summary:
- Located the previous project under `/Users/vitor/Documents/Codex/2026-05-11/chat-irei-construir-um-site-do`.
- Copied the project into the current Codex workspace:
  `/Users/vitor/Documents/Codex/2026-05-12/chat-eu-estava-em-outra-aba`.
- Started a local preview server on port `4181`.

Files involved:
- `index.html`
- `assets/`
- `scripts/`

### 2026-05-12 18:06 BST - Permanent Local Backup

Status: Completed.

Summary:
- Created a permanent local project folder:
  `/Users/vitor/Documents/Godoy-Auto-Detailing-Website`.
- Copied the project files there from the Codex workspace.
- Cleaned up temporary folders accidentally created during an initial path-with-spaces attempt.

Files involved:
- `/Users/vitor/Documents/Godoy-Auto-Detailing-Website/index.html`
- `/Users/vitor/Documents/Godoy-Auto-Detailing-Website/assets/`
- `/Users/vitor/Documents/Godoy-Auto-Detailing-Website/scripts/`

### 2026-05-12 18:13 BST - Pipeline Documentation Added

Status: Completed.

Summary:
- Added this `PROJECT_PIPELINE.md` file.
- Established the rule that every meaningful future project change should be documented here.
- Added a lightweight reusable change template.

Files involved:
- `PROJECT_PIPELINE.md`
- `README.md`

### 2026-05-12 18:37 BST - Gallery And Hero Media Direction

Status: Decision recorded.

Request:
- Define the direction for the website gallery and consider using a short visual sequence near the top of the page.

Summary:
- Gallery should be kept premium and selective, showing only stronger/premium vehicles.
- Each gallery vehicle should use up to 3 images:
  - exterior glossy final result;
  - clean interior or important detail;
  - foam/process image for valet/deep clean, or close-up/reflection/detail for enhancement, paint correction, or ceramic coating.
- A short hero/top-page media sequence can use before/after content from cars that will not appear in the premium gallery.
- This creates a clear split:
  - hero media = transformation proof and emotional impact;
  - gallery = premium portfolio and trust-building.

Files changed:
- `PROJECT_PIPELINE.md`

Verification:
- Design decision only; no site layout changed yet.

Notes:
- Avoid copying the reference site directly. Use the same strategic idea of quick visual proof, but keep Godoy Auto Detailing's own identity and content hierarchy.

### 2026-05-12 18:46 BST - Premium Gallery And Google-Style Reviews

Status: Completed.

Request:
- Start applying the new gallery direction.
- Bring a Google review style into the Godoy website, inspired by the reference site.

Summary:
- Updated the gallery copy to position it as a selective premium portfolio.
- Replaced one homepage gallery card from BMW 330e to Range Rover Evoque.
- Reduced the expanded gallery to premium cases only:
  - Range Rover Velar;
  - Range Rover Evoque;
  - Porsche Macan S;
  - Ford Raptor.
- Limited each expanded gallery case to 3 photos:
  - exterior final result;
  - interior/detail;
  - foam/process or close-up depending on the service type.
- Redesigned the review section with:
  - a Google-style rating summary card;
  - 5-star visual treatment;
  - customer avatar initials;
  - three Google review cards;
  - direct Google review CTA.

Files changed:
- `index.html`
- `PROJECT_PIPELINE.md`

Verification:
- Confirmed the local server responded at `http://localhost:4181/`.
- Checked the updated gallery and review sections visually in the in-app browser.

Notes:
- The hero/top-page short video concept is still pending because it needs selected before/after media assets or a generated short reel from existing photos.

### 2026-05-12 18:55 BST - Gallery Simplified To Photo-Only Grid

Status: Completed.

Request:
- Make the gallery more similar to the Diamond Detailing reference.
- Remove vehicle names and service labels from the gallery.
- Reduce the visual spacing between works and photos.

Summary:
- Replaced the previous card/case-study gallery with a photo-only portfolio grid.
- Removed visible vehicle names, service types, case headings, and booking buttons from the gallery area.
- Added a cleaner `Load More` interaction that reveals additional photos below the first visible grid.
- Kept the gallery focused on premium-looking vehicle images while making it faster to scan.

Files changed:
- `index.html`
- `PROJECT_PIPELINE.md`

Verification:
- Confirmed local server responded at `http://localhost:4181/`.
- Checked the updated gallery visually in the in-app browser with the `Load More` section open.

Notes:
- The gallery now behaves more like a premium image wall. Service context remains available elsewhere in the services section.

### 2026-05-12 19:36 BST - Client Gallery Photo Batch Imported

Status: Completed.

Request:
- Build the gallery using the full photo batch supplied by the client so it can be reviewed and refined.

Summary:
- Imported 36 client-supplied photos into the project under `assets/gallery/selected-gallery/`.
- Stored the client originals with stable filenames from `godoy-gallery-01.jpg` through `godoy-gallery-36.jpg`.
- Replaced the previous gallery images with the new selected batch.
- Kept the photo-only gallery style, with 12 images visible first and the remaining 24 inside `Load More`.
- Added lazy loading, async image decoding, and a cache-busting version parameter to the gallery images.

Files changed:
- `index.html`
- `assets/gallery/selected-gallery/`
- `PROJECT_PIPELINE.md`

Verification:
- Confirmed the local server responded at `http://localhost:4181/`.
- Checked the gallery visually in the in-app browser after a forced reload.
- Confirmed all 36 gallery image elements are present and the `Load More` drawer opens.
- Synced the working project to `/Users/vitor/Documents/Godoy-Auto-Detailing-Website`.

Notes:
- This batch is intended as a review set. Individual photos can now be removed, reordered, or replaced by editing the numbered selected gallery files and the matching image order in `index.html`.
- Attempted automatic compression first, but several outputs rendered black. The project now uses the original client files for visual reliability.

### 2026-05-12 23:34 BST - Navigation Menu Order Updated

Status: Completed.

Request:
- Change the main menu order to: Home, Services, Gallery, Review, Contact Us.

Summary:
- Renamed the menu item from `Our Services` to `Services`.
- Reordered the main navigation links so `Review` appears before `Contact Us`.

Files changed:
- `index.html`
- `PROJECT_PIPELINE.md`

Verification:
- Confirmed the local server responded at `http://localhost:4181/`.
- Reloaded the local browser and confirmed the visible menu order is `Home Services Gallery Review Contact Us`.

Notes:
- The menu links still point to the same page sections.

### 2026-05-13 17:35 BST - Featured Gallery Cars Reordered

Status: Completed.

Request:
- Make the 12 photos before `Load More` show stronger vehicles first: Porsche Macan S, black Velar, Mini Cooper, and red Velar.

Summary:
- Reordered the first visible gallery grid into four 3-photo vehicle groups:
  - Porsche Macan S;
  - black Range Rover Velar;
  - Mini Cooper;
  - red Range Rover Velar.
- Moved the previous first-grid photos into the `Load More` gallery so no photos were removed.

Files changed:
- `index.html`
- `PROJECT_PIPELINE.md`

Verification:
- Confirmed the local server responded at `http://localhost:4181/`.
- Reloaded `http://localhost:4181/#results` in the local browser.
- Confirmed the first 12 gallery image sources are ordered as Macan S, black Velar, Mini Cooper, and red Velar.

Notes:
- This change only adjusts gallery order. The image files and photo-only styling remain unchanged.

### 2026-05-13 17:53 BST - Load More Gallery Trimmed

Status: Completed.

Request:
- Keep a maximum of 3 photos per vehicle in the gallery, specifically keeping Ford Raptor photos from positions 5, 2, and 3, and silver Porsche 911 photos from positions 1, 3, and 6.

Summary:
- Reduced the silver Porsche 911 group in `Load More` to 3 selected photos: gallery images 07, 09, and 12.
- Reduced and reordered the Ford Raptor group in `Load More` to 3 selected photos: gallery images 17, 14, and 15.
- Removed the extra Porsche 911 and Ford Raptor entries from the rendered gallery without deleting the image files.

Files changed:
- `index.html`
- `PROJECT_PIPELINE.md`

Verification:
- Confirmed the HTML now references only the selected Porsche 911 and Ford Raptor images in the `Load More` gallery.
- Confirmed the local server responded at `http://localhost:4181/`.
- Reloaded the gallery with a fresh cache URL and confirmed `Load More` now has 18 images total, with Porsche 911 ordered as 07, 09, 12 and Ford Raptor ordered as 17, 14, 15.

Notes:
- This keeps the gallery rhythm cleaner by limiting each vehicle group to 3 photos.

### 2026-05-13 18:09 BST - Service Areas Simplified

Status: Completed.

Request:
- Remove the listed area names and keep the London & Surrey visual, the `Check My Area` button, and the message that good work should not be turned away just because an area is not shown.

Summary:
- Removed the London and Surrey area name lists from the service areas section.
- Updated the map/photo label to focus on London, Surrey, and selected surrounding areas.
- Kept the postcode-check CTA and rewrote the message to clearly say that Godoy Auto Detailing does not want to turn away good work just because an area is not shown on the page.
- Removed unused CSS for the old area-name list.

Files changed:
- `index.html`
- `PROJECT_PIPELINE.md`

Verification:
- Confirmed the service areas section no longer renders named area lists.
- Confirmed the `Check My Area` CTA and the "do not want to turn away good work" message remain in the section.

Notes:
- The quote form still asks for the customer's location/postcode so availability can be confirmed manually.

### 2026-05-13 18:28 BST - Transformation Reel Added

Status: Completed.

Request:
- Add a transformation video-style element to the "See the difference before choosing a service" section using a few cars.

Summary:
- Added a wide animated transformation reel before the existing before/after cards.
- Built the reel with four quick visual scenes using existing project photos:
  - BMW 330e interior reset;
  - Mini Countryman wheel/detail clean;
  - Range Rover Velar foam-to-finish exterior;
  - Peugeot 3008 interior deep clean.
- Added CSS timing, fade transitions, gentle image movement, overlay labels, captions, mobile responsiveness, and reduced-motion support.

Files changed:
- `index.html`
- `PROJECT_PIPELINE.md`

Verification:
- Confirmed the transformation reel markup and animation styles are present in the page.
- Confirmed the local server responded at `http://localhost:4181/`.
- Reloaded the local page with a fresh cache URL and confirmed the reel is visible with 4 slides and 8 images.

Notes:
- This is a lightweight website-native reel rather than a rendered MP4, so it loads from existing images and can be edited photo-by-photo in HTML.

### 2026-05-14 07:18 BST - Compact 39-photo transformation reel

Status: Completed.

Request:
- Build the transformation reel with exactly the 39 photos sent by the user, showing only `Before` and `After`, without extra transformation photos below the reel.

Summary:
- Rebuilt the transformation section as a single compact Before/After reel using the exact 39 uploaded images in `assets/transformation-reel`.
- Removed the extra transformation cards/photos below the reel so the landing page stays shorter.
- Kept only `Before` and `After` labels; the final 39th image is a single `After` slide so no photo is duplicated or substituted.
- Reduced reel height for desktop and mobile to keep the section tighter.

Files changed:
- `index.html`
- `PROJECT_PIPELINE.md`

Verification:
- Confirmed the reel references all 39 uploaded transformation images.
- Confirmed no transformation carousel/cards, captions, or `During` labels remain.

### 2026-05-18 11:56 BST - Larger 38-photo paired transformation reel

Status: Completed.

Request:
- Make the transformation reel easier to see, faster, and remove the unpaired final photo.

Summary:
- Enlarged the reel frame so the before/after difference is clearer.
- Shortened the reel timing from 80 seconds to 57 seconds, with faster paired slides.
- Removed `transformation-reel-39.jpeg` from the rendered reel so it now shows 38 photos as 19 complete Before/After pairs.
- Kept the page flow as reel directly followed by Services, with no extra transformation photos in between.

Files changed:
- `index.html`
- `PROJECT_PIPELINE.md`

Verification:
- Confirmed the reel references 38 transformation photos.
- Confirmed no `reel-slide-single` or `transformation-reel-39.jpeg` remains in the rendered reel.
- Confirmed the Services section follows immediately after the transformation reel.

### 2026-05-19 21:08 BST - Catalogue service inclusions and Home message

Status: Completed.

Request:
- Update the Home wording and replace the provisional What's Included service bullets with the catalogue inclusions.
- Remove exhaust-tip polishing from Enhancement Detail and make Paint Correction consultation-based.

Summary:
- Changed the Home headline to `Premium Mobile Detailing Across London & Surrey`.
- Rewrote the Home support copy to position Godoy Auto Detailing for family cars, daily drivers, luxury vehicles, performance cars and supercars.
- Updated Maintenance Valet, Interior Deep Clean, Full Deep Clean, Enhancement Detail and Ceramic Coating inclusions from the catalogue screenshots.
- Changed Paint Correction to invite clients to contact us for a multiple-stage correction consultation.

Files changed:
- `index.html`
- `PROJECT_PIPELINE.md`

Verification:
- Confirmed six What's Included panels are still present.
- Confirmed the new Home headline and Paint Correction consultation text are present.

Notes:
- Enhancement Detail no longer mentions exhaust tip polishing.

### 2026-05-20 14:04 BST - Pre-launch readiness pass

Status: Completed.

Request:
- Prepare the website for going live with the improvements identified in the launch review.

Summary:
- Added search/social metadata, robots guidance and LocalBusiness structured data for Godoy Auto Detailing.
- Replaced external Unsplash section backgrounds with local project images and pinned the Lucide icon CDN version.
- Added a quote form privacy note and optimized runtime images for faster loading while preserving the current reel and gallery choices.
- Synced the refreshed project folder to `/Users/vitor/Documents/Godoy-Auto-Detailing-Website/`.

Files changed:
- `index.html`
- `PROJECT_PIPELINE.md`
- Runtime image assets in `assets/`

Verification:
- Confirmed no Unsplash background URLs or `lucide@latest` references remain.
- Confirmed the transformation reel still references 38 photos.

Notes:
- The site is ready for a final hosted-domain test; canonical/live domain metadata can be added once the exact domain is chosen.

## Change Log Template

Use this format for each new project update:

```markdown
### YYYY-MM-DD HH:MM TZ - Short Change Name

Status: Completed / In progress / Blocked.

Request:
- What the user asked for.

Summary:
- What changed.

Files changed:
- `path/to/file`

Verification:
- How it was checked.

Notes:
- Reusable decisions, assets, copy, or implementation details.
```

## Operating Rule Going Forward

For every meaningful project change:

1. Update the working project files in the Codex workspace.
2. Document the change in this pipeline.
3. Verify the site locally when the change affects layout, content, images, or behavior.
4. Sync the latest project files to `/Users/vitor/Documents/Godoy-Auto-Detailing-Website`.
### 2026-05-20 18:55 BST - GitHub repository setup

Status: Completed.

Request:
- Connect the local website project to the GitHub repository supplied by the client.

Summary:
- Prepared the project for version control with a baseline `.gitignore`.
- Connected the local project to `https://github.com/Vitorgodoyy/Godoy-auto-detailing-website.git`.
- Created the first deployment snapshot in Git.
- Pushed the `main` branch to GitHub.
- Synced the same project files to the local backup folder.

Files changed:
- `.gitignore`
- `PROJECT_PIPELINE.md`

Verification:
- Created initial commit `ca50f23`.
- Pushed `main` to the GitHub repository.
- Synced backup folder: `/Users/vitor/Documents/Godoy-Auto-Detailing-Website`.

Notes:
- Next step is connecting the GitHub repository to a hosting provider and pointing the IONOS domain DNS to that host.
