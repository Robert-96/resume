// Generate a PDF version of the resume webpage

const puppeteer = require('puppeteer');

(async () => {
    // Launch a headless browser
    const browser = await puppeteer.launch();
    const page = await browser.newPage();

    await page.goto('https://resume.dezmereanrobert.com/');

    // Remove dark mode class to ensure light theme for PDF
    await page.evaluate(() => {
        document.documentElement.classList.remove('dark');
    });

    // Generate PDF from the page
    const outputPath = './dist/resume.pdf';
    await page.pdf({
        path: outputPath,
        format: 'A4',
        scale: 0.75,
        printBackground: false,
    });

    console.log("PDF generated successfully at: " + outputPath);

    await browser.close();
})();
