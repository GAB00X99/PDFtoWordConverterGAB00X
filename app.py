import os
import tempfile
from flask import Flask, render_template, request, send_file, redirect
from werkzeug.utils import secure_filename
from pdf2docx import Converter

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    # Obtiene el archivo PDF enviado por el formulario
    pdf_file = request.files['pdf_file']
    if pdf_file:
        # Guarda el archivo PDF en un directorio temporal
        pdf_temp = tempfile.NamedTemporaryFile(delete=False)
        pdf_file.save(pdf_temp.name)
        
        # Genera el nombre y la ruta del archivo Word resultante
        docx_filename = secure_filename(pdf_file.filename.rsplit('.', 1)[0] + '.docx')
        docx_path = os.path.join(app.root_path, 'static', docx_filename)
        
        # Realiza la conversión de PDF a Word
        cv = Converter(pdf_temp.name)
        cv.convert(docx_path, start=0, end=None)
        cv.close()
        
        # Elimina el archivo PDF temporal
        pdf_temp.close()
        os.unlink(pdf_temp.name)
        
        # Devuelve el archivo Word descargable o un enlace para descargarlo
        return send_file(docx_path, as_attachment=True)
    
    # Si no se proporcionó un archivo PDF, redirecciona a la página principal
    
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

