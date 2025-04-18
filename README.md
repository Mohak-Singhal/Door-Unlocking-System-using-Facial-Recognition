# Door Unlocking System Using Facial Recognition 🚪📷  

This project is a security-focused door unlocking system leveraging **facial recognition**. It uses **OpenCV** and a prebuilt machine learning model to detect and identify authorized users. The system enhances security by performing specific actions based on whether the face detected is recognized or not.

## 🌟 Features  
1. **Facial Recognition**:  
   - Uses OpenCV with a prebuilt model to detect faces.  
   - Unlocks the door automatically if an authorized face is detected.  

2. **Unauthorized Access Handling**:  
   - Captures a photo of the unrecognized individual.  
   - Rings an alarm immediately to alert nearby individuals.  
   - Sends an **alert email** to the registered user with the captured photo for quick action.  

3. **Seamless and Secure**:  
   - Integrates real-time facial recognition with security features to ensure safety and convenience.  

## 📂 Technologies Used  
- **Python**: Core programming language for the project.  
- **OpenCV**: For facial recognition and image processing.  
- **SMTP (Simple Mail Transfer Protocol)**: To send alert emails to the user.  
- **Hardware Components**:  
  - Camera for real-time face detection.  
  - Door lock mechanism (servo motor or relay module).  
  - Alarm system.  

## 🛠️ How It Works  
1. The camera scans for a face when someone approaches the door.  
2. The system checks the face against the prebuilt model for recognition:  
   - **If Recognized**: Unlocks the door which was demostrated by a servo motor.  
   - **If Unrecognized**:  
     - Takes a photo of the individual.  
     - Rings an alarm to notify nearby people.  
     - Sends an alert email with the captured photo to the user for further action.  



## 🛡️ Applications  
- Home and office security.  
- Restricted access areas in institutions or organizations.  
- Personal projects to explore real-time computer vision applications.  

