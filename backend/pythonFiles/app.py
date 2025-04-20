from flask import Flask, request,jsonify
from flask_cors import CORS
import os
import uploadIMG,segmentation,sliceIMG

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
modality_map = {
        "T1": "0000",
        "T1ce": "0001",
        "T2": "0002",
        "FLAIR": "0003"
    }

@app.route('/')
def index():
    print("")

@app.route('/uploadIMG', methods=['POST'])
def upload_image():
    # Check for file
    if 'file' not in request.files:
        return jsonify({'message': 'No file part'}), 400

    file = request.files['file']
    
    # Check if file is selected
    if file.filename == '':
        return jsonify({'message': 'No file selected'}), 400
    type_img = request.args.get('type', 'default')
    id =0
    # Create subfolder for this type
    type_folder = os.path.join(app.config['UPLOAD_FOLDER'], str(id))
    os.makedirs(type_folder, exist_ok=True)

    #file_ext = os.path.splitext(file.filename)[1]  # Keep original file extension (.nii, .nii.gz, etc.)
    new_filename = f"BraTS2021_0000_{modality_map[type_img]}.nii.gz"
    # Save file inside that folder
    save_path = os.path.join(type_folder, new_filename)
    file.save(save_path)

    return jsonify({'message': f'File saved successfully'})


@app.route('/start-segmentation', methods=['POST'])
def doSegmentation():
    try:
        done = segmentation.segmentationFN()  
        if done:
            return jsonify({'message': 'Segmentation completed successfully!'})
        else:
            return jsonify({'message': 'Segmentation ran but did not complete.'}), 500
    except Exception as e:
        return jsonify({'message': f'Error during segmentation: {str(e)}'}), 500
    

from flask import send_file

@app.route('/visualize-segmentation', methods=['GET'])
def visualize_segmentation():
    try:
        slice_index = int(request.args.get('slice_index', 70))
        orientation = request.args.get('orientation', 'axial')
        id=0
        image_file = os.path.join("uploads/0", "BraTS2021_0000_0000.nii.gz") 
        segmentation_file =  os.path.join("outputs", "BraTS2021_0000.nii.gz")
        output_path = os.path.join("outputs", "visualization.png")

        sliceIMG.visualize_segmentation_slice_greybg_label0grey(
            image_path=image_file,
            segmentation_path=segmentation_file,
            output_path=output_path,
            slice_index=slice_index,
            orientation=orientation
        )

        return send_file(output_path, mimetype='image/png')

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)