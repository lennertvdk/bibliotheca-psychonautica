push t# Claude Design Prompt — Bibliotheca Psychonautica Website

> Paste everything below the line into Claude Design. Upload these files with it:
> the four photos in the project root (`Bücher-Bibliothek-1-WIP.jpeg`, `Bücher-Nachlass-Rätsch-1-Spinnenweben.jpeg`, `Bücher-Nachlass-Rätsch-2-Stapel.jpeg`, `Buch-Title-Page-LSD-Problem-Child-Signed.jpeg`)
> and the three files in `assets/reference/` (old wordmark, old hero banner, Gaia Media logo).

---

## 1. What this is

Design a complete website redesign for **Bibliotheca Psychonautica**, a Swiss non-profit association (Verein, founded 10 November 2012, seat in Solothurn). It collects, preserves and makes accessible private libraries and estates (Nachlässe) of literature on psychedelics, ethnobotany, shamanism, drug policy and consciousness research. Tagline: **"Verein zur Erhaltung und Förderung von geistbewegendem Wissen"**.

The current site is https://bibliotheca-psychonautica.org/ (WordPress, 2012 design). It is dated: glossy label logo, a small banner, sidebar layout, no calls to action, membership signup buried in a long form. All copy from it is included verbatim below and must be reused as-is.

The new site will be built as a static site (HTML/CSS/JS on GitHub Pages, no backend, no CMS). Language: German only.

Long-term vision the site must communicate: a future foundation (Stiftung), digitization of the archive, an AI-assisted online database, and several physical locations. Today: shelves at Nachtschatten Verlag in Solothurn (since July 2013), decentral parts in Zürich, and new: a physical location at **Volkshaus Basel in cooperation with the Gaia Media foundation**.

## 2. Goals, in priority order

1. **Become a member quickly and easily** ("Mitglied werden"). Includes a new free membership option.
2. **Donate easily** ("Spenden") and understand what donations fund.
3. **Present the project convincingly**: what already exists (real photos of the shelves), what is being built (digitization, database, locations), why it matters (estates get lost or sold off).
4. **Recruit people to help build the collection**: donate books or an estate, join, support.

The website is the central hub. Signup and donations happen here, not on a third-party page.

## 3. Audience and tone

German-speaking people (CH, DE, AT) in the psychedelic research and ethnobotany world: researchers, students, therapists, collectors, publishers, the psychedelic science community. Also potential estate donors: older collectors and their families, who need to trust the association with a life's collection.

Tone: serious, scholarly, warm. This is a library and an archive of cultural history, not a festival and not drug promotion. Think university library meets small foundation.

## 4. Sitemap

Top navigation, in this order:

1. **Startseite**
2. **Neuigkeiten & Events** (new) — Beiträge, News, Fotos, and Termine
3. **Themen & Sammlungen**
4. **Der Verein**
5. **Spenden** (new)
6. **Mitglied werden** (replaces "Anmelden"; styled as a highlighted button in the nav)
7. **Kontakt**

The old "Links" page moves into the footer or into "Der Verein" as "Partner & Links". No newsletter anywhere (deliberately left out for now).

## 5. Page by page

### Startseite (hero page, replaces the current layout entirely)

- **Hero**: full-width, one strong image (the signed Hofmann title page or the glass bookcase photo, treated with a dark gradient), the name, the tagline, one umbrella line such as "Hilf mit, geistbewegendes Wissen zu bewahren", and two buttons: primary **"Mitglied werden"**, secondary **"Spenden"**. Optional tertiary text link: "Sammlung oder Nachlass anbieten".
- **Was wir tun**: 3 or 4 cards: Sammeln & Bewahren / Zugänglich machen / Digitalisieren / Orte (Solothurn, Zürich, Basel).
- **Die Bibliothek gibt es schon**: photo strip using the four real photos with captions (see Assets), plus the original homepage text.
- **So kommt eine Sammlung in die Bibliothek**: 3 steps (Kontakt aufnehmen → Sichtung & Abholung → Inventarisierung & Zugang für Mitglieder). Uses the cobweb estate photo to show "this is what rescuing an estate looks like".
- **Stimmen**: 3 testimonial cards with portrait photo + quote (placeholders, see section 9).
- **Neuigkeiten**: latest 3 posts as cards (placeholder) + link to the section.
- **Partner**: Gaia Media logo + "Volkshaus Basel", Nachtschatten Verlag as text.
- **Final CTA band**: "Hilf mit" → Mitglied werden / Spenden.
- **Footer**: address, phone, email, bank details, Facebook, Impressum and Datenschutz links.

### Neuigkeiten & Events

- Two tabs or two stacked sections: **Beiträge** (news and photo posts) and **Termine** (events).
- No events are planned yet. Design a good empty state for Termine, for example: "Aktuell sind keine Veranstaltungen geplant. Mitglieder erfahren es zuerst." with a Mitglied-werden CTA.
- Post card: image, date, title, teaser. Also design one single-post page (title, date, cover image, body, photo gallery).

### Themen & Sammlungen

- Themes as a tag grid (verbatim list below).
- Sammlungen as a list with three visible states: vorhanden, zugesagt, in Aussicht gestellt.
- A section "Kunstwerke aus der Sammlung" as a placeholder gallery (artworks will come later).
- Photo captions from the estate photos can live here too.

### Der Verein

- Founding, seat, founding members, the path toward a Stiftung, the locations, how the board reports (all verbatim text below).
- Membership tiers as a compact overview → CTA to Mitglied werden.
- Partner & Links (the old Links list).

### Spenden (new)

- **Wofür wir Spenden verwenden** (from the association, use this wording as the basis):
  - Miete für die physischen Bücher bezahlen
  - Weitere Projekte planen, z.B. Digitalisierung der Archivmaterialien und Aufbau einer KI-gestützten Onlinedatenbank
- **So kannst du spenden**: bank transfer with the verbatim bank details below, designed so IBAN is easy to copy. Add a slot for a Swiss QR-Rechnung and slots for TWINT / PayPal, all clearly marked [PLATZHALTER] because the channels are not decided yet.
- **Bücher oder Nachlass spenden**: short text + contact CTA.
- Gönner note: "Gönnermitglieder und Sponsoren können auf Wunsch auf der Website erwähnt werden."

### Mitglied werden (replaces Anmelden)

- **Step 1: choose a tier** with one click (cards): Kostenlose Mitgliedschaft (NEW, details to follow) / Passivmitglied / Aktivmitglied / Ermässigt (Studierende) / Gönnermitglied / "Ich habe eine eigene Sammlung oder Bibliothek". Benefits per tier come verbatim from "Der Verein" below.
- **Step 2: short form**: Vorname*, Name*, E-Mail*, Ort, Land, Nachricht (optional). Keep the old optional fields (Firma, Strasse, Telefon, Webseite) inside a collapsed "Weitere Angaben" block. Drop Telefax and Betreff from the visible form.
- **Was danach passiert**: 3 short steps (Bestätigung per E-Mail → Rechnung/Zahlung → Zugang).
- Design it as a normal form. Technically it will be sent via a form service or mailto, so no account creation, no login.

### Kontakt

Address, phone, email, map placeholder, directions (verbatim), and a short contact form (Name*, E-Mail*, Nachricht*).

## 6. Copy, verbatim (German). Use exactly as written.

### Name and tagline

Bibliotheca Psychonautica
Verein zur Erhaltung und Förderung von geistbewegendem Wissen

### Startseite (current homepage text)

Mit Gründung des Vereins Bibliotheca Psychonautica wurde der Grundstein gelegt für eine zukünftige Stiftung mit dem Ziel der Zusammenführung und Bewahrung fundierter Privatsammlungen von psychonautischer Literatur, Videos, DVDs, CDs, Schallplatten, Bildern, Fotos, Kunstwerken, Briefwechseln, Tagebüchern, Forschungsmaterial und Manuskripten, um eine möglichst umfangreiche drogen- und rauschkundliche Bibliothek aufzubauen, die das psychonautische Wissen über veränderte Bewusstseinszustände lebendig erhält.

SammlerInnen von psychonautischer Fachliteratur können ihre privaten Nachlässe dem Verein bzw. der Stiftung vermachen, um dieses wertvolle Material zu erhalten und anderen Interessenten zugänglich zu machen und es vor eigennützigen, gewinnorientierten und kommerziellen Absichten, aber auch vor unachtsamer Entsorgung zu schützen.

Der Verein ist den oben genannten Zielen verpflichtet und unternimmt auf dem Weg zur Gründung einer gemeinnützigen Stiftung geeignete Schritte, um die Bibliothek aufzubauen und den Bestand gegebenenfalls zu ergänzen, zu erweitern und für eventuelle Forschungsvorhaben zugänglich zu machen, z.B. durch Inventarisierung, Ausstellungen, Publikationen etc. Der Vorstand berichtet auf der jährlichen Generalversammlung über den Entwicklungsstand und plant die nächsten Schritte. Er entscheidet auch darüber, welche Objekte der Sammlung (z.B. doppelt vorhandene Bücher) veräussert werden können und welche anderen wichtigen Materialien eventuell angekauft werden sollen.

Für den Aufbau der Bibliothek stehen dem Verein seit Juli 2013 Regalflächen in den Räumen des Nachtschatten Verlages in Solothurn zur Verfügung. Teile der Sammlung befinden sich auch dezentral an anderen Orten (z.B. in Zürich).

Es sind bereits einige umfangreiche Sammlungen von Büchern und Journalen eingegangen, die schrittweise inventarisiert werden. Die Liste des bis jetzt erfassten Bibliotheksbestandes kann beim Verein angefordert werden. Das Entleihen von Büchern ist ausschliesslich Mitgliedern vorbehalten und wird durch den Vereinsvorstand geregelt.

Für den weiteren Aufbau der Bibliotheca Psychonautica brauchen wir dringend aktive und passive Mitglieder sowie grosszügige Gönner und Sponsoren!

Hier anmelden und Vereinsmitglied werden!

Bei Interesse sende eine Mail an info@bibliotheca-psychonautica.org oder nutze das Formular für Mitteilungen und Anfragen.

### Der Verein

Unter dem Namen "Bibliotheca Psychonautica" (BP) besteht ein Verein mit Sitz in 4500 Solothurn (Schweiz). Mit Gründung am 10. November 2012 werden die Statuten des Vereins Bibliotheca Psychonautica wirksam und treten in Kraft. Die Vereinsstatuten können zur Einsicht angefordert werden.

Gründungsmitglieder:
Roger Liggenstorfer, Roger Schweingruber, Michael Schlichting, Christine Heidrich, Markus Berger, Christian Rätsch, Claudia Müller-Ebeling, Marco Domin

Mitgliedschaft:

Aktivmitglieder:
– Zugang zur Bibliothek, mit Ausleihmöglichkeiten
– Information zu den Vereinsaktivitäten, inkl. Teilnahme an Vereinsversammlung
– € 160.- / Fr. 200.- / Ermäßigungen (Studenten oder sonst nach Absprache): € 80.- / Fr. 100.- pro Jahr

Gönnermitglieder und Sponsoren:
– gleiche Bedingungen wie Aktivmitglieder
– zusätzlich mögliche Erwähnung auf der Website,
– privilegierter Erwerb doppelter Exemplare
– ab € 420.- / Fr. 500.- pro Jahr

Passivmitglieder:
– Zugang zur Bibliothek, ohne Ausleihmöglichkeiten
– Information zu Vereinsaktivitäten, ohne Teilnahme an Vereinsversammlungen
– € 50.- / Fr. 60.- pro Jahr

### Mitglied werden (tier options from the current signup form)

Die mit einem * gekennzeichneten Felder sind Pflichtfelder

Mögliche Mitgliedschaft:
– Aktivmitglied (€ 160.- / Fr. 200.-)
– Ermäßigungen (Studenten oder sonst nach Absprache / € 80.- / Fr. 100.- pro Jahr)
– Passivmitglied (€ 50.- / Fr. 60.- pro Jahr)
– Besitzer einer eigenen Sammlung oder Bibliothek (bitte nehmt mit mir Kontakt auf, um Details zu besprechen)
– Gönnermitglied (ab € 420.- / Fr. 500.- pro Jahr)
– NEW, wording placeholder: Kostenlose Mitgliedschaft [PLATZHALTER: Name und Leistungen folgen]

Current form fields: Firma, Name*, Vorname*, Strasse, Ort, Land, Telefon, Telefax, Email*, Webseite, Betreff, Nachricht*

### Themen & Sammlungen

Themen:
Psychedelika, Rauschdrogen, Schamanismus, Ethnobotanik, -medizin, -pharmakologie, Pharmazie, Pharmakologie, Chemie, Psychotherapie, Psychiatrie, Psychologie, Drogenpolitik, Belletristik, Bewusstseinsforschung, Comics, visionäre Kunst, Literatur, Musik, Filme, Periodika etc.

Sammlungen (vorhanden oder zugesagt):
– Günter Amendt
– Hanscarl Leuner
– Gaudenz Bernhardsgrütter
– Freddy Meier
– Adi Dittrich
– René Liechti
– Roger Liggenstorfer und Urs Stauss: Umfangreiche Cannajournalsammlung (z.B. Grow, THcene, Canamo, Hanfblatt etc.)

In Aussicht gestellt:
– Christian Rätsch
– Roger Liggenstorfer
– Michael Schlichting
– Maja Maurer
– Herman de vries
– Juraj Styk

### Kontakt

Bibliotheca Psychonautica
Verein zur Erhaltung und Förderung von geistbewegendem Wissen
Kronengasse 11
CH – 4500 Solothurn
Switzerland

Fon +41 32 621 89 49
Fax +41 32 621 89 47
info@bibliotheca-psychonautica.org
www.bibliotheca-psychonautica.org

Anfahrt:
Öffentlicher Verkehr: Vom Bahnhof sind wir in 10 Minuten erreichbar (Richtung Zentrum/Altstadt über die Aare Richtung Kathedrale)
Auto: Parkplätze vor der Tür (Klosterplatz) oder im nahegelegenen Parkhaus "Baseltor"

### Bankverbindung (for Spenden and footer)

Verein Bibliotheca Psychonautica
Regiobank Solothurn, 4502 Solothurn
Konto Nr. 448.465.50.145
IBAN CH26 0878 5044 8465 5014 5
PC-Konto der Bank: PC 30-38168-4

### Partner & Links

Partner: Gaia Media (Stiftung, Zürich, www.gaiamedia.org), Volkshaus Basel, Nachtschatten Verlag (www.nachtschatten.ch)

Links: www.nachtschatten.ch, www.at-verlag.ch, www.christian-raetsch.de, www.claudia-mueller-ebeling.de, www.erowid.org, www.maps.org, www.heffter.org, www.beckleyfoundation.org, www.psychoactivity.eu, www.gaiamedia.org, www.gruenekraft.com, www.greenearthfound.org, www.storl.de, www.encod.org, www.flashbackbooks.com

Social: Facebook page "Bibliotheca Psychonautica"

## 7. Assets (uploaded with this prompt)

Only these images exist. Do not assume any other photography. Everything else must be typography, colour, texture or illustration.

1. **Bücher-Bibliothek-1-WIP.jpeg** (landscape). Glass-fronted black bookcases in Solothurn, shelves labelled alphabetically (A, B, E, G, L, M, O, P, Q), someone holding an open antiquarian book, a box labelled "Private Bücher A. Hofmann", Shulgin's PiHKAL and TiHKAL visible, a Nachtschatten paper bag. Message: the library exists and is being catalogued. Good for hero or "Die Bibliothek gibt es schon". Suggested caption: "Die Bibliothek in Solothurn: Bestand wird alphabetisch inventarisiert."
2. **Bücher-Nachlass-Rätsch-1-Spinnenweben.jpeg** (portrait). A cobweb-covered wooden shelf from the estate of Christian Rätsch: several copies of "Enzyklopädie der psychoaktiven Pflanzen", "Pflanzen der Liebe", "Urbock", a hand holding the Dutch booklet "Psychedelische perspectieven". Raw and authentic. Message: this is what rescuing an estate looks like. Suggested caption: "Aus dem Nachlass von Christian Rätsch: Bücher, die sonst verloren gingen."
3. **Bücher-Nachlass-Rätsch-2-Stapel.jpeg** (portrait). A stack of spines: Sheldrake, Capra, Ram Dass, Schrödinger, Dürckheim, McKenna, Wilber. Message: breadth of the themes. Suggested caption: "Bewusstseinsforschung, Physik, Philosophie: die Sammlung ist breit."
4. **Buch-Title-Page-LSD-Problem-Child-Signed.jpeg** (portrait). Title page of "LSD, My Problem Child" by Albert Hofmann, signed by Albert Hofmann and by the translator Jonathan Ott. The single most "treasure" image. Ideal for the hero or the Spenden page. Suggested caption: "Signiert von Albert Hofmann und Jonathan Ott: ein Schatz aus der Sammlung."
5. **logo-bibliotheca-psychonautica-2012.png**: the current wordmark (black "Bibliotheca" panel, white "Psychonautica" panel). Reference only.
6. **current-site-hero-banner-2012.jpg**: the current 942x209 banner. Reference only, to show what we are leaving behind.
7. **gaia-media-logo.png**: partner logo, lowercase "gaiamedia, tradition—dimension". Use in the Partner section.

## 8. Visual direction

- You have full artistic freedom. There are no existing brand colours or type rules.
- Reference for feel: Bibliotheca Philosophica Hermetica / Embassy of the Free Mind, Amsterdam (https://embassyofthefreemind.com). Scholarly, contemplative, muted gold on dark and cream, manuscript textures, generous serif typography, support and membership integrated calmly rather than shouted.
- Motifs that fit: book spines, paper and ink, botanical line drawings, marginalia, index cards, shelf labels, archive boxes.
- Avoid: rainbow fractals, neon "trippy" clichés, stock mushroom photos, anything that reads as drug promotion or a party. This is cultural heritage and research.
- Palette starting point (change freely): deep ink or night blue, or a deep forest green, as the base; cream paper for light surfaces; muted gold or ochre accent; one warm accent such as oxblood for primary buttons.
- Typography: a serif display face with character for headings, a clean sans for body and UI. Long German words need generous line length and hyphenation-friendly sizes.
- Logo: propose a refreshed wordmark (2 or 3 variants, keep the two-part name "Bibliotheca | Psychonautica" idea if it helps) or a clean typographic treatment. Keep the name and the tagline unchanged.
- Mobile first. Strong contrast, obvious buttons, no text over busy image areas without an overlay.

## 9. Placeholders and honesty rules

- Mark every placeholder visibly with **[PLATZHALTER]**.
- **Testimonials**: real quotes with portrait photos are being collected and are not available yet. Show 3 cards in this format, labelled "Beispiel": quote, name, role. Example of the intended format, not a confirmed quote: "Die Bibliotheca ist ein unfassbarer Schatz der psychedelischen Kulturgeschichte." — Torsten Passie. Do not present it as real.
- **Free membership**: name and benefits are not decided. Show the card with "Kostenlose Mitgliedschaft [PLATZHALTER: Details folgen]".
- **Events**: none planned. Design the empty state.
- **Artworks**: none available yet. Placeholder gallery with 4 to 6 frames.
- **Donation channels** beyond bank transfer: placeholders only.
- **Fees**: use the existing amounts. Do not invent new prices.
- **Newsletter**: not on the site.

## 10. Deliverables

- **Design system sheet**: palette with roles, type scale, buttons (primary, secondary, text link), cards, form fields, nav bar (desktop + mobile), footer, tag chips, testimonial card, post card, empty state.
- **Desktop artboards (1440 px wide)**: Startseite, Spenden, Mitglied werden, Neuigkeiten & Events (overview with the Termine empty state), single post, Themen & Sammlungen, Der Verein, Kontakt.
- **Mobile artboards (390 px wide)**: Startseite, Spenden, Mitglied werden.
- **Logo exploration**: 2 or 3 wordmark variants on one artboard.

## 11. Build constraints (so the design stays buildable later)

- Static site on GitHub Pages: no backend, no login, no CMS. Forms go through a form service or mailto. News posts are static pages.
- Only the images listed above exist.
- German only. New texts in Swiss spelling ("ss", never "ß") and in the style and gender form of the original texts (for example "SammlerInnen"). Original texts stay verbatim even where they mix spellings.
- The final domain is not decided. Do not bake a URL into any artboard.
- Keep every page to a single flowing artboard; no modals or multi-step wizards except the two-step Mitglied-werden flow.
