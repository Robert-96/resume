// Generate a screenshot of the resume webpage

const puppeteer = require('puppeteer');

(async () => {
  // Launch a headless browser
  const browser = await puppeteer.launch({
    args: ['--window-size=1920,1080'],
    defaultViewport: null
  });
  const page = await browser.newPage();
  await page.setViewport({
    width: 1920,
    height: 1080,
  });

  await page.goto('https://resume.dezmereanrobert.com/', {
    waitUntil: 'networkidle2',
  });

  // Remove dark mode class to ensure light theme for screenshot
  await page.evaluate(() => {
    document.documentElement.classList.remove('dark');
  });
  await new Promise(resolve => setTimeout(resolve, 1000));

  // Generate screenshot from the page
  const outputPath = './screenshots/screenshot.png';
  await page.screenshot({
    path: outputPath,
    fullPage: true,
  });

  // Add dark mode class to ensure dark theme for screenshot
  await page.evaluate(() => {
    document.documentElement.classList.add('dark');
  });
  await new Promise(resolve => setTimeout(resolve, 1000));

  // Generate screenshot from the page dark mode
  const outputPathDark = './screenshots/screenshot-dark.png';
  await page.screenshot({
    path: outputPathDark,
    fullPage: true,
  });

  console.log("Screenshot generated successfully at: " + outputPath);
  console.log("Screenshot generated successfully at: " + outputPathDark);

  await browser.close();
})();
