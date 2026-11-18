# Seven Signals — Your Deadline, Your Design

## Mission and deliverables
**Title:** Seven Signals — A Deadline You Can See

**Goal:** Turn the Handshake mission deadline into an original phone lock-screen series with seven navigational beacons, a practical daily action plan, and a live countdown companion website.

**Deadline:** Monday, November 23, 2026 at 11:59 p.m. Pacific Time. In November, Pacific Time is PST (UTC−8), so the equivalent UTC deadline is November 24, 2026 at 07:59 UTC. The website countdown updates to this exact instant.

**What was built:** Eight distinct 1290 × 2796 PNG wallpapers (Nov 16–23), a 1600 × 900 cover image, downloadable ZIP pack, and responsive interactive website with a live seconds-level countdown, daily task selector, and wallpaper gallery. Wallpapers are static daily snapshots and must be manually changed each day. The phone's clock is not baked into the artwork, so the OS clock remains legible.

## Seven-day action plan
| Day | Date | Action | Success criterion |
|---|---|---|---|
| 1 | Nov 16 | Choose the deadline | Date and time selected |
| 2 | Nov 17 | Map the seven steps | A realistic one-action-per-day plan |
| 3 | Nov 18 | Sketch the screen | Clock-safe layout established |
| 4 | Nov 19 | Build the first draft | Clear countdown and action card |
| 5 | Nov 20 | Test on your phone | Readable at phone scale |
| 6 | Nov 21 | Polish and export | Final PNG and cover assets |
| 7 | Nov 22 | Publish the project | Working public project URL |
| Final | Nov 23 | Verify submission | Handshake confirmation before 11:59 p.m. PT |

## Design decisions
The orbit and seven beacons visualize the route to completion; the illuminated checkpoints change from day to day. The dark cyan/indigo palette improves legibility; subtle contour lines communicate a route forward without distracting from the countdown. The top 700+ pixels are intentionally reserved for the phone's native lock-screen clock and widgets. A single daily action prevents the wallpaper from becoming an overwhelming to-do list.

## Ready-to-paste Handshake submission
**Project title:** Seven Signals — A Deadline You Can See

**Description:**
What if a deadline felt like a route instead of a wall? I designed Seven Signals, an original lock-screen countdown that turns one November 23 deadline into seven visual checkpoints. Every day reveals a different wallpaper, lights another beacon on the orbital progress map, and presents one achievable action. I also built a responsive companion website with a live countdown in Pacific Time, an interactive daily mission selector, and all eight downloadable wallpapers. The phone artwork deliberately leaves room for the real lock-screen clock and notifications. I worked backward from the deadline, created a daily plan, and used ChatGPT for concept/planning and custom Python/Pillow artwork and web development. The wallpapers are daily static snapshots; the website countdown updates live.

**Cover image:** Cover_Seven_Signals_1600x900.png

**Project URL:** https://redafrix.github.io/seven-signals-countdown/

## Tools and transparency
Built with ChatGPT, Python/Pillow, HTML, CSS, and JavaScript. No Gemini usage is claimed, since the participant explicitly preferred ChatGPT, even though the original Handshake learning prompt describes Gemini.

## Folder structure
- index.html — responsive live companion website
- wallpapers/ — eight daily PNG lock screens
- Cover_Seven_Signals_1600x900.png — submission cover
- Seven_Signals_Wallpaper_Pack.zip — downloadable daily wallpaper pack
- build_seven_signals.py — reproducible original art generator
- website_preview_mobile.png — local QA screenshot
- Countdown_Lock_Screen_1290x2796.png and make_wallpaper.py — archived first draft

## Verification checklist
- [x] Deadline and backwards plan selected
- [x] Eight daily wallpapers generated
- [x] Cover generated
- [x] ZIP pack generated
- [x] Website and interactions built
- [x] Mobile browser smoke test: eight steps, eight gallery items, no JS errors, selecting final day works
- [x] Public GitHub Pages deployment configured (live URL: https://redafrix.github.io/seven-signals-countdown/)
- [ ] Handshake submission accepted, URL saved and verified
