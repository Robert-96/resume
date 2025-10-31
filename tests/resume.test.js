const expect = require("expect-puppeteer").expect;

describe("Resume", () => {
  beforeAll(async () => {
    const url = process.env.TEST_URL || "https://resume.dezmereanrobert.com/";
    await page.goto(url);
  });

  it('should display text on page', async () => {
    await expect(page).toMatchTextContent(/Dezmerean Robert/);
  });

  it('should have a title containing "Resume"', async () => {
    const title = await page.title();
    expect(title).toMatch(/Resume/i);
  });

  it('should have a contact section', async () => {
    await expect(page).toMatchTextContent(/Contact/i);
  });

  it('should not have any console errors', async () => {
    const errors = [];
    page.on('console', msg => {
      if (msg.type() === 'error') errors.push(msg.text());
    });
    await page.reload();
    expect(errors.length).toBe(0);
  });
});
