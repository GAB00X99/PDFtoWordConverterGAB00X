# PDF to DOCX Converter using Flask

This is a web application that allows you to convert PDF files to DOCX files using Flask, a Python library for building web applications.

## Functionality

1. The user accesses the main page where they can select a PDF file for conversion.
2. Once the PDF file is selected, a POST request is made to the `/convert` route.
3. The server temporarily saves the PDF file in a temporary directory.
4. A DOCX file is generated using the pdf2docx library to perform the conversion.
5. The resulting DOCX file is saved in the `static` directory of the application.
6. The server sends the DOCX file to the client for download.
7. If no PDF file is provided, the server redirects to the main page.

## Requirements

- Python 3.x
- Flask
- pdf2docx

## Usage

1. Clone this repository to your local machine.
2. Install the dependencies using the following command:
3. Run the application using the following command:
4. Open your web browser and access `http://localhost:5000`.
5. Select a PDF file and click the "Convert" button.
6. A converted DOCX file will be downloaded.

## Credits

- This code utilizes Flask, a Python library for building web applications: [Flask](https://flask.palletsprojects.com/)
- The PDF to DOCX conversion is performed using the pdf2docx library: [pdf2docx](https://github.com/ashish1294/pdf2docx)

## Notes

- This application is provided for educational purposes only and should not be used to infringe copyright or violate the terms of use of any service.
- The code may require additional modifications for implementation in production and ensuring proper security.
- We are not responsible for any misuse of this code.

