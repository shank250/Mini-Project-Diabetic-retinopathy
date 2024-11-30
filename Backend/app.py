# # from flask import Flask, request, jsonify
# # from flask_cors import CORS
# # import numpy as np
# # from PIL import Image
# # import io
# # import base64
# # from tensorflow.keras.models import load_model

# # app = Flask(__name__)
# # CORS(app, resources={r"/process_image": {"origins": "*"}})  # Allow all origins for this specific route

# # model_path = 'model/model.h5'
# # model = load_model(model_path)



# # @app.route('/process_image', methods=['POST'])
# # def process_image():
# #     try:
# #         # Get the base64 encoded image from the request
# #         image_data = request.json['image']
        
# #         # # Remove the base64 prefix if it exists
# #         # if ',' in image_data:
# #         #     image_data = image_data.split(',')[1]
        
# #         # # Decode the base64 image
# #         # image_bytes = base64.b64decode(image_data)
        
# #         # # Open the image with Pillow
# #         # image = Image.open(io.BytesIO(image_bytes))
        
# #         # # Convert image to grayscale numpy array
# #         # image_array = np.array(image.convert('L'))
        
# #         # # Example processing: calculate average pixel intensity
# #         # average_intensity = np.mean(image_array)
        
# #         # # Example processing: calculate image complexity (standard deviation)
# #         # image_complexity = np.std(image_array)
        
# #         # # Return results
# #         # return jsonify({
# #         #     'average_intensity': round(average_intensity, 2),
# #         #     'image_complexity': round(image_complexity, 2)
# #         # })
    
# #     except Exception as e:
# #         return jsonify({'error': str(e)}), 400

# # if __name__ == '__main__':
# #     app.run(debug=True, host='0.0.0.0', port=5000)


# import os
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from werkzeug.utils import secure_filename
# import numpy as np
# from tensorflow.keras.preprocessing import image
# from tensorflow.keras.models import load_model

# app = Flask(__name__)
# CORS(app)

# # Configuration
# UPLOAD_FOLDER = 'uploads'
# ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Suppress TensorFlow warnings
# # Ensure upload directory exists
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# # Configuration parameters (adjust these as per your model)
# IMAGE_HEIGHT = 150  # Example size, adjust to your model's requirements
# IMAGE_WIDTH = 150  # Example size, adjust to your model's requirements

# # Load your pre-trained model
# # Replace 'your_model.h5' with the path to your actual trained model
# # model = load_model('your_model.h5')

# model_path = 'model/model.h5'
# model = load_model(model_path)


# # Predefined class indices and remedies (customize as needed)
# CLASS_INDICES = {
#     0: 'Mild', 
#     1: 'Mild', 
#     2: 'Moderate', 
#     3: 'Severe', 
#     4: 'Proliferative DR'
# }

# REMEDIES_DATA = {
#     'Mild': 'Recommended lifestyle changes and regular monitoring',
#     'Moderate': 'Consider medical intervention and strict diabetes management',
#     'Severe': 'Urgent medical attention and specialized treatment required',
#     'Proliferative DR': 'Immediate medical intervention and potential surgical options'
# }

# def allowed_file(filename):
#     """Check if the file has an allowed extension."""
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route('/process_image', methods=['POST'])
# def process_image():
#     try:
#         # Check if file is present in the request
#         # if 'file' not in request.files:
#         #     return jsonify({'error': 'No file part'}), 400
        
#         file = request.files['file']
        
#         # # Check if filename is empty
#         # if file.filename == '':
#         #     return jsonify({'error': 'No selected file'}), 400
        
#         # Check if file is allowed
#         if file and allowed_file(file.filename):
#             # Create uploads folder if it doesn't exist
#             uploads_folder = 'uploads'
#             os.makedirs(uploads_folder, exist_ok=True)
            
#             # Secure filename and save file
#             filename = secure_filename(file.filename)
#             file_path = os.path.join(uploads_folder, filename)
#             file.save(file_path)
            
#             try:
#                 # Load and preprocess the image
#                 # img = image.load_img(file_path, target_size=(IMAGE_HEIGHT, IMAGE_WIDTH))
                
#                 # Remove the saved file
#                 # os.remove(file_path)
                
#                 # # Convert image to array
#                 # img_array = image.img_to_array(img)
#                 # img_array = np.expand_dims(img_array, axis=0)
#                 # img_array = img_array / 255.0  # Normalize pixel values
                
#                 # Make prediction with graph context
#                 # with tf.device('/CPU:0'):  # Ensure CPU usage
#                 # prediction = model.predict(img_array)
#                 # print(prediction)

#                 # # Get predicted class
#                 # predicted_class_index = np.argmax(prediction)
#                 # predicted_class = CLASS_INDICES.get(predicted_class_index, 'Unknown')
                
#                 # # Get remedy
#                 # remedy = REMEDIES_DATA.get(predicted_class, "No remedy available")
#                 # print(predicted_class, remedy)
#                 print("*"*89)
#                 # Return results
#                 return jsonify({
#                     'result': 77, 
#                     'remedy': "remedy",
#                     'confidence': 99
#                 })
            
#             except Exception as e:
#                 # Remove the file if an error occurs
#                 if os.path.exists(file_path):
#                     os.remove(file_path)
#                 return jsonify({'error': str(e)}), 500
        
#         return jsonify({'error': 'File not allowed'}), 400
    
#     except Exception as e:
#         return jsonify({'error': f'Unexpected error: {str(e)}'}), 500


# # @app.route('/process_image', methods=['POST'])
# # def process_image():
# #     return jsonify({
# #             'result': 9, 
# #             'remedy': "cheack",
# #             'confidence': 98
# #         })


# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)


import os
import uuid
from flask import Flask, request, jsonify
from flask_cors import CORS
import threading
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

app = Flask(__name__)
CORS(app)

# Configuration
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Model loading
model_path = 'model/model.h5'
model = load_model(model_path)

# Task storage
tasks = {}

def process_task(task_id, file_path):
    try:
        # Load and preprocess the image
        img = image.load_img(file_path, target_size=(150, 150))
        img_array = image.img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        # Make predictions
        prediction = model.predict(img_array)
        predicted_class_index = np.argmax(prediction)
        result = {
            'result': ['Mild', 'Moderate', 'Severe', 'Proliferative DR'][predicted_class_index],
            'confidence': float(np.max(prediction)),
        }
        print("*"*89)
        print(result)
        # Store the result in the tasks dictionary
        tasks[task_id]['status'] = 'completed'
        tasks[task_id]['result'] = result

        # Clean up uploaded file
        os.remove(file_path)

    except Exception as e:
        tasks[task_id]['status'] = 'failed'
        tasks[task_id]['error'] = str(e)

@app.route('/upload_image', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    # Save the file and create a job ID
    filename = f"{uuid.uuid4()}.png"
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(file_path)

    # Create a task
    task_id = str(uuid.uuid4())
    print("Task id: " + task_id)
    tasks[task_id] = {'status': 'processing'}

    # Process the file in a separate thread
    threading.Thread(target=process_task, args=(task_id, file_path)).start()

    return jsonify({'task_id': task_id}), 202

@app.route('/get_result/<task_id>', methods=['GET'])
def get_result(task_id):
    if task_id not in tasks:
        return jsonify({'error': 'Invalid task ID'}), 404

    task = tasks[task_id]
    if task['status'] == 'completed':
        return jsonify(task['result'])
    elif task['status'] == 'failed':
        return jsonify({'error': task['error']}), 500
    else:
        return jsonify({'status': task['status']}), 202

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
