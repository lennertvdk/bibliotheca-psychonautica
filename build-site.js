const fs = require('fs');
const path = require('path');

const root = __dirname;
const sourceDir = path.join(root, 'german-website-redesign-project', 'project');
const outputDir = path.join(root, 'site');
const pageFiles = fs.readdirSync(sourceDir)
  .filter((file) => file.endsWith('.dc.html') && !['SiteHeader.dc.html', 'SiteFooter.dc.html'].includes(file));

function readSource(file) {
  return fs.readFileSync(path.join(sourceDir, file), 'utf8');
}

function extractTemplate(source) {
  const match = source.match(/<x-dc>([\s\S]*?)<\/x-dc>/i);
  if (!match) throw new Error(`Missing x-dc template in ${source}`);
  return match[1];
}

function extractHelmet(source) {
  const match = source.match(/<helmet>([\s\S]*?)<\/helmet>/i);
  return match ? match[1].trim() : '';
}

function removePreviewOnlyMarkup(markup) {
  return markup
    .replace(/<script[^>]*src=["']\.\/support\.js["'][^>]*><\/script>/gi, '')
    .replace(/<script[^>]*data-dc-script[\s\S]*?<\/script>/gi, '')
    .replace(/<helmet>[\s\S]*?<\/helmet>/gi, '')
    .replace(/<\/?x-dc>/gi, '')
    .replace(/<\/?body[^>]*>/gi, '')
    .replace(/<\/?html[^>]*>/gi, '')
    .replace(/<dc-import[^>]*>[\s\S]*?<\/dc-import>/gi, '')
    .replace(/<dc-import[^>]*\/>/gi, '')
    .trim();
}

function renderComponent(name, active) {
  let component = removePreviewOnlyMarkup(extractTemplate(readSource(`${name}.dc.html`)));
  component = component.replace(/<sc-if\s+value=["']\{\{\s*(is\w+)\s*\}\}["'][^>]*>([\s\S]*?)<\/sc-if>/gi, (_, prop, content) => {
    const activeName = prop.slice(2).toLowerCase();
    return active === activeName ? content : '';
  });
  return component;
}

function renderStaticInteractions(markup) {
  return markup
    .replace(/<sc-if[^>]*hint-placeholder-val=["']\{\{\s*true\s*\}\}["'][^>]*>([\s\S]*?)<\/sc-if>/gi, '$1')
    .replace(/<sc-if[^>]*hint-placeholder-val=["']\{\{\s*false\s*\}\}["'][^>]*>[\s\S]*?<\/sc-if>/gi, '')
    .replace(/\s+onClick=["']\{\{[^}]+\}\}["']/gi, '')
    .replace(/\{\{\s*heroPos\s*\}\}/gi, 'center')
    .replace(/\{\{\s*kopierLabel\s*\}\}/gi, 'IBAN kopieren')
    .replace(/\{\{\s*gewaehltLabel\s*\}\}/gi, 'Mitgliedschaft wählen')
    .replace(/\{\{[^}]+\}\}/g, '');
}

function renderPage(file) {
  const source = readSource(file);
  const active = {
    'Startseite.dc.html': 'startseite',
    'Neuigkeiten.dc.html': 'neuigkeiten',
    'Themen-und-Sammlungen.dc.html': 'themen',
    'Der-Verein.dc.html': 'verein',
    'Spenden.dc.html': 'spenden',
    'Kontakt.dc.html': 'kontakt'
  }[file] || '';

  let body = extractTemplate(source);
  body = body.replace(/<dc-import\s+name=["']SiteHeader["'][^>]*(?:\/>|>[^]*?<\/dc-import>)/gi, renderComponent('SiteHeader', active));
  body = body.replace(/<dc-import\s+name=["']SiteFooter["'][^>]*(?:\/>|>[^]*?<\/dc-import>)/gi, renderComponent('SiteFooter', active));
  body = renderStaticInteractions(removePreviewOnlyMarkup(body))
    .replace(/\.dc\.html\b/g, '.html')
    .replace(/\{\{\s*heroPos\s*\}\}/g, 'center');

  const helmet = extractHelmet(source);
  const title = file === 'Startseite.dc.html'
    ? 'Bibliotheca Psychonautica | Verein zur Erhaltung geistbewegenden Wissens'
    : 'Bibliotheca Psychonautica';
  return `<!doctype html>\n<html lang="de">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n<meta name="description" content="Verein zur Erhaltung und Förderung von geistbewegendem Wissen">\n<title>${title}</title>\n${helmet}\n</head>\n<body>\n${body}\n</body>\n</html>\n`;
}

fs.rmSync(outputDir, { recursive: true, force: true });
fs.mkdirSync(outputDir, { recursive: true });
fs.writeFileSync(path.join(outputDir, '.nojekyll'), '');
fs.cpSync(path.join(sourceDir, 'assets'), path.join(outputDir, 'assets'), { recursive: true });

for (const file of pageFiles) {
  const outputName = file.replace('.dc.html', '.html');
  fs.writeFileSync(path.join(outputDir, outputName), renderPage(file));
}

fs.copyFileSync(path.join(outputDir, 'Startseite.html'), path.join(outputDir, 'index.html'));

for (const file of fs.readdirSync(outputDir).filter((name) => name.endsWith('.html'))) {
  fs.copyFileSync(path.join(outputDir, file), path.join(root, file));
}
fs.mkdirSync(path.join(root, 'assets'), { recursive: true });
fs.cpSync(path.join(outputDir, 'assets'), path.join(root, 'assets'), { recursive: true, force: true });
fs.writeFileSync(path.join(root, '.nojekyll'), '');
console.log(`Built ${pageFiles.length} pages in ${path.relative(root, outputDir)}/`);
