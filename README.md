# resume

This project is a resume site that showcases my professional experience, education, and skills. The site is built using Python and Node.js.

You can view my resume at <https://resume.dezmereanrobert.com>, or you can download a PDF version <https://resume.dezmereanrobert.com/pdf/Dezmerean%20Robert%20-%20Resume.pdf>.

![Screenshot](/screenshots/screenshot.png)

## Development Setup

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before you get started, you'll need to have the following installed:

* Python3
* Node.js

### Setup

To install the Python dependencies, run the following command:

```bash
python -m pip install -r requirements.txt
```

To install the Node.js dependencies, run the following command:

```bash
npm install
```

### Dev

To start a development server, run the following command:

```bash
npm run dev
```

Navigate to the site at <http://localhost:8080/>.

### Build

To build the project, run the following command:

```bash
npm run build
```

The output will be in the `./dist/` directory.

### Test

To run tests, run the following command:

```bash
# TODO
```

### Deploy

See the deploy job from [main.yml](.github/workflows/main.yml).

## Save as PDF

### Chrome

1. Right-click on the page and select "Print."
1. In the print options, choose "Save as PDF."
1. To set the page size to A4 or Letter, navigate to "More Settings → Paper Size".
1. Click "Save".

### Firefox

1. Click on "File" and select "Print".
1. In the print options, choose "Save as PDF."
1. To set the page size to A4 or Letter, navigate to "More Settings → Paper Size".
1. Click "Save".
