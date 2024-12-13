# Diabetic Retinopathy Detection with CNN

This project is a **Diabetic Retinopathy Detection System** that uses a **Convolutional Neural Network (CNN) With Long Range Units and Inception V3** to classify retinal images. It provides a simple web-based interface for users to upload retinal images and get predictions on the presence of diabetic retinopathy.

---

## 🏗 **Architecture**
1. **Machine Learning**:  
   - A CNN model is built using **TensorFlow** and **Keras** to classify retinal images from the **Messidor dataset**.  
   - Preprocessing steps include resizing images and normalizing pixel values.  
   - The model predicts the severity of diabetic retinopathy.  

2. **Backend**:  
   - The backend is developed using **Flask**, which acts as a bridge between the ML model and the frontend.  
   - It handles image upload, model inference, and result transmission to the client.

3. **Frontend**:  
   - The user interface is built with **HTML** and **CSS**.  
   - Users can upload retinal images and view the classification results.  

---

## 💻 **Tech Stack**
- **Machine Learning**: TensorFlow, Keras, Python
- **Backend**: Flask
- **Frontend**: HTML, CSS
- **Dataset**: Messidor (Retinal Images)

---

## 📂 **Project Structure**
```plaintext
.
├── model/
│   ├── cnn_model.py          # Model architecture and training script
│   ├── model.h5/         # Trained model files
├── Backend/
|   ├── app.py                # Flask backend application
├── Frontend/
│   ├── index.html            # Main frontend HTML file
|   ├── styles.css
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

---

## 🗂 **Dataset**
- **Messidor Dataset**:  
  A publicly available dataset containing retinal images used for detecting diabetic retinopathy.  
  - Images are preprocessed and resized to fit the CNN input shape.  
  - Dataset split: 80% training, 20% validation.

---

## 🚀 **Features**
- Upload retinal images through a user-friendly interface.  
- Real-time prediction of diabetic retinopathy severity.  
- Lightweight Flask backend for seamless communication between frontend and ML model.

---

## 🛠 **Setup Instructions**
1. Clone the repository:  
   ```bash
   git clone https://github.com/shank250/Mini-Project-Diabetic-retinopathy
   cd https://github.com/shank250/Mini-Project-Diabetic-retinopathy
   ```

2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

3. Download the Messidor dataset and preprocess the images using the script in `cnn_model.py`.

4. Train the CNN model:  
   ```bash
   python model/model.py
   ```

5. Run the Flask application:  
   ```bash
   python app.py
   ```

6. Open your browser and navigate to:  
   `http://127.0.0.1:5000/`

---

## 🌟 **Future Enhancements**
- Add additional layers to improve model accuracy.  
- Implement more sophisticated preprocessing techniques for retinal images.  
- Host the application on a cloud platform for wider accessibility.  

---

## 🤝 **Contributing**
Contributions are welcome! Feel free to fork the repository and submit pull requests.

---

## 🤝 **Contributing**
Credits goes to the A deep convolutional neural network for diabetic retinopathy detection via mining local and long‐range dependence
Xiaoling Luo1, Wei Wang1, Yong Xu, Zhihui Lai3, Xiaopeng Jin4, Bob Zhang5, David Zhang for the reasearch work

---

## 📜 **License**
This project is licensed under the MIT License. See `LICENSE` for more details.  

--- 

## 📬 **Contact**
For questions or suggestions, feel free to reach out via GitHub issues or email.  
